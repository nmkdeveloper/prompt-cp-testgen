---
name: offline-package-verifier
description: Builds and runs an offline, locally generated Polygon/VNOJ package verifier using the supplied golden package, available Polygon/package specifications, XML/schema tooling, and real compile/runtime checks; no Polygon API is required.
---
# Offline Package Verifier

This skill is the authoritative offline verification stage before a Polygon/VNOJ package may be declared valid.

## Core rule

Do not declare a package valid because:
- the ZIP opens;
- the directory tree looks plausible;
- `problem.xml` parses;
- a third-party Python library returns success;
- or the package resembles the golden sample.

A valid package requires layered structural, schema, semantic, build, runtime and golden-template verification.

## No API dependency

The verifier must work without Polygon API calls.

Do not use Polygon API as the authoritative verifier in this skill.

If Polygon/online APIs are unavailable, verification must still run using local evidence and local execution.

## Agent-generated verifier

The bundle intentionally contains no ready-made verifier implementation.

The agent must write the verifier for the current host/environment. Prefer Python for orchestration and package inspection because Python's ZIP/XML/filesystem ecosystem is useful here, while using C++ for executable solution/test tooling.

Before writing custom parsing logic, detect available local libraries. Prefer, when installed and appropriate:

- `defusedxml` for safe XML parsing;
- `lxml` for robust XML parsing/XPath and validation;
- `xmlschema` when a trusted local XSD is available;
- `jsonschema` for JSON artifacts with a trusted JSON Schema.

Python standard library fallbacks such as `zipfile`, `pathlib`, `hashlib`, `xml.etree.ElementTree`, `json` and `tomllib`/`yaml` equivalents may be used when specialized libraries are absent.

A specialized library is an implementation aid, not the source of truth. Never treat a library's successful parse as proof that a Polygon package is semantically valid.

## Verification layers

Run every applicable layer, serially.

### Layer 0 — Safe archive inspection

Verify:
- ZIP can be opened and fully read;
- no CRC errors;
- no duplicate archive members;
- no absolute paths;
- no `../` traversal;
- no unexpected symlinks or unsafe special files;
- filenames are valid for the target environment;
- archive contains no internal workspace artifacts that are forbidden by the package contract.

Extract to a clean temporary directory and never execute directly from an untrusted archive path without inspection.

### Layer 1 — Golden-template comparison

Use the supplied user package as a structural golden reference.

Compare package grammar and file-role relationships, including when applicable:
- root files;
- `problem.xml` placement;
- `tests/` and `%02d` naming;
- `statements/`;
- `statement-sections/`;
- `files/`;
- `solutions/`;
- `stresses/`;
- `scripts/`;
- root `doall`/`wipe` scripts;
- `tags`;
- checker and validator resources;
- source/binary declarations;
- `.desc` metadata conventions.

Do NOT compare problem-specific content such as samples, constraints, tags, checker logic or solution answers as though they were reusable template data.

The result must distinguish:
- required by target profile;
- present and correct;
- optional but valid;
- missing;
- inconsistent;
- forbidden;
- unexplained deviation.

### Layer 2 — XML validation

Parse `problem.xml` safely.

When a trusted local XSD or package schema is available, validate against it.

When no trusted XSD is available, perform a strict semantic validation based on:
- the supplied golden package;
- known target package rules available locally;
- the package's own declared relationships.

Check at minimum:
- XML well-formedness;
- required root attributes;
- language/name consistency;
- statement references;
- judging/testset structure;
- test count;
- input path pattern;
- answer path pattern;
- checker references;
- validator references;
- solution source/binary references;
- attachment/resource references;
- stress references;
- tags/resources where applicable.

Never invent unknown XML elements simply to make validation pass.

### Layer 3 — Referential integrity

For every path referenced by `problem.xml`, verify the target exists.

For every packaged source/binary relationship, verify both sides exist where required and correspond to the intended artifact.

Check for:
- dangling paths;
- case mismatches;
- duplicate logical artifacts;
- broken relative paths;
- source/binary type mismatches;
- stale `.desc` filenames;
- missing statement resources;
- missing language directories.

