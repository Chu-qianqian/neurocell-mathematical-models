# Methodology and evidence rules

## Search design

Core searches combine cell-type synonyms with terms such as `mathematical model`, `computational model`, `differential equation`, `calcium dynamics`, `myelination`, `inflammation`, and `neurovascular coupling`. Target sources include PubMed, Europe PMC, Crossref, OpenAlex, Semantic Scholar, ModelDB, BioModels, and code repositories with explicit licenses.

Each formal search must preserve the database, full query, date, result count, deduplication rule, title/abstract/full-text screening counts, and exclusion reasons. The current Crossref queries only verified metadata for a small number of candidates; they are not a database-comprehensive search and do not justify PRISMA counts.

## Evidence states

| State | What it may claim | What it must not claim |
| --- | --- | --- |
| `verified` | DOI and title/authors/year/venue agree with authoritative metadata | Equation, parameter, code, or biological validation is complete |
| `partially verified` | One part of a source, such as metadata or abstract, was checked | Full-text equations were verified |
| `not verified` | The information cannot yet be confirmed | Any inferred detail |
| `full text unavailable` | No lawfully reviewable full text or methods material was obtained | No equation or model exists |
| `license unclear` | An external-code license was not confirmed | The code may be copied or redistributed |
| `parameters incomplete` | Public source material lacks sufficient parameters | The model is invalid or unusable |

## Equation-extraction gate

Before a model row is marked `extracted`, it must record source page/section/equation location, state variables, parameters and units, inputs/outputs, initial/boundary conditions, numerical method, assumptions, scope, and limitations. A second reviewer or reproducible script should check notation and dimensional consistency. Conceptual LaTeX on this repository explains model families only; it does not replace source transcription.

## Quality tiers

- **A:** original or classic model source;
- **B:** model with substantial application or validation evidence;
- **C:** extension adding coupling, space, stochasticity, or disease mechanism;
- **D:** exploratory source, preprint, or source with incomplete parameters/validation.

This tiering does not use fabricated impact factors or fixed citation counts. Any future dynamic citation metric must state its source and query date.
