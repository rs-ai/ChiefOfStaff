# Upgrade Guide

This guide helps AI assistants apply updates when a user upgrades from an older version.

## Current Version: 1.1.0

## Upgrading from 1.0.0 to 1.1.0

This release adds the drift prevention framework. It is purely additive — no existing files change semantics.

### What to copy in

1. Add the `drift-prevention/` directory (framework + 6 agent specs).
2. Add `architecture-spec.md` to the project root. This is a template — the user fills it in with their canonical layout, data files, and (optional) knowledge graph schema.
3. Add `.claude/commands/drift-check.md`.

### What to merge into existing files

- `CLAUDE.md`: add the **Drift Prevention** section with the 6-agent table, links to `drift-prevention/framework.md` and `architecture-spec.md`. Add `/drift-check` to the slash commands table. If the user has customized `CLAUDE.md`, merge — do not overwrite.

### After the upgrade

- Update the version marker in the user's `CLAUDE.md`: `<!-- DO NOT DELETE: rs-ai/chief-of-staff@1.1.0 (2026-04-28) -->`
- Suggest the user run `/drift-check quick` to confirm everything is wired up.

## How Upgrades Work

### How Upgrades Work

When a user asks you to check for updates:

1. Read the `VERSION` file from this repo
2. Compare against the version marker in the user's CLAUDE.md: `<!-- DO NOT DELETE: rs-ai/chief-of-staff@X.Y.Z (YYYY-MM-DD) -->`
3. If a newer version exists, read the relevant sections below for each version between theirs and current
4. Apply changes intelligently — add new features, merge improvements, preserve user customizations
5. Update the version marker in the user's CLAUDE.md

### If the version marker is missing

The user may have deleted it. Try to infer their version:
- Check which commands exist in their `.claude/commands/` directory
- Check which frameworks exist in their `frameworks/` directory
- Compare against the `affected_files` in each release section
- If uncertain, ask the user or offer a fresh setup from the current version

### General upgrade principles

- **Merge, don't overwrite.** Users customize their CLAUDE.md, domains, and frameworks. Preserve their changes.
- **Add new files directly.** New commands, frameworks, or data schemas can be added without conflict.
- **Flag breaking changes.** If a file structure changed, explain what the user needs to do manually.
- **Preserve data.** Never overwrite data/*.json files — those contain the user's information.
