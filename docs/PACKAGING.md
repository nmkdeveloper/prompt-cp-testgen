# Polygon Packaging Policy

## Clean build

Build the final package in a clean staging directory. Never zip the whole work directory.

## Allowlist principle

Include only files required by the target Polygon package format, such as `problem.xml`, `statements/`, `tests/`, `files/`, and `solutions/` only when required.

Exclude:

- logs
- reports
- candidate pools
- internal analysis
- provenance
- temporary build outputs
- generated runtime tooling not required by Polygon
- caches
- unrelated source files

## Samples

Keep statement samples first and preserve their source content exactly. Generated tests follow them.

## Artifact immutability

Final `.in/.out` files are generated artifacts. Any correction is made by changing the source generator/oracle/reference logic and regenerating.

## Agent-generated runtime code

The agent may create `protected_runner.cpp`, generators, validators, brute/reference programs, wrong-solution mutants, benchmarks and checkers in the working directory. These are internal implementation artifacts unless the target Polygon package explicitly requires them.

## Final checks

- ZIP opens successfully.
- Required package paths exist.
- Dynamic optimal number of final tests (covering all subtasks and test types) on successful problems.
- Sample tests are first.
- No accidental internal files are present.
- Test files and answers correspond one-to-one.


## Golden template mode

When a user supplies a reference Polygon package, use it as a structural golden template. Mirror the observed package grammar as closely as possible for the target site.

The default statement language set is:

- english
- vietnamese

The final package should preserve the sample package's useful artifact categories (including C++/scripts/testlib resources) when the target problem actually uses them.

Do not copy the sample problem's content. Copy only its structural conventions.
