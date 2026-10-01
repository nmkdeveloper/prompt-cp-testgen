# Test Design Policy

## Dynamic optimal final size

The final test count is dynamically calculated to be reasonable and optimal for the specific problem (no rigid 100-test requirement). Candidate generation is not capped. The final selected test suite MUST completely cover all subtasks as well as all essential test types:
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

## Answer diversity

Answers must come from the verified reference/oracle. Do not patch answer files. Penalize unnecessary duplicate outputs, but keep duplicate-answer tests when they add correctness, boundary, subtask, structural or killer value.

For numeric outputs, spread values over meaningful regions of the attainable range. Use linear buckets for naturally linear distributions and logarithmic buckets for scale-heavy distributions. Keep a small fraction of valid zero/no-solution results when the statement defines such a case and natural valid cases exist.

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
