# Search strategy and screening protocol

**Protocol version:** 0.1  
**Seed-search date:** 2026-07-22  
**Purpose:** identify published mathematical/computational models by nervous-system cell type; not a systematic review or clinical evidence synthesis.

## Search concepts

| Concept | Example terms |
| --- | --- |
| Cell type | neuron, astrocyte, microglia, oligodendrocyte, OPC, Schwann cell, glia |
| Model | mathematical model, computational model, differential equation, ODE, PDE, stochastic, agent-based |
| Process | excitability, calcium, activation, inflammation, differentiation, myelination |

## Reproducible seed queries

Search each database with both a cell-type query and a process-specific query. Record the exact query, date, source URL/API response, screening decision, and persistent identifier in a future search-log CSV.

- `(neuron OR neuronal) AND ("mathematical model" OR "computational model" OR ODE)`
- `(astrocyte OR astroglia) AND (calcium OR Ca2+) AND (model OR equations)`
- `(microglia OR microglial) AND (activation OR inflammation) AND (model OR ODE OR PDE)`
- `(oligodendrocyte OR OPC) AND (differentiation OR myelination) AND (model OR equations)`
- `("Schwann cell") AND (model OR "differential equation" OR simulation)`

## Sources and provenance

The seed bibliography was checked through the Crossref REST API and source-specific landing pages/indices where available. The following sources are planned for expansion: Crossref, PubMed, OpenAlex, bioRxiv, arXiv, model registries (ModelDB, Open Source Brain), and publisher landing pages. Database coverage, access dates, and deduplication rules must be recorded before a collection is represented as comprehensive.

## Screening workflow

1. Deduplicate by DOI, then by normalized title and year.
2. Screen title/abstract against the inclusion and exclusion rules in `PROJECT_PLAN.md`.
3. Verify bibliography from a persistent source.
4. Classify formalism and target cell type from the primary source.
5. Keep equation extraction and implementation reproduction as separate, auditable tasks.

## Known limitations

The initial records are a deliberately small seed set, not a quantitative survey. The microglial seed uses a simplified activation framing from its source; current biology is more nuanced, so future records must preserve the source's terminology and avoid treating a binary state representation as a universal taxonomy.
