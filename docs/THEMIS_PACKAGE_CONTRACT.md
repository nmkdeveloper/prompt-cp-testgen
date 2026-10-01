# Standard Themis Package Contract

## Overview

In Vietnamese competitive programming contests and high-school / university judging environments, **Themis** is the widely adopted automated grading tool.

Every test engineering run produces a standard Themis companion package ZIP (`<problemname>-themis.zip` or `themis-package.zip`) alongside the Polygon Full Package ZIP.

## Archive Layout

Inside the Themis ZIP archive:

```text
<problemname>/
├── TEST01/
│   ├── <problemname>.<ext_inp>
│   └── <problemname>.<ext_out>
├── TEST02/
│   ├── <problemname>.<ext_inp>
│   └── <problemname>.<ext_out>
├── ...
└── TEST[NN]/
    ├── <problemname>.<ext_inp>
    └── <problemname>.<ext_out>
```

### 1. Root Directory (`<problemname>/`)
- The archive MUST contain a single top-level directory named after the problem's task code / short name (e.g., `SUM`, `solve`, `socdist`).
- The problem code must be consistent with the reconstructed statement and Polygon package.

### 2. Test Subdirectories (`TEST[ID]/`)
- Formatted with the literal prefix `TEST` followed by the test index formatted as two digits `%02d` (e.g., `TEST01`, `TEST02`, ... `TESTNN`), or `%03d` if total tests exceed 99.
- Test numbering is strictly 1-indexed, contiguous, and preserves the sample-first ordering from the Polygon test suite.

### 3. Test Filenames & Extension Casing (`<problemname>.<ext>`)
- **Explicit File I/O in Statement**: If the problem statement specifies explicit file I/O (e.g., `SUM.INP`/`SUM.OUT` or `socdist.in`/`socdist.out`), the files in every `TEST[ID]` directory MUST strictly match that exact name and extension case.
- **Standard I/O in Statement**: If the problem statement specifies standard I/O (stdin / stdout), in Themis the test files standardize to `<problemname>.INP` and `<problemname>.OUT` (or `.inp`/`.out` matching the problem code's casing).

### 4. Byte-for-Byte Fidelity with Polygon Tests
- `TEST[ID]/<problemname>.<ext_inp>` must be byte-for-byte identical to Polygon `tests/[ID]`.
- `TEST[ID]/<problemname>.<ext_out>` must be byte-for-byte identical to Polygon `tests/[ID].a`.
- Original samples come first (`TEST01` through `TEST<N_samples>`).
- Subtask max-boundary tests terminate each subtask.
- Distributed killer tests are present and located at their corresponding test positions.

### 5. Strict Whitespace & Formatting Hygiene
- **Zero trailing whitespace**: absolutely no trailing space (` `) or tab (`\t`) on any line.
- **Zero redundant blank lines**: no empty blank lines unless mandated by problem statement specification.
- **Exact single EOF newline**: every file terminates with exactly one standard newline (`\n`).

## Offline Verification Checklist

The agent-generated `offline-package-verifier` validates the Themis package in Layer 11:
1. `zipfile` opens the Themis package cleanly without CRC error, directory traversal (`../`), or absolute paths.
2. Root directory `<problemname>/` exists.
3. Every test directory `TEST01` through `TESTNN` exists and contains exactly two files.
4. Input and output filenames match statement specification.
5. Content diff between Themis files and Polygon files reports 0 byte difference across all tests.
6. Byte-level whitespace scan passes with 0 violations.
