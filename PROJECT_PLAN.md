# Project plan

## Research objective

Build a transparent, reproducible atlas of mathematical and computational models describing nervous-system cell types. The atlas is a navigation and comparison resource, not a replacement for primary papers or a repository of their proprietary/copyrighted content.

## Cell-type scope

Primary scope: neurons, astrocytes, microglia, oligodendrocytes and oligodendrocyte precursor cells, Schwann cells, ependymal cells, satellite glia, enteric glia, and mixed neuron–glia systems. A model may be listed under more than one cell type only when the source explicitly models each type.

## Inclusion criteria

1. A stable scholarly or archival source is identifiable by DOI, PMID, preprint identifier, or persistent repository URL.
2. The source explicitly presents a mathematical/computational model relevant to at least one scoped cell type.
3. The modelling formalism can be classified (for example ODE, PDE, stochastic, agent-based, compartmental, or hybrid).
4. The record distinguishes paper verification from equation extraction and executable reproduction.

## Exclusion criteria

- Reviews, opinions, or biological experiments without a model are not model records.
- Untraceable claims, scraped equation collections, and license-unclear copied code are excluded.
- Model names alone are not enough: every record needs a primary source.
- Therapeutic or clinical claims are not inferred from model inclusion.

## Literature verification standard

Each `verified_bibliography` record must have its title, authorship, venue/year, and persistent identifier checked against a primary publisher page, PubMed, or Crossref. Records whose equations were not inspected are labelled `not_extracted`; `verified_bibliography` must never be read as independently validated biology or software.

## Equation extraction standard

Equations enter `equation_status=extracted` only when a curator records the source location (equation/section/page), states assumptions and units, and performs a second-person or scripted consistency check. The first seed keeps equation text out of the repository and uses `not_extracted` deliberately.

## Copyright and license compliance

- Cite and link to sources; do not upload article PDFs, figures, tables, or supplementary files unless their license and provenance are recorded.
- Do not copy third-party implementations without a compatible, documented license and attribution.
- Original code is Apache-2.0; original documentation and curation output are CC BY 4.0. Third-party material keeps its original terms.

## Phased tasks

| Phase | Deliverable | Status |
| --- | --- | --- |
| 0 | Governance, licenses, disclaimer, base README | complete |
| 1 | Search protocol, schemas, validation tooling | complete |
| 2 | Bibliographically verified seed records | complete |
| 3 | Equation-level extraction with locators and units | planned |
| 4 | Reproduction notebooks for permissively licensed models | planned |
| 5 | Broad cell-type expansion and independent review | planned |

## Expected structure

`data/models/` curated records; `references/` strategy and citation audits; `docs/` curation guidance; `scripts/` validation tools; `examples/` original minimal examples; `.github/` validation workflow and templates.

## Completion checklist

- [x] Project governance and dual-license policy
- [x] Reproducible search protocol
- [x] Machine-readable schema and seed catalogue
- [x] Citation identifiers independently checked against Crossref
- [ ] Equation-level extraction with source locators
- [ ] Independent equation transcription check
- [ ] Executable model reproductions
- [ ] Broad coverage of all scoped cell types
