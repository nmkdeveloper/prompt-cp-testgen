---
name: wrong-solution-analyzer
description: Executes supplied wrong solutions and meaningful mutants, measures survival profiles across tests and subtasks, and identifies missing killer cases.
---
# Wrong Solution Analyzer

Compile and run supplied wrong solutions where practical. Generate additional meaningful mutants when useful.

Record for each solution:
- passed/failed test counts
- subtask survival profile
- suspected bug class
- killer tests

A wrong solution surviving too much is a signal to strengthen the test suite, not a reason to stop.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.
