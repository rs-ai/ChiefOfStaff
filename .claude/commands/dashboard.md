# /dashboard — All-Domain Dashboard

Show a high-level status dashboard across all your domains. One screen, full picture.

## Steps

1. Read ALL domain files from `domains/`.
2. Read ALL JSON files from `data/`.

## Dashboard Output

### Header
```
CHIEF OF STAFF DASHBOARD — [Date]
```

### Domain Health Table

| # | Domain | Open | Overdue | Last Updated | Health |
|---|--------|------|---------|-------------|--------|

For each domain listed in CLAUDE.md:
- **Active:** Count tasks where domain = short-name AND status = "active"
- **Waiting:** Count tasks where domain = short-name AND type = "waiting-for" AND status = "active"
- **Overdue:** Count tasks where domain = short-name AND status = "active" AND due_date < today
- **Last Updated:** Domain file last modification date (use file timestamp)
- **Health:**
  - Green: updated within 7 days AND no overdue tasks
  - Yellow: not updated in 7-14 days OR has overdue tasks
  - Red: not updated in 14+ days OR has critical overdue tasks (priority = p1 AND overdue)

### Summary Stats

```
Tasks:  [X] open | [X] due this week | [X] overdue | [X] completed this week
Intel:  [X] captured this week | [X] actions pending
```

For "this week": always use calendar week (Monday through Sunday of the current week).
For "completed this week": tasks where status = "done" AND updated_at falls within current Monday-Sunday.

### Recommendation
Based on the dashboard data, recommend the **1-2 domains that need attention most** and why.

Priority logic:
1. Red health domains first
2. Domains with overdue high-priority tasks
3. Domains not updated in 14+ days
4. Yellow health domains

End with: **"Want to deep-dive into any domain? Run `/domain-review [name]`"**

## Format Rules
- Use the table format — it's the most scannable
- Health indicators: use text labels (GREEN / YELLOW / RED) for terminal compatibility
- Keep the entire dashboard to one screen — compress if needed
- If all data files are empty, show the table with zeros and all GREEN, with a note: "System just initialized. Start by adding tasks with `/add-task`."