### Layer 4 — Statement and sample integrity

The final package must preserve original samples exactly.

Compare byte/content identity against the authoritative reconstructed/sample source wherever available.

Verify:
- sample inputs unchanged;
- sample outputs unchanged;
- sample order unchanged;
- sample count unchanged;
- sample references are consistent across statement artifacts;
- no generated test replaced a sample.

Never repair a sample during verification.

Verify canonical `problem.md` against the original source materials for semantic consistency.

### Layer 4.1 — TeX, LaTeX, Markdown & Character Verification (Crash & Conflict Prevention)

Before a package can be accepted, all textual and markup components must pass strict validation against Fura Online Judge's rendering and database constraints to prevent upload errors, crashes, and layout breakage:

1. **Disallowed Characters Sanitization (`DMOJ_PROBLEM_STATEMENT_DISALLOWED_CHARACTERS`)**:
   Fura Online Judge strictly forbids the following Unicode characters in problem statements, names, translations, and editorial content:
   `{ '“', '”', '‘', '’', '−', 'ﬀ', 'ﬁ', 'ﬂ', 'ﬃ', 'ﬄ' }`
   The verifier must scan `problem.xml` (all name and short-name tags), every `problem-properties.json` (`legend`, `input`, `output`, `interaction`, `scoring`, `notes`, `tutorial`), and all `.tex` / `.md` files.
   Zero occurrences of disallowed characters are permitted. The verifier must verify that:
   - Curly double quotes `“` and `”` (U+201C, U+201D) are replaced with ASCII `"` (U+0022).
   - Curly single quotes `‘` and `’` (U+2018, U+2019) are replaced with ASCII `'` (U+0027).
   - Unicode minus `−` (U+2212) is replaced with standard ASCII hyphen-minus `-` (U+002D).
   - Unicode typographic ligatures (`ﬀ`, `ﬁ`, `ﬂ`, `ﬃ`, `ﬄ`) are expanded to ASCII equivalents (`ff`, `fi`, `fl`, `ffi`, `ffl`).

2. **Vietnamese Unicode Integrity & Normalization (NFC & UTF-8)**:
   - Full native support for Vietnamese Unicode: Vietnamese statements (`statements/vietnamese/`), problem names, scoring, notes, and tutorials must faithfully preserve all Vietnamese letters and diacritics (`à, á, ả, ã, ạ, ă, ằ, ắ, ẳ, ẵ, ặ, â, ầ, ấ, ẩ, ẫ, ậ, è, é, ẻ, ẽ, ẹ, ê, ề, ế, ể, ễ, ệ, ì, í, ỉ, ĩ, ị, ò, ó, ỏ, õ, ọ, ô, ồ, ố, ổ, ỗ, ộ, ơ, ờ, ớ, ở, ỡ, ợ, ù, ú, ủ, ũ, ụ, ư, ừ, ứ, ử, ữ, ự, ỳ, ý, ỷ, ỹ, ỵ, đ, Đ` and uppercase).
   - Verify that all statement files are strictly encoded in **UTF-8 without BOM**.
   - Verify that all text is normalized to **Unicode NFC (Normalization Form C)** (`unicodedata.normalize('NFC', text)`). Decomposed diacritics (NFD / tổ hợp) must be composed into NFC to prevent font and rendering defects in Pandoc, KaTeX, and web browsers.
   - Verify zero mojibake, zero replacement characters (`\ufffd`), and that Vietnamese characters are not inadvertently stripped or corrupted during sanitization.

