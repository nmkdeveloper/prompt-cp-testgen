# Test Design Policy

## Dynamic optimal final size

The final test count is dynamically calculated to be reasonable and optimal for the specific problem (no rigid 100-test requirement). The total number of final tests selected must always be a multiple of 10 (e.g. 10, 20, 30, 40, 50, 60, 70, 80, 90, 100... except for specialized problem types). Candidate generation is not capped. The final selected test suite MUST completely cover all subtasks as well as all essential test types:
1. Samples first (byte-for-byte unchanged).
2. Minimal/boundary tests.
3. Brute-verified small cases.
4. Structural and mathematical edge cases.
5. Distributed adversarial killers targeting wrong solutions (WA/TLE/RE).
6. 2–3 maximum-boundary tests ending each subtask.
7. Valid zero/no-solution edge cases when naturally applicable.

## Sample reservation

All original samples go first and remain byte-for-byte unchanged where the target format permits preserving them exactly.

## Subtasks

The subtask count is dynamic. A subtask is meaningful only when it defines a non-trivial algorithmic/structural capability boundary. Do not create arbitrary subtasks solely to manufacture more groups.

When possible:

```text
ST1 ⊆ ST2 ⊆ ... ⊆ FULL
```

and size/value maxima should not overlap the minimum of the next subtask when the problem naturally supports such nesting.

## End-of-subtask boundary rule

Each subtask ends with approximately 2–3 maximum-boundary tests where feasible. These tests must reach the meaningful maximum limits of that subtask and vary structure when possible.

## Test families

Derive families from the actual problem, including only those that are relevant:

- minimal/basic
- boundary
- small/brute
- monotone/reverse
- duplicate-heavy
- sparse/dense
- graph shape extremes
- special mathematical structures
- adversarial constructions
- overflow-sensitive values
- maximum constraints
- complexity worst cases
- wrong-solution targeted killers

## Answer diversity & Output distribution statistics

Answers must come from the verified reference/oracle. Never manually alter or fabricate outputs.

- **Statistical Distribution Audit**: Compute output frequency and value distribution statistics across all non-sample testcases.
- **Spectrum Diversity & Anti-O(1)**: The output distribution must exhibit broad spread across the valid output domain (some small, some medium, some large, boundary extremes, and a small fraction of valid zero/no-solution cases when applicable). Avoid generating testsets where answers overwhelmingly cluster on a constant value (e.g., all 0, all -1, all 1), which could permit trivial constant/$O(1)$ guessing solutions to pass.
- **Generator Modification & Regeneration Loop**: If post-generation analysis reveals that too many non-sample outputs are identical (excluding problem-specific structural exceptions like boolean YES/NO), test selection alone is insufficient: the agent MUST immediately modify generator parameters and generation logic (`generator.cpp`) and regenerate the candidate test pool from scratch until output diversity is achieved.

## Selection

Think of candidate selection as a set-cover problem over:

- sample preservation
- subtask separation
- boundary coverage
- structural coverage
- wrong-solution kills
- performance stress
- answer diversity
- redundancy reduction

Correctness is a hard constraint, not a score bonus.
