---
name: polygon-importer-tester
description: Generates an offline standalone Python importer test script based on the exact structure of references/codeforces_polygon.py (strictly READONLY) to test and verify package synchronization and executable import compatibility without requiring a live Django database.
---
# Polygon Importer Tester

This skill provides the methodology to generate and run an offline, standalone Python verification script that mirrors the exact structure, parsing pipeline, and validation rules of `references/codeforces_polygon.py` (which is strictly **READONLY**). It validates that a staged or generated Polygon Full Package ZIP (`work/<problem-id>/<problem-id>-polygon.zip`) can synchronize and import seamlessly into Fura Online Judge without runtime errors, schema crashes, or data truncation.

## Authoritative reference & strictly READONLY rule

The importer reference source code resides at:
- `references/codeforces_polygon.py`

**CRITICAL NOTICE**:
The reference `references/codeforces_polygon.py` is strictly **READONLY**. Never modify, delete, or overwrite `references/codeforces_polygon.py`. The agent must generate a standalone test script (e.g. `sync_test_importer.py`) based on its structural and behavioral logic to test package synchronization.

## Purpose & Execution Model

In production, `codeforces_polygon.py` relies on the full Django runtime, database models (`Problem`, `ProblemTestCase`, `ProblemData`, `ProblemTranslation`, `Solution`, `SolutionTranslation`, `django_uploader`, `martor`), and settings.

During offline test generation and package verification:
1. Live Django database and authentication services are absent.
2. The agent generates a standalone Python test harness script (`sync_test_importer.py`) that encapsulates:
   - The exact class hierarchy (`ImportPolygonError`, `PolygonImporter`).
   - All validation checks from `PolygonImporter.validate()`.
   - Asset parsing (`parse_assets()`), interactor / custom testlib checker checks (`lang='CPP20'`, `type='testlib'`), and percentage points flag.
   - Testcase & batch parsing (`parse_tests()`), time/memory limits, `complete-group` vs `each-test` policy, dependency validation, fractional points normalization via GCD, total points calculation (`partial` flag), and File I/O extraction.
   - Statement parsing (`parse_statements()`), `problem-properties.json` key validation, Pandoc markdown conversion (Pandoc >= 3.0.0), image reference integrity, multilingual statements, and multilingual tutorials (`default_lang_map = {'vietnamese': 'vi', 'english': 'en', 'russian': 'ru'}`).
   - Solution parsing (`parse_solutions()`), spoiler code block generation, and appending to all tutorial translations.
   - Simulated model creation and `ProblemDataCompiler.generate` assertion (`total_points > 0`, non-empty tests, empty feedback).
3. The generated test script is executed serially under protected runner limits against the generated Polygon package ZIP.

## Structure of the Generated Test Script

The generated script must mirror the exact logic of `references/codeforces_polygon.py`:

```python
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import tempfile
import zipfile
from operator import itemgetter
from typing import BinaryIO, List, Union

class ImportPolygonError(Exception):
    pass

# Mock Django settings and models to allow offline execution
class MockSettings:
    LANGUAGES = [('vi', 'Vietnamese'), ('en', 'English'), ('ru', 'Russian')]
    DMOJ_PROBLEM_MIN_MEMORY_LIMIT = 0
    DMOJ_PROBLEM_MAX_MEMORY_LIMIT = 1048576
    MARTOR_UPLOAD_MEDIA_DIR = 'martor'

# Standalone Pandoc conversion helper mirroring codeforces_polygon.py
def pandoc_get_version():
    res = subprocess.run(['pandoc', '--version'], stdout=subprocess.PIPE, text=True, check=True)
    first_line = res.stdout.splitlines()[0]
    m = re.search(r'(\d+)\.(\d+)(?:\.(\d+))?', first_line)
    return tuple(map(int, [g for g in m.groups() if g is not None]))

def pandoc_tex_to_markdown(tex):
    # Converts TeX fragment to Markdown using pandoc
    cmd = ['pandoc', '-f', 'latex', '-t', 'gfm']
    proc = subprocess.run(cmd, input=tex, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return proc.stdout

class StandalonePolygonImporter:
    def __init__(self, package_path, code, interactive=False, config=None):
        self.code = code
        self.package_path = package_path
        self.interactive = interactive
        self.config = config or {
            'main_statement_language': 'vietnamese',
            'main_tutorial_language': 'vietnamese',
            'append_main_solution_to_tutorial': True,
        }
        self.package = zipfile.ZipFile(package_path, 'r')
        if 'problem.xml' not in self.package.namelist():
            raise ImportPolygonError('problem.xml not found')
        import xml.etree.ElementTree as ET
        self.root = ET.fromstring(self.package.read('problem.xml'))
        self.meta = {'code': code}
        self.validate()

    def validate(self):
        # Mirrored from codeforces_polygon.py validate()
        testset = self.root.find('.//testset[@name="tests"]')
        if testset is None:
            raise ImportPolygonError('testset tests not found')
        tests_elem = testset.find('tests')
        if tests_elem is None or len(list(tests_elem)) == 0:
            raise ImportPolygonError('no testcases found')
        input_pattern = testset.find('input-path-pattern').text
        if (input_pattern % 1) not in self.package.namelist():
            raise ImportPolygonError('not full package')

    def run(self):
        self.meta['image_cache'] = {}
        self.meta['tmp_dir'] = tempfile.TemporaryDirectory()
        try:
            self.parse_assets()
            self.parse_tests()
            self.parse_statements()
            self.parse_solutions()
            self.verify_problem_data()
        finally:
            self.meta['tmp_dir'].cleanup()
            self.package.close()

    # Replicate parse_assets, parse_tests, parse_statements, parse_solutions, verify_problem_data
```

## Step-by-Step Workflow

1. **Preflight**:
   - Confirm `references/codeforces_polygon.py` exists and is untouched (read-only).
   - Ensure the generated Polygon ZIP archive exists in the problem work directory: `work/<problem-id>/<problem-id>-polygon.zip`.
2. **Generate Test Script**:
   - Write `sync_test_importer.py` in `work/<problem-id>/` or scratch directory.
   - Include dense, compact Python code with English comments on core functions.
3. **Execute Test Script**:
   - Run: `python work/<problem-id>/sync_test_importer.py work/<problem-id>/<problem-id>-polygon.zip <problem_code>`
   - Capture stdout and returncode.
4. **Evaluate Results**:
   - If the script runs to completion and logs success, the package is verified to be 100% synchronized and compatible with `codeforces_polygon.py`.
   - If any `ImportPolygonError`, `KeyError`, or validation error occurs, diagnose the root cause, fix the package generator, regenerate the Polygon ZIP, and rerun until clean PASS.
5. **Cleanup**:
   - Delete temporary test scripts if not needed for reporting.
   - Record test outcomes in the final report.
