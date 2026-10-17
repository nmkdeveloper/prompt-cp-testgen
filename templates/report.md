# OJ Test Engineering Report

## Final status

**STATUS: {{STATUS}}**

## Problem

- Problem: {{PROBLEM}}
- Input source: {{INPUT_SOURCE}}
- Reconstructed statement: `problem.md`
- Samples: {{SAMPLE_COUNT}}
- Subtasks: {{SUBTASK_COUNT}}
- Final tests: {{FINAL_TEST_COUNT}} (multiple of 10: {{MULTIPLE_OF_10_CONFIRMED}})
- Problem score: {{PROBLEM_SCORE}} (statement points or 1đ default)
- Candidate tests generated: {{CANDIDATE_COUNT}}
- Brute-verified candidates: {{BRUTE_VERIFIED_COUNT}}

## Reference

| Candidate | Type | Verified | Brute scope | Adversarial | Benchmark |
|---|---|---|---:|---|---|
| {{REFERENCE_SOURCE}} | {{REFERENCE_TYPE}} | {{REFERENCE_STATUS}} | {{BRUTE_SCOPE}} | {{ADVERSARIAL_STATUS}} | {{BENCHMARK_STATUS}} |

## Subtasks

| ID | Restriction | Test range | Max-boundary tests | Expected capability | Status |
|---|---|---:|---:|---|---|
| {{SUBTASK_ROWS}} |

## Wrong solutions / mutants

| ID | Type | Passed | Failed | Surviving subtasks | Killer tests | Status |
|---|---|---:|---:|---|---|---|
| {{WRONG_ROWS}} |

## Answer distribution & Output statistics

- Unique answers: {{UNIQUE_ANSWERS}}
- Duplicate-answer tests: {{DUPLICATE_ANSWER_TESTS}}
- Zero/no-solution cases: {{ZERO_CASES}}
- Output distribution statistics: {{OUTPUT_DISTRIBUTION_AUDIT}}
- Generator regeneration loop triggered: {{GENERATOR_REGENERATION_TRIGGERED}}
- Distribution notes: {{ANSWER_DISTRIBUTION}}

## Verification

- Test count multiple of 10: {{MULTIPLE_OF_10_STATUS}}
- Output statistics & anti-O(1) diversity: {{OUTPUT_DIVERSITY_STATUS}}
- Problem score matches statement/default: {{PROBLEM_SCORE_STATUS}}
- Validator: {{VALIDATOR_STATUS}}
- Reference on all final tests: {{REFERENCE_FINAL_STATUS}}
- Brute/reference differential: {{BRUTE_FINAL_STATUS}}
- Wrong-solution audit: {{WRONG_STATUS}}
- Benchmark: {{BENCHMARK_STATUS}}
- Manual testcase editing detected: {{MANUAL_EDIT_STATUS}}
- Strict I/O whitespace compliance: {{IO_WHITESPACE_STATUS}}
- LaTeX subscript escaping ($s\_1$): {{LATEX_SUBSCRIPT_STATUS}}
- TeX/Markdown/Characters sanitization: {{STATEMENT_SANITIZATION_STATUS}}
- Vietnamese Unicode (NFC/UTF-8): {{VIETNAMESE_UNICODE_STATUS}}

## Packaging (Dual Packaging)

- Polygon staging: `{{PACKAGE_DIR}}`
- Polygon ZIP: `{{POLYGON_ZIP_PATH}}`
- Themis staging: `{{THEMIS_PACKAGE_DIR}}`
- Themis ZIP: `{{THEMIS_ZIP_PATH}}`
- Polygon package audit: {{POLYGON_PACKAGE_STATUS}}
- Themis package audit: {{THEMIS_PACKAGE_STATUS}}

## Recovery / anomalies

{{RECOVERY_LOG}}

## Notes

{{NOTES}}


## I/O Contract

| Field | Value |
|---|---|
| I/O method | standard / file |
| Input filename | exact source value or N/A |
| Output filename | exact source value or N/A |
| `judging@input-file` preserved | PASS/FAIL |
| `judging@output-file` preserved | PASS/FAIL |
| `problem-properties.json` I/O preserved | PASS/FAIL |
| Generated solution/brute/benchmark I/O matches | PASS/FAIL |

## Tutorial Languages

| Language | Statement | Tutorial | `problem-properties.json` tutorial | XML tutorial entry |
|---|---|---|---|---|
| English | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL |
| Vietnamese | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL |
