---
name: subtask-designer
description: Designs a dynamic number of meaningful subtasks from problem constraints, algorithmic complexity, special cases and structural properties, including maximum-boundary tests at subtask ends.
---
# Subtask Designer

Do not use a fixed subtask count. If useful subtasks are provided by the statement, audit and preserve them. If not, synthesize a natural difficulty ladder.

Prefer nested subtasks when the problem naturally supports them. Otherwise use meaningful structural or mathematical restrictions.

A restriction is a subtask only when it creates an algorithmic/capability boundary. Do not turn arbitrary cute cases into subtasks.

For every subtask record:
- restriction
- reason it exists
- expected solution capability
- relevant test families
- 2–3 meaningful maximum-boundary tests at the end when feasible


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.
