# Default Statement Languages

The default generated Polygon package uses exactly two statement language identifiers:

```text
english
vietnamese
```

Use them consistently in:

- `problem.xml`
- `statements/`
- `statement-sections/`
- HTML outputs
- PDF outputs
- tutorial outputs
- problem-properties metadata

If one language is missing from the input, create a faithful translation from the canonical reconstructed specification. Translation is not permission to change the problem semantics.

Original source language(s), if different, remain preserved internally for provenance and are not silently rewritten.


## Tutorial languages

The default tutorial languages are also `english` and `vietnamese` when a tutorial is part of the target package. Never silently remove the second tutorial because the VNOJ importer selects one main tutorial for site display.
