<!-- Generated from models/model_catalog.csv; do not edit by hand. -->
# Project plan and completion status

## Research objective

Build a maintainable atlas of mathematical models for nervous-system cells. Each model record keeps bibliography, equation evidence, implementation status, license status, and biological interpretation distinct. The project delivers a small, reliable core before expanding coverage.

## Scope and evidence boundary

The catalogue covers neurons, glia, associated nervous-system cell types, and explicitly modelled mixed-cell systems. An included record needs a traceable stable source and an explicit mathematical or computational model. Experimental papers that merely mention a cell, secondary claims without a source, copied code with unclear licensing, and paper full text are excluded. Candidate and canonical records remain separate.

Original code is licensed Apache-2.0. Original documentation and curator-created tables are licensed CC BY 4.0. External material retains its original terms.

## Current catalogue snapshot

These counts are generated from `models/model_catalog.csv` and `references/model_screening_master.csv`; do not maintain a second statistics table by hand.

- Canonical model records: **25**
- Records with equation evidence at `equation_located` or stronger: **17**
- Equation transcriptions awaiting a maintainer second pass: **14**
- Maintainer second-pass checked records: **3**
- Independently checked records: **0**
- Original Brian2 implementation-only records with smoke tests: **5**
- Bibliography-only holding records: **8**
- Screening inventory rows: **278**

## Work phases

| Phase | Deliverable | Status |
| --- | --- | --- |
| 0 | Governance files, dual licenses, disclaimer, and repository initialization | Complete |
| 1 | Search protocol, data schema, and baseline validator | Complete |
| 2 | Bibliographically verified seed records | Complete |
| 3 | English navigation, classification, candidate queue, and gap analysis | Complete |
| 4 | Equation locations, transcription, variable/parameter extraction, and independent checking | In progress: equation evidence exists for 17 records; independent checking remains at 0. |
| 5 | Original minimal implementations from clearly licensed sources | In progress: 5 records are smoke-tested implementation-only examples; paper-result reproduction remains separate. |
| 6 | Multi-database systematic search and broad cell-type expansion | In progress: the screening master has 278 rows; underrepresented cell types remain evidence-gated. |

## Remaining work

- Complete maintainer and independently documented checks without promoting a record beyond its recorded evidence.
- Expand source-specific coverage for underrepresented cell types, including Schwann, ependymal, radial glial, neural stem, pericyte, and endothelial systems.
- Add implementations only where source evidence and licensing permit; distinguish numerical tests, reference behavior, and paper-result reproduction.
- Keep generated views synchronized by running `python scripts/build_tables.py` before review.
