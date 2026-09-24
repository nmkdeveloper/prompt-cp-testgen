---
name: test-auditor
description: Performs the final correctness, integrity, coverage, answer-diversity, benchmark and artifact audit before Polygon packaging.
---
# Test Auditor

Verify:
- exact final count of 100 on success
- samples first and unchanged
- all tests pass validator
- reference passes all tests
- brute/reference agree wherever applicable
- subtask boundary tests exist where feasible
- meaningful wrong solutions are tested and addressed
- answer distribution is reasonable without fabricated outputs
- benchmark requirements completed where applicable
- generated artifacts were not manually edited

Write findings incrementally to logs, invoke the offline-package-verifier, and summarize the complete verification matrix in `report.md`. Do not declare PASS from structural inspection alone.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.


Generated testcase integrity: never edit `.in`, `.out`, or sample artifacts directly. Any correction must modify the generator/oracle/source and regenerate.
