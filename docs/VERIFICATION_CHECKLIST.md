# Final Verification Checklist

Before declaring a Polygon/VNOJ package successful, the agent must check every applicable item.

## Archive

- [ ] ZIP opens and all entries can be read.
- [ ] No duplicate members.
- [ ] No absolute or traversal paths.
- [ ] No forbidden workspace artifacts.

## Golden package compatibility

- [ ] Root/package areas follow the supplied golden template where applicable.
- [ ] `problem.xml` references real resources.
- [ ] `files/testlib.h` is present when required.
- [ ] Checker/validator/solution source and binary relationships are consistent.

## Statement

- [ ] `problem.md` exists.
- [ ] PDF/images/source materials were inspected.
- [ ] No semantic changes to the original statement.
- [ ] Original samples are unchanged.
- [ ] Sample order is unchanged.
- [ ] Default package languages are `english` and `vietnamese`.

## Tests

- [ ] Exactly 100 final tests.
- [ ] Samples are first.
- [ ] Every input has an answer.
- [ ] Every final test passes validation.
- [ ] Every subtask ends with max-boundary tests when feasible.
- [ ] Killer tests are distributed across the suite.
- [ ] Answer duplication is minimized without weakening coverage.
- [ ] Natural zero/no-solution cases are represented when applicable.

## Code verification

- [ ] Supplied AC/reference code was verified before reuse.
- [ ] Brute/reference agreement was checked on the safe brute domain.
- [ ] Wrong solutions were run serially.
- [ ] Meaningful wrong solutions have specialized killers.
- [ ] Reference passes all final tests.
- [ ] Benchmark/stress behavior was checked.
- [ ] Testlib sources use exactly `#include <testlib.h>`.

## Generation integrity

- [ ] No final `.in/.out` was manually edited.
- [ ] Any correction was made at source and regenerated.
- [ ] Generated tests are reproducible from generator + seed/parameters.

## Execution safety

- [ ] 1 GiB RAM limit configured.
- [ ] 1 second wall limit configured.
- [ ] CPU limit enforced where reliable.
- [ ] Process tree is killed on violation.
- [ ] No background test process survives.
- [ ] No subagents.
- [ ] No concurrent OJ task execution.

## Reporting

- [ ] Incremental logs were written throughout.
- [ ] Final report contains the complete verification matrix.
- [ ] All recovery attempts are documented.
- [ ] Any unresolved problem is marked literally `FAIL`.

## Packaging

- [ ] Clean staging directory.
- [ ] Allowlist packaging only.
- [ ] Final ZIP contains only required Polygon package files.
- [ ] ZIP can be reopened after creation.
