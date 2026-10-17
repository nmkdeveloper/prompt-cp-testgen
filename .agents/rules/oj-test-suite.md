---
trigger: always_on
description: "Always-on requirements for dynamic optimal final tests, subtasks, boundary cases and answer diversity."
---
# OJ Test Suite Requirements

- Dynamically calculate the optimal, reasonable number of final tests (no rigid 100-test requirement); ensure the total number of testcases is always a multiple of 10 (except for special problem types) such as 10, 20, 30, 40, 50, 60, 70, 80, 90, 100...; the suite MUST completely cover all subtasks as well as all essential test types (samples, minimal/boundary, brute-verified, structural/special cases, distributed adversarial killers, max-boundary stress, zero/no-solution).
- Original sample tests come first.
- Every subtask ends with approximately 2–3 maximum-boundary tests whenever feasible.
- Subtask count is dynamic.
- Prefer nested subtasks when natural; structural subtasks are allowed when they create real capability boundaries.
- Brute/reference differential testing is required where practical.
- Wrong-solution survival must be measured and targeted.
- Answer diversity & output statistics: perform statistical analysis of outputs across all non-sample tests. If there are too many identical outputs (excluding samples and problem-specific structural exceptions), modify generator code and regenerate tests from scratch until satisfied. Ensure output diversity across the spectrum (some small, some large, broad spread) and actively prevent trivial $O(1)$ solutions from succeeding (except for special problem types).
- Include a small fraction of valid zero/no-solution cases when naturally applicable.
- Problem score: when importing via Polygon package, problem score equals the points specified in the problem statement; if not specified, default to 1 point (1đ).
- All test inputs and outputs must strictly conform to problem format with zero trailing spaces, no redundant blank lines, and exactly one trailing newline at EOF.
