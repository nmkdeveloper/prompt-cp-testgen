---
name: oj-test-engineering
description: Autonomous, single-agent, serial competitive-programming test engineering from a PDF/image/file problem package. Reconstructs problem.md without changing source semantics, generates an OS-adapted C++ toolchain including protected execution, verifies reference code with brute force, designs dynamic subtasks, attacks wrong solutions, benchmarks, selects exactly 100 tests, logs every step, and builds a clean Polygon package.
---
# OJ Test Engineering

Use the full pipeline in `../../../docs/WORKFLOW.md` and enforce `../../../AGENTS.md`, `../../../docs/GENERATED_TOOLCHAIN.md`, `../../../docs/OS_EXECUTION.md`, and `../../../docs/SERIAL_EXECUTION.md`.

## Non-negotiable execution model
- Single agent only. Never spawn subagents.
- Serial only. Never run multiple test-engineering tasks concurrently.
- Do not rely on generic pre-written runtime source. Generate the required code for the actual OS/toolchain.
- Prefer C++20, then C++17.
- Protected child execution: 1024 MiB, 1000 ms wall, 1000 ms CPU where reliable; kill the full process tree on violation.
- Testlib C++ include must be `#include <testlib.h>`.

## Required order
1. Discover every input file and classify its role.
2. Reconstruct `problem.md` from authoritative sources without semantic changes.
3. Preserve all original samples exactly and reserve them as the first tests.
4. Resolve canonical filenames when unspecified.
5. Detect OS, architecture, compiler, C++ standard, process/resource facilities and testlib availability.
6. Generate the minimal native C++ toolchain required for the problem, including a protected runner.
7. Verify any supplied AC/official/reference code before trusting or reusing it.
8. Determine the safe brute domain and run differential checks serially.
9. Analyze intended, partial and wrong solution classes.
10. Design a dynamic number of meaningful subtasks.
11. Design problem-specific test families.
12. Generate a large candidate pool with reproducible provenance.
13. Validate candidates and run brute/reference/wrong-solution checks serially.
14. Benchmark performance-sensitive structures under the same protected limits.
15. Generate targeted counterexamples for meaningful survivors.
16. Select exactly 100 final tests, preserving samples and subtask boundaries.
17. Audit answer diversity without editing answers.
18. Re-run final validation and produce incremental logs/final report.
19. Build a clean Polygon package using the VNOJ Polygon golden-package profile.
20. Run the offline-package-verifier against the staged package and final ZIP. Do not use Polygon API as the authoritative verification path.
21. Only declare success after all mandatory offline verification layers pass; otherwise record FAIL and skip in batch mode.

## Generated code policy
The agent writes all problem-specific executable code itself unless a supplied implementation is explicitly being reused after verification. This includes generators, validators, brute solvers, benchmark programs, checkers, mutants and the protected execution harness.

Do not include a generic runner implementation from the bundle.

## Hard integrity rules
- Never invent or silently alter the statement.
- Never modify original sample input/output.
- Never manually edit generated `.in/.out`.
- If generated data is wrong, fix source and regenerate.
- If supplied reference code conflicts with brute/adversarial evidence, investigate instead of trusting its label.

## Final conditions
Success requires exactly 100 final tests, preserved samples first, subtask boundary coverage, reference/brute verification where applicable, wrong-solution analysis, answer-diversity audit, protected execution, incremental logs, detailed report, a clean Polygon ZIP, and a PASS from the offline-package-verifier. ZIP readability or XML parse success alone is never sufficient.

If recovery is exhausted, write `FAIL` in the report and skip the problem in batch mode.


## Golden-package output contract

The final package must mirror the user-supplied Polygon Full Package structure as closely as possible. Treat the sample package as a structural golden template.

Default statement languages are exactly:

- `english`
- `vietnamese`

If one of the two default languages is absent from the supplied statement, create a faithful translation from the canonical reconstructed statement without altering semantics, constraints, samples or I/O rules. If both are supplied, preserve them as authoritative source variants.

Where the golden package contains them and the target profile supports them, generate and package:

- `problem.xml`
- `tests/01` ... `tests/100` and `.a` answers
- `statements/english/` and `statements/vietnamese/`
- `statement-sections/english/` and `statement-sections/vietnamese/`
- `statements/.html/english/` and `statements/.html/vietnamese/`
- `statements/.pdf/english/` and `statements/.pdf/vietnamese/`
- `files/` including `testlib.h`, checker, validator, generators, resources and required binaries
- `files/tests/checker-tests/` and `files/tests/validator-tests/` when used
- `solutions/` with source, `.desc` metadata and target binaries when required
- `stresses/`
- `scripts/`
- `doall.sh`, `doall.bat`, `wipe.sh`, `wipe.bat`
- root checker mirror files when required
- `tags`

Do not invent unsupported Polygon XML elements. If a feature is not present in the golden sample, rely on verified Polygon schema knowledge or existing package examples rather than guessing.

## Distributed killer-test contract

Killer tests are not allowed to exist only in one contiguous block near tests 81-100. The final selection must distribute specialized tests across the suite and across relevant subtasks while preserving sample-first ordering and the requirement that each subtask ends with max-boundary tests whenever feasible.

For each meaningful wrong solution:

1. Analyze its failure condition.
2. Construct a specialized counterexample.
3. Verify the reference solution gets AC.
4. Verify the wrong solution gets a non-AC result: WA, TLE, or RE.
5. Prefer tests that distinguish multiple wrong solutions simultaneously.
6. Scatter selected killer tests throughout the final suite rather than clustering them.

Attempt to construct universal-killer tests on which all known wrong solutions are non-AC while the verified reference is AC. If this is not possible, use a distributed hitting set so every meaningful wrong solution is killed by at least one final test.

Do not label a killer as successful based on theory alone; execute it.


## Offline package verification contract

Before success, invoke the `offline-package-verifier` skill. The verifier must be generated for the actual environment and may use locally available Python libraries such as `defusedxml`, `lxml`, `xmlschema`, and `jsonschema` when appropriate, with correct standard-library fallbacks. It must validate the package in layers: safe ZIP inspection, golden-template comparison, XML/schema/semantic validation, referential integrity, sample/statement immutability, exact 100-test integrity, testlib/checker/validator runtime checks, reference/brute/wrong-solution checks, protected execution, benchmark evidence and reproducibility. Do not use Polygon API as the authoritative verifier.


## I/O contract — immutable

The original I/O mechanism is part of the problem specification. Never convert file I/O to stdin/stdout or vice versa. Preserve exact input/output filenames and case. Preserve `problem.xml` judging `input-file`/`output-file` values and `problem-properties.json` `inputFile`/`outputFile` values. If standard I/O is specified, do not invent filenames. If file I/O is specified, generated solution/brute/benchmark/protected execution must use the exact filenames. Any mismatch requires a source-level fix and regeneration.

## Bilingual tutorial — required

The successful default package contains both English and Vietnamese tutorials whenever tutorials are supported. Preserve supplied tutorial text in its source language and faithfully translate the missing default language. Keep problem.xml, tutorial files and problem-properties.json synchronized.
