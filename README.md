# AI Chief of Staff

**An AI-powered executive operating system that runs your life across every domain that matters.**

Point your AI coding tool at this repo. It becomes your Chief of Staff — proactive, opinionated, and relentless about follow-through.

---

## What This Does

You clone this repo. You edit one file (`CLAUDE.md`) with your details. You open your AI tool. It reads the instructions and becomes a Chief of Staff that:

- **Manages your life domains** — career, strategy, leadership, family, health, side projects — whatever matters to you
- **Runs a daily operating rhythm** — morning briefings, evening debriefs, proactive nudges throughout the day
- **Tracks everything and follows up** — tasks, contacts, decisions, meetings, intelligence. Nothing slips through the cracks.
- **Maintains a knowledge graph** — discovers connections between your contacts, tasks, and intelligence. Surfaces insights like "this task + this contact + this news = time to act."
- **Runs background research agents** — persistent agents that search on a cadence (industry news every 3 days, conferences every 7 days). They only surface what's new.
- **Challenges you** — no sycophancy. Pushes back when priorities don't make sense. Holds you accountable.
- **Classifies every item** — DISPATCH (AI handles it), PREP (AI does 80%), YOURS (needs your judgment), SKIP (low priority)
- **Guards your data** — auto-detects sensitive information, classifies it, and keeps it local until encrypted

## Who This Is For

- **Executives and senior leaders** managing multiple domains of responsibility
- **Professionals** managing career growth alongside day-to-day responsibilities
- **Founders and side-project builders** juggling professional and personal initiatives
- **Anyone who wants an AI that acts, not just answers**

## Works With Any AI Coding Tool

This is not a plugin or extension. It's a structured repo with instructions that any AI tool can read.

| Tool | How to Use |
|------|-----------|
| **Claude Code** | `cd ai-chief-of-staff && claude` — reads CLAUDE.md automatically |
| **Codex (OpenAI)** | `cd ai-chief-of-staff && codex` — reads AGENTS.md automatically |
| **Gemini CLI** | `cd ai-chief-of-staff && gemini` — reads GEMINI.md automatically |
| **Aider** | `cd ai-chief-of-staff && aider` — reads conventions from repo |
| **Cursor / Windsurf** | Open folder — reads project instructions from repo |
| **Any MCP-capable tool** | Point it at the repo root |

The `CLAUDE.md` file is the primary instruction set. For non-Claude tools, adapter files (`AGENTS.md`, `GEMINI.md`) translate the same instructions into tool-specific formats.

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-chief-of-staff.git
cd ai-chief-of-staff

# 2. Edit CLAUDE.md — fill in the {{placeholders}} with your details
#    This takes 10-15 minutes. It's the only setup you need.

# 3. Open your AI tool
claude                    # Claude Code
# or: codex              # OpenAI Codex
# or: gemini             # Google Gemini CLI

# 4. Your Chief of Staff is live.
#    Try: "Good morning, what should I focus on today?"
```

## What's Inside

```
ai-chief-of-staff/
├── CLAUDE.md                          # The operating system (edit this)
├── AGENTS.md                          # Codex/OpenAI adapter
├── GEMINI.md                          # Gemini CLI adapter
├── mistakes.md                        # Learning log (grows over time)
│
├── domains/                           # Your life domains (examples — customize)
│   ├── 01-current-role.md             # Example: your day job
│   ├── 02-career-growth.md            # Example: career development
│   ├── 03-leadership.md               # Example: team & org leadership
│   ├── 04-side-projects.md            # Example: projects outside work
│   ├── 05-health.md                   # Example: health & wellbeing
│   ├── 06-learning.md                 # Example: learning & development
│   └── ...                            # Add as many as you need
│
├── data/                              # Structured data (JSON)
│   ├── tasks.json                     # Tasks across all domains
│   ├── intelligence.json              # News, insights, research
│   ├── contacts.json                  # Network & stakeholders
│   ├── decisions.json                 # Decision log
│   ├── meetings.json                  # Meeting prep & outcomes
│   ├── connections.json               # Knowledge graph relationships
│   └── background-research-agents.json # Persistent research agents
│
├── frameworks/                        # Decision frameworks
│   ├── ai-use-case-evaluation.md      # Evaluating AI initiatives
│   ├── stakeholder-influence-map.md   # Mapping stakeholder dynamics
│   ├── executive-narrative.md         # Crafting C-suite communications
│   ├── build-vs-buy.md               # Technology decisions
│   ├── data-maturity-model.md         # Assessing organizational maturity
│   ├── team-capability-matrix.md      # Skills gaps & hiring
│   └── eval-framework.md             # Evaluating solutions
│
├── .claude/commands/                  # Slash commands
│   ├── briefing.md                    # /briefing — morning touch point
│   ├── debrief.md                     # /debrief — evening capture
│   ├── add-task.md                    # /add-task — quick task capture
│   ├── add-intel.md                   # /add-intel — capture intelligence
│   ├── dashboard.md                   # /dashboard — all-domain status
│   └── domain-review.md              # /domain-review — deep dive
│
├── scripts/
│   ├── graph-query.py                 # Knowledge graph engine (DuckDB)
│   ├── notify.py                      # Email notifications (optional)
│   └── .env.example                   # Email config template
│
└── examples/
    ├── example-briefing.md            # What a morning briefing looks like
    ├── example-debrief.md             # What an evening debrief looks like
    └── example-dashboard.md           # What a dashboard looks like
