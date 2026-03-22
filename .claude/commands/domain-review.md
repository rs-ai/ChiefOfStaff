# /domain-review — Deep Dive One Domain

Deep dive into a specific domain. Shows current state, tasks, intel, contacts, decisions, and strategic analysis.

## Arguments
- `$ARGUMENTS` — Domain name or number (optional, will ask if not provided)

## Steps

1. **Select domain.** If `$ARGUMENTS` provided, match to domain short-name or number. If not provided, show:
   ```
   Which domain to review?
   [List domains read from the Domains table in CLAUDE.md]
   ```

2. **Read the domain file** from `domains/XX-[short-name].md`.

3. **Read all JSON files** and filter by domain short-name:
   - `data/tasks.json` → all records where domain = short-name
   - `data/intelligence.json` → all records where domain = short-name
   - `data/contacts.json` → all records where domain = short-name
   - `data/decisions.json` → all records where domain = short-name
   - `data/meetings.json` → all records where domain = short-name

4. **Read relevant framework** from `frameworks/` if one applies to this domain. Scan the list in CLAUDE.md and pick whichever framework best fits the domain under review. If none clearly applies, skip this step.

## Review Structure

### Domain Status
- Summary from the domain file: current state, active initiatives

### Open Tasks ([count])
- List all where status = "active" or "waiting"
- Sort by priority then due_date
- If zero: "No open tasks in this domain."

### Recent Intelligence ([count])
- Last 10 items, most recent first
- If zero: "No intelligence captured for this domain."

### Key Contacts ([count])
- All contacts in this domain
- Flag any exceeding staleness threshold

### Decisions Made ([count])
- Active decisions, most recent first
- If zero: "No decisions logged."

### Upcoming Meetings
- Meetings linked to this domain with status = "upcoming"

### Strategic Analysis
Using the relevant framework(s):
- **What's going well** — concrete observations from the data
- **What needs attention** — gaps, staleness, overdue items
- **One recommendation** — the single most impactful thing to move this domain forward

### Update Offer
Ask: **"Want me to update the domain file with anything from this review?"**

If yes, update the domain file's Recent Updates and Next Actions sections.

## Rules
- Be opinionated in the strategic analysis — don't hedge
- Connect observations to the user's aspirations and goals
- If a framework applies, use it explicitly (reference specific dimensions/criteria)
- Keep it scannable — tables and bullet points, not paragraphs
