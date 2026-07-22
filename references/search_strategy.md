# Search strategy and screening protocol

**Protocol version:** 0.2

**Seed-search date:** 2026-07-22

**Purpose:** identify mathematical and computational models for nervous-system cells. This core release is not a completed systematic review or clinical evidence synthesis.

## Databases and use order

1. Crossref: verify DOI, title, authors, year, and venue.
2. PubMed / Europe PMC: discover biomedical primary literature and lawfully readable full text.
3. OpenAlex / Semantic Scholar: assist citation chaining; any dynamic metric must state its source and query date.
4. ModelDB, BioModels, Open Source Brain, and GitHub: locate models/code only; external-code licenses require separate verification.
5. bioRxiv, medRxiv, and arXiv: supplement preprints, not peer-reviewed evidence.

## Concept groups and query templates

For every database, retain the full query, date, result count, deduplication rule, screening decision, and persistent link. The general template is:

```text
(cell-type synonym) AND ("mathematical model" OR "computational model"
OR "differential equation" OR ODE OR PDE OR stochastic)
AND (process synonym)
```

| Scope | Priority query example |
| --- | --- |
| Neuron | `(neuron OR neuronal) AND ("mathematical model" OR ODE OR "conductance-based")` |
| Astrocyte | `(astrocyte OR astroglia) AND (calcium OR Ca2+ OR IP3) AND (model OR equations)` |
| Microglia | `(microglia OR microglial) AND (activation OR inflammation OR chemotaxis) AND (model OR ODE OR PDE)` |
| Oligodendrocyte / OPC | `(oligodendrocyte OR OPC OR NG2) AND (differentiation OR myelination OR migration) AND (model OR equations)` |
| Schwann cell | `("Schwann cell") AND (myelination OR regeneration OR "Wallerian degeneration") AND (model OR simulation)` |
| Neurovascular cells | `(pericyte OR "brain endothelial" OR "neurovascular unit") AND (model OR equations)` |

## Screening rules

1. Deduplicate by DOI, then normalised title and year.
2. Use title/abstract screening to exclude papers that clearly lack a mathematical model.
3. Verify bibliography against Crossref, PubMed, or a publisher page.
4. Upgrade equation evidence only when lawfully reviewable full text, methods, supplement, model database, or code confirms the equation/algorithm.
5. Treat implementation and license checking as independent steps; a public webpage is not reusable code.
6. Preserve `not verified`, `full text unavailable`, `license unclear`, and `parameters incomplete` when needed; do not fill gaps by inference.

## Boundary of the current seed round

The current round only verified Crossref bibliography for six core records and placed five classic candidates in a screening queue. It did not run an exhaustive multi-database search and does not report PRISMA counts. Any claim of comprehensive coverage must wait until the formal search log is complete.
