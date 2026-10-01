# Run Contract

The main orchestrator is responsible for creating a problem work directory and writing logs continuously.

Minimum artifacts:

```text
problem.md
manifest.yaml
analysis/
generators/
validators/
checkers/
brute/
reference/
wrong-solutions/
benchmark/
candidate-tests/
final-tests/
logs/
report.md
polygon-package/
themis-package/
<problemname>-polygon.zip
<problemname>-themis.zip
```

A final successful problem requires a dynamically calculated optimal number of final input/output test pairs covering all subtasks and test types, packaged into both Polygon Full Package ZIP and standard Themis Package ZIP.
