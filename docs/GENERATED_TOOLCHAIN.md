# Generated Toolchain Policy

## Purpose

This bundle intentionally does NOT ship pre-written runtime Python/C++ tools such as a protected runner, generator, validator, brute solver, checker, benchmark executable, or orchestration program.

The agent must create the required source code for each actual problem and execution environment. This prevents the bundle from hard-coding assumptions about a user's OS, compiler, filesystem, sandbox, or installed toolchain.

## Language Priority

For problem-specific executable code, the preferred implementation language is C++. Use C++ first for:

- reference/solution code
- brute-force code
- wrong-solution mutants when generated
- generators
- validators
- custom checkers
- benchmark programs
- protected execution wrappers
- helper executables that directly launch or inspect child processes

Prefer the newest C++ standard that is reliably supported by the detected environment. Prefer C++20, then C++17 when C++20 is not reliably available.

Do not rewrite a supplied AC/reference solution merely for style. Once verified, reuse it.

## Toolchain Preflight & Portable Fallback (g++ and python)

Immediately after confirming the problem statement/input files exist, the very first toolchain action is verifying whether `g++` and `python` are available on the host system:
1. Check executable paths (`where.exe g++`, `where.exe python` on Windows, or `which g++`, `which python3` on Unix).
2. If `g++` is missing: Search and download a trusted portable/standalone distribution (e.g., WinLibs standalone MinGW-w64 build for Windows via official/GitHub releases, or standalone toolchain archive). Unpack locally into a workspace toolchain directory and configure environment paths to use it.
3. If `python` is missing: Download an official portable/embeddable package (e.g., Python embeddable zip from python.org). Unpack locally and configure environment paths.
4. Use these verified portable toolchains across all subsequent compilation, testing, and script executions.

## Runaway Execution Auto-Break & Process-Tree Termination

The generated protected runner must actively guard against runaway tasks:
- **Infinite loops & recursion**: Automatically detect and break execution when child processes run past time limits due to infinite loops (`while(true)`), infinite recursion (deep stack hangs), or exponential algorithms.
- **Process-tree termination**: When the timeout limit is reached or a runaway break is triggered, forcefully kill the entire process tree (parent executable and all spawned descendant processes).
- **Zero background leakage**: Guarantee that no orphaned or zombie tasks remain running in the OS.

## Token Economy in Generated Code

To conserve token budget across prompts and outputs without sacrificing algorithmic precision:
- **Dense code style**: Place multiple simple statements on a single line where appropriate (e.g., `if (x < 0) return 0;`, `for (int i=0; i<n; ++i) cin >> a[i];`, combining declarations).
- **Concise naming**: Use short, compact, meaningful names (`n, m, k, a, b, ans, res, adj, vis, dis, dp, solve(), calc(), get(), init()`) rather than verbose multi-word identifiers.

## Code Comments Policy

- **Minimal & selective**: Add comments ONLY to functions that genuinely require explanation. Trivial or self-explanatory functions must have zero comments.
- **Strict 3-part format**: When a comment is necessary, record strictly:
  1. Core logic/algorithm
  2. Received data/inputs
  3. Returned result/output
  (e.g., `// Logic: Dijkstra shortest path. In: src node, adj list with weights. Out: min distance vector.`)
- **English only**: All comments throughout all generated sources must be written exclusively in English.

## Agent-Owned Code Generation

At the start of each problem, the agent must detect:

- operating system and version
- architecture
- compiler family/version
- supported C++ standard
- available process/resource APIs
- available testlib installation
- target package requirements

Then generate the smallest project-specific native toolchain needed for the problem.

The agent may create temporary source files inside the working directory, compile them, test them, replace them, and regenerate them. None of these internal source files should enter the final Polygon ZIP unless the target package requires them.

## No Generic Runtime Assumption

Do not assume that one pre-written runner will behave identically across Windows, Linux, macOS, FreeBSD, or other systems. The agent must use OS-specific native APIs where they provide stronger enforcement or process-tree control.

## Testlib

When C++ testlib is used, the source MUST contain exactly:

```cpp
#include <testlib.h>
```

and MUST NOT contain:

```cpp
#include "testlib.h"
```

The agent must locate or configure the installed testlib include directory and verify the generated source before compilation.

## Source-of-Truth Rule

Generated runtime code is derived from the reconstructed problem and verified inputs. It must not invent unsupported semantics.

## Regeneration

If generated source is wrong, fix the source and regenerate. Never manually patch generated input or answer artifacts.


## Polygon-package runtime artifacts

The generated C++/script toolchain may be internal during test engineering, but when the target Polygon/VNOJ profile requires sources, scripts or binaries inside the final package, the agent must generate and package those artifacts in the same role/layout as the golden package.

The generated package-side C++ testlib components must use:

```cpp
#include <testlib.h>
```

The actual `testlib.h` used for compilation must be copied into `files/testlib.h` when required by the package profile.
