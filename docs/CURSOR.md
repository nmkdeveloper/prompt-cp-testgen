# Cursor Integration

Cursor discovers Agent Skills from project-level locations including:

```text
.agents/skills/
.cursor/skills/
```

This bundle keeps the shared skills under `.agents/skills/` so the same skill tree can be used by both Antigravity and Cursor.

Cursor-specific persistent rules are under:

```text
.cursor/rules/*.mdc
```

The workflow is intentionally single-agent and serial; do not spawn subagents or run multiple OJ tasks concurrently.
