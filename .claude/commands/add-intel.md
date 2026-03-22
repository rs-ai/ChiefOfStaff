# /add-intel — Capture Intelligence

Capture a piece of industry intelligence, news, insight, or research finding.

## Arguments
- `$ARGUMENTS` — The intelligence to capture (URL, headline, observation, or insight)

## Steps

1. **Parse input.** If `$ARGUMENTS` provided, use it. If empty, ask: "What did you learn or find?"

2. **Determine domain.** Infer which domain(s) from CLAUDE.md this is most relevant to.

3. **Create summary.** If input is a URL, describe what's at the URL and why it matters. If input is text, create a 2-3 sentence summary.

4. **Assess relevance.** Write a one-line statement of why this matters specifically to the user's situation — connect it to their goals, role, or domains.

5. **Assess action required.** Does this need a follow-up task?
   - Affects a pending decision → action_required: true
   - Requires the user to do something → action_required: true
   - Good-to-know, no action needed → action_required: false

6. **Generate ID.** Format: `{domain-short-name}-{YYYYMMDD}-{HHMMSSmmm}` (with milliseconds to prevent collisions)

7. **Read `data/intelligence.json`**, append:
   ```json
   {
     "id": "generated-id",
     "domain": "domain-short-name",
     "title": "concise headline",
     "summary": "2-3 sentence summary",
     "source": "URL or source description",
     "relevance": "why this matters to the user specifically",
     "category": "intel",
     "action_required": true/false,
     "captured_date": "YYYY-MM-DD",
     "tags": ["relevant", "tags"]
   }
   ```

8. **Write updated `data/intelligence.json`.**

9. **If action_required is true**, also create a task in `data/tasks.json`:
   - Title: "Follow up: [intel title]"
   - Domain: same domain
   - Priority: medium (unless obviously urgent)
   - Notes: "Linked to intel: [intel-id]"

10. **Confirm:** "Intel captured: **[title]** → [Domain Name]. Action required: [yes/no]"
    - If action created: "Task also created: [task title]"

## Rules
- Be fast — capture first, refine later
- Connect every piece of intel to the user's specific context (not generic "this is important")
- When in doubt about action_required, default to false — don't create noise
