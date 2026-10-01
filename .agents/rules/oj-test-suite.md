---
trigger: always_on
description: "Always-on requirements for dynamic optimal final tests, subtasks, boundary cases and answer diversity."
---
# OJ Test Suite Requirements

- Dynamically calculate the optimal, reasonable number of final tests (no rigid 100-test requirement); the suite MUST completely cover all subtasks as well as all essential test types (samples, minimal/boundary, brute-verified, structural/special cases, distributed adversarial killers, max-boundary stress, zero/no-solution).
- Original sample tests come first.
- Every subtask ends with approximately 2–3 maximum-boundary tests whenever feasible.
- Subtask count is dynamic.
- Prefer nested subtasks when natural; structural subtasks are allowed when they create real capability boundaries.
- Brute/reference differential testing is required where practical.
- Wrong-solution survival must be measured and targeted.
- Answer diversity is optimized without falsifying or manually editing outputs.
- Include a small fraction of valid zero/no-solution cases when naturally applicable.
- Default problem score is 1đ (1 point), conforming to Fura Online Judge import conventions.
- All test inputs and outputs must strictly conform to problem format with zero trailing spaces, no redundant blank lines, and exactly one trailing newline at EOF.
