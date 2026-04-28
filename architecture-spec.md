# Architecture Spec — [Project Name]

**Purpose:** Reference specification for the Architect agent. Defines what "good" looks like for this project's file system and knowledge graph.

---

## File System Structure

### Canonical Layout

<!-- Define your canonical folder layout here. List every top-level directory
     and its purpose. Use the tree format below as a starting point. -->

```
project-root/
├── .claude/
│   └── commands/           # Slash commands
├── src/                    # Source code
├── docs/                   # Documentation
├── data/                   # Structured data files (JSON, CSV)
├── scripts/                # Automation scripts
├── tests/                  # Test files
├── config/                 # Configuration files
├── drift-prevention/       # Drift prevention framework
│   └── agents/             # 6 agent specs
└── root files              # CLAUDE.md, architecture-spec.md, README.md, etc.
```

### What Goes Where

<!-- Map each content type to its canonical location. Add rows as needed. -->

| Content Type | Location | Examples |
|-------------|----------|---------|
| Source code | `src/` | <!-- e.g., app.py, index.ts --> |
| Structured data | `data/` | <!-- e.g., users.json, config.json --> |
| Documentation | `docs/` | <!-- e.g., requirements.md, architecture.md --> |
| Automation scripts | `scripts/` | <!-- e.g., deploy.sh, migrate.py --> |
| Test files | `tests/` | <!-- e.g., test_app.py, app.test.ts --> |
| Configuration | `config/` | <!-- e.g., .env.example, settings.yaml --> |
| Slash commands | `.claude/commands/` | <!-- e.g., drift-check.md --> |

### Naming Conventions

| Folder | Convention | Example |
|--------|-----------|---------|
| `src/` | `{kebab-case}.{ext}` | `user-service.ts` |
| `data/` | `{noun-plural}.json` | `tasks.json`, `connections.json` |
| `docs/` | `{slug}.md` | `requirements.md`, `architecture.md` |
| `scripts/` | `{verb-noun}.{ext}` | `run-tests.sh`, `deploy-prod.py` |
| `.claude/commands/` | `{verb-noun}.md` or `{noun}.md` | `drift-check.md`, `briefing.md` |
| `tests/` | `test_{module}.{ext}` or `{module}.test.{ext}` | `test_user.py`, `user.test.ts` |

### Rules

- **Max folder depth:** 3 levels from project root
- **Max files per directory:** 15 before considering subdirectories
- **New subdirectory threshold:** 3+ files with shared purpose
- **Merge threshold:** <3 files in a subdirectory for 60+ days
- **No binary files in root** except distribution artifacts (review periodically)

---

## Data Files Registry

<!-- Register every structured data file so the Consistency and Architect
     agents know what should exist and what sensitivity level it carries. -->

| File | Purpose | Sensitivity |
|------|---------|-------------|
| <!-- data/example.json --> | <!-- What this file stores --> | <!-- PUBLIC / INTERNAL / SENSITIVE --> |

**Sensitivity levels:**
- **PUBLIC** — Safe for git, no risk if leaked
- **INTERNAL** — Private but not damaging
- **SENSITIVE** — Must be gitignored until encryption is configured
- **CRITICAL** — Never store (passwords, API keys, tokens)

---

## Knowledge Graph Schema

<!-- If your project uses a connections/relationship graph (e.g., connections.json),
     define the schema here. If not, remove this section. -->

### Entity Types

<!-- List every type of entity that can participate in the graph. -->

| Type | Data File | Can Be Source? | Can Be Target? |
|------|-----------|----------------|----------------|
| <!-- e.g., task --> | <!-- tasks.json --> | <!-- Yes --> | <!-- Yes --> |
| <!-- e.g., contact --> | <!-- contacts.json --> | <!-- Yes --> | <!-- Yes --> |

### Relationship Types

<!-- Define the allowed relationship types between entities. -->

| Type | Definition | Valid Source -> Target |
|------|-----------|----------------------|
| <!-- e.g., enables --> | <!-- Source makes target possible --> | <!-- task -> task, contact -> task --> |
| <!-- e.g., blocks --> | <!-- Source prevents target --> | <!-- task -> task --> |

### Connection Required Fields

<!-- Define the fields every connection record must have. Example: -->

Every connection MUST have: `id`, `source_id`, `source_type`, `target_id`, `target_type`, `relationship`, `strength`, `notes`, `created_at`, `last_validated`

Recommended: `created_by` (`"auto-scan"` or `"manual"`)

### Strength Values

`strong`, `moderate`, `weak`

### Density Targets

<!-- Set minimum connection counts per entity type to ensure the graph stays useful. -->

| Entity Type | Min Connections Per Item |
|-------------|------------------------|
| <!-- e.g., tasks --> | <!-- 1 --> |
| <!-- e.g., contacts --> | <!-- 2 --> |
