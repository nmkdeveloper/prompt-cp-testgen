# Workflow

## Phase 0 — Input Discovery

Inspect every supplied file and classify its role. Do not trust filenames alone.

## Phase 1 — Problem Reconstruction

Read PDFs, scans, images, diagrams and text. Reconstruct a complete `problem.md` without changing meaning. Samples and explicit source data are immutable.

## Phase 2 — Host/Toolchain Preflight & Portable Fallback

Immediately after confirming problem statement files exist:
1. Check availability of `g++` and `python` in system PATH (`where.exe` / `which`).
2. If missing, automatically download trusted portable standalone builds (WinLibs MinGW-w64 standalone archive, official Python embeddable zip), extract locally, and configure environment paths to use them.
3. Detect OS, architecture, compiler capabilities, and testlib availability. Decide which native process/resource backend is required.

## Phase 3 — Agent-Generated Runtime Toolchain

Write the required C++ sources for the actual environment and problem. This includes a protected execution runner and any generators/validators/checkers/brute/reference/benchmark tools that are needed.

- **Protected limits & auto-break**: All untrusted executables run serially under 1 GiB RAM with hard time limits (solutions/mutants: strict 1000 ms; generators/tooling: calibrated hard limit derived from a host FLOPS benchmark); an active auto-break watchdog terminates runaway execution (infinite loops, deep recursion) and kills the entire process tree.
- **Token economy**: Generated code must be dense and compact (multiple statements per line where practical) with short, concise variable/function names to conserve token budget.
- **Selective English comments**: Comment only on functions that genuinely require explanation; state strictly logic, inputs, and return value; write comments exclusively in English.

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

Select the optimal, reasonable number of final tests (dynamically calculated; no rigid 100-test requirement). Preserve samples first, completely cover all subtasks and essential test types, satisfy subtask boundaries, maximize useful coverage, minimize answer redundancy, and include natural no-solution cases.

## Phase 12 — Final Audit

Re-run required checks. Verify no generated artifact was manually edited.

## Phase 13 — Dual Packaging (Polygon & Themis)

Build clean staging trees for both targets:
1. **Polygon Full Package ZIP**: `<problemname>-polygon.zip` (for FuraOJ / VNOJ / Polygon).
2. **Standard Themis Package ZIP**: `<problemname>-themis.zip` (hierarchy `<problemname>/TEST[ID]/<problemname>.<ext>` for Themis grading).
Verify both packages using `offline-package-verifier`.

## Failure Recovery

Never ask the user to continue. Diagnose, fix source, regenerate, verify and continue. If a problem remains unrecoverable after reasonable automatic recovery, record `FAIL`, skip it in batch mode and continue.


## Mandatory I/O contract stage

Before generating any executable code, create and freeze an internal `io_contract` extracted from the authoritative statement/package.

The contract must specify whether the problem uses standard I/O or file I/O and, when applicable, the exact input/output filenames.

Every generated executable must implement that contract. The protected runner may provide a platform-specific execution adapter, but must not rewrite the problem's I/O semantics.

Any mismatch triggers repair-and-regenerate, never manual testcase/output editing.
