# Final FuraOJ / VNOJ Contract

The final target is a Fura Online Judge / VNOJ compatible Polygon Full Package, not merely a ZIP that looks plausible.
The authoritative importer is in Fura Online Judge (`D:\Workspaces\Github\furavietnam\furaoj`, strictly READONLY).

## Default Resource Limits & Scoring

Unless overridden by the reconstructed problem statement, standard package defaults are:
- **Memory Limit**: **1 GB RAM** (`<memory-limit>1073741824</memory-limit>` bytes, imported into FuraOJ as 1048576 KB = 1024 MB).
- **Time Limit**: **1s** (`<time-limit>1000</time-limit>` milliseconds, imported into FuraOJ as 1.0 second).
- **Points**: **1đ** (1 point: unbatched non-partial imports assign `last_case.points = 1`, giving 1đ total for the problem).

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

## Vietnamese Unicode Support

- Fully support Vietnamese Unicode across statements, problem names, notes, and tutorials.
- All files must be encoded in **UTF-8 without BOM**.
- All text must be normalized to **Unicode NFC (Form C)** to ensure diacritics are precomposed and render correctly.
- Preserve all Vietnamese letters and diacritics (`đ, Đ, ư, ơ, ê, ô, ă, â` and all accented vowels); sanitization against disallowed punctuation must never strip or alter Vietnamese letters.

## Importer compatibility

The offline verifier must model the Fura Online Judge importer (`judge/utils/codeforces_polygon.py`), including:
- `problem.xml`;
- `time-limit` (default 1000 ms = 1s);
- `memory-limit` (default 1073741824 bytes = 1 GB);
- `points` (default 1đ);
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
