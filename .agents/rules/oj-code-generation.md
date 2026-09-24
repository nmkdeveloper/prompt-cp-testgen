---
trigger: always_on
description: "Always-on policy for agent-generated OS-adapted executable tooling and preferred C++."
---
# OJ Agent-Generated Toolchain

- Do not rely on pre-written runtime Python/C++ tools from the bundle.
- The agent must generate the executable toolchain for the actual problem and detected OS.
- Prefer C++20, then C++17.
- Prefer C++ for solution, brute, generator, validator, checker, benchmark and protected-runner code.
- Adapt process control and resource enforcement to Windows/macOS/Linux/FreeBSD/etc. using native APIs.
- All protected executions use 1 GiB RAM and 1 second limits and must kill the process tree on violation.
- Use `#include <testlib.h>` only when testlib is used.
