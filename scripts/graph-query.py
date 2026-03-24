#!/usr/bin/env python3
"""
Chief of Staff -- Knowledge Graph Engine
========================================
Builds a property graph over all JSON data files using DuckDB + DuckPGQ.
Discovers connections, surfaces insights, and outputs findings for standup briefings.

Usage:
    python scripts/graph-query.py                    # Full analysis
    python scripts/graph-query.py --standup           # Standup-formatted output
    python scripts/graph-query.py --summary           # One-line summary
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"


def load_json(filename):
    path = DATA_DIR / filename
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filename, data):
    path = (PROJECT_ROOT / filename).resolve()
    if not str(path).startswith(str(PROJECT_ROOT.resolve())):
        raise ValueError(f"Output path escapes project root: {filename}")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def build_nodes_and_raw_map():
    """
    Build unified nodes. Every node gets a unique graph_id = '{type}::{raw_id}'.
    Returns (nodes_list, raw_id_to_graph_ids_map).
    """
    nodes = []
    raw_map = {}  # raw_id -> [(graph_id, type), ...]

    def add(node_type, raw_id, label, domain="", company="", tags=None, **extra):
        gid = f"{node_type}::{raw_id}"
        node = {"graph_id": gid, "raw_id": raw_id, "type": node_type,
                "label": label, "domain": domain, "company": company,
                "tags": tags or [], **extra}
        nodes.append(node)
        raw_map.setdefault(raw_id, []).append((gid, node_type))

    for item in load_json("tasks.json"):
        add("task", item["id"], item.get("title", ""), item.get("domain", ""),
            tags=item.get("tags", []), status=item.get("status", "open"),
            priority=item.get("priority", "medium"))

    for item in load_json("intelligence.json"):
        add("intel", item["id"], item.get("title", ""), item.get("domain", ""),
            tags=item.get("tags", []), category=item.get("category", "research"))

    for item in load_json("contacts.json"):
        add("contact", item["id"],
            f"{item.get('name', 'Unknown')} ({item.get('role', '')})",
            item.get("domain", ""), item.get("company", ""),
            tags=item.get("tags", []), tier=item.get("tier", 2))

    # Auto-discover domains from domains/ folder
    domains_dir = PROJECT_ROOT / "domains"
    if domains_dir.exists():
        for df in sorted(domains_dir.glob("*.md")):
            slug = df.stem.split("-", 1)[-1] if "-" in df.stem else df.stem
            add("domain", f"domain-{slug}", slug.replace("-", " ").title(), domain=slug)

    return nodes, raw_map


def resolve_id(raw_id, type_hint, raw_map):
    """Resolve a raw_id + type_hint to a graph_id."""
    candidates = raw_map.get(raw_id, [])
    if not candidates:
        return None
    # Prefer type-matching
    for gid, t in candidates:
        if t == type_hint:
            return gid
    return candidates[0][0]


def build_explicit_edges(raw_map):
    """Load connections.json and resolve to graph IDs."""
    edges = []
    for conn in load_json("connections.json"):
        src = resolve_id(conn["source_id"], conn.get("source_type", ""), raw_map)
        dst = resolve_id(conn["target_id"], conn.get("target_type", ""), raw_map)
        if src and dst:
            edges.append({
                "id": conn["id"], "src": src, "dst": dst,
                "relationship": conn["relationship"],
                "strength": conn.get("strength", "moderate"),
                "notes": conn.get("notes", ""),
                "explicit": True,
            })
    return edges


def discover_implicit_edges(nodes):
    """Discover implicit connections: same company, shared tags (>=2, cross-type)."""
    edges = []
    counter = 0

    by_company = {}
    by_tag = {}
    for n in nodes:
        if n["type"] == "domain":
            continue
        company = n.get("company", "").strip()
        if company:
            by_company.setdefault(company.lower(), []).append(n)
        for tag in n.get("tags", []):
            by_tag.setdefault(tag, []).append(n)

    # Same company: contact <-> intel/task
    for company_key, cnodes in by_company.items():
        contacts = [n for n in cnodes if n["type"] == "contact"]
        others = [n for n in cnodes if n["type"] in ("intel", "task")]
        for c in contacts:
            for o in others:
                counter += 1
                edges.append({
                    "id": f"impl-co-{counter:04d}", "src": c["graph_id"], "dst": o["graph_id"],
                    "relationship": "works_at_company",
                    "strength": "strong",
                    "notes": f"Both at {c.get('company', '')}",
                    "explicit": False,
                })

    # Shared tags (>=2, cross-type only)
    seen_pairs = set()
    for tag, tnodes in by_tag.items():
        for i, a in enumerate(tnodes):
            for b in tnodes[i + 1:]:
                if a["type"] == b["type"]:
                    continue
                pair = tuple(sorted([a["graph_id"], b["graph_id"]]))
                if pair in seen_pairs:
                    continue
                shared = set(a.get("tags", [])) & set(b.get("tags", []))
                if len(shared) >= 2:
                    seen_pairs.add(pair)
                    counter += 1
                    edges.append({
                        "id": f"impl-tag-{counter:04d}", "src": a["graph_id"], "dst": b["graph_id"],
                        "relationship": "shared_context",
                        "strength": "strong" if len(shared) >= 3 else "moderate",
                        "notes": f"Shared tags: {', '.join(sorted(shared))}",
                        "explicit": False,
                    })

    return edges


def run_duckdb_analysis(nodes, edges):
    """Run DuckDB + DuckPGQ graph queries. Returns insights dict."""
    import duckdb

    HAS_PGQ = False
    conn = duckdb.connect()
    try:
        conn.execute("INSTALL duckpgq FROM community")
        conn.execute("LOAD duckpgq")
        HAS_PGQ = True
    except Exception:
        print("  Note: DuckPGQ extension not available. Graph path queries disabled. Basic analysis will still work.")

    # Load nodes
    conn.execute("CREATE TABLE nodes (id VARCHAR PRIMARY KEY, type VARCHAR, label VARCHAR, domain VARCHAR, company VARCHAR)")
    for n in nodes:
        conn.execute("INSERT INTO nodes VALUES (?, ?, ?, ?, ?)",
                     [n["graph_id"], n["type"], n["label"], n.get("domain", ""), n.get("company", "")])

    # Load edges
    conn.execute("CREATE TABLE edges (id VARCHAR, src VARCHAR, dst VARCHAR, relationship VARCHAR, strength VARCHAR, notes VARCHAR)")
    graph_ids = {n["graph_id"] for n in nodes}
    for e in edges:
        if e["src"] in graph_ids and e["dst"] in graph_ids:
            conn.execute("INSERT INTO edges VALUES (?, ?, ?, ?, ?, ?)",
                         [e["id"], e["src"], e["dst"], e["relationship"], e["strength"], e["notes"]])

    # Create property graph (requires DuckPGQ)
    if HAS_PGQ:
        conn.execute("""
            CREATE PROPERTY GRAPH chief_graph
            VERTEX TABLES (nodes)
            EDGE TABLES (edges SOURCE KEY (src) REFERENCES nodes(id)
                               DESTINATION KEY (dst) REFERENCES nodes(id))
        """)

    insights = {}

    # Most connected nodes
    try:
        r = conn.execute("""
            SELECT n.id, n.type, n.label, COUNT(*) as connections
            FROM nodes n JOIN edges e ON n.id = e.src OR n.id = e.dst
            GROUP BY n.id, n.type, n.label ORDER BY connections DESC LIMIT 10
        """).fetchall()
        insights["most_connected"] = [{"id": x[0], "type": x[1], "label": x[2], "connections": x[3]} for x in r]
    except Exception as e:
        insights["most_connected_error"] = str(e)

    # Orphan nodes
    try:
        r = conn.execute("""
            SELECT n.id, n.type, n.label FROM nodes n
            WHERE n.type NOT IN ('domain')
            AND n.id NOT IN (SELECT src FROM edges)
            AND n.id NOT IN (SELECT dst FROM edges)
        """).fetchall()
        insights["orphan_nodes"] = [{"id": x[0], "type": x[1], "label": x[2]} for x in r]
    except Exception as e:
        insights["orphan_nodes_error"] = str(e)

    # Cross-type connections
    try:
        r = conn.execute("""
            SELECT n1.type, n1.label, e.relationship, n2.type, n2.label, e.strength, e.notes
            FROM edges e JOIN nodes n1 ON e.src = n1.id JOIN nodes n2 ON e.dst = n2.id
            WHERE n1.type != n2.type AND e.strength IN ('strong', 'moderate')
            ORDER BY CASE e.strength WHEN 'strong' THEN 1 ELSE 2 END, e.relationship
        """).fetchall()
        insights["cross_type_connections"] = [
            {"source_type": x[0], "source": x[1], "relationship": x[2],
             "target_type": x[3], "target": x[4], "strength": x[5], "notes": x[6]}
            for x in r
        ]
    except Exception as e:
        insights["cross_type_connections_error"] = str(e)

    # Two-hop contact -> task paths (networking opportunities) -- requires DuckPGQ
    if HAS_PGQ:
        try:
            r = conn.execute("""
                FROM GRAPH_TABLE(chief_graph
                    MATCH (a:nodes)-[r1:edges]->(b:nodes)-[r2:edges]->(c:nodes)
                    WHERE a.type = 'contact' AND c.type = 'task'
                    COLUMNS (a.label AS contact, r1.relationship AS rel1,
                             b.label AS via, r2.relationship AS rel2, c.label AS task)
                )
            """).fetchall()
            insights["contact_to_task_paths"] = [
                {"contact": x[0], "rel1": x[1], "via": x[2], "rel2": x[3], "task": x[4]}
                for x in r
            ]
        except Exception as e:
            insights["contact_to_task_paths_note"] = str(e)
    else:
        insights["contact_to_task_paths_note"] = "DuckPGQ required for graph traversal queries"

    # Company clusters
    try:
        r = conn.execute("""
            SELECT company, COUNT(*) as items, COUNT(DISTINCT type) as diversity,
                   STRING_AGG(DISTINCT type, ', ') as types
            FROM nodes WHERE company != '' AND type != 'domain'
            GROUP BY company HAVING COUNT(*) >= 2
            ORDER BY diversity DESC, items DESC
        """).fetchall()
        insights["company_clusters"] = [
            {"company": x[0], "items": x[1], "type_diversity": x[2], "types": x[3]}
            for x in r
        ]
    except Exception as e:
        insights["company_clusters_error"] = str(e)

    # Domain density
    try:
        r = conn.execute("""
            SELECT n.domain, COUNT(DISTINCT n.id) as nodes, COUNT(DISTINCT e.id) as connections
            FROM nodes n LEFT JOIN edges e ON (n.id = e.src OR n.id = e.dst)
            WHERE n.type != 'domain' AND n.domain != ''
            GROUP BY n.domain
            ORDER BY CAST(connections AS FLOAT) / GREATEST(nodes, 1) DESC
        """).fetchall()
        insights["domain_density"] = [
            {"domain": x[0], "nodes": x[1], "connections": x[2],
             "density": round(x[2] / max(x[1], 1), 2)}
            for x in r
        ]
    except Exception as e:
        insights["domain_density_error"] = str(e)

    conn.close()
    return insights


def generate_findings(nodes, explicit_edges, implicit_edges, insights):
    """Generate actionable findings from graph analysis."""
    non_domain = [n for n in nodes if n["type"] != "domain"]
    meaningful_implicit = [e for e in implicit_edges if e["relationship"] != "belongs_to"]

    summary = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "graph_stats": {
            "total_nodes": len(non_domain),
            "by_type": dict(Counter(n["type"] for n in non_domain)),
            "domains": len(set(n.get("domain", "") for n in non_domain if n.get("domain", ""))),
            "explicit_connections": len(explicit_edges),
            "implicit_connections_discovered": len(meaningful_implicit),
            "total_edges": len(explicit_edges) + len(meaningful_implicit),
        },
        "insights": insights,
        "actionable_findings": [],
    }

    findings = []

    # Orphans
    orphans = insights.get("orphan_nodes", [])
    if orphans:
        findings.append({
            "type": "orphan_alert", "severity": "medium",
            "message": f"{len(orphans)} items have zero connections",
            "items": [f"{o['type']}: {o['label']}" for o in orphans[:5]],
        })

    # Company clusters with multiple types = networking opportunities
    for c in insights.get("company_clusters", []):
        if c["type_diversity"] >= 2:
            findings.append({
                "type": "company_opportunity", "severity": "high",
                "message": f"{c['company']}: {c['items']} items across {c['types']} -- leverage these connections",
            })

    # Strategic hubs
    most = insights.get("most_connected", [])
    if most:
        findings.append({
            "type": "strategic_hub", "severity": "info",
            "message": f"Most connected: {most[0]['label']} ({most[0]['type']}) with {most[0]['connections']} connections",
        })

    # Sparse domains
    for d in insights.get("domain_density", []):
        if d["density"] < 0.5 and d["nodes"] > 0:
            findings.append({
                "type": "sparse_domain", "severity": "low",
                "message": f"Domain '{d['domain']}' has low connection density ({d['density']}) -- needs more links",
            })

    summary["actionable_findings"] = findings
    return summary


def format_standup(summary):
    """Format for standup briefing."""
    lines = ["## Knowledge Graph Pulse", ""]
    s = summary["graph_stats"]
    lines.append(f"**Graph:** {s['total_nodes']} nodes | {s['explicit_connections']} explicit + {s['implicit_connections_discovered']} discovered connections")
    lines.append(f"**Nodes:** {' | '.join(f'{v} {k}s' for k, v in sorted(s['by_type'].items()))}")
    lines.append("")

    for f in summary.get("actionable_findings", []):
        sev = {"high": "[!!]", "medium": "[!]", "low": "[.]", "info": "[i]"}.get(f["severity"], "[-]")
        lines.append(f"- {sev} **{f['type'].replace('_', ' ').title()}:** {f['message']}")
        for item in f.get("items", [])[:3]:
            lines.append(f"  - {item}")

    cross = summary.get("insights", {}).get("cross_type_connections", [])
    if cross:
        lines.extend(["", "### Key Connections"])
        for c in cross[:7]:
            lines.append(f"- **{c['source']}** --({c['relationship']})--> **{c['target']}**")
            if c.get("notes"):
                lines.append(f"  _{c['notes']}_")

    paths = summary.get("insights", {}).get("contact_to_task_paths", [])
    if paths:
        lines.extend(["", "### Contact-to-Task Paths (2-hop)"])
        for p in paths[:5]:
            lines.append(f"- {p['contact']} --({p['rel1']})--> {p['via']} --({p['rel2']})--> {p['task']}")

    return "\n".join(lines)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Chief of Staff Knowledge Graph Engine")
    parser.add_argument("--standup", action="store_true", help="Standup-formatted output")
    parser.add_argument("--summary", action="store_true", help="One-line summary")
    parser.add_argument("--output", default="data/graph-insights.json")
    args = parser.parse_args()

    print("[graph] Building knowledge graph...")
    nodes, raw_map = build_nodes_and_raw_map()
    explicit_edges = build_explicit_edges(raw_map)
    implicit_edges = discover_implicit_edges(nodes)
    all_edges = explicit_edges + implicit_edges

    non_domain = [n for n in nodes if n["type"] != "domain"]
    meaningful_implicit = [e for e in implicit_edges]
    print(f"  Nodes: {len(non_domain)} ({', '.join(f'{v} {k}' for k, v in Counter(n['type'] for n in non_domain).items())})")
    print(f"  Explicit connections: {len(explicit_edges)}")
    print(f"  Implicit connections discovered: {len(meaningful_implicit)}")

    if args.summary:
        print(f"Graph: {len(non_domain)} nodes, {len(explicit_edges)}+{len(meaningful_implicit)} connections")
        return

    print("[graph] Running DuckDB + DuckPGQ analysis...")
    insights = run_duckdb_analysis(nodes, all_edges)

    summary = generate_findings(nodes, explicit_edges, implicit_edges, insights)
    save_json(args.output, summary)
    print(f"[graph] Analysis saved to {args.output}")

    if args.standup:
        print()
        print(format_standup(summary))
    else:
        # Console output
        for f in summary.get("actionable_findings", []):
            sev = {"high": "!!", "medium": "!", "low": ".", "info": "i"}.get(f["severity"], "-")
            print(f"  [{sev}] {f['message']}")

        most = insights.get("most_connected", [])
        if most:
            print("\n  Most Connected:")
            for m in most[:5]:
                print(f"    {m['connections']}x -- {m['type']}: {m['label']}")

        orphans = insights.get("orphan_nodes", [])
        if orphans:
            print(f"\n  {len(orphans)} orphan nodes (no connections)")

        clusters = insights.get("company_clusters", [])
        if clusters:
            print("\n  Company Clusters:")
            for c in clusters[:5]:
                print(f"    {c['company']}: {c['items']} items ({c['types']})")

        paths = insights.get("contact_to_task_paths", [])
        if paths:
            print("\n  Contact -> Task Paths:")
            for p in paths[:5]:
                print(f"    {p['contact']} ->({p['rel1']})-> {p['via']} ->({p['rel2']})-> {p['task']}")


if __name__ == "__main__":
    main()
