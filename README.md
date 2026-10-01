# OJ Test Engineering — Antigravity + Cursor

A specification-first, autonomous competitive-programming test-engineering skill bundle for Antigravity and Cursor. It reconstructs problems from PDFs/images/files, verifies supplied solutions, designs dynamic subtasks, generates and audits tests, benchmarks code, and produces clean Polygon packages.

## Important architectural change

This bundle intentionally ships **no pre-written runtime Python/C++ implementation** for the protected runner, generators, validators, checkers, brute solvers, benchmark executables, or solution runners.

The agent must inspect the actual operating system/toolchain and **write the required code itself**, with C++ as the preferred language for executable components. This avoids hard-coded assumptions and allows native optimization for Windows, Linux, macOS, FreeBSD, and other detected systems.


## Agent-generated runtime tooling

The bundle contains no ready-made runtime Python/C++ implementation. The agent must detect the actual host and write the required executable tooling itself. Prefer C++20, falling back to C++17.

Typical generated files include `protected_runner.cpp`, `generator_*.cpp`, `validator.cpp`, `brute.cpp`, `reference.cpp` when a new reference is required, `wrong_*.cpp`, `checker.cpp` and `benchmark.cpp`. Supplied AC/reference code is reused only after verification.

The generated protected runner must enforce 1024 MiB RAM and 1000 ms wall time, plus 1000 ms CPU time where reliably enforceable, and must kill the complete process tree on violation. Use native OS APIs rather than assuming Linux behavior.

## Supported surfaces

- Google Antigravity: `.agents/skills/`, `.agents/rules/`, `AGENTS.md`
- Cursor: `.cursor/rules/`; shared skills live in `.agents/skills/`

## Core workflow

```text
Problem Input Package
        ↓
Input Discovery
        ↓
Problem Reconstruction
        ↓
problem.md
        ↓
Detect OS/toolchain
        ↓
Agent generates native C++ toolchain
        ↓
Verify supplied AC/reference code
        ↓
Brute verification
        ↓
Dynamic subtask design
        ↓
Large candidate pool
        ↓
Wrong-solution attack
        ↓
Benchmark
        ↓
Select exactly 100 final tests
        ↓
Final audit
        ↓
Clean Polygon ZIP
```

## Toolchain Preflight & Portable Fallback

Immediately after confirming problem statement existence, the system verifies `g++` and `python` availability:
- If either tool is absent from PATH, automatically search and download trusted portable standalone distributions (e.g. WinLibs standalone MinGW-w64 for Windows, official Python embeddable zip).
- Extract them into a local directory and configure the environment to use them for all subsequent compilation and execution phases.

## Hard execution policy & runaway watchdog

Every untrusted executable in the testing workflow runs through an agent-generated protected runner with:

- **1 GiB RAM**
- **Strict 1000 ms hard limit for solutions and mutants** (reference solution, brute force, wrong solutions WA/TLE/RE)
- **Calibrated hard limit for generators and tooling** derived empirically from a host FLOPS micro-benchmark
- **active runaway auto-break watchdog** to interrupt infinite loops (`while(true)`), infinite recursion, and hanging tasks past their hard time limit
- **process-tree kill on limit violation or auto-break** (forcefully killing parent and all descendant tasks)
- **serial execution only**

When a limit is exceeded or runaway code is detected, the protected runner must kill the complete process tree and log the reason. No timed-out or runaway process may continue in the background.

Windows should prefer native Job Objects; Linux should use native POSIX/Linux resource controls and process groups; macOS and FreeBSD should use the resource/process APIs actually available on the detected system. If a platform cannot provide reliable enforcement, the agent must not silently run unprotected; after reasonable recovery it must mark the problem `FAIL`.

## Token economy & English code comments

- **Token Economy**: All generated C++/Python code should be written compactly, placing multiple simple statements on a single line where practical, and using concise variable and function names (`n, m, k, a, ans, adj, dp, solve(), calc()`) to minimize token overhead.
- **Selective Comments**: Add comments only to functions that genuinely require explanation. When commenting, state strictly: (1) core logic, (2) received parameters/inputs, (3) return value/result. All comments must be written exclusively in English.

## No subagents / no concurrency

The workflow is explicitly single-agent and serial. Do not spawn subagents or run multiple test-engineering tasks simultaneously. This is intentional for deterministic logs, reproducible benchmarking, and controlled resource usage.

## Testlib

For C++ testlib code, use:

```cpp
#include <testlib.h>
```

Never use:

```cpp
#include "testlib.h"
```

