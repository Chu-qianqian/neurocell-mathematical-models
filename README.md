# Neurocell Mathematical Models

> A traceable, copyright-compliant atlas of mathematical and computational models for nervous-system cells.

This repository is an equation-level knowledge base, not a paper mirror or a collection of third-party code. It separates bibliography verification from equation verification and never treats a model-family summary as a paper-level reproduction.

## Current evidence counts

- Bibliography-verified records: **6**
- Equation-located records: **3**
- Equation-transcribed records: **3**
- Independently checked equation records: **3**
- Candidate records awaiting equation screening: **5**
- Records with unavailable or uninspected full-text equations: **3**

## Verified equations

| Cell type | Model | Equation status | Equation page |
| --- | --- | --- | --- |
| Neuron | Hodgkin-Huxley conductance model | independently checked | [source-traceable equations](equations/models/hodgkin_huxley_1952.md) |
| Neuron | Izhikevich simple spiking-neuron model | independently checked | [source-traceable equations](equations/models/izhikevich_2003.md) |
| Astrocyte | G-ChI calcium and IP3 model | independently checked; parameters incomplete | [source-traceable equations](equations/models/de_pitta_2009_gchi.md) |
| Mixed neuron-glia system | Functional neuron-astrocyte calcium-network model | bibliography verified only | [holding record](equations/models/postnov_2009_neuron_astrocyte.md) |
| Microglia | Ischemic-penumbra dynamics model | bibliography verified only | [holding record](equations/models/amato_arnold_2025_microglia.md) |
| Oligodendrocyte | Differentiation dynamics model | bibliography verified only | [holding record](equations/models/nikolov_2022_oligodendrocyte.md) |

The catalogue is machine-readable in [models/model_catalog.csv](models/model_catalog.csv). Every displayed equation has an audit row in [data/equations/equation_audit.csv](data/equations/equation_audit.csv). Candidate literature is not automatically promoted to a core record; see [references/screening_candidates.csv](references/screening_candidates.csv).

## Evidence and copyright boundary

Equation pages require a source locator, source-access status, transcription type, and audit row. Sources with no inspected equation location remain holding records or candidates. The repository stores original explanatory prose and concise cited mathematics only; it does not distribute PDFs, publisher figures, copied tables, supplements, or third-party code. Linked third-party code remains outside this repository unless its license has been recorded as compatible.

## Navigation

- [Verified-equation index](equations/README.md)
- [Equation curation protocol](docs/equation_curation_protocol.md)
- [Equation notation policy](docs/equation_notation_policy.md)
- [Model scope taxonomy](docs/model_scope_taxonomy.md)
- [Cell-type pages](docs/cell_types/README.md)
- [Research gaps](docs/research_gaps.md)
- [Search log](references/search_log.csv) and [exclusion log](references/exclusion_log.csv)
- [Data dictionary](docs/data_dictionary.md)
- [Contribution guide](docs/CONTRIBUTING.md)

## Cell-type coverage

The current directly displayed systems cover two neuron models and one astrocyte model. Microglia and oligodendrocyte records are bibliography-verified holding records. Schwann cells, OPCs, ependymal cells, radial glia, neural stem cells, pericytes, and endothelial cells are documented search-queue categories rather than equation-verified models.

## Licenses and disclaimer

- Original code: Apache-2.0, see [LICENSE-CODE](LICENSE-CODE).
- Original documentation, tables, and explanations: CC BY 4.0, see [LICENSE-DOCS](LICENSE-DOCS).
- Third-party material is not relicensed; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- This repository is a literature-navigation and educational resource; see [DISCLAIMER.md](DISCLAIMER.md).

Last verified: 2026-07-22.
