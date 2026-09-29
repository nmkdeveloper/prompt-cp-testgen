---
name: problem-analyzer
description: Reconstructs a competitive-programming problem from PDF, images, text and supporting files into a complete canonical problem.md without changing meaning, samples, constraints or requirements.
---
# Problem Analyzer

Inspect all statement sources, PDFs, images, diagrams and tables. Correct only extraction/OCR/formatting defects. Never rewrite semantics.

Create `problem.md` containing title, statement, definitions, input, output, constraints, samples, notes, subtasks/scoring if supplied, file I/O details and information conveyed by figures/tables.

Samples are immutable. Copy sample input/output exactly from the source. Never invent missing samples or outputs.

If a source is ambiguous, investigate other supplied materials before deciding. If ambiguity remains genuinely unrecoverable, report it for the orchestrator to handle with the FAIL policy.


## Execution constraints

Run this skill as part of a single-agent, strictly serial workflow. Do not spawn subagents and do not execute multiple OJ tasks concurrently. Any executable work must use the agent-generated, OS-adapted protected toolchain with 1 GiB RAM and 1 second limits. Prefer C++ for executable components.


## Statement-language policy

The canonical output package defaults to exactly two statement languages: `english` and `vietnamese`.

- Preserve supplied versions when present.
- If only one is supplied, derive a faithful translation for the missing default language from the canonical reconstructed statement.
- Do not alter any sample input/output, constraints, I/O semantics, scoring, filenames or mathematical definitions during translation.
- Record source-vs-generated language provenance in the internal report.


## Character & typography sanitization (FuraOJ safety)

To prevent upload errors and display crashes on Fura Online Judge:
- Strictly sanitize extracted text and translations against `DMOJ_PROBLEM_STATEMENT_DISALLOWED_CHARACTERS`:
  `{ '“', '”', '‘', '’', '−', 'ﬀ', 'ﬁ', 'ﬂ', 'ﬃ', 'ﬄ' }`
- Replace curly double quotes `“`, `”` with ASCII `"`.
- Replace curly single quotes `‘`, `’` with ASCII `'`.
- Replace Unicode minus `−` (U+2212) with ASCII `-` (U+002D).
- Expand typographic ligatures `ﬀ`, `ﬁ`, `ﬂ`, `ﬃ`, `ﬄ` to `ff`, `fi`, `fl`, `ffi`, `ffl`.
- Use `$ ... $` for inline math, `$$ ... $$` for display math, and escape literal dollar signs as `\$`.
- **Vietnamese Unicode Support (NFC & UTF-8)**:
  - Fully preserve all Vietnamese letters and diacritics (`à, á, ả, ã, ạ, ă, ằ, ắ, ẳ, ẵ, ặ, â, ầ, ấ, ẩ, ẫ, ậ, è, é, ẻ, ẽ, ẹ, ê, ề, ế, ể, ễ, ệ, ì, í, ỉ, ĩ, ị, ò, ó, ỏ, õ, ọ, ô, ồ, ố, ổ, ỗ, ộ, ơ, ờ, ớ, ở, ỡ, ợ, ù, ú, ủ, ũ, ụ, ư, ừ, ứ, ử, ữ, ự, ỳ, ý, ỷ, ỹ, ỵ, đ, Đ` and uppercase equivalents).
  - Save all files as **UTF-8 without BOM**.
  - Normalize text to **Unicode NFC** (`unicodedata.normalize('NFC', text)`) to avoid broken separated diacritics.
  - Never strip, remove, or modify Vietnamese characters during sanitization.


## Immutable statement/sample contract

Use the original PDF/images/files as authoritative source material. `problem.md` is normalized documentation, not permission to rewrite the problem. The generated `problem.tex` and each language's `problem-properties.json` must preserve the original statement semantics and exact original sample input/output.

For every section copied into `problem-properties.json`, keep the source content traceable. Do not replace `legend`/`input`/`output` with AI-authored paraphrases unless the package is intentionally generating a faithful missing-language translation; even then, do not alter samples, constraints or semantics.


## I/O contract — immutable

The original I/O mechanism is part of the problem specification. Never convert file I/O to stdin/stdout or vice versa. Preserve exact input/output filenames and case. Preserve `problem.xml` judging `input-file`/`output-file` values and `problem-properties.json` `inputFile`/`outputFile` values. If standard I/O is specified, do not invent filenames. If file I/O is specified, generated solution/brute/benchmark/protected execution must use the exact filenames. Any mismatch requires a source-level fix and regeneration.

## Bilingual tutorial — required

The successful default package contains both English and Vietnamese tutorials whenever tutorials are supported. Preserve supplied tutorial text in its source language and faithfully translate the missing default language. Keep problem.xml, tutorial files and problem-properties.json synchronized.
