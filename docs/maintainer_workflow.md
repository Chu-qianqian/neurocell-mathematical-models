# Maintainer workflow

Use a focused branch and pull request for each coherent change. Keep the canonical catalogue, generated views, and evidence states aligned; do not treat a successful build as evidence that a source transcription, independent review, or paper-result reproduction is complete.

## Repository boundaries

- The only hand-maintained catalogue is `models/model_catalog.csv`.
- Generated views must be refreshed with `python scripts/build_tables.py`; do not edit generated files by hand.
- Original code is Apache-2.0. Original documentation and curator-created tables are CC BY 4.0. Third-party material is not relicensed.
- Do not add paper PDFs, publisher figures, copied tables, supplements, datasets, or third-party code unless its reusable license and provenance are explicitly documented.

## Change workflow

1. Start from the current default branch and preserve unrelated working-tree changes.
2. State the evidence level supported by each record: bibliography verification, equation location, transcription, maintainer second pass, or independently documented checking.
3. Update the canonical CSV and supporting audit files before regenerating derived views.
4. For an implementation, record numerical-test status, reference-behavior status, and paper-result reproduction status separately.
5. Run the validation sequence below and include the results in the pull request.

## Required validation sequence

Run these commands in order from the repository root:

```text
python scripts/validate_catalogue.py
python scripts/build_tables.py
python scripts/build_tables.py
python scripts/validate_references.py
python scripts/validate_equations.py
python scripts/validate_links.py
python scripts/validate_language.py
python -m unittest discover -s tests -v
git diff --check
```

The second build and `validate_references.py` detect generation drift; continuous integration also checks the generated-file diff in a clean checkout. A clean validation run does not replace independent scientific review.
