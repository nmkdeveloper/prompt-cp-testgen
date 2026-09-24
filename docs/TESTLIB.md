# testlib Policy

Use testlib as the preferred C++ library for direct testcase generation, validation and custom checking when applicable.

## Mandatory include form

Always:

```cpp
#include <testlib.h>
```

Never:

```cpp
#include "testlib.h"
```

## Typical APIs

Generators: `registerGen`, `rnd` and related generator helpers.

Validators: `registerValidation`, `inf`, `ensure`, `ensuref`.

Checkers: `registerTestlibCmd`, `ouf`, `ans`, `quitf`.

## Agent-generated code

The bundle does not ship ready-made generator, validator or checker source. The agent must write the required C++ source for the actual problem.

Before compilation, the agent must locate the approved `testlib.h` installation and pass its containing directory through the compiler include path.

## Reproducibility

Use deterministic seeds/parameters for generated tests. Record them in internal provenance.

## Integrity

Validator failures are generator failures. Do not manually patch generated input/output to bypass a validator or checker problem. Fix source and regenerate.

## Scope

Python or other languages may be used for non-executable orchestration only when there is a concrete reason, but C++ is preferred for executable test-engineering components and all solution/brute/generator/validator/checker/benchmark/protected-runner code.