3. **LaTeX & Math Delimiter Verification**:
   - Inline math must strictly use single dollar delimiters: `$ ... $`.
   - Display/block math must strictly use double dollar delimiters: `$$ ... $$`.
   - Unescaped dollar signs in regular text are forbidden: currency or literal dollars must be written as `\$` or enclosed in backtick code spans.
   - **Subscript Underscore Escaping (`$s\_1$` mandatory)**:
     All math subscripts MUST escape underscores with a backslash: `$s\_1$`, `$a\_i$`, `$dp\_{i, j}$`, `$x\_{max}$` instead of raw `$s_1$`, `$a_i$`. The verifier must inspect all math formulas across TeX, Markdown, and `problem-properties.json` fields, rejecting unescaped subscript underscores that trigger Markdown italic markup corruption.
   - LaTeX bracket balance: all `\left ... \right`, `{ ... }`, `( ... )`, and math environments must be balanced.
   - Pandoc macro compatibility: only use standard TeX macros compatible with FuraOJ's Pandoc pipeline (`\bf`, `\it`, `\tt`, `\t`, `\text`, `\textbf`, `\textit`). Avoid unparseable raw LaTeX packages or undefined macros.

4. **Pandoc Conversion Dry-Run**:
   - The verifier must perform a dry-run conversion of all TeX sections using pandoc (GFM markdown target) to confirm that pandoc converts every statement section without syntax errors or process exceptions.

5. **Image & Asset Path Integrity**:
   - Every image referenced via Markdown `![image](<path>)` or HTML `<img src="<path>">` must exist as a real file in the corresponding statement directory.
   - Broken image paths cause upload warnings or broken web pages.

6. **Upload Conflict & Page Crash Prevention**:
   - **Problem Code**: Alphanumeric lowercase `^[a-z0-9]+$`, maximum length 20 characters, no spaces, hyphens, or uppercase letters.
   - **Problem Name**: Non-empty, maximum length 100 characters, passes `disallowed_characters_validator`.
   - **Resource Limits in Range**:
     - Time limit: default `1000` ms (1.0s), strictly within `[0.01, 60.0]` seconds.
     - Memory limit: default `1073741824` bytes (1 GB = 1048576 KB), strictly within `[0, 1048576]` KB (`DMOJ_PROBLEM_MAX_MEMORY_LIMIT`).
   - **Total Points > 0**:
     - Total problem points must be strictly greater than 0 (default 1đ).
     - For non-partial/unbatched problems, FuraOJ awards 1đ via `last_case.points = 1`.
     - For batched subtasks, verify that all batches contain at least one test, dependencies are valid, and sum of points > 0.
   - **init.yml Compilation Safety**:
     - Verify that `ProblemDataCompiler.generate` would succeed without raising `ProblemDataError` or setting `problem_data.feedback`.

### Layer 5 — Test-set semantics

Verify the final testset has a valid, dynamically calculated optimal test count covering all subtasks and essential test types for a successful problem (no rigid 100-test requirement).

Verify:
- tests are contiguous 01..NN under the target naming convention (%02d pattern preferred);
- every input has an answer;
- no missing answer files;
- no orphan input/output files;
- sample tests are first;
- subtask/group assignment matches the intended design and covers all subtasks;
- each subtask ends with multiple max-boundary tests whenever feasible;
- generator metadata resolves to real resources when retained in the package;
- no final testcase was manually patched.

### Layer 5.1 — Strict I/O formatting & whitespace verification

Verify byte-level whitespace and newline conformity across all test input and answer files (`tests/01`..`tests/NN`, `tests/01.a`..`tests/NN.a`):
- **Exact problem specification conformity**: data layout, token counts, and lines conform strictly to statement definitions.
- **Zero trailing whitespace**: absolutely NO line in any input or answer file contains trailing spaces (` `) or trailing tabs (`\t`).
- **Zero redundant blank lines**: absolutely NO consecutive newline characters (`\n\n`) unless explicitly required by the problem statement.
- **Single EOF newline termination**: every file must terminate with exactly ONE `\n`; zero trailing blank lines at the end of the file.

### Layer 6 — Runtime verification

The verifier must compile and run required package components using the agent-generated native protected execution toolchain.

Use the configured limits:
- 1024 MiB RAM;
- 1000 ms wall time;
- 1000 ms CPU target/limit where reliably enforceable;
- kill the complete process tree on violation;
- strictly serial execution.

Run applicable:
- validator tests;
- checker tests;
- reference solution;
- brute/reference differential checks;
- wrong solutions;
- benchmark programs;
- generator smoke tests.

A process exit of zero is not automatically equivalent to logical correctness; inspect declared verdicts and outputs.

