---
trigger: always_on
description: "Always-on protected execution limits and process-tree termination policy."
---
# OJ Protected Execution

- The agent must generate the protected runner itself for the detected OS/toolchain.
- Do not use a pre-written Python/C++ runner from the bundle.
- Hard limits: 1024 MiB RAM, 1000 ms wall time, 1000 ms CPU time where a reliable native limit exists.
- Active runaway auto-break: detect and break processes that hang, run into infinite loops (`while(true)`), or enter infinite recursion.
- Exceeding any limit or breaking runaway execution requires killing the complete process tree (parent and all descendant tasks).
- No timed-out or runaway child may remain running in the background.
- Prefer native OS resource/process APIs.
- If reliable enforcement cannot be established, do not run unprotected; after reasonable recovery mark the problem FAIL.
