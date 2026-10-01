# Decision Tree

## Statement source

- PDF/image/text supplied -> reconstruct `problem.md` first.
- Multiple conflicting sources -> investigate; never silently rewrite samples.

## Reference

- Supplied AC/official/reference -> verify first, then reuse.
- Brute available -> determine safe domain and differential-test.
- No reliable reference -> derive independently, cross-check where practical.

## Subtasks

- Useful supplied subtasks -> preserve/audit.
- No useful subtasks -> design a dynamic number.
- Nested restrictions natural -> prefer a ladder.
- Structural distinction is more meaningful -> use structural subtask.

## Test generation

- Generate a large candidate pool.
- Reserve immutable samples first.
- Reserve max-boundary tests for the end of each subtask.
- Use brute on safe small cases.
- Attack wrong solutions and mutants.
- Benchmark worst-case structures.
- Dynamically calculate and select optimal final tests (covering all subtasks and test types).

## Failure

- Recover automatically when reasonable.
- Never manually patch generated files.
- If unrecoverable -> `FAIL`, detailed report, skip in batch mode.
