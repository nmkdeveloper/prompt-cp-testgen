# OJ Test Engineering — Workspace Rules

When a task is about generating/validating competitive-programming tests from a supplied problem package, use the `oj-test-engineering` skill.

Non-negotiable principles:

- Read all supplied problem resources before generating final tests.
- Reconstruct a complete `problem.md` without changing statement semantics.
- Right after verifying problem statement existence, immediately check system availability of `g++` and `python`. If either is missing, automatically download portable standalone builds from trusted sources and configure the environment to use them throughout execution.
- Preserve original sample inputs/outputs exactly; samples go first.
- Never invent or silently repair the statement, samples, constraints, scoring or explicit filenames.
- Prefer supplied AC/reference code, but verify it with brute/adversarial checks before promoting it to the reference.
- Dynamically design subtasks; prefer nested ladders when naturally possible and use meaningful structural subtasks when appropriate.
- Dynamically calculate the optimal, reasonable number of final tests (no rigid 100-test requirement); the suite MUST completely cover all subtasks as well as all essential test types (samples, minimal/boundary, brute-verified, structural/special cases, distributed adversarial killers, max-boundary stress, zero/no-solution).
- Put multiple meaningful max-boundary tests at the end of each subtask whenever feasible.
- Use testlib for direct C++ test-engineering components where applicable and include it as `#include <testlib.h>` only.
- Do not manually edit generated `.in/.out` files. Fix source and regenerate.
- Keep answers generated from the verified reference; minimize unnecessary answer duplication and include a small number of valid no-solution/zero cases when applicable.
- Every untrusted executable must be run through an agent-generated native protected runner with 1 GiB RAM and enforced hard time limits: solutions and mutant codes have a strict 1000 ms limit; generators and tooling codes have a calibrated hard limit derived from a host FLOPS benchmark. Include an active auto-break watchdog that terminates runaway execution (infinite loops, infinite recursion) and kills the entire process tree.
- Token economy in generated code: generate dense, compact code (multiple statements per line where practical) and concise variable/function names to conserve tokens without altering semantics.
- Code comments convention: comment only on functions that genuinely require explanation; comments must strictly state core logic, inputs, and return value, and must be written exclusively in English.
- Generate runtime tooling per detected OS/toolchain; prefer C++ for solution/brute/generator/validator/checker/benchmark/runner code.
- Do not rely on a generic prewritten runtime implementation shipped by this bundle.
- Never spawn subagents and never run multiple test-engineering tasks concurrently. Execute serially.
- Log significant work incrementally and write a detailed final report.
- Do not ask the user for approval during autonomous execution.
- If a problem becomes unrecoverably abnormal after reasonable automatic recovery, write `FAIL`, document it, skip the problem in batch mode and continue.
- Final ZIP must contain only required Polygon package files.


Golden Package Profile (FuraOJ / VNOJ Polygon Full Package)

- Treat the user-provided sample Polygon package as the structural golden template.
- Mirror its package layout and descriptor relationships as closely as the target problem permits.
- Default statement languages are `english` and `vietnamese`.
- Default import resource limits & scoring:
  - **1 GB RAM** memory limit (`<memory-limit>1073741824</memory-limit>` bytes, parsed by FuraOJ as `1048576` KB = 1024 MB).
  - **1s time** limit (`<time-limit>1000</time-limit>` milliseconds, parsed by FuraOJ as `1.0` second).
  - **1đ** problem score (1 point: unbatched / non-partial imports assign `last_case.points = 1` yielding 1đ total for the problem, or default problem point value 1đ).
- Produce the same categories of artifacts when applicable: `problem.xml`, `tests/`, `statements/`, `statement-sections/`, `files/`, `solutions/`, `stresses/`, `scripts/`, `doall.sh`, `doall.bat`, `wipe.sh`, `wipe.bat`, root checker mirrors, solution `.desc` metadata, generated platform binaries, validator/checker tests, and `tags`.
- Include `files/testlib.h` in the final Polygon package when the target profile uses testlib, and ensure all testlib-based C++ sources contain exactly `#include <testlib.h>`.
- Do not guess Polygon XML structures for features that are not evidenced by the golden template or verified platform knowledge; preserve/emit only valid package schema.
- Final `problem.xml` must reference every packaged source/binary/resource path consistently.
- On successful processing, final tests are contiguous `tests/01` through `tests/NN` with corresponding `tests/01.a` through `tests/NN.a` (%02d pattern preferred).

Distributed Wrong-Solution Killer Requirement

- Do not cluster all killer tests into one final block.
- Distribute specialized killer tests across the suite and across relevant subtasks, while preserving sample-first ordering and subtask max-boundary endings.
- For every meaningful wrong solution, create at least one dedicated final killer test whenever feasible.
- Whenever a single input can make every known wrong solution terminate non-AC (WA/TLE/RE) while the verified reference is AC, prioritize and distribute such universal-killer tests.
- If no single universal-killer input exists, build a small distributed hitting set so every meaningful wrong solution is defeated by one or more specialized tests.


