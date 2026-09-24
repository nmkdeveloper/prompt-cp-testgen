# Workflow

## Phase 0 — Input Discovery

Inspect every supplied file and classify its role. Do not trust filenames alone.

## Phase 1 — Problem Reconstruction

Read PDFs, scans, images, diagrams and text. Reconstruct a complete `problem.md` without changing meaning. Samples and explicit source data are immutable.

## Phase 2 — Host/Toolchain Detection

Detect OS, architecture, compiler and testlib availability. Decide which native process/resource backend is required.

## Phase 3 — Agent-Generated Runtime Toolchain

Write the required C++ sources for the actual environment and problem. This includes a protected execution runner and any generators/validators/checkers/brute/reference/benchmark tools that are needed.

All untrusted executables must run serially under the 1 GiB / 1 second protected limits.

## Phase 4 — Reference Verification

Prefer supplied AC/official/reference code, but verify it against brute on a safe domain plus adversarial/boundary tests. Only then promote it to `VERIFIED_REFERENCE`.

## Phase 5 — Solution/Weakness Analysis

Identify intended complexity, intermediate capability classes and likely wrong-solution patterns.

## Phase 6 — Dynamic Subtasks

Create a problem-specific number of meaningful subtasks. Prefer nested ladders when possible. Structural/special-property subtasks are allowed and often preferable to arbitrary limit changes.

## Phase 7 — Candidate Generation

Generate a large candidate pool using reproducible C++ testlib generators where applicable. Validate every candidate.

## Phase 8 — Oracle Verification

For brute-eligible candidates: validator → brute → verified reference → compare. Resolve every conflict.

## Phase 9 — Wrong-Solution Attack

Run provided wrong solutions and meaningful mutants serially. Generate targeted counterexamples for survivors.

## Phase 10 — Benchmark

Run benchmark inputs serially under the protected 1 second / 1 GiB policy and identify performance-sensitive structures.

## Phase 11 — Final Selection

Select exactly 100 final tests. Preserve samples first, satisfy subtask boundaries, maximize useful coverage, minimize answer redundancy, and include natural no-solution cases.

## Phase 12 — Final Audit

Re-run required checks. Verify no generated artifact was manually edited.

## Phase 13 — Packaging

Build a clean Polygon staging tree and package only files required by Polygon.

## Failure Recovery

Never ask the user to continue. Diagnose, fix source, regenerate, verify and continue. If a problem remains unrecoverable after reasonable automatic recovery, record `FAIL`, skip it in batch mode and continue.


## Mandatory I/O contract stage

Before generating any executable code, create and freeze an internal `io_contract` extracted from the authoritative statement/package.

The contract must specify whether the problem uses standard I/O or file I/O and, when applicable, the exact input/output filenames.

Every generated executable must implement that contract. The protected runner may provide a platform-specific execution adapter, but must not rewrite the problem's I/O semantics.

Any mismatch triggers repair-and-regenerate, never manual testcase/output editing.
