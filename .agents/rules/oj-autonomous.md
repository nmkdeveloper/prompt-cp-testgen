---
trigger: always_on
description: "Always-on autonomous execution policy for OJ test engineering."
---
# OJ Autonomous Completion

When processing OJ test packages, do not ask the user for approval or permission to continue.

Automatically diagnose, repair, regenerate and rerun ordinary failures. Continue until success or the problem reaches an unrecoverable FAIL state.

For unrecoverable problems, write the literal `FAIL` in the report, document the cause and skip that problem in batch mode.

Before declaring success, run the offline-package-verifier and require PASS from every mandatory verification layer. Do not use Polygon API as the authoritative verifier.
