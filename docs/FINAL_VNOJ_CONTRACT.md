# Final VNOJ Contract

The final target is a VNOJ-compatible Polygon Full Package, not merely a ZIP that looks plausible.

## Immutable I/O

The original I/O mode is sacred. Never convert:
- file I/O -> stdin/stdout;
- stdin/stdout -> file I/O.

Preserve exact explicit input/output filenames and relevant XML/properties values.

## Default languages

Use:
- `english`
- `vietnamese`

For tutorials, keep both languages whenever tutorials are supported.

## Importer compatibility

The offline verifier must model the supplied importer, including:
- `problem.xml`;
- `testset` `tests`;
- input/answer path patterns;
- Full Package test 1;
- checker type and source;
- statement nodes;
- `problem-properties.json`;
- required fields such as `legend`, `input`, `output`, `interaction`, `scoring`, `sampleTests`, `notes`, and `tutorial`;
- tutorial entries and language paths;
- image/resource paths;
- main solution source path when used.

## Final verdict

PASS only after structural, semantic, source-integrity, runtime and importer-compatibility checks succeed.