### Layer 7 — Testlib verification

If testlib is used:
- verify `files/testlib.h` exists when the target profile requires it;
- compile every testlib-based source;
- statically inspect included testlib headers where practical;
- require the source include spelling to be exactly:
  `#include <testlib.h>`
- reject the quoted form:
  `#include "testlib.h"`
- run validator/checker test suites where present;
- verify checker verdict behavior on its checker-test corpus.

### Layer 8 — Semantic checker verification

Do not rely only on a checker executable existing.

Execute supplied checker self-tests when available and add targeted checker tests when needed.

Verify representative outcomes such as:
- correct answer;
- wrong answer;
- malformed output;
- presentation-format edge cases when relevant;
- invalid output structure;
- no-solution output when relevant.

The checker must not be weakened merely to accept a reference solution.

### Layer 9 — Solutions and survival verification

Run the verified reference on all final tests.

Run all meaningful wrong solutions/mutants serially.

The final report must show which tests produce:
- AC;
- WA;
- TLE;
- RE;
- other non-AC states where applicable.

Specialized killer tests must be distributed across the final suite, not clustered into one block.

When feasible, verify universal killers where all known wrong solutions are non-AC while the verified reference is AC.

### Layer 10 — Reproducibility and provenance

For every generated test, preserve internal provenance:
- generator source/hash;
- seed;
- parameters;
- validator version/hash;
- reference source/hash;
- test generation timestamp.

Regenerate selected tests from provenance and compare outputs. Any mismatch is a reproducibility failure.

Generated `.in` and `.out` artifacts remain immutable.

## PASS criteria

A package may be marked `PASS` only if every mandatory applicable layer passes and no unresolved critical issue remains.

A clean ZIP alone is insufficient.

## FAIL criteria

Mark the package `FAIL` if, after reasonable automatic recovery:
- required paths remain broken;
- schema/semantic validation remains unresolved;
- samples cannot be proven unchanged;
- reference and brute remain inconsistent on required domains;
- final testset is incomplete;
- checker/validator behavior is unresolved;
- runtime protection cannot be trusted on the host;
- package grammar is incompatible with the target golden profile;
- any other critical correctness issue cannot be resolved.

Write the literal `FAIL` into the final report and skip to the next problem in batch mode.

## Reporting

Log each verification layer as soon as it executes.

The final report must include a verification matrix:

| Layer | Status | Evidence | Failures/Warnings | Recovery |
|---|---|---|---|---|
| Archive | PASS/FAIL | ... | ... | ... |
| Golden template | PASS/FAIL | ... | ... | ... |
| XML/schema | PASS/FAIL | ... | ... | ... |
| References | PASS/FAIL | ... | ... | ... |
| Samples | PASS/FAIL | ... | ... | ... |
| TeX/Markdown/Characters | PASS/FAIL | ... | ... | ... |
| Tests | PASS/FAIL | ... | ... | ... |
| I/O Whitespace & Format | PASS/FAIL | ... | ... | ... |
| Testlib | PASS/FAIL | ... | ... | ... |
| Runtime | PASS/FAIL | ... | ... | ... |
| Solutions | PASS/FAIL | ... | ... | ... |
| Reproducibility | PASS/FAIL | ... | ... | ... |
| Final package | PASS/FAIL | ... | ... | ... |

The report must never claim a check ran when it did not.


## FuraOJ / VNOJ importer compatibility layer

The offline verifier must include a dedicated compatibility layer derived from the Fura Online Judge importer implementation (`D:\Workspaces\Github\furavietnam\furaoj\judge\utils\codeforces_polygon.py`) and `references/vnoj_codeforces_polygon_importer.py`. The importer source is behavioral truth for this target.

**CRITICAL NOTICE ON FURAOJ DIRECTORY**:
The directory `D:\Workspaces\Github\furavietnam\furaoj` contains the Fura Online Judge codebase.
**THIS DIRECTORY IS STRICTLY READONLY**. Never write to, modify, or delete any files in `D:\Workspaces\Github\furavietnam\furaoj`.

At minimum, model and verify these observed assumptions:

