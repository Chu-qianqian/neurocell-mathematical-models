## Summary

Describe the atlas change and its target cell type(s).

## Evidence state and review boundary

- [ ] Each changed record states its evidence state without promotion beyond the recorded evidence.
- [ ] Any independent check identifies the independent checker, frozen source, method, and discrepancy resolution.
- [ ] Generated files were rebuilt twice and the generated-file drift check is clean.
- [ ] Numerical tests, reference behavior, and paper-result reproduction are reported as separate states.

## Provenance and licensing

- [ ] Each new record has a persistent primary source.
- [ ] Bibliography status is not overstated.
- [ ] No third-party paper content or unlicensed code was added.
- [ ] Any third-party asset has source, version, and license documented.

## Validation

Run this sequence in order:

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

- [ ] `python scripts/validate_catalogue.py` passed locally.
- [ ] `python scripts/build_tables.py` passed twice.
- [ ] The generated-file drift check passed.
- [ ] `python scripts/validate_references.py` passed locally.
- [ ] `python scripts/validate_equations.py` passed locally.
- [ ] `python scripts/validate_links.py` passed locally.
- [ ] `python scripts/validate_language.py` passed locally.
- [ ] `python -m unittest discover -s tests -v` passed locally.
- [ ] `git diff --check` passed locally.
