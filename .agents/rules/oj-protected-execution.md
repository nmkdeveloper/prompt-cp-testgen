---
trigger: always_on
description: "Always-on protected execution limits and process-tree termination policy."
---
# OJ Protected Execution

- The agent must generate the protected runner itself for the detected OS/toolchain.
- Do not use a pre-written Python/C++ runner from the bundle.
- Hard limits: 1024 MiB RAM, 1000 ms wall time, 1000 ms CPU time where a reliable native limit exists.
- Exceeding a limit requires killing the complete process tree.
- No timed-out child may remain running in the background.
- Prefer native OS resource/process APIs.
- If reliable enforcement cannot be established, do not run unprotected; after reasonable recovery mark the problem FAIL.
