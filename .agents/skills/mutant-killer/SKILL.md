---
name: mutant-killer
description: Generates targeted counterexamples for surviving wrong solution classes and closes test-suite blind spots through iterative kill-and-regenerate loops.
---
# Mutant Killer

For each meaningful surviving wrong solution:
1. Analyze the behavior on passed and failed tests.
2. Infer the missing distinction.
3. Construct a targeted candidate input.
4. Validate it.
5. Run reference/brute where applicable.
6. Run the target wrong solution.
7. Keep it if it kills the target and adds coverage.

Do not modify existing `.in/.out` artifacts manually.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.


## Universal and distributed killer search

The goal is not merely to maximize the number of mutants killed somewhere in the suite. Search for compact specialized inputs with strong discriminatory power.

Priorities:

1. Find inputs where the verified reference is AC and every known wrong solution is non-AC.
2. If impossible, find a small distributed hitting set that collectively defeats every meaningful wrong solution.
3. Spread those tests across test IDs and relevant subtasks instead of clustering all killers at the end.

Accepted wrong-solution failure outcomes are WA, TLE, and RE. Any unexpected AC must trigger counterexample search.
