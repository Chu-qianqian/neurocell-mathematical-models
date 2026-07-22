# Project plan and completion status

## Research objective

Build a maintainable atlas of mathematical models for nervous-system cells. Each model record keeps bibliography, equation evidence, implementation status, license status, and biological interpretation distinct. The project delivers a small, reliable core release before expanding coverage.

## Scope

Neurons, astrocytes, microglia, oligodendrocytes, OPC/NG2 glia, Schwann cells, ependymal cells, radial glia, neural stem cells, pericytes, brain endothelial cells, and explicitly modelled mixed-cell systems.

## Inclusion and exclusion

An included model needs a traceable stable source and an explicit mathematical or computational model. Experimental papers that merely mention a cell, secondary claims without a source, copied code with unclear licensing, and paper full text are excluded. Candidate and core records are stored separately.

## Literature and equation verification

- Bibliography verification: DOI, title, authors, year, and venue are checked against Crossref, PubMed, or a publisher page.
- Equation verification: a source location, variables, units, initial/boundary conditions, assumptions, and an independent consistency check are required before a record becomes `extracted`.
- Implementation verification: external code must have a clear source and license; otherwise only its link and status may be recorded.

## Copyright compliance

No paper PDF, original figure, full table, supplement, or third-party code with unclear licensing is included. Original code is Apache-2.0; original documentation and curator-created tables are CC BY 4.0; external materials retain their original terms.

## Work phases

| Phase | Deliverable | Status |
| --- | --- | --- |
| 0 | Governance files, dual licenses, disclaimer, `main` initialisation | Complete |
| 1 | Search protocol, data schema, baseline validator | Complete |
| 2 | Six bibliographically verified seed records | Complete |
| 3 | English navigation, classification, candidate queue, and gap analysis | Complete |
| 4 | Equation locations, variable/parameter extraction, and independent checking | Planned |
| 5 | Original minimal implementations from clearly licensed sources | Planned |
| 6 | Multi-database systematic search and broad cell-type expansion | Planned |

## Intended structure

- `data/models/`: minimal, strictly validated core records;
- `models/`: expanded CSV/JSON/YAML catalogue contract;
- `references/`: search strings, candidate queue, BibTeX, and verification audit;
- `docs/` and `equations/`: original English explanations, classification, and research gaps;
- `scripts/`: offline validation; `.github/`: validation on pull requests.

## Completion checklist

- [x] Governance, dual-license policy, and disclaimer
- [x] Reproducible search strategy and baseline data schema
- [x] Bibliographically verified seed catalogue
- [x] English core navigation and evidence-state conventions
- [ ] Equation-level source locations and independent checking
- [ ] Systematic all-cell-type search and complete screening counts
- [ ] Original minimal implementations from clearly licensed sources
- [ ] Record-level auditing of public code and experimental validation
