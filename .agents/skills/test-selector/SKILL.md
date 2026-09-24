---
name: test-selector
description: Selects exactly 100 final tests from a verified candidate pool using coverage, subtask boundaries, wrong-solution kills, stress value, answer diversity and redundancy reduction.
---
# Test Selector

On success, select exactly 100 final tests.

Hard priorities:
1. correctness
2. preserved samples
3. subtask separation and maximum-boundary requirements
4. wrong-solution killing
5. structural/constraint/performance coverage
6. answer diversity
7. redundancy reduction

Do not alter outputs to improve diversity. Select better inputs instead.

All original sample tests come first. Where feasible, place multiple meaningful maximum-boundary tests at the end of each subtask.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.


Generated testcase integrity: never edit `.in`, `.out`, or sample artifacts directly. Any correction must modify the generator/oracle/source and regenerate.
