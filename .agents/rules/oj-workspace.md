---
trigger: always_on
description: "Mandates isolated work directory work/<problem-id>/ for all intermediate files, todo tracking, and final Polygon and Themis packages."
---
# Isolated Work Directory Hierarchy

For every problem processed by the agent:

- **Dedicated Directory**: Immediately create and operate inside `work/<problem-id>/` (where `<problem-id>` is the problem code/short name, e.g. `work/aplusb/`).
- **All Sources & Binaries Contained**: ALL source files (`.cpp`, `.py`, `.h`, `.sh`, `.bat`), compiled executables/binaries (`.exe`, ELF binaries, `.o`), and runtime tooling generated for the problem MUST be created, compiled, and executed strictly inside `work/<problem-id>/`.
- **All Operations Contained**: All intermediate files, statement reconstructions (`problem.md`), task tracking (`todo.md`), test candidate pools, logs, and reports (`report.md`) must be generated and kept inside `work/<problem-id>/`.
- **Packaging Staging**: Staging trees must be constructed inside `work/<problem-id>/`:
  - Polygon staging: `work/<problem-id>/polygon-package/`
  - Themis staging: `work/<problem-id>/themis-package/<problem-id>/`
- **Final Distribution Archives**: Both final test packages must be created directly in `work/<problem-id>/`:
  1. Polygon Full Package ZIP: `work/<problem-id>/<problem-id>-polygon.zip`
  2. Standard Themis Package ZIP: `work/<problem-id>/<problem-id>-themis.zip`
- **Root Cleanliness**: Never write, compile, or leave problem-specific sources (`.cpp`, `.py`), compiled binaries, temporary tests, or package ZIPs directly in the workspace root.
