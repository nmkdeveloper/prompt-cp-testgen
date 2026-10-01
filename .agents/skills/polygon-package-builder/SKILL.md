---
name: polygon-package-builder
description: Builds a clean Polygon package from verified generated artifacts and exports a ZIP containing only the files required by the target package format.
---
# Polygon Package Builder

Create a clean staging directory. Use an allowlist, not a recursive zip of the whole workspace.

Potential package content includes:
- problem.xml
- statements/
- tests/
- files/
- solutions/ only when required

Exclude internal analysis, logs, reports, candidate pools, provenance, caches, temporary files and unrelated source files.

Run the offline-package-verifier after staging and again after ZIP creation. Verify the ZIP opens and contains the required files before declaring success. Never use ZIP readability alone as proof of package validity.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.


## FuraOJ / VNOJ golden-template mode

Use the user-supplied Polygon Full Package as the golden structural template. Reproduce its package grammar and relationships as closely as possible while replacing only problem-specific content.

### FuraOJ default import limits & scoring

When building the package and generating `problem.xml`, use the standard Fura Online Judge defaults:
- **Default Memory Limit**: **1 GB RAM** (`<memory-limit>1073741824</memory-limit>` bytes, parsed by FuraOJ's importer as `1048576` KB = 1024 MB).
- **Default Time Limit**: **1s time** (`<time-limit>1000</time-limit>` milliseconds, parsed by FuraOJ's importer as `1.0` second).
- **Default Points**: **1đ** (1 point: for standard unbatched tests, FuraOJ's importer sets `last_case.points = 1` when `total_points == 0`, giving 1 point total for passing all tests; if subtasks are specified, ensure subtask points sum to the target score or 1đ default).

### Default languages

Use these two statement languages by default:

- `english`
- `vietnamese`

Use directory names and `problem.xml` language attributes matching these identifiers.

### Expected package areas

When applicable, the package should mirror the golden sample's areas:

```text
problem.xml
check.cpp / check.exe                 # root mirrors when required
doall.sh / doall.bat
wipe.sh / wipe.bat
files/
  testlib.h
  problem.tex
  tutorial.tex
  statements.ftl
  olymp.sty
  check.cpp / validator.cpp / generators
  corresponding target binaries
  tests/checker-tests/
  tests/validator-tests/
statements/
  english/
  vietnamese/
  .html/english/
  .html/vietnamese/
  .pdf/english/
  .pdf/vietnamese/
statement-sections/
  english/
  vietnamese/
solutions/
stresses/
scripts/
tests/
tags
```

The exact presence of an artifact is conditional on whether the problem actually uses that component and whether the target profile requires it. Do not add meaningless placeholder binaries or unrelated files.

### Test descriptor

For a successful problem, `problem.xml` must declare the selected final tests (contiguous `01`..`NN`) and reference:

```text
tests/%02d
tests/%02d.a
```

or the exact equivalent required by the verified target profile.
Every test input and answer file must strictly conform to problem specifications with zero trailing whitespace, zero redundant blank lines, and exactly one terminating newline (`\n`) at EOF.

### C++ / testlib

If `testlib.h` is used by any packaged C++ generator, validator or checker, include the actual version used by the build in `files/testlib.h`, and every such source must contain:

```cpp
#include <testlib.h>
```

Never use a quoted include.

### Generated scripts and binaries

The agent must write the package's C++ and script content itself. It may generate both `.sh` and `.bat` control scripts when the golden profile uses both. Binaries must correspond exactly to their declared source paths and binary types in `problem.xml`.

Do not lie about binary types. If the target package requires a platform-specific binary that cannot be produced reliably on the current machine, use verified cross-compilation if available; otherwise mark the problem FAIL rather than inserting a fake or incompatible binary.

### TeX, LaTeX, Markdown & Character Sanitization (Crash & Conflict Prevention)

Before finalizing statement files and packaging:
1. **Character Sanitization (`DMOJ_PROBLEM_STATEMENT_DISALLOWED_CHARACTERS`)**:
   Scan all names and statement fields in `problem.xml`, `problem-properties.json`, and `.tex` files.
   Zero occurrences of disallowed characters `{ '“', '”', '‘', '’', '−', 'ﬀ', 'ﬁ', 'ﬂ', 'ﬃ', 'ﬄ' }` are permitted.
   - Replace curly double quotes `“`, `”` with ASCII `"`.
   - Replace curly single quotes `‘`, `’` with ASCII `'`.
   - Replace Unicode minus `−` with ASCII `-`.
   - Expand ligatures `ﬀ`, `ﬁ`, `ﬂ`, `ﬃ`, `ﬄ` to `ff`, `fi`, `fl`, `ffi`, `ffl`.
2. **Vietnamese Unicode Support (NFC & UTF-8)**:
   - Full native preservation of Vietnamese Unicode in `statements/vietnamese/` and `problem.xml`. Never strip, remove, or corrupt Vietnamese tone marks or letters (`đ, Đ, ư, ơ, ê, ô, ă, â` and all accented vowels).
   - Encode all statement files strictly in **UTF-8 without BOM**.
   - Normalize all text with **Unicode NFC** (`unicodedata.normalize('NFC', text)`) to ensure diacritics are precomposed and render correctly across Pandoc, KaTeX, and web browsers.
3. **LaTeX & Math Delimiters**:
   - Strictly use `$ ... $` for inline math and `$$ ... $$` for display math.
   - Escape literal dollar signs as `\$`.
   - **Subscript Underscore Escaping (`$s\_1$` mandatory)**: All math subscripts MUST escape underscores with backslash (`$s\_1$`, `$a\_i$`, `$dp\_{i, j}$` instead of raw `$s_1$`, `$a_i$`) to prevent the markdown parser from interpreting underscores as italic emphasis.
   - Ensure all math environments and braces are balanced.
4. **Image & Resource Paths**:
   - Ensure every image linked via `![image](<path>)` or `<img src="<path>">` exists within the statement directory.

### Final verification

After staging:

1. Validate every `problem.xml` path.
2. Verify language directories and statement files.
3. Verify TeX, LaTeX, Markdown formatting and zero disallowed characters.
4. Verify all final test/answer pairs exist and match.
5. Verify strict I/O formatting: zero trailing whitespace on any line, no redundant blank lines, and exactly one terminating newline (`\n`) at EOF across all test inputs and outputs.
6. Verify checker/validator resources and tests.
7. Verify every declared source/binary pair exists and corresponds to the intended artifact.
8. Verify all `solution .desc` files are consistent with their source filenames/tags.
9. Verify no internal workspace files are included.
10. Open and structurally inspect the ZIP before success.


## FuraOJ / VNOJ importer compatibility is mandatory

Do not declare package success from Polygon-like structure alone. Before final ZIP success, run the agent-generated offline verifier against:

1. Polygon package structure,
2. the user-supplied golden package, and
3. the Fura Online Judge importer logic (`D:\Workspaces\Github\furavietnam\furaoj\judge\utils\codeforces_polygon.py`).

**CRITICAL NOTICE ON FURAOJ DIRECTORY**:
The directory `D:\Workspaces\Github\furavietnam\furaoj` contains the Fura Online Judge codebase (including `judge/management/commands/import_polygon_package.py` and `judge/utils/codeforces_polygon.py`).
**THIS DIRECTORY IS STRICTLY READONLY**. Never write to, modify, or delete any files in `D:\Workspaces\Github\furavietnam\furaoj`. All package creation and testing must reside strictly in the workspace `prompt-cp-testgen`.

The staged package must satisfy the actual access patterns of `PolygonImporter` and prevent upload conflicts or page crashes:
- `time-limit` defaults to 1000 ms (1s) and `memory-limit` defaults to 1073741824 bytes (1 GB); limits must remain within FuraOJ supported range.
- Points default to 1đ (1 point), total points must be strictly > 0.
- All text fields in `statement/<language>/problem-properties.json` (`legend`, `input`, `output`, `interaction`, `scoring`, `sampleTests`, `notes`, `tutorial`) must be present, valid UTF-8, and free of disallowed characters.
- Problem code must be clean lowercase alphanumeric (`^[a-z0-9]+$`), length <= 20.
- Problem name must be non-empty, length <= 100, and free of disallowed characters.

The package must be importable without triggering failures such as `KeyError: 'legend'`.


## I/O contract — immutable

The original I/O mechanism is part of the problem specification. Never convert file I/O to stdin/stdout or vice versa. Preserve exact input/output filenames and case. Preserve `problem.xml` judging `input-file`/`output-file` values and `problem-properties.json` `inputFile`/`outputFile` values. If standard I/O is specified, do not invent filenames. If file I/O is specified, generated solution/brute/benchmark/protected execution must use the exact filenames. Any mismatch requires a source-level fix and regeneration.

## Bilingual tutorial — required

The successful default package contains both English and Vietnamese tutorials whenever tutorials are supported. Preserve supplied tutorial text in its source language and faithfully translate the missing default language. Keep problem.xml, tutorial files and problem-properties.json synchronized.


## I/O MUST NOT BE NORMALIZED

The package builder must not decide that stdin/stdout is "more standard" and rewrite a source problem to use it.

The builder must first create an immutable `io_contract` from the authoritative statement and the supplied Polygon package.

The contract includes:
- io_method: `standard` or `file`;
- exact input filename, or null;
- exact output filename, or null;
- original `judging` attributes;
- original `problem-properties.json` `inputFile`/`outputFile`.

The final package must preserve that contract exactly.

Generated solution/brute/benchmark programs must be written to match that contract. Runtime wrappers may stage files internally but must not alter the observable problem I/O.

If the source uses standard I/O, do not add filenames.
If the source uses file I/O, do not replace the filenames with generic names such as `input.txt`, `output.txt`, `input.inp`, or `output.out`.

## TUTORIALS ARE TWO-LANGUAGE ARTIFACTS

When tutorials are supported by the golden profile, the builder must produce both English and Vietnamese tutorials.

Keep:
- `problem.xml` tutorial entries for both languages;
- `statements/english/tutorial.tex`;
- `statements/vietnamese/tutorial.tex`;
- `statement-sections/english/tutorial.tex`;
- `statement-sections/vietnamese/tutorial.tex`;
- both languages' `problem-properties.json` `tutorial`.

A supplied tutorial must be preserved in its source language. If the other default language is missing, create a faithful translation. Do not delete the second tutorial because the site importer later selects one main tutorial.
