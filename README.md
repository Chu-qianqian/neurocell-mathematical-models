<!-- Generated from models/model_catalog.csv; do not edit by hand. -->
# Neurocell Mathematical Models

> A traceable, copyright-compliant atlas of mathematical and computational models for nervous-system cells.

This repository is an equation-level knowledge base, not a paper mirror or a collection of third-party code. It separates bibliography verification, equation transcription, maintainer second-pass checking, and genuinely independent checking. A model-family screening item is never treated as a source-specific verified model without an identified primary source.

## Current evidence counts

- Canonical model records: **10**
- Bibliography-only holding records: **5**
- Equation-located or stronger records: **5**
- Equation-transcribed records awaiting a second pass: **2**
- Maintainer second-pass checked records: **3**
- Independently checked records: **0**
- Records with incomplete parameter registries: **9**
- Records explicitly marked full text unavailable: **0**
- Records whose source full text is unavailable or not yet inspected: **5**
- Records with unclear external-code licensing: **10**
- Screening inventory rows: **278** (5 promoted to the canonical catalogue)

## Independently checked equations

No records currently meet this evidence state.

Independent status requires a named checker, check date, method, verification source, source version, access date, and discrepancy resolution in the equation audit. No record currently satisfies that contract.

## Maintainer second-pass checked equations

| Cell type | Model | Equation status | Brian2 compatibility | Equation page |
| --- | --- | --- | --- | --- |
| Neuron | Hodgkin-Huxley conductance model | `second_pass_checked` | `native` | [record](equations/models/hodgkin_huxley_1952.md) |
| Neuron | Izhikevich simple spiking-neuron model | `second_pass_checked` | `native` | [record](equations/models/izhikevich_2003.md) |
| Astrocyte | G-ChI astrocyte calcium and IP3 model | `second_pass_checked` | `possible_custom_ode` | [record](equations/models/de_pitta_2009_gchi.md) |

These records received a second check within the maintainer workflow. They are deliberately not described as independently checked.

## Equation-transcribed models

| Cell type | Model | Equation status | Brian2 compatibility | Equation page |
| --- | --- | --- | --- | --- |
| Neuron | Wilson-Cowan excitatory-inhibitory population model | `equation_transcribed` | `possible_custom_ode` | [record](equations/models/wilson_cowan_1972.md) |
| Neuron | Montbrio-Pazo-Roxin exact neural-mass reduction | `equation_transcribed` | `possible_custom_ode` | [record](equations/models/montbrio_pazo_roxin_2015.md) |

These transcriptions have exact source locators and equation-audit rows but still await a documented second pass.

## Bibliography-verified holding records

| Cell type | Model | Equation status | Brian2 compatibility | Equation page |
| --- | --- | --- | --- | --- |
| Mixed neuron-glia system | Functional neuron-astrocyte calcium-network model | `bibliography_verified` | `not_assessed` | [record](equations/models/postnov_2009_neuron_astrocyte.md) |
| Microglia | Data-driven microglial ischemic-penumbra model | `bibliography_verified` | `not_assessed` | [record](equations/models/amato_arnold_2025_microglia.md) |
| Oligodendrocyte | Oligodendrocyte differentiation dynamics model | `bibliography_verified` | `not_assessed` | [record](equations/models/nikolov_2022_oligodendrocyte.md) |
| Neuron | Potjans-Diesmann cortical microcircuit model | `bibliography_verified` | `not_assessed` | [record](equations/models/potjans_diesmann_2014_microcircuit.md) |
| Neuron | Recurrent decision-network model | `bibliography_verified` | `not_assessed` | [record](equations/models/wong_wang_2006_decision.md) |

Holding records do not display reconstructed source-specific equations.

## Brian2 feasibility and implementation evidence

