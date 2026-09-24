# Installation and Usage

## Antigravity

Copy the bundle into the project root so these paths are available:

```text
.agents/skills/
.agents/rules/
AGENTS.md
```

The main skill is:

```text
.agents/skills/oj-test-engineering/SKILL.md
```

## Cursor

Copy the bundle into the project root so these paths are available:

```text
.agents/skills/
.cursor/rules/
AGENTS.md
```

The same shared skills are used; Cursor-specific behavior is enforced through `.cursor/rules/*.mdc`.

## Runtime toolchain

Do not install a generic prewritten runner from this bundle. The agent must inspect the actual host and generate the protected runner and other executable tools itself.

Preferred language: C++.
Preferred standard: C++20, falling back to C++17 if necessary.

## testlib

Provide an approved `testlib.h` installation. The generated C++ source must use:

```cpp
#include <testlib.h>
```

never:

```cpp
#include "testlib.h"
```

## Execution limits

The generated protected runner must enforce:

- 1024 MiB memory
- 1000 ms wall time
- 1000 ms CPU time where the host exposes a reliable CPU-time limit
- process-tree cleanup

## Invocation

Open the repository in Antigravity or Cursor and invoke the `oj-test-engineering` skill. Give the agent the problem input package. The workflow is autonomous, single-agent, and serial; it must not ask for approval or spawn subagents.

## Offline package verification

The mandatory verifier skill is:

```text
.agents/skills/offline-package-verifier/SKILL.md
```

It must run without Polygon API calls. The agent generates the verifier locally for the detected host and uses the strongest locally available XML/JSON tooling plus real compile/runtime checks. The user-provided Polygon package is the structural golden template.