## Offline package verification (mandatory)

Before declaring a final Polygon/FuraOJ/VNOJ package successful, run the `offline-package-verifier` skill. Do not rely on Polygon API calls. The verifier is generated by the agent for the current host and may use locally available `defusedxml`, `lxml`, `xmlschema`, and `jsonschema` when appropriate, with standard-library fallbacks. It must perform layered verification: safe ZIP inspection, golden-package comparison, XML/schema/semantic validation, reference/path integrity, immutable sample verification, comprehensive test-suite validation (covering all subtasks and test types), testlib/checker/validator runtime checks, reference/brute differential checks, wrong-solution attacks, benchmark evidence and reproducibility. A ZIP that merely opens or parses is not considered valid.


Fura Online Judge (FuraOJ) importer source-of-truth rule

- The directory `D:\Workspaces\Github\furavietnam\furaoj` is the authoritative codebase of Fura Online Judge (containing `judge/management/commands/import_polygon_package.py` and `judge/utils/codeforces_polygon.py`).
- **CRITICAL — STRICTLY READONLY**: `D:\Workspaces\Github\furavietnam\furaoj` is strictly **READONLY**. Never modify, delete, or create files in `D:\Workspaces\Github\furavietnam\furaoj`. All package generation, tooling, verification, and code must occur within `prompt-cp-testgen`.
- Treat the FuraOJ `codeforces_polygon.py` importer logic and the supplied Polygon Full Package ZIP as structural/behavioral golden references.
- Default import settings are **1 GB RAM** (`1073741824` bytes), **1s time** (`1000` ms), and **1đ** (1 point).
- **TeX, LaTeX, Markdown & Character Sanitization (Preventing Page Crashes)**:
  - Statements, problem names, notes, scoring, and tutorials must be strictly sanitized against `DMOJ_PROBLEM_STATEMENT_DISALLOWED_CHARACTERS`:
    `{ '“', '”', '‘', '’', '−', 'ﬀ', 'ﬁ', 'ﬂ', 'ﬃ', 'ﬄ' }`.
  - Replace curly quotes with ASCII `"` and `'`.
  - Replace Unicode minus `−` with ASCII `-`.
  - Expand ligatures `ﬀ`, `ﬁ`, `ﬂ`, `ﬃ`, `ﬄ` to `ff`, `fi`, `fl`, `ffi`, `ffl`.
  - Format math strictly with `$ ... $` (inline) and `$$ ... $$` (display). Escape literal dollars as `\$`.
  - **Subscript Underscore Escaping in LaTeX (`$s\_1$` mandatory)**: Do NOT use raw `$s_1$` or `$a_i$`; all subscripts in LaTeX math MUST escape underscores with a backslash: `$s\_1$`, `$a\_i$`, `$dp\_{i, j}$`, `$x\_{max}$` due to site-specific markdown parser behavior (FuraOJ / DMOJ / Martor interprets unescaped `_` inside math as Markdown italic emphasis, corrupting the formula before MathJax/KaTeX rendering).
  - Verify that all referenced images exist within the statement folder.
- **Vietnamese Unicode Support (NFC & UTF-8)**:
  - Full native support for Vietnamese Unicode: all Vietnamese statements (`statements/vietnamese/`), problem names, scoring, notes, and tutorials must fully preserve Vietnamese diacritics and letters (`à, á, ả, ã, ạ, ă, ằ, ắ, ẳ, ẵ, ặ, â, ầ, ấ, ẩ, ẫ, ậ, è, é, ẻ, ẽ, ẹ, ê, ề, ế, ể, ễ, ệ, ì, í, ỉ, ĩ, ị, ò, ó, ỏ, õ, ọ, ô, ồ, ố, ổ, ỗ, ộ, ơ, ờ, ớ, ở, ỡ, ợ, ù, ú, ủ, ũ, ụ, ư, ừ, ứ, ử, ữ, ự, ỳ, ý, ỷ, ỹ, ỵ, đ, Đ` and uppercase variants).
  - All files must be saved in **UTF-8 without BOM**.
  - Normalize all text to **Unicode NFC (Normalization Form C)** (`unicodedata.normalize('NFC', text)`) to prevent decomposed diacritics (tổ hợp) from breaking Pandoc/KaTeX rendering or database lookups.
  - Crucial distinction: `DMOJ_PROBLEM_STATEMENT_DISALLOWED_CHARACTERS` applies exclusively to typographic quotes, unicode minus, and Latin ligatures; it must NEVER strip or alter Vietnamese letters or diacritics (`đ`, `Đ`, `ư`, `ơ`, `ê`, `ô`, `ă`, `â` etc. are fully valid and preserved).
- **Upload Conflict & Crash Prevention**:
  - Problem code must be alphanumeric lowercase (`^[a-z0-9]+$`), maximum length 20.
  - Problem name must be non-empty, maximum length 100, and free of disallowed characters.
  - Limits must stay within FuraOJ supported range (time: 0.01s - 60s; memory: 0 - 1048576 KB).
  - Total points must be strictly greater than 0 (default 1đ).
