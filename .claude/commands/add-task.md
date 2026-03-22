# /add-task — Quick Task Capture

Capture a new task quickly. User provides the description as an argument or you ask.

## Arguments
- `$ARGUMENTS` — Task description (optional, will ask if not provided)

## Steps

1. **Parse input.** If `$ARGUMENTS` is provided, use it as the task title/description. If empty, ask: "What's the task?"

2. **Determine domain.** Infer from context if obvious. If unclear, show:
   ```
   Which domain?
   [List domains read from the Domains table in CLAUDE.md]
   ```

3. **Determine priority.** Infer from language:
   - urgent/critical/asap/blocking → `high`
   - should/need/important → `medium`
   - might/could/nice-to-have/when-possible → `low`
   - If unclear, default to `medium`

4. **Determine due date.** Only ask if the task sounds time-sensitive. Otherwise, set to `null`.

5. **Generate ID.** Format: `{domain-short-name}-{YYYYMMDD}-{HHMMSSmmm}` (with milliseconds to prevent collisions).

6. **Read `data/tasks.json`**, append the new record:
   ```json
   {
     "id": "generated-id",
     "domain": "domain-short-name",
     "title": "concise task title",
     "description": "fuller description if provided",
     "status": "active",
     "type": "next-action",
     "priority": "p2",
     "due_date": "YYYY-MM-DD or null",
     "defer_date": null,
     "flagged": false,
     "energy": "medium",
     "estimated_minutes": null,
     "waiting_on": null,
     "waiting_since": null,
     "tags": ["inferred", "tags"],
     "subtasks": [],
     "deliverable": null,
     "notes": "",
     "created_at": "ISO timestamp",
     "updated_at": "ISO timestamp",
     "completed_at": null,
     "review_interval_days": 7,
     "last_reviewed": null
   }
   ```

7. **Write updated `data/tasks.json`** back.

8. **Confirm:** "Task added to **[Domain Name]**: [title] (priority: [X])"

## Rules
- Be fast — this is a quick capture, not a conversation
- Infer as much as possible from context to minimize questions
- If the user gives a one-liner, that's the title. Don't ask for more detail.
- Tags should be 2-4 relevant keywords inferred from the title
