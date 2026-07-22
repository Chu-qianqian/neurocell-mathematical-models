# Neurocell Mathematical Models

> A traceable, copyright-compliant atlas of mathematical and computational models for neurons and nervous-system glia.

This repository catalogues nervous-system cell models that are represented by explicit mathematical formalisms. It is not a full-text paper mirror, a collection of third-party code, or a directory of papers that merely mention a cell type. Model names, variable names, and original paper titles are retained in English for source traceability.

## Purpose

- Record each model's cellular scope, mathematical form, biological function, evidence tier, and reproducibility status separately.
- Provide a stable data interface for later equation-level verification, parameter extraction, and original minimal implementations.
- Distinguish cell-intrinsic models, single-function models, cell-population models, multicellular coupled models, and indirect parameterizations.
- Do not distribute copyrighted paper PDFs, figures, supplements, or third-party code with unclear licensing.

## Current core release

The core release contains **six bibliographically verified seed records**: two neuronal records, one astrocyte record, one neuron–astrocyte coupled record, one microglial record, and one oligodendrocyte record. Their DOI, author, year, and venue have been checked against Crossref. Equation-level verification, parameter transcription, third-party-code license assessment, and executable reproduction have not been completed and are never claimed as complete.

| Cell type | Model | Mathematical form | Function simulated | Original paper | Code | License | Reproducibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Neuron | Hodgkin-Huxley conductance model | ODE / conductance-based | Membrane excitability and action potentials | [Hodgkin & Huxley (1952)](https://doi.org/10.1113/jphysiol.1952.sp004764) | Not assessed | Not assessed | Bibliography only |
| Neuron | Izhikevich simple spiking-neuron model | ODE | Spiking dynamics | [Izhikevich (2003)](https://doi.org/10.1109/tnn.2003.820440) | Not assessed | Not assessed | Bibliography only |
| Astrocyte | G-ChI model | ODE | Glutamate-regulated Ca²⁺/IP3 dynamics | [De Pittà et al. (2009)](https://doi.org/10.1007/s10867-009-9155-y) | Not assessed | Not assessed | Bibliography only |
| Mixed neuron–glia | Functional neuron-astrocyte calcium-network model | ODE | Neuron–astrocyte Ca²⁺ signalling | [Postnov et al. (2009)](https://doi.org/10.1007/s10867-009-9156-x) | Not assessed | Not assessed | Bibliography only |
| Microglia | Ischemic-penumbra dynamics model | ODE | Microglial dynamics in ischemic penumbra | [Amato & Arnold (2025)](https://doi.org/10.1016/j.mbs.2025.109549) | Not assessed | Not assessed | Bibliography only |
| Oligodendrocyte | Differentiation dynamics model | ODE | Oligodendrocyte differentiation | [Nikolov et al. (2022)](https://doi.org/10.3390/math10162928) | Not assessed | Not assessed | Bibliography only |

The machine-readable seed catalogue is [data/models/catalogue.csv](data/models/catalogue.csv). The expanded catalogue contract is [models/model_catalog.csv](models/model_catalog.csv). Candidate literature is not automatically treated as a core model record; see [references/screening_candidates.csv](references/screening_candidates.csv).

## Inclusion and exclusion criteria

**Inclusion gate:** a stable source is identifiable; the paper explicitly presents or uses a cell-relevant mathematical/computational model; its formalism can be classified; and bibliography, equation, implementation, and license statuses are recorded independently.

**Excluded from core model records:** experimental papers without a model, review-only conclusions, untraceable claims, models that only parameterize myelin or glia without explicit cellular scope, and copied third-party code with unclear licensing. Literature without equation verification remains in the screening queue.

## Navigation

- [Scope and classification](docs/overview.md)
- [Methodology and evidence rules](docs/methodology.md)
- [Comparison matrix](docs/comparison_matrix.md)
- [Research gaps](docs/research_gaps.md)
- [Cell-type pages](docs/cell_types/README.md)
- [Equation-reading guide](equations/README.md)
- [Search strategy](references/search_strategy.md)
- [Data dictionary](docs/data_dictionary.md)
- [Contribution guide](docs/CONTRIBUTING.md)

## Model classification

Classification tags cover mathematical form (ODE, PDE, SDE, reaction-diffusion, conductance-based, agent-based, hybrid, and more), biological scale (molecular to systems level), and function (electrical activity, calcium signalling, inflammation, myelination, vascular regulation, and more). Each record also uses one of `cell_intrinsic`, `cell_function`, `cell_population`, `coupled_multicellular`, or `indirect_parameterization`. These are curator classifications, not replacements for author terminology.

## Literature quality and verification tiers

`A`, `B`, `C`, and `D` mean foundational/classic, important application, coupled/extended, and exploratory sources. They are not journal-impact-factor labels or fixed citation counts. Evidence states include `verified`, `partially verified`, `not verified`, `full text unavailable`, `license unclear`, `code unavailable`, and `parameters incomplete`. All current seed records are **bibliography verified and equation not verified**.

## Citation and contribution

Please cite both this repository version and the relevant original paper. Repository metadata is in [CITATION.cff](CITATION.cff). Before contributing, read [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) and provide a traceable primary source, verification notes, and code-license information.

## Licenses and disclaimer

- Original code: Apache-2.0, see [LICENSE-CODE](LICENSE-CODE).
- Original documentation, tables, and explanations: CC BY 4.0, see [LICENSE-DOCS](LICENSE-DOCS).
- Third-party material is not relicensed; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- This repository is a literature-navigation and educational resource; see [DISCLAIMER.md](DISCLAIMER.md).

Last updated: 2026-07-22 (core release; see each record's `last_verified`).
