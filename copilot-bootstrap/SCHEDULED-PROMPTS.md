# AI Chief of Staff — Scheduled Prompt Templates

> **These prompts use 5 of your 10 available scheduled prompt slots** in M365 Copilot. Keep the other 5 for future use or personal prompts.

## How to Set Up a Scheduled Prompt

1. Open M365 Copilot (in Teams or at microsoft365.com/copilot)
2. Paste the prompt text and press Enter
3. Review the response to make sure it works correctly
4. Hover over the response and click the **Schedule** icon (clock/calendar icon)
5. Set the frequency (daily, weekly, monthly) and delivery method (email)
6. Choose the time you want it delivered

If you don't see the Schedule icon, your tenant may not have it enabled yet. Ask your IT admin about "Copilot scheduled prompts" or check back after the next M365 update.

---

## Prompt 1: Morning Briefing

**Purpose:** The daily hook. Arrives before you open Copilot so you start every day informed.

**Frequency:** Every weekday (Monday-Friday)
**Delivery:** Email, 30 minutes before your first typical meeting
**Slot:** 1 of 5

### Prompt

```
Read my StrategicPriorities.docx, People.docx, and ChiefPreferences.docx from my ChiefOfStaff folder. Then do the following:

1. EMAILS: Scan emails received since the last working day. Group into two lists: (a) Needs my response — sender, subject, one-line summary, and why it matters. (b) FYI only — sender, subject, one line. Limit to the 5 most important in each group.

2. TEAMS: Check Teams messages from the last working day that explicitly ask me a question or request something. List who, what channel, and what they need. Skip casual chat.

3. TODAY'S MEETINGS: List each meeting with time, attendees, and one line of context: what it is about and which of my strategic priorities it connects to. Flag any meeting where I should prepare something specific.

4. OVERDUE AND DUE TODAY: If I have a file called ChiefWorkbook.xlsx, check the Registry sheet for items where Status is open and DueDate is today or past due. If I have ChiefRegistry.docx instead, check the Tasks and Decisions sections for anything overdue or due today. List what you find. If neither file exists, skip this section.

5. CHIEF NOTICED: End with ONE observation I have not asked about. A pattern in my emails, a meeting that conflicts with my priorities, a person I have not heard from in a while, or a risk I might be overlooking. Be specific and opinionated.

Format: bullet points, grouped by section, no paragraphs. Lead with the most urgent item across all sections.
```

### What to check when it arrives
- Are the emails correctly grouped by urgency?
- Do meeting summaries connect to your actual priorities?
- Is the "Chief Noticed" insight specific and useful, not generic?

---

## Prompt 2: Weekly Review

**Purpose:** The accountability check. Forces you to confront what moved, what stalled, and what is due next.

**Frequency:** Every Friday
**Delivery:** Email, mid-afternoon (gives you time to act before end of week)
**Slot:** 2 of 5

### Prompt

```
Read my StrategicPriorities.docx from my ChiefOfStaff folder. Then do the following weekly review:

1. OPEN ITEMS BY PRIORITY: If I have ChiefWorkbook.xlsx, read the Registry sheet. If I have ChiefRegistry.docx, read the Tasks and Decisions sections. Group all open items by priority: Now (high priority or overdue), Soon (due within 14 days), and Someday (no due date or due date beyond 14 days). Show the title, type, and due date for each.

2. PROGRESS THIS WEEK: List items whose status changed this week or that were completed and moved to Archive. If nothing changed, say so plainly.

3. STALE ITEMS: Flag any open item that has not been updated in 14 or more days. Show the title, type, and how many days since the last update.

4. NEXT WEEK: List items with due dates in the next 7 calendar days. Include the title, type, due date, and which strategic priority it supports.

5. STRATEGIC CHECK: Based on my StrategicPriorities.docx, which priority got the most attention this week? Which got the least? Is the balance right?

Format: grouped sections, bullet points, concise. No paragraphs. If any section has zero items, say "None" and move on.
```

### What to check when it arrives
- Are stale items actually stale, or did you complete them outside the system?
- Does the strategic balance section reflect reality?
- Update or close items that are done before the weekend

---

## Prompt 3: Friday Wins

**Purpose:** The retention hook. Reminds you the system is working and celebrates progress.

**Frequency:** Every Friday (arrives after the Weekly Review, or combine into one slot)
**Delivery:** Email, late afternoon
**Slot:** 3 of 5

### Prompt

```
Read my ChiefOfStaff folder. Check ChiefWorkbook.xlsx (all sheets: Capture, Registry, Archive) or ChiefCapture.docx and ChiefRegistry.docx if I use Word instead.

Give me a Friday Wins summary:

1. COMPLETED: Count the items completed or archived this week. List the top 3 by impact.

2. CAPTURED: Count new items added to Capture this week. This tells me how much I used the system.

3. MEETINGS PREPPED: Check my calendar for this week. How many meetings did I have? For how many did I open Copilot to prepare? Estimate based on our conversation history this week.

4. DECISIONS MADE: Count any items of type "decision" that were resolved this week.

5. STREAK: Check ChiefPreferences.docx for a "Current Streak" line. If it exists, add this week's active days. If I used Chief every workday this week, add 5. If I missed days, reset to the count of consecutive days from this week only. Update the streak count in ChiefPreferences.docx so it persists across weeks.

6. TOP WIN: Pick the single most impactful thing I completed or progressed this week. Tell me why it matters in one sentence.

Tone: brief, celebratory, specific. No fluff. End with one sentence of encouragement that references a specific accomplishment, not a generic motivational quote.
```

