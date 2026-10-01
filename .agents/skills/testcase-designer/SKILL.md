---
name: testcase-designer
description: Designs reproducible competitive-programming test families and large candidate pools, balancing boundary, structural, adversarial, performance and wrong-solution coverage.
---
# Testcase Designer

Generate far more than 100 candidates when useful. Derive families from the actual problem instead of applying a blind fixed list.

Use testlib-based C++ generators when appropriate. Generators must be deterministic/reproducible by seed and parameters.

Candidate roles may include minimal, boundary, brute-small, structural, adversarial, maximum, stress and wrong-solution killer cases.

Never manually edit generated test data. Fix the generator and regenerate instead.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and enforced hard time limits (solutions/mutants: strict 1000 ms; generators: calibrated hard limit derived from a host FLOPS benchmark). Prefer C++ for executable components.


## Specialized and distributed killer tests

Do not reserve one contiguous range of final test IDs solely for wrong-solution killers.

Killer tests must be distributed across the final suite and, where possible, embedded within the relevant subtask regions. Preserve the rule that each subtask ends with multiple max-boundary tests; therefore killer tests should be placed in earlier/middle positions or in non-boundary positions inside the same subtask whenever possible.

For every meaningful wrong solution, create an executed counterexample that causes one of:

- WA
- TLE
- RE

while the verified reference solution receives AC under the protected execution contract.

Whenever possible, search for universal-killer inputs that defeat all known wrong solutions on one input. If no universal killer exists, create a distributed hitting set of specialized killer tests.

A test counts as a killer only after execution confirms the required verdicts. Do not infer verdicts without running the programs.


## Strict I/O Formatting & Whitespace Hygiene

Generators and test-design scripts must produce test data conforming strictly to the problem statement format:
- **Zero trailing whitespace**: absolutely NO trailing spaces (` `) or trailing tabs (`\t`) on any line.
- **Zero redundant newlines**: absolutely NO consecutive newline characters (`\n\n`) and NO trailing blank lines.
- **Exact single newline at EOF**: every input file must end with exactly one standard newline (`\n`).
- **Clean output formatting in loops**: C++ generator loops must output delimiters cleanly without dangling spaces before `\n` (e.g. `for (int i = 0; i < n; ++i) cout << a[i] << (i + 1 == n ? '\n' : ' ');`).


## I/O contract — immutable

The original I/O mechanism is part of the problem specification. Never convert file I/O to stdin/stdout or vice versa. Preserve exact input/output filenames and case. Preserve `problem.xml` judging `input-file`/`output-file` values and `problem-properties.json` `inputFile`/`outputFile` values. If standard I/O is specified, do not invent filenames. If file I/O is specified, generated solution/brute/benchmark/protected execution must use the exact filenames. Any mismatch requires a source-level fix and regeneration.

## Bilingual tutorial — required

The successful default package contains both English and Vietnamese tutorials whenever tutorials are supported. Preserve supplied tutorial text in its source language and faithfully translate the missing default language. Keep problem.xml, tutorial files and problem-properties.json synchronized.
