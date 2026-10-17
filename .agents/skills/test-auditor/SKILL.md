---
name: test-auditor
description: Performs the final correctness, integrity, coverage, answer-diversity, benchmark and artifact audit before Polygon packaging.
---
# Test Auditor

Verify:
- dynamic optimal final test count on success: total test count must always be a multiple of 10 (e.g. 10, 20, 30, 40, 50, 60, 70, 80, 90, 100... except for specialized problem types); suite completely covers all subtasks and essential test types
- samples first and unchanged
- all tests pass validator
- reference passes all tests
- brute/reference agree wherever applicable
- subtask boundary tests exist where feasible
- meaningful wrong solutions are tested and addressed
- answer distribution and output statistics: statistical frequency of non-sample outputs demonstrates broad spectrum diversity (some small, some large, anti-O(1) protection); if outputs overly cluster on identical values (excluding samples and YES/NO tasks), generator must be modified and candidate tests regenerated from scratch
- problem score equals statement points or 1đ default
- benchmark requirements completed where applicable
- generated artifacts were not manually edited
- strict I/O whitespace formatting: zero trailing spaces on any line, zero redundant blank lines, and exactly one terminating newline (`\n`) at EOF across all test inputs and outputs
- LaTeX math subscript escaping: all math subscripts escape underscores (`$s\_1$`, `$a\_i$`, `$dp\_{i, j}$` instead of `$s_1$`), zero disallowed characters, Unicode NFC normalized
- both Polygon and Themis packages staged and verified (Themis structure: `<problemname>/TEST[ID]/<problemname>.<ext>` matching Polygon test contents byte-for-byte)

Write findings incrementally to logs, invoke the offline-package-verifier, and summarize the complete verification matrix in `work/<problem-id>/report.md`. Do not declare PASS from structural inspection alone.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. All code, compiled binaries, logs, and packages must reside strictly inside `work/<problem-id>/`. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.


Generated testcase integrity: never edit `.in`, `.out`, or sample artifacts directly. Any correction must modify the generator/oracle/source and regenerate.