- `problem.xml` exists and is parseable.
- A `testset` named `tests` exists.
- `testset/tests` is non-empty.
- `input-path-pattern` and `answer-path-pattern` resolve to real ZIP members for every test.
- At least test 1 exists at the exact resolved input path; this is the importer's definition of a Full Package check.
- Default resource limits and scoring in `problem.xml`:
  - `time-limit` defaults to `1000` (milliseconds, corresponding to 1s time limit in FuraOJ).
  - `memory-limit` defaults to `1073741824` (bytes, corresponding to 1048576 KB / 1 GB RAM in FuraOJ).
  - Points default to `1đ` (1 point: unbatched non-partial imports award 1 point via `last_case.points = 1`, or subtask points must sum to 1đ default or problem points).
- Non-interactive packages require a checker. The checker must have `type="testlib"`.
- Built-in checker names used by the importer map to supported DMOJ checker modes; otherwise a C++ checker source must exist.
- Custom checker sources must be `.cpp` and are treated as testlib checker sources.
- Interactive packages require a C++ interactor source; the importer ignores the checker in this mode.
- Every statement with `type="application/x-tex"` must have a `path`, and its sibling `<statement-folder>/problem-properties.json` must exist.
- The `problem-properties.json` object must contain every key actually indexed by the importer: `legend`, `input`, `output`, `interaction`, `scoring`, `sampleTests`, `notes`, and `tutorial`; also verify `sampleTests` item shape.
- The statement language is taken from the `language` attribute; default output profile languages are `english` and `vietnamese`.
- For multilingual statements, the package must contain valid language identifiers that can be mapped to the target site's configured languages.
- `problem-properties.json` is decoded as UTF-8.
- Images referenced after statement conversion must point to actual package members before importer media upload.
- Main solution is expected under `<solutions>` with `tag="main"` if solution parsing is needed; its source path must exist.

The verifier must report importer-contract failures before the ZIP is handed to FuraOJ / VNOJ.

## Golden package comparison

Compare package *shape*, not problem-specific content. Check directory names, path conventions, descriptor relationships, statement language layout, files/resources layout, test numbering, `.a` answers, checker/validator test directories, solution descriptor conventions, `problem.xml` path patterns and script roles.

Do not copy the golden package's samples, checker, generators, solutions, tags, answers or problem text into a new package.


## I/O contract — immutable

The original I/O mechanism is part of the problem specification. Never convert file I/O to stdin/stdout or vice versa. Preserve exact input/output filenames and case. Preserve `problem.xml` judging `input-file`/`output-file` values and `problem-properties.json` `inputFile`/`outputFile` values. If standard I/O is specified, do not invent filenames. If file I/O is specified, generated solution/brute/benchmark/protected execution must use the exact filenames. Any mismatch requires a source-level fix and regeneration.

## Bilingual tutorial — required

The successful default package contains both English and Vietnamese tutorials whenever tutorials are supported. Preserve supplied tutorial text in its source language and faithfully translate the missing default language. Keep problem.xml, tutorial files and problem-properties.json synchronized.


## Additional hard checks: I/O and tutorials

### I/O contract check

Extract the I/O contract from the authoritative source before generation. Compare it against:
- original/golden package metadata;
- `problem.xml` judging `input-file` and `output-file`;
- each language's `problem-properties.json` `inputFile` and `outputFile`;
- generated solution/brute/benchmark source behavior;
- protected-run invocation mode.

Reject any silent normalization between file I/O and standard I/O.

When both XML judging file attributes are empty, the expected mode is standard I/O unless the source package proves otherwise. Do not invent filenames during package creation.

### Bilingual tutorial check

For successful packages using tutorials, require both English and Vietnamese tutorial artifacts and verify:
- both language directories exist;
- both tutorial files exist where the golden profile uses them;
- `problem.xml` references both;
- both `problem-properties.json` objects contain `tutorial`;
- supplied tutorial source is preserved exactly;
- generated translation is faithful to the source tutorial;
- tutorial language and statement language remain consistent.

The importer selecting one main tutorial is not permission to omit the other tutorial from the Polygon package.
