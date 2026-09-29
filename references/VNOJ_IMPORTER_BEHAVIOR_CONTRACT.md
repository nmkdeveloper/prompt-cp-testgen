# FuraOJ / VNOJ Importer Behavior Contract

This contract is derived from the Fura Online Judge importer at `D:\Workspaces\Github\furavietnam\furaoj\judge\utils\codeforces_polygon.py` and management command `judge/management/commands/import_polygon_package.py`.

**CRITICAL NOTICE — FURAOJ DIRECTORY IS READONLY**:
The codebase at `D:\Workspaces\Github\furavietnam\furaoj` is strictly **READONLY**. Do not write, modify, or create files within `D:\Workspaces\Github\furavietnam\furaoj`. It serves solely as an authoritative behavioral reference.

## Default Resource Limits & Scoring

When generating a Polygon package for Fura Online Judge, use these standard defaults unless the problem statement explicitly defines otherwise:

- **Time Limit**: Default **1s** (`1000` ms in `problem.xml`). FuraOJ parses this as:
  `self.meta['time_limit'] = float(testset.find('time-limit').text) / 1000` -> `1.0` second.
- **Memory Limit**: Default **1 GB RAM** (`1073741824` bytes in `problem.xml`). FuraOJ parses this as:
  `self.meta['memory_limit'] = int(testset.find('memory-limit').text) // 1024` -> `1048576` KB (1024 MB).
- **Points**: Default **1đ** (1 point).
  In FuraOJ's importer, if testcases have 0 points (or unbatched non-partial):
  `if not self.meta['partial'] and last_case is not None: last_case.points = 1`
  awarding exactly 1đ for solving the problem. If subtasks are used, subtask point values should sum to the problem's total points or default 1đ.

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

## Statement Character & Markdown Rendering Constraints (Crash Prevention)

In Fura Online Judge (`judge/models/problem.py`), problem name, description, translations, and editorial content are validated by `disallowed_characters_validator`:
- Prohibited characters: `DMOJ_PROBLEM_STATEMENT_DISALLOWED_CHARACTERS = {'“', '”', '‘', '’', '−', 'ﬀ', 'ﬁ', 'ﬂ', 'ﬃ', 'ﬄ'}`.
- If ANY of these characters exist in `name` or `description`, Django raises a `ValidationError`, which can break import or crash site views.
- **Normalization required**:
  - `“` and `”` -> `"`
  - `‘` and `’` -> `'`
  - `−` (U+2212) -> `-`
  - `ﬀ`, `ﬁ`, `ﬂ`, `ﬃ`, `ﬄ` -> `ff`, `fi`, `fl`, `ffi`, `ffl`
- **Math Formatting**:
  - Pandoc filter converts inline math to `$ ... $` and display math to `$$ ... $$`.
  - Escaped dollars: Currency or literal `$` in text must be escaped as `\$`.
  - LaTeX macros supported by FuraOJ's Lua filter: `\bf`, `\it`, `\tt`, `\t`, `\text`, `\textbf`, `\textit`.
- **Image Assets**:
  - Markdown `![image](<path>)` and `<img src="<path>">` are extracted and re-uploaded via Django storage. If the file `<path>` is missing from the ZIP, extraction fails and image rendering breaks.
- **Vietnamese Unicode Support (NFC & UTF-8)**:
  - Statements in Vietnamese (`vietnamese`) and Vietnamese problem names must be fully preserved with complete tone marks and diacritics (`đ, Đ, ư, ơ, ê, ô, ă, â` and all accented vowels).
  - All files must be saved in **UTF-8 without BOM**.
  - Text must be normalized to **Unicode NFC** (`unicodedata.normalize('NFC', text)`) to avoid detached diacritics (tổ hợp) that break Pandoc and web browsers.
  - The disallowed characters filter strictly targets typographic symbols and ligatures; it must NEVER alter or strip Vietnamese characters.

## Upload Conflict & Page Crash Prevention

- **Problem Code**: Must be lowercase alphanumeric `^[a-z0-9]+$`, length <= 20. If code exists in database without `--update`, importer aborts with `ImportPolygonError`.
- **Memory Limit Bounds**: FuraOJ enforces `DMOJ_PROBLEM_MAX_MEMORY_LIMIT = 1048576` KB (1 GB). The default `1073741824` bytes maps to `1048576` KB. Packages must not specify memory limits beyond this.
- **Time Limit Bounds**: FuraOJ validates `time_limit` within `[0.01, 60.0]` seconds. The default `1000` ms maps to `1.0` second.
- **Total Points Requirement**: In `judge/utils/problem_data.py`, `ProblemDataCompiler.generate` asserts `total_points > 0`. An empty score or non-positive total points raises `ProblemDataError('Total points must be greater than 0.')`, failing the import. Default score is 1đ.

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
