# Offline Polygon/VNOJ Package Verification

This workflow verifies a generated Polygon Full Package without relying on Polygon API calls.

## Verification stack

Use the strongest locally available combination:

1. Safe ZIP/archive inspection with Python `zipfile` and filesystem checks.
2. XML parsing with `defusedxml` or `lxml` when available.
3. XML Schema validation with `xmlschema` or `lxml` only when a trusted local XSD is available.
4. JSON Schema validation with `jsonschema` for generated JSON artifacts when a trusted schema exists.
5. Structural comparison against the user-provided golden package.
6. Referential and semantic checks for `problem.xml` and package contents.
7. Native compile/runtime checks using the agent-generated protected runner.
8. Testlib validator/checker self-tests.
9. Reference/brute differential testing.
10. Wrong-solution and mutant survival testing.
11. Benchmarking and reproducibility checks.

No single library is authoritative. The strongest result comes from multiple independent layers.

## Python library guidance

The agent should inspect the host before coding the verifier. If these packages are installed, prefer them where appropriate:

- `defusedxml` — safe XML parsing.
- `lxml` — XML/XPath processing and schema validation when an XSD is available.
- `xmlschema` — XSD-driven validation when a trusted XSD is available.
- `jsonschema` — validation of JSON artifacts against a trusted schema.

Do not install or require a package merely to make the verifier appear stronger. If a dependency is missing, use a correct standard-library fallback when possible and record the fallback in the log.

`polyconv` or other conversion/import utilities must not be treated as the authoritative Polygon package validator unless their capabilities have been independently verified for the exact package features being tested.

## Golden package as structural oracle

The supplied sample package is the primary structural reference for VNOJ compatibility.

Use it to learn package conventions such as:

```text
problem.xml
check.cpp / check.exe
files/
statements/
statement-sections/
solutions/
stresses/
scripts/
tests/
tags
doall.sh
 doall.bat
wipe.sh
wipe.bat
```

The exact presence of each artifact remains problem-dependent. The verifier must not require files that the target package does not need.

The golden package's problem-specific samples, constraints, checker logic, generator logic, answers and tags are not copied into new problems.

## Recommended verification gate

```text
ZIP SAFE
   ↓
GOLDEN STRUCTURE OK
   ↓
XML / SCHEMA OK
   ↓
ALL REFERENCES RESOLVE
   ↓
SAMPLES IMMUTABLE
   ↓
FINAL TESTS OK
   ↓
TESTLIB / CHECKER / VALIDATOR OK
   ↓
REFERENCE OK
   ↓
BRUTE DIFFERENTIAL OK
   ↓
WRONG SOLUTIONS ATTACKED
   ↓
BENCHMARK OK
   ↓
REPRODUCIBILITY OK
   ↓
PACKAGE PASS
```

Any mandatory failure blocks `PASS`.
