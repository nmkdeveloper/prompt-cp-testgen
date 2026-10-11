---
trigger: always_on
description: "Always-on task tracking and dynamic todo list management for AI agent execution."
---
# AI Agent Todo List & Task Tracking

To maintain execution rigor and prevent goal drift across multi-phase competitive programming tasks:

- **Persistent Todo List**: At the start of every task, the agent must initialize and maintain a structured `todo.md` checklist at the project root (or within its active workspace context) following `docs/TODO_LIST_PROTOCOL.md`.
- **Atomic Checklist Format**: Tasks must use markdown checkbox syntax:
  - `- [ ]` Pending
  - `- [-]` In Progress (strictly ONE task in progress at any given moment)
  - `- [x]` Completed (verified with concrete evidence)
  - `- [!]` Blocked / Failed (requires automatic remediation loop)
- **Plan → Execute → Update Loop**:
  - Before starting any phase, mark it `- [-]`.
  - Execute the phase serially following all integrity and protected execution rules.
  - After verifying results, immediately mark it `- [x]` and update the log.
- **Dynamic Recovery Insertion**: When any step fails (e.g., differential check mismatch, compilation error, generator timeout, unkilled mutant), dynamically insert remediation subtasks directly under the failing phase instead of losing context.
- **Pre-Completion Audit**: Never declare completion or return a final report until every phase in `todo.md` has been successfully executed, verified, and checked off as `- [x]`.
