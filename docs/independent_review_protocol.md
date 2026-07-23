# Independent equation review protocol

Independent review is stricter than a maintainer second pass. A record may use `independently_checked` only when a checker who did not perform the original transcription completes this protocol against a frozen direct source.

## Required workflow

1. Record the checker name, role, check date, source identifier, source version, source access date, and frozen repository commit.
2. Extract the equations independently without consulting the repository transcription.
3. Compare the independent extraction with the repository only after the extraction is complete.
4. Compare signs, exponents, subscripts, variable definitions, units, parameter contexts, initial conditions, event handling, and equation numbering.
5. Record every discrepancy and its resolution. An unresolved discrepancy blocks `independently_checked`.
6. Record the resolution date when discrepancies require changes. Use `not_applicable` only when no discrepancy exists.

The machine-readable fields are defined in `data/equations/equation_audit.csv`. The header-only template at `data/equations/independent_review_template.csv` can be copied for an external review package. A maintainer re-reading the same source remains `second_pass_checked`.

## Frozen review package

The review package must identify:

- `checker_name`
- `checker_role`
- `check_date`
- `check_method`
- `source_identifier`
- `source_version`
- `source_access_date`
- `frozen_commit_sha`
- `discrepancies_found`
- `discrepancy_resolution`
- `resolution_date`

No current row is promoted merely because this protocol exists.
