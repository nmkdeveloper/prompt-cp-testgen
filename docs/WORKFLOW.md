# Workflow

## Phase 0 — Input Discovery & Workspace Isolation

Inspect every supplied file and classify its role. Do not trust filenames alone. Immediately create the dedicated problem directory `work/<problem-id>/` (where `<problem-id>` is the problem code/short name, e.g. `work/aplusb/`) and initialize `work/<problem-id>/todo.md`. All subsequent work will be contained strictly inside `work/<problem-id>/`.

## Phase 1 — Problem Reconstruction

Read PDFs, scans, images, diagrams and text. Reconstruct a complete canonical statement at `work/<problem-id>/problem.md` without changing meaning. Samples and explicit source data are immutable.

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

## Phase 11 — Final Selection & Output Statistics

Select the optimal, reasonable number of final tests (dynamically calculated; total test count must always be a multiple of 10, e.g. 10, 20, 30, 40, 50, 60, 70, 80, 90, 100... except for specialized problem types). Preserve samples first, completely cover all subtasks and essential test types, satisfy subtask boundaries, maximize useful coverage, and include natural no-solution cases.
Perform statistical audit of output distributions across non-sample tests. If too many outputs are identical or fail to exhibit spectrum diversity (risking trivial O(1) guess solutions, excluding structural formats like boolean YES/NO), modify generator source code (`generator.cpp`) and regenerate tests from scratch until diversity is achieved.

## Phase 12 — Strict Formatting & Whitespace Audit

Audit every candidate and selected test file against strict formatting rules:
- Zero trailing spaces or tabs on any line.
- Zero redundant blank lines.
- Exactly one terminating newline (`\n`) at EOF.
- LaTeX math subscripts escaped (`$s\_1$`, `$a\_i$`).
- Verify no generated artifact was manually edited.

## Phase 13 — Dual Packaging (Polygon & Themis)

Build clean staging trees and final ZIP archives directly inside `work/<problem-id>/`:
- Configure problem scoring in `problem.xml` to match the points specified in the problem statement (e.g. 100, 70, 10) or default to 1đ (1 point) when unspecified.
- Polygon staging tree: `work/<problem-id>/polygon-package/`
- Themis staging tree: `work/<problem-id>/themis-package/<problem-id>/`
- Final Polygon Full Package ZIP: `work/<problem-id>/<problem-id>-polygon.zip` (for FuraOJ / Polygon).
- Final Standard Themis Package ZIP: `work/<problem-id>/<problem-id>-themis.zip` (hierarchy `<problemname>/TEST[ID]/<problemname>.<ext>` for Themis grading).

## Phase 14 — Offline Package Verification & Importer Check

Run `offline-package-verifier` against both packages in `work/<problem-id>/` and verify compatibility with `references/codeforces_polygon.py` (strictly READONLY). Check XML schema, ZIP integrity, testlib compilation, solutions, and subtask coverage.

## Phase 15 — Final Execution Report Generation

Generate comprehensive execution report at `work/<problem-id>/report.md` documenting subtask ladder, verification matrix, wrong-solution kill table, benchmark timings, and audit evidence.

## Task State Management (`todo.md`)

Throughout execution, the AI agent maintains a persistent checklist at `work/<problem-id>/todo.md` initialized from `templates/todo.md` following `docs/TODO_LIST_PROTOCOL.md`:
- **State transitions**: Mark the active phase `- [-]` before beginning, and `- [x]` immediately upon verifying its artifacts.
- **Single active task**: Exactly ONE task is `- [-]` at any given time.
- **Dynamic recovery**: If an invariant is violated (e.g. Phase 8 brute mismatch, Phase 9 unkilled mutant), mark the phase `- [!]` and insert remediation subtasks directly beneath it.
- **Completion requirement**: All 16 phases (Phase 0 through Phase 15) must be verified and checked off as `- [x]` before declaring final success.

## Failure Recovery

Never ask the user to continue. Diagnose, fix source, regenerate, verify and continue. If a problem remains unrecoverable after reasonable automatic recovery, record `FAIL`, skip it in batch mode and continue.


## Mandatory I/O contract stage

Before generating any executable code, create and freeze an internal `io_contract` extracted from the authoritative statement/package.

The contract must specify whether the problem uses standard I/O or file I/O and, when applicable, the exact input/output filenames.

Every generated executable must implement that contract. The protected runner may provide a platform-specific execution adapter, but must not rewrite the problem's I/O semantics.

Any mismatch triggers repair-and-regenerate, never manual testcase/output editing.
