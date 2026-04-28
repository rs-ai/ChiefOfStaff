# /drift-check — Run Drift Prevention Agents

Detect drift, **fix what's safe, flag what's not.** This is not a report generator — it's a maintenance crew.

## Usage

- `/drift-check all` — Run all 6 agents (full maintenance pass)
- `/drift-check defender` — Security drift only
- `/drift-check healer` — Code drift only
- `/drift-check simplifier` — Complexity drift only
- `/drift-check psychologist` — Behavioral drift only
- `/drift-check consistency` — Data consistency only
- `/drift-check architect` — File system + knowledge graph only
- `/drift-check quick` — Cheap checks only (Consistency C1-C10 + Architect FS-03, FS-05, FS-07, KG-01, KG-02) — runs in <30 seconds, suitable for daily scan

## Core Principle: Fix First, Flag Second

Every agent follows this protocol:
1. **Detect** the issue
2. **Auto-fix** if the correction is unambiguous, reversible, and can't break functionality
3. **Flag** everything else for human review
4. **Log** every action taken (fixes AND flags) in the report

### What Gets Auto-Fixed (no human approval needed)

| Agent | Auto-Fixes |
|-------|-----------|
| **Defender** | Add missing .gitignore entries for sensitive files, __pycache__, *.pyc |
| **Healer** | Broken links, stale config values, dead code removal, typo fixes |
| **Simplifier** | Dead code removal, obvious nesting flattening |
| **Psychologist** | No file changes — acts by pushing quality and challenging laziness in the current session |
| **Consistency** | Missing `created_at`/`updated_at` timestamps, trailing whitespace, `"null"` string -> JSON null, manifest creation/update |
| **Architect** | .gitignore additions, stale .gitignore entry removal |

### What Gets Flagged (needs human decision)

- Duplicate IDs (which record gets renamed?)
- Enum values not in allowed set (add to set or fix the data?)
- File moves (HTML out of data/, markdown out of data/)
- Folder restructuring
- Deprecated directory removal
- Behavior-changing code fixes
- Knowledge graph: orphan rate actions, connection generation candidates

## Instructions

1. Read `drift-prevention/framework.md` for the overall approach
2. Read the specific agent spec from `drift-prevention/agents/{agent}.md`
3. For Architect: also read `architecture-spec.md` as the reference standard
4. **Execute fixes** for everything in the auto-fix list
5. **Flag** everything else with clear recommended action
6. Produce the report

### When running ALL agents:

Run in this order (dependencies matter):
1. **Defender + Consistency + Architect** — run in parallel (independent)
2. **Healer** — runs after the above complete (needs clean data to work on)
3. **Simplifier** — runs after Healer
4. **Psychologist** — runs last (reviews quality of everything, including the drift fixes)

### When running QUICK checks (daily scan integration):

Run only the cheap, fast checks:
- Consistency: C1-C10 (JSON validity, record counts, ID checks, enums, referential integrity)
- Architect: FS-03 (CLAUDE.md references), FS-05 (build artifacts), FS-07 (sensitive files), KG-01/KG-02 (broken edges)

Auto-fix what's safe. Flag the rest. Total time: <30 seconds.

## Output

```
=== DRIFT PREVENTION REPORT ===
Date: {date}
Mode: {all / quick / individual agent}
Agents Run: {list}

FIXES APPLIED:
  [FIX] {agent}: {what was fixed} — {file}

FLAGGED FOR HUMAN:
  [FLAG] {severity}: {agent}: {what needs decision} — {recommended action}

SUMMARY:
- Fixed: {count}
- Flagged: {count} (Critical: {n}, Error: {n}, Warning: {n}, Info: {n})

Overall Health: {CLEAN / NEEDS ATTENTION / CRITICAL}
=== END REPORT ===
```

Save the report to `data/drift-report-latest.md`.
