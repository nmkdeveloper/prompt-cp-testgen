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

### Layer 5 — Test-set semantics

Verify the final testset has exactly 100 tests for a successful problem.

Verify:
- tests are contiguous 01..100 under the target naming convention;
- every input has an answer;
- no missing answer files;
- no orphan input/output files;
- sample tests are first;
- subtask/group assignment matches the intended design;
- each subtask ends with multiple max-boundary tests whenever feasible;
- generator metadata resolves to real resources when retained in the package;
- no final testcase was manually patched.

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
| Tests | PASS/FAIL | ... | ... | ... |
| Testlib | PASS/FAIL | ... | ... | ... |
| Runtime | PASS/FAIL | ... | ... | ... |
| Solutions | PASS/FAIL | ... | ... | ... |
| Reproducibility | PASS/FAIL | ... | ... | ... |
| Final package | PASS/FAIL | ... | ... | ... |

The report must never claim a check ran when it did not.


## VNOJ importer compatibility layer

The offline verifier must include a dedicated compatibility layer derived from `references/vnoj_codeforces_polygon_importer.py`. The importer source is behavioral truth for this target.

At minimum, model and verify these observed assumptions:

- `problem.xml` exists and is parseable.
- A `testset` named `tests` exists.
- `testset/tests` is non-empty.
- `input-path-pattern` and `answer-path-pattern` resolve to real ZIP members for every test.
- At least test 1 exists at the exact resolved input path; this is the importer's definition of a Full Package check.
- The testset time limit is milliseconds and memory limit is bytes; verify units before building.
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

The verifier must report importer-contract failures before the ZIP is handed to the VNOJ site.

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
