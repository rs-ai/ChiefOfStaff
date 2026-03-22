# AGENTS.md — OpenAI Codex CLI Adapter

This project is designed for Claude Code using `CLAUDE.md` as the instruction file.

If you are using OpenAI Codex CLI, the system instructions live in `CLAUDE.md`. Codex CLI reads `AGENTS.md` by default, so this file serves as the bridge.

## Getting Started

**Start your first message with:** "Read CLAUDE.md in this directory and follow all instructions in it."

This loads the full operating system: domains, data files, slash commands, guardrails, and proactive behaviors.

## Setup

1. Read `CLAUDE.md` in this directory — it contains all operating instructions, domain definitions, data file locations, slash commands, and guardrails.
2. Follow those instructions exactly as written. The system is agent-agnostic in design; only the instruction file name differs.
3. Read `mistakes.md` before any work session (mandatory per system rules).

## Running Slash Commands

Slash commands are defined as markdown files in `.claude/commands/`. To run them, ask the agent to read and execute the file.

**Examples:**
- To run a briefing: "Read `.claude/commands/briefing.md` and execute it."
- To add a task: "Read `.claude/commands/add-task.md` and execute it with: Build Q2 roadmap deck"
- To run a debrief: "Read `.claude/commands/debrief.md` and execute it."

Available commands: `briefing`, `debrief`, `add-task`, `add-intel`, `dashboard`, `domain-review`.

## Key Differences

- Codex CLI uses `AGENTS.md`; Claude Code uses `CLAUDE.md`. The content is identical in intent.
- Data files in `data/*.json` and domain files in `domains/*.md` are read/written directly by the agent.

## Notes

- The notification script (`scripts/notify.py`) and graph engine (`scripts/graph-query.py`) work with any agent — they operate on the JSON data files independently.
- Frameworks in `frameworks/` are plain markdown and agent-agnostic.
