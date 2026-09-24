---
trigger: always_on
description: "Always-on serial execution policy; no subagents or concurrent OJ tasks."
---
# OJ Serial Execution

- The workflow is single-agent and serial.
- Do not spawn subagents.
- Do not run test-engineering tasks concurrently.
- Do not use background jobs, process pools, `xargs -P`, `parallel`, `Promise.all`, or equivalent task fan-out.
- Run generator, validator, brute, reference, wrong solutions and benchmarks one at a time.
- Prefer a single supervisory protected runner process without unnecessary worker threads.
