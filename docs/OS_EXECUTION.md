# Cross-Platform Protected Execution

## Fixed policy

Every untrusted executable used in the OJ test-engineering workflow must be launched through an agent-generated native protected runner with:

- 1024 MiB memory limit
- 1000 ms wall-clock limit
- 1000 ms CPU-time limit where the OS exposes a reliable mechanism
- process-tree cleanup on termination

When a limit is crossed, classify the run as `LIMIT_EXCEEDED`, terminate the complete process tree, wait for cleanup, and write the event to the incremental log.

## Agent-generated, OS-specific implementation

Do not ship or assume one generic implementation. First detect the host and then generate the native implementation.

### Windows

Prefer Win32 Job Objects for grouping processes, resource limits/accounting and group termination. Microsoft documents Job Objects as a mechanism to manage associated processes as a unit, enforce limits and terminate the associated processes. The generated C++ runner should use appropriate Job Object limits and native process waiting/timeout logic.

Recommended building blocks:

- CreateProcess
- CreateJobObject
- AssignProcessToJobObject
- SetInformationJobObject
- QueryInformationJobObject
- TerminateJobObject

### Linux

Prefer POSIX/Linux process controls and resource limits. Use the mechanisms actually available on the host, such as `setrlimit`/`prlimit`, process groups and native process-memory observation. Linux documents `RLIMIT_CPU` and `RLIMIT_AS` resource limits. Use a monotonic wall-clock watchdog in addition to CPU limits.

### macOS

Use the Darwin/POSIX APIs available in the detected SDK. Use process groups and resource controls where applicable, plus native resource observation for memory and a monotonic wall-time guard. Do not assume `/proc` exists.

### FreeBSD

Use FreeBSD/POSIX process controls and available resource-accounting facilities. Use process groups for cleanup and native resource observation where a direct hard limit is unavailable in the current environment. Do not assume Linux-specific interfaces.

### Other operating systems

Implement an appropriate native backend when reliable enforcement is possible. Do not silently fall back to unrestricted execution. If reliable 1 GiB/1 second enforcement cannot be established after reasonable recovery, mark the problem FAIL.

## Runner behavior

The generated runner should:

1. Launch exactly one protected child at a time.
2. Apply limits before or immediately at process start according to the OS mechanism.
3. Monitor wall time using a monotonic clock.
4. Monitor relevant memory usage using native facilities.
5. Kill the complete process tree on timeout/resource violation.
6. Wait for confirmed cleanup.
7. Return a machine-readable execution status.
8. Append a structured event to the log.

Avoid unnecessary watchdog threads; a single supervisory flow is preferred.

## Benchmarking

Benchmark executions use the same protected limits. A reference program that reaches the 1 second or 1 GiB threshold is classified and logged; it must not be allowed to continue beyond the guard.

## Integrity

The protected runner is internal generated tooling. It is not automatically placed into the final Polygon package.
