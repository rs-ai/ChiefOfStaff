# AI Chief of Staff for Microsoft 365

Build your own AI Chief of Staff using M365 Copilot. No coding. No admin access. 30 minutes to set up.

## What It Does

A personal strategic advisor that knows your priorities, your people, and your landscape. Five capabilities:

- **Morning briefing** — what matters today, meetings to prep for, what's slipping
- **Meeting prep** — stakeholder context, talking points, what to listen for
- **Capture session** — brain dump everything on your mind, Chief sorts and classifies it
- **Strategic brainstorm** — frameworks (Eisenhower, Eat That Frog, RPM, GTD) to sharpen your thinking
- **System maintenance** — archive old items, flag stale work, keep the system healthy

It reads your calendar, emails, and a personal knowledge base you build during setup. Gets smarter over time as you use it.

## The Habit Stack

1. **Email hook** — automated morning briefing arrives in your inbox (no action needed)
2. **Daily session** — 30-min calendar block with Chief (prep meetings, capture thoughts, think strategically)
3. **Compounding system** — the more you capture, the better the briefings get

## Get Started

1. Open [SETUP.md](SETUP.md) and copy the full prompt
2. Paste into M365 Copilot (Teams or microsoft365.com/copilot)
3. Follow the interactive setup — Copilot guides you step by step
4. You'll get your first useful insight in under 5 minutes. Full setup takes ~30 minutes.

**Optional enhancements:**
- Create your own custom agent for a persistent persona — see [AGENT-INSTRUCTIONS.md](AGENT-INSTRUCTIONS.md)
- Set up automated briefings with scheduled prompts — see [SCHEDULED-PROMPTS.md](SCHEDULED-PROMPTS.md)

## What You Need

- Microsoft 365 with Copilot. That's it.
- The setup adapts to what your Copilot can do (Excel write-back, agent creation, or prompts only)

## How It Works

1. You answer a structured interview about your role, priorities, people, and landscape (30 min)
2. Your answers become Word docs in a personal OneDrive folder
3. Copilot reads those docs plus your calendar and emails to deliver grounded briefings
4. A data layer (Excel workbook or Word docs, auto-detected) tracks tasks, decisions, intel, and contacts
5. Scheduled prompts deliver briefings to your email automatically

## Files

| File | What |
|------|------|
| [SETUP.md](SETUP.md) | The onboarding prompt — start here |
| [AGENT-INSTRUCTIONS.md](AGENT-INSTRUCTIONS.md) | Create a custom agent with Chief persona |
| [SCHEDULED-PROMPTS.md](SCHEDULED-PROMPTS.md) | 5 automated prompt templates |
| static/ | Landing page |

## Your Data Stays Yours

Everything lives in your OneDrive. The Chief of Staff reads your files but doesn't send them anywhere. No external servers, no analytics. Your private strategic advisor.

## License

MIT. Build on it, modify it, share it.
