# VNOJ Importer Behavior Contract

This contract is derived from the user-supplied `codeforces_polygon.py` importer. It is a behavioral compatibility reference, not a generic Polygon specification.

## Hard package assumptions observed in the importer

- `problem.xml` must exist.
- A `<testset name="tests">` must exist.
- `<tests>` must contain at least one test.
- `input-path-pattern` must resolve test 1 to an existing ZIP member; the importer uses this as the Full Package check.
- `answer-path-pattern` must resolve each test answer to an existing ZIP member.
- Statement nodes are expected as `<statement type="application/x-tex" ...>`.
- For every statement path, `<statement-folder>/problem-properties.json` must exist.
- `legend`, `input`, `output`, `interaction`, `scoring`, `sampleTests`, `notes`, and `tutorial` are directly accessed by the importer.
- Custom checkers must be C++ testlib checkers.
- Interactive interactor sources must be C++.
- The importer reads solution source paths for `<solution tag="main">` when configured to append the main solution to the tutorial.
- The importer maps Polygon time limit from milliseconds to DMOJ seconds and memory from bytes to kilobytes.

## Consequence for package generation

A package that is syntactically a ZIP and resembles a Polygon package is not enough. The final package must survive the actual importer access patterns.

The agent must create an offline preflight verifier that models these accesses and fails before upload if the package would hit an uncaught `KeyError`, missing path, missing checker, invalid testset or similar importer failure.


## I/O preservation rule

The importer reads the `judging` input-file/output-file attributes and only configures file I/O when both are non-empty. The package generator must preserve the source values exactly rather than forcing a local stdin/stdout convention. Separately preserve `problem-properties.json` inputFile/outputFile metadata.

## Bilingual tutorial rule

The target package may contain tutorials for multiple statement languages. Keep both default language tutorial artifacts in the package even though this importer selects one main tutorial language when importing into the site.


## Exact I/O behavior

The supplied importer inspects `judging` file attributes and only activates file I/O when both `input-file` and `output-file` are non-empty. Do not use this importer behavior as permission to rewrite the source problem: preserve the original contract first, then ensure the generated package and executables are consistent with it.

## Tutorial retention

The importer may select one tutorial for the destination site's single tutorial field. The package itself should retain both English and Vietnamese tutorials when the target profile is bilingual.
