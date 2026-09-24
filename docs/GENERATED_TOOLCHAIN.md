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