### What to check when it arrives
- Does the completed count match your sense of the week?
- If the streak is broken, consider what got in the way
- The top win should feel right. If it picks the wrong thing, your priority tagging may need updating.

---

## Prompt 4: Monthly Strategic Nudge

**Purpose:** The deep think trigger. Surfaces decisions you have been sitting on and documents going stale.

**Frequency:** 1st of every month
**Delivery:** Email, morning
**Slot:** 4 of 5

### Prompt

```
Read all files in my ChiefOfStaff folder: StrategicPriorities.docx, People.docx, LandscapeAndSignals.docx, ChiefPreferences.docx, and either ChiefWorkbook.xlsx or ChiefRegistry.docx.

Give me a monthly strategic nudge:

1. STALE DECISIONS: Find any items of type "decision" that have been open for more than 30 days. For each one, list the title, how many days it has been open, and ask me directly: "What is holding you back on this?"

2. PARKED THOUGHTS: If I have items tagged as "thought" or "someday" or in a Thoughts section, surface 2-3 worth revisiting. Tell me why now might be the right time.

3. DOCUMENT FRESHNESS: Check when StrategicPriorities.docx, People.docx, and LandscapeAndSignals.docx were last modified. If any is older than 90 days, flag it: "Your [document] hasn't been updated in [X] days. Has your world changed since then?"

4. DECISION JOURNAL: Find decisions marked as completed or resolved 90 or more days ago. For each one, ask: "You decided [X] three months ago. How did it play out? Would you decide the same way today?"

5. PRIORITY DRIFT: Compare my open tasks and recent activity against my StrategicPriorities.docx. Am I spending time on things that do not connect to my stated priorities? Call it out.

Tone: direct, provocative, coaching. Challenge me. Do not be polite about stale decisions. If something has been sitting for 45 days, say so bluntly.
```

### What to check when it arrives
- Are the stale decisions actually unresolved, or did you decide without logging it?
- Update any knowledge base docs flagged as stale
- Spend 15 minutes on the decision journal questions. They compound over time.

---

## Prompt 5: Maintenance Reminder

**Purpose:** The system health nudge. Keeps your data layer clean so everything else works.

**Frequency:** Monthly (15th of each month, offset from the Strategic Nudge)
**Delivery:** Email, morning
**Slot:** 5 of 5

### Prompt

```
Read my ChiefOfStaff folder. Check ChiefWorkbook.xlsx (Capture, Registry, and Archive sheets) or ChiefCapture.docx and ChiefRegistry.docx if I use Word.

Give me a system maintenance report:

1. CAPTURE INBOX: Count items in Capture where Status is "new" or has no status. These have not been processed yet. If more than 5, say: "Your capture inbox has [X] unprocessed items. Time to promote or discard them."

2. STALE REGISTRY: Count open items in Registry that have not been updated in 30 or more days. List the top 5 oldest. For each, ask: "Still active, or should this be archived?"

3. PREFERENCES CHECK: Check when ChiefPreferences.docx was last modified. If older than 60 days, say: "Your preferences file is [X] days old. Have your working patterns or priorities shifted?"

4. SYSTEM HEALTH SCORE: Rate the system 1-5 based on: capture inbox size (fewer unprocessed is better), registry staleness (fewer stale items is better), and document freshness (recently updated is better). Show the score and one sentence explaining it.

5. RECOMMENDED ACTION: Say: "Open a session with your Chief of Staff and say: Run maintenance. I will walk you through cleaning up your capture inbox, archiving stale items, and updating your preferences."

Keep this short. No more than 15 lines total. Actionable, not nagging.
```

### What to check when it arrives
- If the health score is 3 or below, schedule 20 minutes for cleanup
- Process any unprocessed capture items (promote to Registry or discard)
- Archive anything in Registry that is done or no longer relevant

---

## Quick Reference

| # | Prompt | Frequency | Day/Time | Slot |
|---|--------|-----------|----------|------|
| 1 | Morning Briefing | Weekdays | 30 min before first meeting | 1 |
| 2 | Weekly Review | Weekly | Friday mid-afternoon | 2 |
| 3 | Friday Wins | Weekly | Friday late afternoon | 3 |
| 4 | Monthly Strategic Nudge | Monthly | 1st of month, morning | 4 |
| 5 | Maintenance Reminder | Monthly | 15th of month, morning | 5 |

**Tip:** If you want to save a slot, combine Prompts 2 and 3 into a single Friday prompt. Append the Friday Wins section to the Weekly Review prompt. That frees up a slot for something custom.
