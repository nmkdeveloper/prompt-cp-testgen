# Immutable Input/Output Contract

The I/O mechanism is part of the problem specification, not a formatting preference.

## Required behavior

1. Read the original statement and supplied Polygon package.
2. Determine whether the task uses standard streams or explicit files.
3. Record the exact mode and filenames in the internal problem model.
4. Use that exact mode for every generated executable.
5. Preserve the same mode in the final Polygon/VNOJ package.

### Standard I/O

If the source specifies standard input/output and the relevant package fields are empty:
- use stdin/stdout;
- do not add `input-file` or `output-file`;
- do not invent filenames.

### File I/O

If the source specifies file I/O:
- preserve exact input filename;
- preserve exact output filename;
- preserve case;
- use those names for solution/brute/benchmark/protected execution;
- validate that statement, XML, properties and runtime agree.

The local protected runner may stage files internally, but that is an execution implementation detail and MUST NOT change the problem contract.

### Consistency checks

Compare, when present:
- statement's explicit I/O description;
- `problem.xml` `<judging input-file="..." output-file="...">`;
- `problem-properties.json` `inputFile` and `outputFile`;
- supplied solution code behavior;
- generated solution/brute/benchmark code behavior.

If sources disagree, investigate. Do not normalize away the discrepancy.

## Failure

Any unresolved I/O mismatch is a correctness failure. Fix the source implementation/configuration and regenerate all affected artifacts. Never patch generated `.in`/`.out` files or samples.
