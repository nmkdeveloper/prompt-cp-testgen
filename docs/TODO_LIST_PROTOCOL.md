# AI Agent Todo List Protocol

This document defines the standard protocol for AI agent task tracking, state management, and execution monitoring within this workspace.

## 1. Core Principle — Externalized State & Anti-Drift

Complex competitive programming test engineering consists of 15+ interdependent phases (discovery, statement reconstruction, compiler preflight, runner generation, reference verification, brute differential testing, subtask ladder design, candidate generation, wrong-solution killer attacks, benchmarking, test selection, format auditing, dual packaging, and offline package verification).

To prevent goal drift, lost context, skipped verification phases, or premature completion:
- The AI agent must maintain a persistent, structured **`todo.md`** file at the workspace root (or in its active execution context).
- The todo list serves as the single source of truth for the agent's real-time execution state.
- The agent must read, update, and persist this checklist incrementally as work progresses.

## 2. Task States & Syntax

The todo list strictly uses GitHub-flavored markdown checklist syntax with standard state markers:

| Marker | State | Description |
|---|---|---|
| `- [ ]` | **Pending** | Task is queued and waiting to be started. |
| `- [-]` or `- [/]` | **In Progress** | Task is actively being executed right now. **Strict constraint**: Only ONE task may be in progress at any time. |
| `- [x]` | **Completed** | Task completed successfully and its output/invariants were verified. |
| `- [!]` | **Failed / Blocked** | Task failed or hit an anomaly. Automatically triggers a recovery loop. |

## 3. Standard OJ Execution Task Template

When starting a competitive programming test generation task, the AI agent initializes `todo.md` with the following canonical phases:

```markdown
# Problem Execution Todo List: <problemname>

- [ ] Phase 0: Input Discovery & Classification
- [ ] Phase 1: Problem Statement Reconstruction (`problem.md`)
- [ ] Phase 2: Toolchain Preflight & Portable Fallback (`g++`, `python`)
- [ ] Phase 3: Native Protected Runner Generation (1000ms / 1GB RAM / Process-Tree Watchdog)
- [ ] Phase 4: Reference Verification & Safe Brute Force Oracle Domain
- [ ] Phase 5: Solution Analysis & Algorithmic Capability Boundaries
- [ ] Phase 6: Dynamic Subtask Design & Nested Ladders
- [ ] Phase 7: Candidate Test Generation & Validation Pool
- [ ] Phase 8: Oracle Differential Verification (Brute vs Reference)
- [ ] Phase 9: Wrong Solution Analysis & Distributed Killer Attacks
- [ ] Phase 10: Benchmark & Performance Sensitivity Profiling
- [ ] Phase 11: Dynamic Optimal Test Selection (Samples First, End-Boundary Tests)
- [ ] Phase 12: Strict Formatting & Whitespace Audit (Zero trailing spaces, LaTeX `$s\_1$` escaping)
- [ ] Phase 13: Dual Packaging (Polygon Full Package ZIP & Standard Themis ZIP)
- [ ] Phase 14: Offline Package Verification & Importer Synchronization Check
- [ ] Phase 15: Final Execution Report Generation (`report.md`)
```

## 4. Execution Loop: Plan → Execute → Update

For each item in `todo.md`:
1. **Transition to In Progress**:
   Change `- [ ] Task Name` to `- [-] Task Name`.
   Record the start of the task in the execution log.
2. **Execute Serially**:
   Perform the task following all workspace rules (serial execution, protected runner, immutable samples/statements).
3. **Verify Outcome**:
   Verify that generated artifacts, test outputs, or compilation results meet all invariants before declaring the task done.
4. **Transition to Completed**:
   Change `- [-] Task Name` to `- [x] Task Name`.
   Briefly note key findings (e.g. `[x] Phase 4: Reference Verified (100% agreement with brute on N=20 domain)`).

## 5. Dynamic Error Recovery & Subtask Insertion

When a task fails or an anomaly is encountered:
1. Mark the failing task as `- [!] Task Name: Failed - <reason>`.
2. **Dynamically insert remediation subtasks** directly under the failing item:
   ```markdown
   - [!] Phase 8: Oracle Differential Verification
     - [ ] Diagnose mismatch on small test seed #42
     - [ ] Repair reference source logic
     - [ ] Re-run brute differential verification
   ```
3. Execute and complete the remediation subtasks sequentially.
4. Once all recovery subtasks pass, mark the parent phase as `- [x] Completed (Recovered)`.

## 6. Pre-Completion Audit

Before declaring final success:
- The agent must verify that **every** task in `todo.md` is checked off as `- [x]`.
- Zero `- [ ]`, zero `- [-]`, and zero unresolved `- [!]` items may remain.
- If any item is unresolved, the agent must continue execution or, if unrecoverable, record `FAIL` in `report.md`.
