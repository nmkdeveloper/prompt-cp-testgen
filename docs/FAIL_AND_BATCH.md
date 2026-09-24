# Failure, Recovery and Batch Policy

## Never stop early

Do not pause for user approval. Repair ordinary failures automatically and continue.

Recovery pattern:

```text
FAIL -> CLASSIFY -> DIAGNOSE -> FIX SOURCE -> REGENERATE -> REVALIDATE -> CONTINUE
```

Typical recoverable failures include compile errors, invalid generated inputs, brute/reference mismatch, weak wrong-solution coverage, weak stress cases, packaging mistakes and low answer diversity.

## FAIL condition

If abnormal behavior remains after all reasonable automated recovery strategies, write the literal word:

```text
FAIL
```

into the problem's final report. Explain the blocking condition, attempted recoveries and exact last known state. Do not fabricate a package.

## Batch mode

When multiple problems are present:

```text
problem A -> success -> package
problem B -> FAIL -> report -> SKIP
problem C -> continue
```

One failed problem must not stop the remaining problems.
