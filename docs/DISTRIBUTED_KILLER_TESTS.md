# Distributed Killer Tests

## Goal

The final test suite must contain specialized tests that cause known wrong solutions to receive a non-AC verdict while the verified intended/reference solution receives AC.

Accepted wrong-solution outcomes:

- WA
- TLE
- RE

## Distribution rule

Do not put all killer tests in one contiguous block such as tests 81-100.

Instead:

- distribute killers across different subtasks;
- place some killers among small/medium tests;
- place some among structural/adversarial tests;
- preserve sample-first ordering;
- preserve the max-boundary tests at the end of every subtask.

The final selection algorithm should treat killer tests as constraints on the 100-test set, not merely as an optional category.

## Per-wrong-solution requirement

For each meaningful wrong solution, find at least one executed final testcase that kills it whenever feasible.

A useful killer satisfies:

```text
verified reference → AC
wrong solution → WA/TLE/RE
```

The exact wrong verdict should be recorded when deterministic.

## Universal killers

Search for inputs on which:

```text
reference → AC
W01 → non-AC
W02 → non-AC
W03 → non-AC
...
```

These are valuable because one test can eliminate many wrong solutions.

Do not require a universal killer to exist. If none exists, construct a distributed hitting set.

## Hitting-set objective

A final set of killer tests should cover all meaningful wrong solutions with as few redundant tests as practical.

Example:

```text
T17 → kills W01 W04 W07
T29 → kills W02 W03
T44 → kills W05 W07 W08
T63 → kills W06
```

## Never prove by inspection

A killer is valid only after execution. The agent must not claim that a test kills a wrong solution merely because the failure seems obvious from source inspection.
