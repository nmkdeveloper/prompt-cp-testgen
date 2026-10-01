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

## TeX, LaTeX & Markdown Verification (Crash Prevention)

- [ ] Disallowed characters check: ZERO occurrences of `{ '“', '”', '‘', '’', '−', 'ﬀ', 'ﬁ', 'ﬂ', 'ﬃ', 'ﬄ' }` across all XML, JSON, TeX, and Markdown files.
- [ ] Smart quotes normalized to ASCII `"` and `'`.
- [ ] Unicode minus `−` normalized to ASCII `-`.
- [ ] Ligatures expanded to ASCII (`ff`, `fi`, `fl`, `ffi`, `ffl`).
- [ ] Vietnamese Unicode supported: all Vietnamese letters and diacritics (`đ, Đ, ư, ơ, ê, ô, ă, â` and all accented vowels) preserved without loss.
- [ ] UTF-8 without BOM confirmed for all statement and descriptor files.
- [ ] Unicode NFC normalization confirmed (`unicodedata.normalize('NFC', text)`).
- [ ] Zero mojibake or replacement characters (`\ufffd`).
- [ ] Math delimiters: `$ ... $` for inline, `$$ ... $$` for display.
- [ ] Literal dollar signs escaped as `\$`.
- [ ] Subscript underscore escaping: all math subscripts MUST escape underscores with backslash (`$s\_1$`, `$a\_i$`, `$dp\_{i, j}$` instead of `$s_1$`, `$a_i$`).
- [ ] Pandoc conversion dry-run passes without error.
- [ ] All image references (`![image](...)` and `<img>`) exist in statement directories.

## FuraOJ Importer Compatibility & Upload Safety

- [ ] Problem code: lowercase alphanumeric `^[a-z0-9]+$`, max 20 characters.
- [ ] Problem name: non-empty, max 100 characters.
- [ ] Memory limit: default 1 GB RAM (`<memory-limit>1073741824</memory-limit>` bytes = 1048576 KB, within range).
- [ ] Time limit: default 1s (`<time-limit>1000</time-limit>` ms, within range 0.01 - 60.0s).
- [ ] Points: default 1đ, total problem points strictly > 0.
- [ ] All 8 keys present in `problem-properties.json` (`legend`, `input`, `output`, `interaction`, `scoring`, `sampleTests`, `notes`, `tutorial`).
- [ ] Full package check: test 1 input and answer exist at resolved paths.
- [ ] Batches/groups: non-empty, valid points policy, valid dependencies.
- [ ] `D:\Workspaces\Github\furavietnam\furaoj` treated strictly as READONLY.

## Tests & Strict I/O Whitespace Formatting

- [ ] Dynamically calculated optimal final test count (no rigid 100-test requirement; complete coverage of all subtasks and test types).
- [ ] Samples are first.
- [ ] Every input has an answer.
- [ ] Strict I/O whitespace compliance: all test inputs and outputs (`tests/01`..`tests/NN`, `tests/01.a`..`tests/NN.a`, `.inp`, `.out`) adhere strictly to problem format.
- [ ] ZERO trailing spaces or tabs on any line in any test input/output file.
- [ ] ZERO redundant newlines (no consecutive empty lines `\n\n`) and exactly one terminating newline at EOF.
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
