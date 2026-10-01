# Architecture

The bundle is specification-first. It provides skills, rules, schemas and documentation, not a generic runtime executable.

```text
Input Package
    ↓
Input Discovery
    ↓
problem.md
    ↓
Host/Toolchain Detection
    ↓
Agent-Generated Native C++ Toolchain
    ├── protected_runner.cpp
    ├── generator_*.cpp
    ├── validator.cpp
    ├── brute.cpp
    ├── reference.cpp (only if needed/new)
    ├── checker.cpp
    └── benchmark.cpp
    ↓
Serial Verification
    ↓
Candidate Pool
    ↓
Wrong-Solution Attack
    ↓
Optimal Final Tests
    ↓
Audit
    ↓
Polygon ZIP
```

The agent must not spawn subagents or run concurrent tasks.

All untrusted binaries execute through the generated protected runner.
