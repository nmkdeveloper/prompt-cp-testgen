---
name: test-auditor
description: Performs the final correctness, integrity, coverage, answer-diversity, benchmark and artifact audit before Polygon packaging.
---
# Test Auditor

Verify:
- dynamic optimal final test count on success (no rigid 100 requirement; suite completely covers all subtasks and essential test types)
- samples first and unchanged
- all tests pass validator
- reference passes all tests
- brute/reference agree wherever applicable
- subtask boundary tests exist where feasible
- meaningful wrong solutions are tested and addressed
- answer distribution is reasonable without fabricated outputs
- benchmark requirements completed where applicable
- generated artifacts were not manually edited
- strict I/O whitespace formatting: zero trailing spaces on any line, zero redundant blank lines, and exactly one terminating newline (`\n`) at EOF across all test inputs and outputs
- LaTeX math subscript escaping: all math subscripts escape underscores (`$s\_1$`, `$a\_i$`, `$dp\_{i, j}$` instead of `$s_1$`), zero disallowed characters, Unicode NFC normalized

Write findings incrementally to logs, invoke the offline-package-verifier, and summarize the complete verification matrix in `report.md`. Do not declare PASS from structural inspection alone.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.


Generated testcase integrity: never edit `.in`, `.out`, or sample artifacts directly. Any correction must modify the generator/oracle/source and regenerate.
