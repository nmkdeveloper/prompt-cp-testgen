---
name: test-selector
description: Selects an optimal, reasonable number of final tests from a verified candidate pool (covering all subtasks and essential test types) using coverage, subtask boundaries, wrong-solution kills, stress value, answer diversity and redundancy reduction.
---
# Test Selector

On success, dynamically calculate and select the optimal, reasonable number of final tests. The total number of final tests selected must always be a multiple of 10 (e.g., 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, etc., except for specialized problem types). The selected suite must completely cover all subtasks and include all essential test types (samples first, minimal/boundary, brute-verified small, structural/special cases, distributed adversarial killers, max-boundary stress ending each subtask, zero/no-solution).

Hard priorities:
1. correctness
2. preserved samples
3. subtask separation and maximum-boundary requirements
4. wrong-solution killing
5. structural/constraint/performance coverage
6. answer diversity & output distribution statistics
7. redundancy reduction

## Output Distribution Statistics & Regeneration Loop
Perform an output frequency and value distribution audit across all non-sample testcases:
- If too many outputs are identical or cluster on trivial values (excluding sample tests and problem-specific structural formats like boolean YES/NO), test selection alone is insufficient.
- The agent must immediately modify the test generator (`generator.cpp`) and regenerate the candidate test pool from scratch until broad spectrum diversity is achieved (including both small and large answer values across the output domain) and trivial constant / $O(1)$ guessing solutions are thoroughly defeated.
- Do not manually alter outputs to improve diversity. Modify generator logic and select valid inputs instead.

All original sample tests come first. Where feasible, place multiple meaningful maximum-boundary tests at the end of each subtask.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. All code and test generation artifacts must reside strictly inside `work/<problem-id>/`. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.


Generated testcase integrity: never edit `.in`, `.out`, or sample artifacts directly. All test inputs and outputs must adhere strictly to statement formatting with zero trailing spaces, zero redundant blank lines, and exactly one terminating newline at EOF. Any correction must modify the generator/oracle/source and regenerate.
