---
trigger: always_on
description: "Mandates isolated work directory work/<problem-id>/ for all intermediate files, todo tracking, and final Polygon and Themis packages."
---
# Isolated Work Directory Hierarchy

For every problem processed by the agent:

- **Dedicated Directory**: Immediately create and operate inside `work/<problem-id>/` (where `<problem-id>` is the problem code/short name, e.g. `work/aplusb/`).
- **All Operations Contained**: All intermediate files, statement reconstructions (`problem.md`), task tracking (`todo.md`), C++ sources, compiled binaries, test candidate pools, logs, and reports (`report.md`) must be generated and kept inside `work/<problem-id>/`.
- **Packaging Staging**: Staging trees must be constructed inside `work/<problem-id>/`:
  - Polygon staging: `work/<problem-id>/polygon-package/`
  - Themis staging: `work/<problem-id>/themis-package/<problem-id>/`
- **Final Distribution Archives**: Both final test packages must be created directly in `work/<problem-id>/`:
  1. Polygon Full Package ZIP: `work/<problem-id>/<problem-id>-polygon.zip`
  2. Standard Themis Package ZIP: `work/<problem-id>/<problem-id>-themis.zip`
- **Root Cleanliness**: Never write problem-specific build artifacts, temporary tests, or package ZIPs directly to the workspace root.
