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

## Strict Whitespace & Formatting Hygiene

All generated test inputs and outputs (`.inp`, `.out`, `tests/01`..`tests/100`, `tests/01.a`..`tests/100.a`) must adhere strictly to the problem format with surgical precision:

1. **Zero Trailing Whitespace**:
   - Absolutely NO trailing spaces (` `) or tabs (`\t`) at the end of any line.
   - Every line must end cleanly immediately following the last character/token.
2. **Zero Redundant Newlines**:
   - Absolutely NO extraneous empty lines or blank lines (e.g. consecutive `\n\n`) within the file or at the end of the file, unless the problem statement explicitly mandates blank lines in its specification.
3. **Exact EOF Line Termination**:
   - Every file must terminate with exactly ONE newline (`\n`). There must be no missing trailing newline, and no multiple blank lines after the final data line.
4. **Clean Token Output in Generators & Solutions**:
   - In C++ generators, validators, and solutions, loops must separate items with spaces and terminate the line with a newline without leaving a dangling trailing space (e.g., `for (int i = 0; i < n; ++i) cout << a[i] << (i + 1 == n ? '\n' : ' ');`).

## Failure

Any unresolved I/O mismatch or formatting violation is a correctness failure. Fix the source implementation/configuration and regenerate all affected artifacts. Never patch generated `.in`/`.out` files or samples.
