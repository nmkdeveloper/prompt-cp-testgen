---
name: solution-analyzer
description: Analyzes intended, accepted, reference, brute, partial and wrong competitive-programming solutions to infer algorithmic capability boundaries and likely bugs.
---
# Solution Analyzer

Discover all candidate implementations. Prefer supplied AC/official/reference code, but never trust the label without verification.

Infer:
- intended complexity and bottleneck
- brute complexity and safe domain
- intermediate algorithm classes
- likely implementation mistakes
- properties that make the problem easier
- which solution classes should pass each potential subtask

Produce a capability matrix used by subtask and test design.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.


## I/O contract — immutable

The original I/O mechanism is part of the problem specification. Never convert file I/O to stdin/stdout or vice versa. Preserve exact input/output filenames and case. Preserve `problem.xml` judging `input-file`/`output-file` values and `problem-properties.json` `inputFile`/`outputFile` values. If standard I/O is specified, do not invent filenames. If file I/O is specified, generated solution/brute/benchmark/protected execution must use the exact filenames. Any mismatch requires a source-level fix and regeneration.

## Bilingual tutorial — required

The successful default package contains both English and Vietnamese tutorials whenever tutorials are supported. Preserve supplied tutorial text in its source language and faithfully translate the missing default language. Keep problem.xml, tutorial files and problem-properties.json synchronized.


## Solution I/O preservation

When reviewing or writing a solution, first determine the original I/O mode from the authoritative problem statement and package.

Do not rewrite a file-based problem to use `cin/cout` simply because it is easier for local testing, and do not rewrite a standard-I/O problem to use invented files.

For a file-I/O problem, the generated/reference/brute/benchmark solutions must open the exact specified filenames with exact case.

For a standard-I/O problem, use standard streams.

The protected runner must adapt to the same contract instead of changing the solution source.
