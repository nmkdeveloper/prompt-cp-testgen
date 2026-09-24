# Serial Execution and No-Subagent Policy

## Mandatory

The entire OJ test-engineering workflow is single-agent and serial.

The agent MUST NOT:

- spawn subagents
- delegate test-engineering stages to another agent
- run independent tasks concurrently
- use parallel workers for testcase execution
- run multiple solutions simultaneously
- run brute/reference/wrong solutions simultaneously
- generate multiple testcase families concurrently
- benchmark multiple binaries concurrently

## Required Pattern

Use:

```text
Task A
  ↓
finish A
  ↓
Task B
  ↓
finish B
  ↓
Task C
```

not:

```text
A ─┐
B ─┼─ concurrent
C ─┘
```

## Determinism

Serial execution is required so that:

- logs remain ordered
- resource measurements remain attributable
- generated artifacts are reproducible
- failures are easier to diagnose
- no two processes compete for CPU/RAM and distort benchmark measurements

## If the Host Suggests Parallelism

Ignore the suggestion and keep this workflow serial. Do not use host-level subagent orchestration for this skill.
