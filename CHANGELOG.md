# Changelog

All notable changes to the Chief of Staff operating system will be documented in this file.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.1.0] - 2026-04-28

### Added
- Drift prevention framework with 6 specialized agents (Defender, Healer, Simplifier, Psychologist, Consistency, Architect) for detecting and fixing security, code, complexity, behavioral, data, and structural drift
- `/drift-check` slash command with `all`, `quick`, and per-agent modes
- `architecture-spec.md` reference template — fill-in-the-blanks scaffold for the Architect agent's structural rules
- Drift Prevention section in `CLAUDE.md` linking the agents and command into the operating system

### Changed
- `CLAUDE.md` slash command table now includes `/drift-check`

## [1.0.0] - 2026-03-22

### Added
- Chief of Staff operating system with 6 customizable life/work domains
- 6 slash commands: briefing, debrief, add-task, add-intel, dashboard, domain-review
- Knowledge graph system with connections tracking
- Background research agents with configurable cadences
- 7 decision frameworks (AI use case evaluation, stakeholder influence, executive narrative, build vs buy, data maturity, team capability, eval)
- Notification system via email (scripts/notify.py)
- Multi-platform support: Claude Code (CLAUDE.md), Codex (AGENTS.md), Gemini (GEMINI.md)
