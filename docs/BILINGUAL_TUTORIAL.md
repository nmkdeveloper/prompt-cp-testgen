# Bilingual Tutorial Contract

The default target package has two tutorial languages when tutorials are supported:
- English
- Vietnamese

## Source preservation

If a supplied tutorial exists in English or Vietnamese, preserve the supplied source text exactly in that language.

## Missing language

If one default tutorial language is absent, create a faithful translation from the available authoritative tutorial or explanation.

The translation must preserve:
- algorithm;
- invariant;
- proof idea;
- complexity;
- edge cases;
- correctness claims.

Do not invent a different algorithm merely to fill a missing translation.

## Package consistency

When the golden package uses tutorial artifacts, keep all applicable copies consistent:
- `problem.xml` tutorial entries;
- `statements/<language>/tutorial.tex`;
- `statement-sections/<language>/tutorial.tex`;
- `statements/<language>/problem-properties.json` `tutorial`.

Both languages remain package artifacts even if the VNOJ importer ultimately stores one selected tutorial in the site's single tutorial field.
