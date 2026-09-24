# Reference snapshot: user-supplied VNOJ/DMOJ Polygon importer behavior.
# This file is intentionally reference-only; it is not standalone because the real importer
# depends on the OJ/Django codebase. The canonical behavior is taken from the user-provided source.
#
# Critical observed access patterns:
#   self.package = zipfile.ZipFile(package, 'r')
#   if 'problem.xml' not in self.package.namelist(): raise ImportPolygonError(...)
#   self.root = ET.fromstring(self.package.read('problem.xml'))
#   testset = self.root.find('.//testset[@name="tests"]')
#   input_path = testset.find('input-path-pattern').text % 1
#   answer_path = testset.find('answer-path-pattern').text % (i + 1)
#   checker = self.root.find('.//checker')
#   checker.get('type') == 'testlib'
#   statements = self.root.findall('.//statement[@type="application/x-tex"]')
#   problem_properties_path = os.path.join(statement_folder, 'problem-properties.json')
#   problem_properties = json.loads(self.package.read(problem_properties_path).decode('utf-8'))
#   description += pandoc_tex_to_markdown(problem_properties['legend'])
#   description += pandoc_tex_to_markdown(problem_properties['input'])
#   description += pandoc_tex_to_markdown(problem_properties['output'])
#   if problem_properties['interaction'] is not None: ...
#   if problem_properties['scoring'] is not None: ...
#   for i, sample in enumerate(problem_properties['sampleTests'], start=1): ...
#   if problem_properties['notes'] != '': ...
#   tutorial = problem_properties['tutorial']
#   solutions = self.root.find('.//solutions')
#   main_solution = solutions.find('solution[@tag="main"]')
#   source = main_solution.find('source')
#   source_code = self.package.read(source.get('path')).decode('utf-8').strip()
#
# The actual full source supplied by the user is preserved semantically in the rules and
# behavior contract shipped alongside this file. When developing inside the OJ repository,
# prefer the repository's live source over this snapshot.

from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Iterable

REQUIRED_PROBLEM_PROPERTIES_KEYS = (
    'legend', 'input', 'output', 'interaction', 'scoring',
    'sampleTests', 'notes', 'tutorial',
)

@dataclass(frozen=True)
class ImporterContract: 
    statement_mime: str = 'application/x-tex'
    checker_type: str = 'testlib'
    main_solution_tag: str = 'main'
    required_problem_properties_keys: tuple[str, ...] = REQUIRED_PROBLEM_PROPERTIES_KEYS

def statement_properties_path(statement_path: str) -> str:
    p = PurePosixPath(statement_path)
    return str(p.parent / 'problem-properties.json')

def importer_required_problem_properties_keys() -> tuple[str, ...]:
    return REQUIRED_PROBLEM_PROPERTIES_KEYS
