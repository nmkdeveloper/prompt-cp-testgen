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


## VNOJ golden-template mode

Use the user-supplied Polygon Full Package as the golden structural template. Reproduce its package grammar and relationships as closely as possible while replacing only problem-specific content.

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

For a successful problem, `problem.xml` must declare exactly 100 final tests and reference:

```text
tests/%02d
 tests/%02d.a
```

or the exact equivalent required by the verified target profile.

### C++ / testlib

If `testlib.h` is used by any packaged C++ generator, validator or checker, include the actual version used by the build in `files/testlib.h`, and every such source must contain:

```cpp
#include <testlib.h>
```

Never use a quoted include.

### Generated scripts and binaries

The agent must write the package's C++ and script content itself. It may generate both `.sh` and `.bat` control scripts when the golden profile uses both. Binaries must correspond exactly to their declared source paths and binary types in `problem.xml`.

Do not lie about binary types. If the target package requires a platform-specific binary that cannot be produced reliably on the current machine, use verified cross-compilation if available; otherwise mark the problem FAIL rather than inserting a fake or incompatible binary.

### Final verification

After staging:

1. Validate every `problem.xml` path.
2. Verify language directories and statement files.
3. Verify all 100 test/answer pairs.
4. Verify checker/validator resources and tests.
5. Verify every declared source/binary pair exists and corresponds to the intended artifact.
6. Verify all `solution .desc` files are consistent with their source filenames/tags.
7. Verify no internal workspace files are included.
8. Open and structurally inspect the ZIP before success.


## VNOJ importer compatibility is mandatory

Do not declare package success from Polygon-like structure alone. Before final ZIP success, run the agent-generated offline verifier against:

1. Polygon package structure,
2. the user-supplied golden package, and
3. the supplied VNOJ importer source.

The staged package must satisfy the actual access patterns of `PolygonImporter`, including `statement/<language>/problem-properties.json` fields consumed by `parse_statements()`.

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
