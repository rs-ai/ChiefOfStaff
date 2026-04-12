# Example Evening Debrief

*This is what a typical `/debrief` output looks like. All names, roles, and scenarios are entirely fictitious.*

---

**Friday, March 21, 2026**

## What Happened Today

- Finalized Q2 OKRs with leadership team — aligned on 4 objectives, deferred one metric to next week
- Vendor demo for project management tool went well — evaluation framework scored it 7/10, missing SSO integration
- 1:1 with S.M. surfaced a retention risk — they're being recruited externally. Drafted counter-proposal talking points.
- Missed the intelligence briefing review — rolled to Monday

## Tasks Updated

| Task | Domain | Status | Notes |
|------|--------|--------|-------|
| Submit speaker proposal for Tech Summit | Career | **Completed** | Submitted before deadline |
| Finalize Q2 OKRs | Strategy | **In Progress** | 4/5 objectives locked, one deferred |
| Vendor evaluation write-up | Strategy | **New** | Created from today's demo — due Mar 28 |
| Draft retention counter-proposal for S.M. | Leadership | **New** | PREP — talking points ready for your review |

## New Intel Captured

- **[RESEARCH]** Project management tooling market consolidating — two mid-tier vendors acquired in Q1. Affects build-vs-buy decision.
- **[INTEL]** S.M. mentioned industry trend toward skills-based hiring over credential-based. Worth tracking for team development strategy.

## Tomorrow's Priorities

1. **YOURS** — Review retention counter-proposal for S.M. before Monday 1:1
2. **PREP** — Monday leadership sync agenda (draft ready by morning briefing)
3. **DISPATCH** — Research upcoming industry conference speakers and topics
4. **SKIP** — Conference CFP roundup (deadline is April 15, no rush)

## Sensitivity Sweep

- `data/tasks.json` — clean, no sensitive data detected
- `data/intelligence.json` — [SENSITIVITY FLAG] New entry contains named individual assessment (SENSITIVE). File is gitignored.
- `data/contacts.json` — Using initials only. Compliant.
- **Reminder:** git-crypt is not yet configured. Sensitive files are local-only via .gitignore.

## System Improvement Proposal

**Friction noticed:** During the vendor demo, I wanted to log the evaluation score but there's no `data/evaluations.json` file. I stored it as a decision log entry, which felt awkward.

**Proposed change:** Add a row to the Data Files table in CLAUDE.md:
```
| `data/evaluations.json` | Vendor/tool evaluations with scores |
```

**Why:** Evaluations are distinct from decisions — they have structured scores, criteria, and comparisons. Mixing them into decisions.json makes both harder to query.

*Awaiting your approval before making this change.*

---

**Chief of Staff signing off. See you in the morning.**
