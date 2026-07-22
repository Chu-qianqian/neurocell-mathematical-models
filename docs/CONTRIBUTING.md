# Contributing

Submit changes through a branch and pull request. Do not add paper PDFs, publisher figures, supplements, or external code without an explicit reusable license.

A new model record needs a primary persistent identifier, target cell type, mathematical form, model classification, evidence for that classification, and separate bibliography/equation/implementation states. When information is insufficient, add the source to `references/screening_candidates.csv` rather than promoting it directly to the core catalogue.

Before submitting, run:

```text
python scripts/validate_catalogue.py
python scripts/build_tables.py
python scripts/validate_references.py
python scripts/validate_links.py
```

Only sources, equation locations, variables/parameters, and licenses that can be audited may upgrade a record's evidence state. Summarise sources in your own words, cite original papers, and preserve uncertainty explicitly.