```

## Key Features

### Daily Operating Rhythm
Your Chief of Staff runs a daily standup that scans everything — tasks, contacts, news, your knowledge graph — and writes results to files. When you open a session, it briefs you from the scan. No wasted tokens re-scanning.

### Knowledge Graph
Every piece of data connects to every other piece. A contact links to intelligence about their company, which links to a task you created last week. The Chief of Staff surfaces these connections automatically.

### Background Research Agents
Persistent agents that run on a cadence:
- **Intelligence scanner** — every 3 days, finds relevant industry news
- **Conference scanner** — weekly, finds speaking opportunities

Each agent compares findings against what it already knows and only surfaces what's new.

### Contact Staleness Tracking
Every contact has a tier (1/2/3) and a staleness threshold. Tier 1 contacts get flagged after 14 days of no outreach. The Chief of Staff tracks whether you actually reached out — not just whether you said you would.

### Action Accountability
Surfacing information is not the job. **Ensuring action is the job.** Every briefing checks: "You said you'd do X. Did you?" High-priority items sitting untouched for 3+ days get flagged.

### Data Sensitivity Auto-Detection
When writing to any data file, the system auto-detects sensitive content (salary info, named individuals with opinions, health data) and flags it. Critical data (passwords, API keys) is refused entirely.

### Item Classification
Every item surfaced gets classified:
- **DISPATCH** — AI handles completely (research, drafts)
- **PREP** — AI does 80%, you finish (board updates, talking points)
- **YOURS** — Requires your judgment (strategy decisions, live conversations)
- **SKIP** — Low priority, distant deadline

## Customization

### Add or Remove Domains
The included domains are examples. Add, remove, or rename them to match your priorities. Each domain is a markdown file in `domains/` — add context, goals, and current state.

### Add Frameworks
Drop any decision framework into `frameworks/` as a markdown file. Reference it in `CLAUDE.md` and the Chief of Staff will use it when relevant.

### Add Background Research Agents
Edit `data/background-research-agents.json` to add new persistent research topics. Define the scope, cadence, and output file.

### Configure Email Notifications
Copy `scripts/.env.example` to `scripts/.env`, add your email API key, and the Chief of Staff will email you intelligence updates, contact reminders, and domain alerts.

## Philosophy

This system is built on a few beliefs:

1. **An AI assistant should act, not just answer.** If it surfaces a task, it should track whether you did it.
2. **Everything is connected.** Contacts, news, tasks — they form a graph. The value is in the connections.
3. **Proactive beats reactive.** Don't wait to be asked. Surface what matters before it becomes urgent.
4. **Simple systems that grow.** Start with markdown and JSON. Upgrade to a database when the data demands it.
5. **Privacy by default.** Your data stays local. Sensitive content is flagged and protected.

## Inspired By

- [gstack](https://github.com/garrytan/gstack) by Garyy Tan — the model for packaging AI workflows as a shareable repo
- The real-world operating rhythm of executive Chiefs of Staff
- Personal knowledge management systems (Zettelkasten, PARA, GTD)

## License

MIT — use it, fork it, make it yours.

## Contributing

Found a better framework? Built a useful slash command? Open a PR. The system gets better through use.

---

**Built by someone who needed a Chief of Staff and built one.**
