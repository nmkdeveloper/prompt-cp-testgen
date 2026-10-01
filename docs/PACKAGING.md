# Packaging Policy (Dual Packaging: Polygon & Themis)

## Dual packaging requirement

Every successful problem run generates two distinct distribution archives:
1. **Polygon Full Package ZIP**: `<problemname>-polygon.zip` (for FuraOJ / VNOJ / Polygon).
2. **Standard Themis Package ZIP**: `<problemname>-themis.zip` (for Themis grading software).

## Clean build

Build both packages in clean staging directories (`polygon-package/` and `themis-package/<problemname>/`). Never zip the whole workspace directory.

## Allowlist principle

Include only files required by each target package format.

Exclude:

- logs
- reports
- candidate pools
- internal analysis
- provenance
- temporary build outputs
- generated runtime tooling not required by Polygon or Themis
- caches
- unrelated source files

## Themis package structure

The companion Themis archive layout:
```text
<problemname>/
  TEST01/
    <problemname>.<ext_inp>
    <problemname>.<ext_out>
  TEST02/
    <problemname>.<ext_inp>
    <problemname>.<ext_out>
  ...
  TEST[NN]/
    <problemname>.<ext_inp>
    <problemname>.<ext_out>
```

- `<problemname>`: the problem code / short name (e.g. `SUM`, `socdist`, `solve`).
- `TEST[ID]`: directory name formatted as `TEST01`, `TEST02`, ... `TESTNN` (%02d pattern, or %03d if tests >= 100).
- `<problemname>.<ext_inp>` & `<problemname>.<ext_out>`: exact filenames and extensions as mandated by the problem statement (preserving exact case, e.g. `sum.inp`/`sum.out` or `SUM.INP`/`SUM.OUT`). If standard I/O (stdin/stdout) was specified in the problem statement, in Themis it standardizes to `<problemname>.INP` and `<problemname>.OUT` (or `.inp`/`.out` matching problem code case).
- Test contents in `<problemname>.<ext_inp>` and `<problemname>.<ext_out>` correspond byte-for-byte to the verified Polygon tests `01`..`NN` and answers `01.a`..`NN.a`.
- Strict I/O whitespace formatting rules apply equally: zero trailing spaces/tabs, zero redundant blank lines, and exactly one terminating newline (`\n`) at EOF.

## Samples

Keep statement samples first and preserve their source content exactly. Generated tests follow them.

## Artifact immutability

Final `.in/.out` files are generated artifacts. Any correction is made by changing the source generator/oracle/reference logic and regenerating.

## Agent-generated runtime code

The agent may create `protected_runner.cpp`, generators, validators, brute/reference programs, wrong-solution mutants, benchmarks and checkers in the working directory. These are internal implementation artifacts unless the target package explicitly requires them.

## Final checks

- Both Polygon and Themis ZIPs open successfully.
- Required package paths exist in both packages.
- Dynamic optimal number of final tests (covering all subtasks and test types) on successful problems.
- Sample tests are first.
- Themis layout `<problemname>/TEST[ID]/<problemname>.<ext>` verified with byte-for-byte fidelity against Polygon tests.
- No accidental internal files are present in either ZIP.
- Test files and answers correspond one-to-one with zero whitespace violations.


## Golden template mode

When a user supplies a reference Polygon package, use it as a structural golden template. Mirror the observed package grammar as closely as possible for the target site.

The default statement language set is:

- english
- vietnamese

The final package should preserve the sample package's useful artifact categories (including C++/scripts/testlib resources) when the target problem actually uses them.

Do not copy the sample problem's content. Copy only its structural conventions.