The agent locates/uses the installed testlib rather than assuming a bundled snapshot.

## Immutable statement and samples

Original statement content and samples are authoritative. The agent may normalize formatting when creating `problem.md`, but must never change meaning, constraints, examples, sample inputs, sample outputs, scoring or explicit filenames.

Samples are preserved exactly and appear first in the final test suite.

## Generated artifacts are immutable

Never manually edit generated `.in`/`.out` artifacts. If something is wrong, fix the generator/oracle/reference/validator/checker/source and regenerate.

## Dynamic subtasks

Subtask count is not fixed. If the problem has no useful subtasks, the agent designs meaningful subtasks from constraints, complexity thresholds, structural properties, mathematical properties and special cases. Prefer nested ladders when naturally possible. Each subtask ends with multiple meaningful max-boundary tests when feasible.

## Exactly 100 final tests

A successfully processed problem must end with exactly 100 final tests. The agent may generate a much larger candidate pool before selecting them. Test selection balances correctness, samples, subtask coverage, max-boundary coverage, wrong-solution killing, stress value, structural diversity and answer diversity.

## Reference priority

Provided AC/accepted/reference code is prioritized but never trusted blindly. Verify it with brute force on a safe small domain and with adversarial/boundary checks before promoting it to `VERIFIED_REFERENCE`. Once verified, reuse it rather than rewriting it unnecessarily.

## Answer policy

Answers are generated from the verified reference/oracle. Avoid unnecessary repeated results; distribute numeric answers over meaningful ranges and include a small amount of valid zero/no-solution coverage when the statement naturally supports it. Never modify an answer by hand to improve diversity.

## Logging and final report

Write logs incrementally as work happens. At the end create a detailed `report.md` containing input discovery, problem reconstruction, subtask design, generated candidate counts, brute/reference verification, wrong-solution results, benchmark data, final 100-test composition, answer distribution, failures/recoveries, and package status.

## FAIL policy

Do not fabricate success. If a problem remains unrecoverable after reasonable automatic attempts, write the literal `FAIL`, document the cause, skip that problem in batch mode, and continue to the next problem.

## Files in this bundle

- `.agents/skills/` — shared skills
- `.agents/rules/` — Antigravity rules
- `.cursor/rules/` — Cursor rules
- `docs/` — detailed contracts and platform/toolchain guidance
- `schemas/` — machine-readable report/manifest/toolchain schemas
- `templates/` — report templates
- `vendor/testlib/README.md` — dependency guidance, no frozen testlib source

No generic runtime source is shipped. The agent generates it per problem and per platform.

## VNOJ Polygon golden-package profile

The final package builder is configured around the user-supplied Polygon Full Package as a structural golden template for VNOJ compatibility. The goal is not to reproduce one problem's content; it is to reproduce the same *package grammar and artifact relationships*.

Default statement languages:

- `english`
- `vietnamese`

For each language, generate the statement-side artifacts required by the target profile when the necessary toolchain is available: `statements/<language>/problem.tex`, `statements/<language>/tutorial.tex`, `statements/<language>/problem-properties.json`, sample files, `statement-sections/<language>/...`, and generated HTML/PDF counterparts when supported by the local Polygon-compatible build workflow.

The package should also mirror the golden sample's operational areas when applicable:

- `problem.xml`
- `tests/01` ... `tests/100` and corresponding `.a` answer files
- `files/` resources, checker, validator, generators, `testlib.h`, checker/validator test suites and required binaries
- `solutions/` source, `.desc` metadata, and target binaries
- `stresses/`
- `scripts/`
- `doall.sh`, `doall.bat`, `wipe.sh`, `wipe.bat`
- `tags`
- root checker mirror files when the target profile requires them

The agent must generate all problem-specific C++ and script content itself. The bundle contains no generic runtime implementation to copy. The sample package is a structural oracle, not a source of problem-specific code.

## Specialized killer tests

The final 100 tests must contain specialized tests that are *distributed* through the suite rather than placed in one contiguous "wrong-solution" block. A meaningful wrong solution must be defeated by at least one final test whenever feasible. The agent should also search for universal-killer inputs on which every known wrong solution gets a non-AC outcome (WA/TLE/RE) while the verified reference gets AC; when no universal input exists, use a distributed hitting set of specialized tests.


## Offline package verification (mandatory)

