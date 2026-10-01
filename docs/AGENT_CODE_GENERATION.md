# Agent Code Generation Contract

This bundle intentionally contains no ready-made runtime implementation. The agent must generate the actual executable code needed for each problem and host environment.

## Preferred executable language

Use C++ by default for:

- accepted/reference solution
- brute-force solution
- wrong-solution mutants
- testcase generators
- validators
- checkers
- benchmark programs
- protected execution harness
- process/resource adapters

Prefer C++20, falling back to C++17 when needed by the detected compiler.

Do not rewrite a supplied accepted/reference solution just for stylistic consistency. After verification, reuse it.

## Toolchain preflight (g++ and python portable check)

Immediately after checking problem statement existence:
- Check for `g++` and `python` in system PATH.
- If missing, download trusted portable builds (WinLibs standalone MinGW-w64 for Windows, official Python embeddable zip).
- Unpack locally and configure execution PATH to use them.

## Token economy in generated code

To minimize token usage during code generation:
- Write dense, compact code by placing multiple simple statements on a single line where appropriate (`if (x < 0) return 0;`, `for (int i=0; i<n; ++i) cin >> a[i];`).
- Use concise variable and function names (`n, m, k, a, ans, adj, dp, solve(), calc()`) instead of verbose long identifiers.

## Code comments policy

- Comment ONLY on functions that genuinely require explanation. Omit comments for obvious logic.
- When commenting, strictly document: (1) core logic, (2) received parameters/inputs, (3) return value/result.
- All comments must be written exclusively in English.

## Host detection before code generation

Detect before writing the runner/toolchain:

- OS and version
- CPU architecture
- compiler family and version
- supported C++ standard
- C/C++ runtime characteristics
- available native process APIs
- available resource-limit APIs
- available testlib installation
- target Polygon/VNOJ packaging constraints

Use this information to select the most appropriate native implementation.

## Protected runner & runaway watchdog

The agent must generate a protected runner for each actual environment. It must enforce:

- memory: 1024 MiB
- wall time: 1000 ms
- CPU time: 1000 ms where a reliable native limit exists
- active auto-break: detect and break infinite loops (`while(true)`), infinite recursion, and hanging tasks
- kill complete process tree (parent and all descendant tasks) on violation or runaway break
- no lingering child process after timeout

Preferred platform strategies are documented in `docs/OS_EXECUTION.md`.

The runner must not silently downgrade to unrestricted execution. If reliable enforcement cannot be established after reasonable attempts, mark the problem `FAIL`.

## Process-tree control

The runner must account for child processes created by the protected program. A timeout, runaway break, or memory violation must forcefully terminate the complete process tree.

## Single supervisory flow

Do not use worker pools or unnecessary worker threads. Prefer one supervisory execution flow with native OS waits/timers/resource controls. The overall workflow is strictly serial.

## Testlib

When testlib is used, generated C++ must contain:

```cpp
#include <testlib.h>
```

Never use the quoted form.

## Generated source lifecycle

Source code may be generated, compiled, tested, replaced and regenerated during the job. Generated artifacts have provenance. Runtime source is normally excluded from the final Polygon ZIP.

## Failure handling

Compilation or runtime failures are debugged automatically. Fix source and regenerate. Do not patch generated `.in/.out` artifacts manually.