| Cell type | Model | Equation status | Brian2 compatibility | Equation page |
| --- | --- | --- | --- | --- |
| Neuron | Hodgkin-Huxley conductance model | `second_pass_checked` | `native` | [record](equations/models/hodgkin_huxley_1952.md) |
| Neuron | Izhikevich simple spiking-neuron model | `second_pass_checked` | `native` | [record](equations/models/izhikevich_2003.md) |
| Astrocyte | G-ChI astrocyte calcium and IP3 model | `second_pass_checked` | `possible_custom_ode` | [record](equations/models/de_pitta_2009_gchi.md) |
| Mixed neuron-glia system | Functional neuron-astrocyte calcium-network model | `bibliography_verified` | `not_assessed` | [record](equations/models/postnov_2009_neuron_astrocyte.md) |
| Microglia | Data-driven microglial ischemic-penumbra model | `bibliography_verified` | `not_assessed` | [record](equations/models/amato_arnold_2025_microglia.md) |
| Oligodendrocyte | Oligodendrocyte differentiation dynamics model | `bibliography_verified` | `not_assessed` | [record](equations/models/nikolov_2022_oligodendrocyte.md) |
| Neuron | Wilson-Cowan excitatory-inhibitory population model | `equation_transcribed` | `possible_custom_ode` | [record](equations/models/wilson_cowan_1972.md) |
| Neuron | Potjans-Diesmann cortical microcircuit model | `bibliography_verified` | `not_assessed` | [record](equations/models/potjans_diesmann_2014_microcircuit.md) |
| Neuron | Montbrio-Pazo-Roxin exact neural-mass reduction | `equation_transcribed` | `possible_custom_ode` | [record](equations/models/montbrio_pazo_roxin_2015.md) |
| Neuron | Recurrent decision-network model | `bibliography_verified` | `not_assessed` | [record](equations/models/wong_wang_2006_decision.md) |

Compatibility is a feasibility classification, not execution evidence. Every current record remains `not_implemented`, with `numerical_test_status=not_run`, `reference_behavior_status=not_assessed`, and `reproduction_status=not_attempted`.

## Canonical data and generated views

The only hand-maintained model catalogue is [models/model_catalog.csv](models/model_catalog.csv). [JSON](models/model_catalog.json), [YAML](models/model_catalog.yaml), and this README are generated by `python scripts/build_tables.py`. The legacy `data/models/catalogue.csv` index was removed after its six records were confirmed to be represented in the canonical catalogue.

Every displayed equation has an audit row in [data/equations/equation_audit.csv](data/equations/equation_audit.csv). The complete requested screening scope is tracked in [references/model_screening_master.csv](references/model_screening_master.csv), with a line-level request snapshot in [references/model_screening_inventory.csv](references/model_screening_inventory.csv).

## Evidence and copyright boundary

Equation pages require a lawful source, a precise locator, a transcription type, and an audit row. The repository stores original explanatory prose and concise cited mathematics only; it does not distribute paper PDFs, publisher figures, copied tables, supplements, unlicensed third-party code, or unauthorized data. Paper access status and code-license status are recorded separately.

## Navigation

- [Equation index](equations/README.md)
- [Equation curation protocol](docs/equation_curation_protocol.md)
- [Evidence-status migration](docs/evidence_status_migration.md)
- [Equation notation policy](docs/equation_notation_policy.md)
- [Model scope taxonomy](docs/model_scope_taxonomy.md)
- [Cell-type pages](docs/cell_types/README.md)
- [Research gaps](docs/research_gaps.md)
- [Screening master](references/model_screening_master.csv)
- [Data dictionary](docs/data_dictionary.md)
- [Contribution guide](docs/CONTRIBUTING.md)

## Canonical catalogue coverage

- Astrocyte: **1**
- Microglia: **1**
- Mixed neuron-glia system: **1**
- Neuron: **6**
- Oligodendrocyte: **1**

Synaptic models, neuron-microglia models, myelinated-axon and myelin-plasticity models, Schwann-cell models, neurovascular multicellular models, and other-cell categories remain evidence-gated screening items unless a source-specific canonical record says otherwise.

## Licenses and disclaimer

- Original code: Apache-2.0, see [LICENSE-CODE](LICENSE-CODE).
- Original documentation, tables, and explanations: CC BY 4.0, see [LICENSE-DOCS](LICENSE-DOCS).
- Third-party material is not relicensed; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- This repository is a literature-navigation and educational resource; see [DISCLAIMER.md](DISCLAIMER.md).

Last verified: 2026-07-23.
