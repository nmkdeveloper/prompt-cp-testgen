# Antigravity Integration

Current workspace skill location:

```text
.agents/skills/<skill-folder>/SKILL.md
```

Current workspace rules location:

```text
.agents/rules/*.md
```

Each rule file in `.agents/rules/` must use Antigravity rule frontmatter, for example:

```yaml
---
trigger: always_on
description: "Always-on OJ test engineering constraint."
---
```

`AGENTS.md` is also supported as an always-on workspace rule.

This bundle uses a single custom agent under:

```text
.agents/agents/oj-test-engineer/agent.md
```

The workflow is intentionally single-agent and serial; do not spawn subagents.