- Before declaring a generated package valid, derive and execute an offline compatibility checklist from the FuraOJ importer source, then compare the staged package against the golden package's artifact layout.
- In particular, validate every `statement` language referenced by `problem.xml`, the corresponding `problem-properties.json`, required keys such as `legend`, `input`, `output`, `interaction`, `scoring`, `sampleTests`, `notes`, and `tutorial`, and every path consumed by the importer.
- Do not require these fields merely because a generic Polygon specification suggests them; require them because the target importer source actually consumes them.
- Never use the golden package's problem-specific content as generated content for another problem.


## STRICT I/O FORMATTING & IMMUTABILITY — ABSOLUTE

Treat the original I/O mode as immutable source data and test inputs/outputs as strictly formatted artifacts.

- Never convert file I/O to stdin/stdout.
- Never convert stdin/stdout to file I/O.
- Preserve explicit input/output filenames exactly, including case.
- Preserve `problem.xml` `judging@input-file` and `judging@output-file` exactly when present.
- Preserve `problem-properties.json` `inputFile` and `outputFile` exactly when present.
- If file I/O is specified, all locally executed solutions, brute programs, benchmarks and protected runs must use the exact filenames.
- If standard I/O is specified, use standard streams and do not invent filenames.
- Any mismatch is a correctness failure; fix source/configuration and regenerate.
- **Strict I/O Whitespace & Format Conformity**:
  - All test inputs and outputs (`.inp`, `.out`, `tests/01`..`tests/NN`, `tests/01.a`..`tests/NN.a`, sample tests) must conform strictly to the problem statement format.
  - Absolutely NO redundant whitespace: zero trailing spaces (` `) or trailing tabs (`\t`) on any line.
  - Absolutely NO redundant newlines: zero extraneous blank lines (e.g. consecutive `\n\n`) and zero trailing blank lines.
  - Every file must terminate with exactly one standard newline (`\n`), with no multiple trailing newlines at EOF.
  - All generators and reference solutions must output tokens cleanly without dangling spaces before `\n` (e.g. `cout << a[i] << (i + 1 == n ? '\n' : ' ');`).

## BILINGUAL TUTORIAL — ABSOLUTE

The final default package must contain both English and Vietnamese tutorials whenever tutorials are supported by the target profile. Preserve supplied tutorial source text verbatim and faithfully translate only the missing default language. Keep both languages represented in package artifacts even though the importer selects one main tutorial for the site.

## TOOLCHAIN PREFLIGHT & PORTABLE RUNTIME

- **Initial Check**: Immediately after verifying that problem files/statement exist, check whether `g++` and `python` are available in PATH.
- **Automatic Portable Fallback**: If `g++` or `python` is missing, search web and download trusted portable standalone builds (e.g., WinLibs standalone MinGW-w64 archive for Windows, official Python embeddable zip).
- **Trusted Sources Only**: Ensure portable archives originate from reliable official/reputable repositories.
- **Local Isolation & Configuration**: Extract portable toolchains into a local directory and configure environment paths so all compilation, validation, and execution steps seamlessly utilize them.

## RUNAWAY WATCHDOG & PROCESS TREE KILL

- **Hard Time Limits for All Executables**:
  - **Solutions & Mutants**: All solution codes (reference, brute force, wrong solutions WA/TLE/RE) have an absolute strict hard time limit of **1000 ms** (1.0 second).
  - **Generators & Tooling Code**: All generator, validator, checker, and auxiliary code must also have an enforced hard time limit. This limit is calibrated empirically based on host environment capabilities by running a quick host micro-benchmark to estimate FLOPS/throughput and assigning a reasonable hard limit (e.g. allowing complex generation on slower CPUs while strictly bounding runaway time).
- **Auto-Break Runaway Execution**: The protected runner must actively detect and interrupt code that executes past its designated hard time limit due to infinite loops (`while(true)`), infinite recursion (stack overflows or hangs), or exponential search spaces.
- **Process Tree Kill**: When runaway execution is broken or a hard limit is exceeded, forcefully terminate the entire process tree (parent process and all spawned child processes/tasks).
- **No Background Stragglers**: Ensure zero lingering child processes or zombie tasks survive in the operating system.

## TOKEN ECONOMY & CODE COMMENT CONVENTION

- **Token Economy (Compact Code)**: To save tokens, write dense and compact code in all agent-generated sources (solutions, brutes, generators, validators, checkers, runners):
  - Place multiple simple statements on a single line where appropriate (e.g. `if (x < 0) return 0;`, `for (int i=0; i<n; ++i) cin >> a[i];`).
  - Use concise variable and function names (`n, m, k, a, ans, adj, dp, solve(), calc()`) rather than verbose multi-word identifiers.
- **Selective English Comments**:
  - Comment ONLY on functions that genuinely require explanation. Avoid trivial or boilerplate comments.
  - When commenting, strictly record: (1) core logic, (2) received data/parameters, (3) return value/result.
  - All comments must be written exclusively in English.
