# Equation curation protocol

## Evidence gate

An equation is displayed only after a curator has inspected a lawful full-text, author-posted preprint, publisher supplement, model database entry, or source-code location and recorded a precise locator. Bibliographic verification alone does not authorize equation display.

The catalogue uses these states:

- `bibliography_verified`: title, authors, venue, year, and DOI were checked against Crossref or another authoritative metadata record.
- `equation_located`: a source containing the system was inspected and its locator was recorded.
- `equation_transcribed`: a displayed equation has an audit row and transcription type.
- `second_pass_checked`: the displayed transcription received a second check in the same maintainer workflow.
- `independently_checked`: a separate checker is documented with date, method, source version, verification source, and discrepancy resolution.
- `parameters_incomplete`: an equation may be located, but the source parameters have not been fully curated.
- `full_text_unavailable`: the source could not be inspected lawfully in this curation pass.
- `license_unclear`: a linked code or database item has no documented reuse assessment.

`not_verified` is reserved for a record that has no equation-level source inspection. A page with this state must not contain a paper-specific reconstructed equation.

## Curation procedure

1. Verify bibliography through Crossref, PubMed, publisher metadata, or an equivalent authoritative record.
2. Inspect a lawful equation source and record page, section, equation, supplement, database, or code locator.
3. Add variables, parameters, and every displayed equation to the CSV registries under `data/equations/`.
4. State whether a transcription is exact, equivalent with a symbol mapping, or conceptual. Only the first two are permitted on a model-specific verified page.
5. Record unverified inputs, initial conditions, boundary conditions, numerical methods, and code licenses explicitly rather than filling gaps from secondary sources.
6. Record a maintainer second pass separately from an independent check. Re-reading a source in one workflow is not independent evidence.
7. Run the local validators before proposing the change.

`equation_located` does not authorize displayed source equations. Displayed mathematics requires `equation_transcribed` or stronger evidence, registry coverage, and an audit row. The independent-review contract is defined in [independent_review_protocol.md](independent_review_protocol.md).

Boundary conditions, network conditions, event handling, external input, initial conditions, and numerical integration settings are audited independently. `not_applicable` for a non-spatial ODE boundary does not imply that connectivity or threshold/reset rules are absent.

No PDFs, copied figures, copied tables, supplements, or third-party code are stored in this repository.
