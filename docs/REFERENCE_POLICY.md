# Reference and Oracle Policy

## Priority

Prefer supplied AC/accepted/official/reference code. Next prefer a supplied implementation consistent with an official explanation. Then use an independently derived intended solution. Never equate priority with trust.

## Verification ladder

```text
candidate
 -> compile
 -> validator
 -> brute comparison on safe small domain
 -> adversarial cases
 -> boundary cases
 -> independent property/alternate implementation when practical
 -> benchmark
 -> VERIFIED_REFERENCE
```

## Existing answer files

Use them as evidence, not unquestioned truth. Where practical, regenerate their outputs with the verified reference and compare. Investigate disagreement; never manually patch outputs.

## Independent checks

Whenever feasible, retain at least one independent check such as brute force, a different formulation, invariants or metamorphic testing. The purpose is to reduce shared conceptual errors.
