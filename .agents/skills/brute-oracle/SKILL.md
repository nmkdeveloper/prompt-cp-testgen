---
name: brute-oracle
description: Establishes a safe brute-force domain and performs differential verification between brute and the preferred reference solution on diverse small cases.
---
# Brute Oracle

Determine the largest practical brute domain from complexity. Generate a broad pool of small and structured-small candidates.

For eligible candidates:
validator -> brute -> reference -> compare

Every disagreement is an investigation target. Never patch output files to resolve a conflict. Repair the source oracle/reference/generator and regenerate.

Retain the count and scope of brute-verified candidates in logs and the final report.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.


## I/O contract — immutable

The original I/O mechanism is part of the problem specification. Never convert file I/O to stdin/stdout or vice versa. Preserve exact input/output filenames and case. Preserve `problem.xml` judging `input-file`/`output-file` values and `problem-properties.json` `inputFile`/`outputFile` values. If standard I/O is specified, do not invent filenames. If file I/O is specified, generated solution/brute/benchmark/protected execution must use the exact filenames. Any mismatch requires a source-level fix and regeneration.

## Bilingual tutorial — required

The successful default package contains both English and Vietnamese tutorials whenever tutorials are supported. Preserve supplied tutorial text in its source language and faithfully translate the missing default language. Keep problem.xml, tutorial files and problem-properties.json synchronized.
