# Polygon/VNOJ Golden Package Profile

This document records the structural profile observed from the user-provided reference package and used by `polygon-package-builder`.

The reference package is treated as a **structural golden template**, not as a source of problem-specific data.

## Root-level pattern

Typical root artifacts in the reference package:

```text
problem.xml
check.cpp
check.exe
doall.sh
doall.bat
wipe.sh
wipe.bat
files/
statements/
statement-sections/
solutions/
stresses/
scripts/
tests/
tags
```

Root checker mirrors and binaries are conditional: include them when the target profile uses them.

## Files area

The reference package uses:

```text
files/
├── testlib.h
├── problem.tex
├── tutorial.tex
├── statements.ftl
├── olymp.sty
├── check.cpp
├── check.exe
├── validator.cpp
├── validator.exe
├── generator sources
├── generator binaries
└── tests/
    ├── checker-tests/
    └── validator-tests/
```

For testlib-based C++ files the required include is:

```cpp
#include <testlib.h>
```

The final package should contain the actual `testlib.h` used by the build when the target profile requires testlib.

## Statements

Default languages for generated packages are:

```text
english
vietnamese
```

Recommended structure, matching the reference package:

```text
statements/
├── english/
│   ├── problem.tex
│   ├── tutorial.tex
│   ├── problem-properties.json
│   ├── example.01
│   └── example.01.a
├── vietnamese/
│   ├── problem.tex
│   ├── tutorial.tex
│   ├── problem-properties.json
│   ├── example.01
│   └── example.01.a
├── .html/
│   ├── english/
│   └── vietnamese/
└── .pdf/
    ├── english/
    └── vietnamese/
```

Also mirror the section-based statement structure:

```text
statement-sections/
├── english/
└── vietnamese/
```

The exact set of `tutorial`, `notes`, `legend`, `input`, `output`, and example section files is derived from the reconstructed problem rather than invented.

## Tests

Successful problems have exactly:

```text
100 final tests
```

with:

```text
01 ... 100
01.a ... 100.a
```

The first tests are the original samples, preserved exactly. The sample order and contents are immutable.

## Solutions

The reference package stores solutions as:

```text
solutions/
├── source.cpp
├── source.cpp.desc
├── source.exe
└── ...
```

The `.desc` files record the solution filename, tag and author metadata. The generated package should keep descriptors consistent with their sources.

Prefer C++ solutions. Supplied AC/reference code remains the preferred implementation only after independent verification with brute force and adversarial tests.

## Stresses

When stress tests are useful, mirror:

```text
stresses/
├── 001
├── 002
└── ...
```

Stress artifacts are package content only when the target profile/problem uses them.

## Scripts

The reference package contains both Unix and Windows control scripts under `scripts/` and at the root. Generate the corresponding scripts yourself for the target problem/toolchain rather than copying generic implementations from this skills bundle.

Typical responsibilities include:

- input generation
- answer generation
- input-via-file(s)/stdout helpers
- checker tests
- validator tests
- full package build (`doall`)
- cleanup (`wipe`)

## `problem.xml`

The descriptor must be internally consistent with every packaged path and artifact.

### Fura Online Judge Default Limits & Scoring

Unless explicitly specified otherwise in the reconstructed problem statement, standard package defaults conforming to Fura Online Judge (`D:\Workspaces\Github\furavietnam\furaoj`, strictly READONLY) are:

- **Time limit**: Default **1s** (`<time-limit>1000</time-limit>` milliseconds). FuraOJ parses this as seconds: `float(testset.find('time-limit').text) / 1000` = `1.0`s.
- **Memory limit**: Default **1 GB RAM** (`<memory-limit>1073741824</memory-limit>` bytes). FuraOJ parses this into kilobytes: `int(testset.find('memory-limit').text) // 1024` = `1048576` KB (1024 MB).
- **Points**: Default **1đ** (1 point). For non-batched/standard tests, FuraOJ's importer sets `last_case.points = 1` if `total_points == 0`, giving 1 point total for solving the problem. For subtasks, point allocations should sum to the target points or 1đ default.

For the main final testset, use exactly 100 tests. `%02d` is preferred because it matches the reference profile and renders test 100 correctly.

Do not invent undocumented Polygon XML elements. For groups, points policies, dependencies or other advanced features, use verified Polygon package syntax from trusted source material or existing known-good packages.

## Fura Online Judge Importer Reference

The authoritative importer implementation is maintained in the Fura Online Judge repository at:
`D:\Workspaces\Github\furavietnam\furaoj\judge\utils\codeforces_polygon.py`
and CLI command:
`D:\Workspaces\Github\furavietnam\furaoj\judge\management\commands\import_polygon_package.py`

**CRITICAL NOTICE**:
`D:\Workspaces\Github\furavietnam\furaoj` is strictly **READONLY**. Never modify, delete, or add files to this directory. It is used exclusively as a behavioral reference.

## Golden-template principle

The agent should reproduce the **shape** of the reference package as closely as possible while still obeying the actual problem statement.

Do not copy:

- the reference problem's samples
- its constraints
- its checker logic
- its generator logic
- its tags
- its solutions
- its answers

Only the package structure and proven file-role conventions are reusable.
