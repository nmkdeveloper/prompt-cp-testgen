# Golden Package Contract

This is a lightweight, problem-agnostic contract extracted from the user-supplied Polygon Full Package sample. It describes structure and relationships, not problem-specific content.

## Observed root categories

```text
problem.xml
check.cpp / check.exe (when mirrored)
doall.sh / doall.bat
wipe.sh / wipe.bat
files/
statements/
statement-sections/
solutions/
stresses/
scripts/
tests/
tags
```

## Observed `problem.xml` relationships

The sample uses relationships for:

- `<names>` / language-specific names
- `<statements>` and optional `<tutorials>`
- `<judging>` → `<testset>` → `<test-count>` / path patterns / `<tests>`
- `<files>` → resources / attachments / executables
- `<assets>` → checker / validators / solutions
- `<properties>`
- `<stresses>`
- `<tags>`

The verifier should validate all paths referenced by these relationships when those elements occur in the target package.

## Observed test layout

The golden sample uses `%02d` for the primary input/answer path patterns and stores tests as paired files such as:

```text
tests/01
tests/01.a
...
tests/36
tests/36.a
```

The new workflow requires exactly 100 final tests on success, so the target package should use the same `%02d` convention for `01` through `100` unless verified target syntax requires another equivalent pattern.

## Observed statement layout

The sample contains source, HTML and PDF statement artifacts plus `statement-sections`. The generated target defaults to exactly two languages:

```text
english
vietnamese
```

When a target problem requires a tutorial, properties JSON, examples, or specific statement sections, generate them consistently across the configured languages. Do not copy the sample's Russian language merely because the golden sample uses it.

## Observed testlib layout

The sample stores `files/testlib.h` and testlib-based checker/validator sources under `files/`. When testlib is used, the target package should include the actual header needed by the generated package and the C++ sources must use:

```cpp
#include <testlib.h>
```

## Observed checker/validator test suites

The sample includes:

```text
files/tests/checker-tests/
files/tests/validator-tests/
```

When checker/validator self-tests are used, the verifier must execute and confirm their declared outcomes.

## Observed solutions/stresses

The sample has a `solutions/` directory with source/binary/`.desc` artifacts and a `stresses/` directory referenced by `problem.xml`. Include these only when the target package actually uses them.

## Golden principle

Copy structure, not content. Never copy the golden problem's samples, answers, constraints, checker logic, generators, tags, or solutions into another problem.
