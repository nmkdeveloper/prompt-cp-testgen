---
trigger: always_on
description: "Always-on policy for agent-generated OS-adapted executable tooling and preferred C++."
---
# OJ Agent-Generated Toolchain

- Right after verifying problem files exist, immediately verify availability of `g++` and `python`; if missing, automatically download portable standalone builds from trusted sources and use them.
- Do not rely on pre-written runtime Python/C++ tools from the bundle.
- The agent must generate the executable toolchain for the actual problem and detected OS.
- Prefer C++20, then C++17.
- Prefer C++ for solution, brute, generator, validator, checker, benchmark and protected-runner code.
- All protected executions use 1 GiB RAM with hard time limits: solutions and mutants have a strict 1000 ms limit; generators and tooling code have a calibrated hard limit computed from a host FLOPS benchmark; an active auto-break watchdog interrupts runaway code (infinite loop, recursion) and kills the complete process tree.
- Token economy in generated code: write dense, compact code (multiple statements per line where practical) and short, concise variable/function names to minimize tokens.
- Code comments: comment only on functions that genuinely require explanation; state only logic, received inputs, and return value; write all comments exclusively in English.
- Use `#include <testlib.h>` only when testlib is used.
