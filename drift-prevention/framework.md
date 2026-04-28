# Drift Prevention Framework

**Version:** 1.0
**Purpose:** Prevent the 6 types of drift that accumulate in AI-assisted projects.

---

## Why This Exists

AI-assisted projects grow fast. An AI agent generates code, data, and structure at speed — but doesn't maintain at speed. Over time, small inconsistencies compound:

- Security vulnerabilities creep in via dependencies or rushed code
- Bugs accumulate in corners no one revisits
- Abstractions pile up without justification
- The AI itself becomes passive, waiting instead of solving
- Data contradicts itself across files
- File systems sprawl and knowledge graphs decay

These are not bugs. They are **drift** — the slow, silent degradation of system integrity. Each type of drift has its own agent.

## The 6 Pillars

| # | Agent | Drift Type | What It Prevents |
|---|-------|-----------|-----------------|
| 1 | **Defender** | Security drift | Vulnerabilities, leaked secrets, dependency CVEs, OWASP violations |
| 2 | **Healer** | Code drift | Bugs, broken imports, stale config, dead code, type errors |
| 3 | **Simplifier** | Complexity drift | Over-engineering, unnecessary abstractions, deep nesting, bloat |
| 4 | **Psychologist** | Behavioral drift | AI passivity, lazy shortcuts, low-quality output, blocked-without-trying |
| 5 | **Consistency** | Data drift | Contradictions across files, schema violations, stale data, data loss |
| 6 | **Architect** | Structural drift | File system sprawl, naming chaos, knowledge graph decay, orphaned structures |

## How They Work

### Scan Method: Random + Targeted

Agents 1-4 (Defender, Healer, Simplifier, Psychologist) use **random scanning** — picking a random starting point each run to avoid predictable blind spots. This ensures every corner of the project eventually gets attention.

Agents 5-6 (Consistency, Architect) use **full scanning** — they check the entire data set and file system against defined specs. Consistency is meaningless if you only check half the data.

### Severity Model (Universal)

| Level | Meaning | Response |
|-------|---------|----------|
| **CRITICAL** | Active harm — data loss, security breach, broken functionality | STOP. Fix immediately. Block further work. |
| **HIGH/ERROR** | Integrity violation — unreliable data, exploitable vulnerability | Fix this session. Flag in briefing. |
| **MEDIUM/WARNING** | Quality degradation — inconsistency, complexity, staleness | Fix within 7 days. Include in reports. |
| **LOW/INFO** | Best practice violation — minor, no immediate harm | Log for periodic review. |

### Auto-Fix Rules (Universal)

**Conservative by default.** Auto-fix only when:
1. The correction is **unambiguous** (only one possible fix)
2. The correction is **reversible** (can be undone if wrong)
3. The correction **cannot break functionality** (whitespace, timestamps, formatting)

Everything else: **flag for human review.** Bad auto-fixes erode trust faster than the drift itself.

### Constraints (Universal)

1. **Never break existing functionality.** Fix the problem, not the feature.
2. **Never delete data.** Mark as archived/deprecated, never remove.
3. **Never suppress without reason.** If you skip a check, log why.
4. **Respect the "never delete" rule in CLAUDE.md.** Status changes, not record removal.

## Execution Model

### Per-Project Triggers

Each project decides how to trigger drift checks:

| Trigger | What Runs | When |
|---------|----------|------|
| `/drift-check all` | All 6 agents sequentially | On-demand |
| `/drift-check [agent]` | Single agent | On-demand |
| Orchestrator integration | All agents in Phase 1 | Part of orchestrator runs |
| Daily scan integration | Cheap checks from Consistency + Architect | Before daily standup |

### Frequency Guide

| Agent | Minimum Frequency | Why |
|-------|------------------|-----|
| Defender | Every deploy/push | Security gates must block releases |
| Healer | Weekly | Bugs compound if left more than a week |
| Simplifier | Monthly | Complexity is slow drift, not urgent |
| Psychologist | Every significant output | Quality degrades per-output, not per-calendar |
| Consistency | Session start (cheap), weekly (full) | Data integrity must be verified before acting on data |
| Architect | Monthly (full), session start (critical checks) | Structure changes slowly |

## Output

Each agent produces a report section with:
- Scan path or scope
- Findings table: severity, location, issue, status (FIXED/FLAGGED)
- Health score (agent-specific metric)
- Recommendations

Reports integrate into the project's existing briefing/standup system.

## Adapting for New Projects

When deploying to a new project:

1. Copy `drift-prevention/` folder
2. Create `architecture-spec.md` for the project (Architect needs a reference)
3. The Consistency agent auto-discovers data files on first run (no config needed)
4. The Psychologist is universal — no project-specific tuning required
5. Add `/drift-check` command to `.claude/commands/`
6. Reference from CLAUDE.md (one line: `See drift-prevention/framework.md`)

## Agent Specs

Each agent's full specification lives in `drift-prevention/agents/`:

- [`defender.md`](agents/defender.md) — Security drift
- [`healer.md`](agents/healer.md) — Code drift
- [`simplifier.md`](agents/simplifier.md) — Complexity drift
- [`psychologist.md`](agents/psychologist.md) — Behavioral drift
- [`consistency.md`](agents/consistency.md) — Data drift
- [`architect.md`](agents/architect.md) — Structural drift (file system + knowledge graph)