Before declaring a final Polygon/VNOJ package successful, run the `offline-package-verifier` skill. Do not rely on Polygon API calls. The verifier is generated by the agent for the current host and may use locally available `defusedxml`, `lxml`, `xmlschema`, and `jsonschema` when appropriate, with standard-library fallbacks. It must perform layered verification: safe ZIP inspection, golden-package comparison, XML/schema/semantic validation, reference/path integrity, immutable sample verification, exact 100-test validation, testlib/checker/validator runtime checks, reference/brute differential checks, wrong-solution attacks, benchmark evidence and reproducibility. A ZIP that merely opens or parses is not considered valid.

## Offline package verification (new in v2.3.0)

The bundle now includes `offline-package-verifier`. It is a mandatory pre-release gate and does not depend on Polygon API. The agent must generate the verifier for the current host and use the strongest available local stack: safe ZIP inspection, `defusedxml`/`lxml` when installed, `xmlschema` when a trusted local XSD exists, `jsonschema` for trusted JSON schemas, golden-package structural comparison, semantic `problem.xml` checks, path/resource integrity, immutable sample verification, compile/runtime checks, testlib checker/validator tests, reference/brute differential testing, wrong-solution testing, benchmarking and reproducibility checks.

A package is not PASS merely because its ZIP opens or `problem.xml` parses. All mandatory layers must pass.


## Supplied VNOJ importer + golden packages

This bundle ships read-only reference artifacts under `references/`:

- `vnoj_codeforces_polygon_importer.py` — the supplied importer behavior snapshot.
- `golden-package-example.zip` — the supplied Polygon Full Package used as the primary structural golden package.
- `socdist-polygon-package.zip` — an latest supplied Polygon package, used as a high-priority structural reference.

The agent must research these before package generation. The importer is the behavioral contract; the golden package is the structural contract.


## v2.4.2 — I/O immutability and bilingual tutorial hardening

### Sacred I/O contract

The package builder MUST NOT normalize, reinterpret, or replace the problem's input/output mechanism.

Before generating any solution, brute, generator, checker, validator, benchmark, or statement artifact, inspect and record the I/O contract from the original statement and supplied package.

Preserve exactly:
- whether the problem uses standard input/output or file I/O;
- explicit input filename;
- explicit output filename;
- filename case;
- all input/output semantics;
- `judging@input-file` and `judging@output-file` when present;
- `problem-properties.json` `inputFile` and `outputFile` values when present.

If both `judging@input-file` and `judging@output-file` are empty, that means standard I/O. Do NOT add invented filenames.

If file I/O is specified, generated executable tests MUST use those exact filenames. Do not convert file I/O into stdin/stdout.

If standard I/O is specified, do not invent file names.

### Strict I/O Formatting & Whitespace Hygiene

All test inputs and outputs (`.inp`, `.out`, `tests/01`..`tests/100`, `tests/01.a`..`tests/100.a`) must adhere strictly to the problem statement format:
- **Zero trailing whitespace**: absolutely NO trailing spaces (` `) or trailing tabs (`\t`) on any line.
- **Zero redundant blank lines**: absolutely NO consecutive newline characters (`\n\n`) and NO trailing blank lines.
- **Exact single newline at EOF**: every file must terminate with exactly one standard newline (`\n`).
- **Clean output formatting in loops**: C++ generators and reference solutions must output delimiters cleanly without dangling spaces before `\n` (e.g. `cout << a[i] << (i + 1 == n ? '\n' : ' ');`).

An I/O mismatch or formatting violation is a correctness failure and must be fixed at the source and regenerated.

### LaTeX Subscript Escaping ($s\_1$ mandatory)

Due to specific markdown parser behavior on FuraOJ / DMOJ / Martor, unescaped underscores inside inline math are intercepted as markdown italic emphasis (`_..._`). All LaTeX math subscripts MUST escape underscores with a backslash: `$s\_1$`, `$a\_i$`, `$dp\_{i, j}$`, `$x\_{max}$` instead of raw `$s_1$`, `$a_i$`.

### Bilingual tutorials

Successful packages MUST contain tutorials in both default languages whenever the target profile supports tutorials:
- `english`
- `vietnamese`

Provide all tutorial artifacts required by the golden package/profile, including when applicable:
- `statements/english/tutorial.tex`
- `statements/vietnamese/tutorial.tex`
- `statement-sections/english/tutorial.tex`
- `statement-sections/vietnamese/tutorial.tex`
- corresponding `problem.xml` tutorial entries
- corresponding `problem-properties.json` `tutorial` fields

If a supplied tutorial exists, preserve it exactly in its original language and create a faithful translation for the missing default language.

A tutorial translation must not alter algorithmic meaning, complexity, edge cases, or correctness claims.

The agent must never silently drop one language because the importer ultimately displays one selected tutorial.
