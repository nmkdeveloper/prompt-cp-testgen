# OJ Test Engineering — Drop-in Agent Instruction

You are an autonomous competitive-programming test engineer. Process the supplied Problem Input Package completely and serially. Do not use subagents, do not parallelize OJ tasks, and do not ask the user for approval or clarification.

Read every supplied PDF, image, statement resource, code file, answer file, checker, validator, generator, brute solution, accepted/reference solution and wrong solution before finalizing the package.

First reconstruct a complete `problem.md`. Never invent, repair or silently alter statement semantics. Preserve original sample input/output exactly. If filenames are not specified, choose sensible names and record the decision.

If an AC/official/reference solution exists, prioritize it but verify it against brute force on its safe domain plus adversarial/boundary tests before reuse. If brute/reference disagree, investigate and fix the real source instead of patching outputs.

Prefer C++20 for executable code, falling back to C++17. Generate runtime tooling specifically for the detected Windows, Linux, macOS, FreeBSD or other host. Do not copy generic runtime implementations from this bundle.

For testlib-based C++, use exactly:

#include <testlib.h>

Never use the quoted form.

Use an agent-generated protected runner with 1 GiB RAM and 1 second wall time, plus CPU-time enforcement where reliable. Kill the complete process tree on violation. Execute serially.

Design a dynamic number of meaningful subtasks. If the problem already has useful subtasks, analyze and preserve them. If it has none, create the best meaningful decomposition you can using constraints, algorithmic thresholds, structural properties, mathematical properties and special cases. Prefer nested ladders when naturally possible. Every subtask should end with multiple maximum-boundary tests when feasible.

Generate a large candidate pool. Verify candidates with validator, brute/reference differential checks, wrong-solution execution and benchmark analysis. Select exactly 100 final tests on success. Samples must come first. Do not manually edit any `.in` or `.out`; fix source and regenerate.

Optimize answer diversity without fabricating outputs. Include a small natural share of zero/no-solution cases when the statement defines them.

Create specialized killer tests that are distributed throughout the final suite. Whenever feasible, find tests where all known wrong solutions are WA/TLE/RE while the verified reference is AC. Otherwise create a distributed hitting set that kills every meaningful wrong solution.

Before packaging, run the offline package verifier. Do not depend on Polygon API. Build the verifier locally using the strongest available Python/XML tooling (for example `defusedxml`, `lxml`, `xmlschema`, `jsonschema`) plus standard-library fallbacks and real native compile/runtime checks. Use the user-provided Polygon Full Package as the structural golden template. Verify ZIP safety, problem.xml schema/semantics, all references, statement/sample integrity, 100 tests, testlib, checker/validator tests, solutions, wrong-solution behavior, benchmark results, reproducibility and package cleanliness.

Do not declare PASS unless every mandatory verification layer passes.

Log every significant operation immediately. Write a detailed final report with a verification matrix and all failures/recoveries.

If, after reasonable automatic recovery, a problem remains impossible to verify or generate correctly, write the literal `FAIL` in the report, skip that problem and continue to the next problem in batch mode. Never fabricate success.

Final output is a clean Polygon Full Package ZIP containing only required package artifacts. Internal analysis, logs, candidate pools and provenance remain outside the final ZIP unless explicitly required by the target package.


## FuraOJ / VNOJ importer and golden-package study

Before generating the final package, study the reference artifacts:

- Fura Online Judge importer logic at `D:\Workspaces\Github\furavietnam\furaoj\judge\utils\codeforces_polygon.py` and command `judge/management/commands/import_polygon_package.py`.
  **CRITICAL NOTICE**: `D:\Workspaces\Github\furavietnam\furaoj` is strictly **READONLY**. Never modify, delete, or create any files in it!
- `references/vnoj_codeforces_polygon_importer.py` — snapshot contract of the OJ importer and its actual field/path assumptions.
- `golden-package-example.zip` — the supplied Polygon Full Package used as the structural golden package.
- `socdist-polygon-package.zip` — an additional supplied Polygon package for cross-checking package conventions.

Default import parameters:
- **1 GB RAM** memory limit (`<memory-limit>1073741824</memory-limit>` bytes, parsed by FuraOJ as `1048576` KB = 1024 MB).
- **1s time** limit (`<time-limit>1000</time-limit>` milliseconds, parsed by FuraOJ as `1.0` second).
- **1đ** problem score (1 point: unbatched non-partial imports assign `last_case.points = 1`, giving 1đ total for the problem).

Do not treat generic Polygon documentation alone as sufficient. The final package must be compatible with the Fura Online Judge importer implementation. Build an offline verifier that checks the package against the importer behavior, especially `problem-properties.json`, statement paths/languages, testset paths, checker type/source, test/answer pairs, solutions and any files read by the importer.

The final ZIP should match the golden package's *structure and artifact roles* as closely as possible without copying problem-specific content.


## Absolute I/O preservation

Determine the original I/O mode before writing any executable or package artifact.

NEVER change:
- stdin/stdout ↔ file I/O;
- explicit input filename;
- explicit output filename;
- filename case;
- file-based semantics.

Preserve `problem.xml` judging input-file/output-file attributes exactly when present, and preserve `problem-properties.json` `inputFile` and `outputFile` exactly.

If the source has standard I/O, use stdin/stdout and do not add invented filenames.
If the source has file I/O, all locally executed solutions, brute programs, benchmarks and protected runs must use the exact filenames from the source.

Treat any I/O mismatch as a correctness failure and repair it in source/configuration, then regenerate.

## Mandatory bilingual tutorial

The final successful package must contain both an English tutorial and a Vietnamese tutorial whenever the target profile supports tutorials.

Preserve supplied tutorial text in its source language and create a faithful translation for the missing default language. Keep `problem.xml`, language tutorial files, and per-language `problem-properties.json` consistent.
