---
trigger: always_on
description: "Always-on source, statement, sample, oracle and generated-artifact integrity rules."
---
# OJ Test Integrity

This is a non-negotiable source-integrity rule for OJ test engineering.

- Original statement content is authoritative.
- Never invent constraints, semantics, scoring, filenames or answers.
- Never change original sample input/output or sample order.
- `problem.md` may normalize extraction/formatting only; it must not alter meaning.
- Generated `.in/.out` artifacts are immutable. Fix source and regenerate.
- Never manually patch an output to make a solution pass.
