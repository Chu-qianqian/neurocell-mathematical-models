<!-- Generated from models/model_catalog.csv; do not edit by hand. -->
# Neurocell Mathematical Models

> A traceable, copyright-compliant atlas of mathematical and computational models for nervous-system cells.

This repository is an equation-level knowledge base, not a paper mirror or a collection of third-party code. It separates bibliography verification, equation transcription, maintainer second-pass checking, and genuinely independent checking. A model-family screening item is never treated as a source-specific verified model without an identified primary source.

## Coverage summary

- Canonical model records: **25**
- Bibliography-only holding records: **18**
- Equation-located or stronger records: **7**
- Equation-transcribed records awaiting a second pass: **2**
- Maintainer second-pass checked records: **3**
- Independently checked records: **0**
- Records with incomplete parameter registries: **9**
- Records explicitly marked full text unavailable: **0**
- Records whose source full text is unavailable or not yet inspected: **18**
- Records with unclear external-code licensing: **10**
- Screening inventory rows: **278** (20 promoted to the canonical catalogue)

## Model catalogue

| Model ID | Model | Biological scope | Cell or network type | Scale | Equation status | Primary source | Equation locator | Review scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `hodgkin_huxley_1952` | [Hodgkin-Huxley conductance model](equations/models/hodgkin_huxley_1952.md) | `neuronal` | `neuron` / `not_applicable` | `single_cell` | `second_pass_checked` | [DOI](https://doi.org/10.1113/jphysiol.1952.sp004764) | pp. 505 and 518-519 equations (1)-(7) (15)-(16) and (26) | maintainer second pass |
| `izhikevich_2003` | [Izhikevich simple spiking-neuron model](equations/models/izhikevich_2003.md) | `neuronal` | `neuron` / `not_applicable` | `single_cell` | `second_pass_checked` | [DOI](https://doi.org/10.1109/tnn.2003.820440) | p. 1569 Section II equations (1)-(3) | maintainer second pass |
| `de_pitta_2009_gchi` | [G-ChI astrocyte calcium and IP3 model](equations/models/de_pitta_2009_gchi.md) | `glial` | `astrocyte` / `not_applicable` | `single_cell` | `second_pass_checked` | [DOI](https://doi.org/10.1007/s10867-009-9155-y) | author preprint pp. 8 and 18 equations (5) (6) and (20) | maintainer second pass |
| `postnov_2009_neuron_astrocyte` | [Functional neuron-astrocyte calcium-network model](equations/models/postnov_2009_neuron_astrocyte.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `large_scale_network` | `bibliography_verified` | [DOI](https://doi.org/10.1007/s10867-009-9156-x) | not verified | bibliography only |
| `amato_arnold_2025_microglia` | [Data-driven microglial ischemic-penumbra model](equations/models/amato_arnold_2025_microglia.md) | `glial` | `microglia` / `not_applicable` | `population` | `bibliography_verified` | [DOI](https://doi.org/10.1016/j.mbs.2025.109549) | not verified | bibliography only |
| `nikolov_2022_oligodendrocyte` | [Oligodendrocyte differentiation dynamics model](equations/models/nikolov_2022_oligodendrocyte.md) | `glial` | `oligodendrocyte` / `not_applicable` | `population` | `bibliography_verified` | [DOI](https://doi.org/10.3390/math10162928) | not verified | bibliography only |
| `wilson_cowan_1972` | [Wilson-Cowan excitatory-inhibitory population model](equations/models/wilson_cowan_1972.md) | `neural_population` | `neural_population` / `firing_rate_network` | `population` | `equation_transcribed` | [DOI](https://doi.org/10.1016/s0006-3495(72)86068-5) | article p. 8, equations (7)-(8) | transcribed; review pending |
| `potjans_diesmann_2014` | [Potjans-Diesmann cortical microcircuit model](equations/models/potjans_diesmann_2014_microcircuit.md) | `neural_population` | `neural_population` / `cortical_microcircuit` | `local_microcircuit` | `bibliography_verified` | [DOI](https://doi.org/10.1093/cercor/bhs358) | not verified | bibliography only |
| `montbrio_pazo_roxin_2015` | [Montbrio-Pazo-Roxin exact neural-mass reduction](equations/models/montbrio_pazo_roxin_2015.md) | `neural_population` | `neural_population` / `neural_mass` | `neural_mass` | `equation_transcribed` | [DOI](https://doi.org/10.1103/physrevx.5.021028) | arXiv:1506.06581v1, Section II.B, equations (12a)-(12b) | transcribed; review pending |
| `wong_wang_2006` | [Recurrent decision-network model](equations/models/wong_wang_2006_decision.md) | `neural_population` | `neural_population` / `attractor_network` | `population` | `bibliography_verified` | [DOI](https://doi.org/10.1523/jneurosci.3733-05.2006) | not verified | bibliography only |
| `morris_lecar_1981` | [Morris-Lecar excitable-membrane model](equations/models/morris_lecar_1981.md) | `other_nervous_system_related` | `excitable_membrane` / `not_applicable` | `single_cell` | `bibliography_verified` | [DOI](https://doi.org/10.1016/s0006-3495(81)84782-0) | not_verified | bibliography only |
| `brette_gerstner_2005_adex` | [Adaptive exponential integrate-and-fire model](equations/models/brette_gerstner_2005_adex.md) | `neuronal` | `neuron` / `not_applicable` | `single_cell` | `bibliography_verified` | [DOI](https://doi.org/10.1152/jn.00686.2005) | not_verified | bibliography only |
| `tsodyks_markram_1998_stp` | [Tsodyks-Pawelzik-Markram dynamic-synapse model](equations/models/tsodyks_markram_1998_stp.md) | `synaptic` | `synapse` / `not_applicable` | `subcellular` | `bibliography_verified` | [DOI](https://doi.org/10.1162/089976698300017502) | not_verified | bibliography only |
| `brunel_2000_ei_network` | [Brunel sparse excitatory-inhibitory network](equations/models/brunel_2000_ei_network.md) | `neural_population` | `neural_population` / `spiking_network` | `large_scale_network` | `bibliography_verified` | [DOI](https://doi.org/10.1023/a:1008925309027) | not_verified | bibliography only |
| `hopfield_1982` | [Hopfield associative-memory network](equations/models/hopfield_1982.md) | `neural_population` | `neural_population` / `attractor_network` | `large_scale_network` | `bibliography_verified` | [DOI](https://doi.org/10.1073/pnas.79.8.2554) | not_verified | bibliography only |
| `wang_buzsaki_1996_gamma` | [Wang-Buzsaki inhibitory gamma network](equations/models/wang_buzsaki_1996_gamma.md) | `neural_population` | `neural_population` / `interneuron_network` | `local_microcircuit` | `bibliography_verified` | [DOI](https://doi.org/10.1523/jneurosci.16-20-06402.1996) | not_verified | bibliography only |
| `li_rinzel_1994` | [Li-Rinzel reduced IP3-receptor calcium mechanism](equations/models/li_rinzel_1994.md) | `other_nervous_system_related` | `astrocyte_relevant_calcium_mechanism` / `not_applicable` | `subcellular` | `bibliography_verified` | [DOI](https://doi.org/10.1006/jtbi.1994.1041) | not_verified | bibliography only |
| `mrg_2002_myelinated_axon` | [McIntyre-Richardson-Grill myelinated-axon model](equations/models/mrg_2002_myelinated_axon.md) | `neuronal` | `myelinated_axon` / `not_applicable` | `multicompartment_cell` | `bibliography_verified` | [DOI](https://doi.org/10.1152/jn.00353.2001) | not_verified | bibliography only |
| `jirsa_2014_epileptor` | [Epileptor seizure-dynamics model](equations/models/jirsa_2014_epileptor.md) | `neural_population` | `neural_population` / `neural_mass` | `neural_mass` | `bibliography_verified` | [DOI](https://doi.org/10.1093/brain/awu133) | not_verified | bibliography only |
| `polykretis_2018_neural_astrocytic_network` | [Polykretis neural-astrocytic network architecture](equations/models/polykretis_2018_neural_astrocytic_network.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `local_microcircuit` | `equation_located` | [DOI](https://doi.org/10.1145/3229884.3229890) | arXiv:1807.02514v1, Methods, equations (1)-(9) | source located; transcription pending |
| `halnes_2013_electrodiffusive_astrocyte` | [Halnes astrocyte-extracellular electrodiffusive model](equations/models/halnes_2013_electrodiffusive_astrocyte.md) | `glial` | `astrocyte_extracellular_system` / `not_applicable` | `multicompartment_cell` | `equation_located` | [DOI](https://doi.org/10.1371/journal.pcbi.1003386) | PMC3868551, Model, equations (1)-(6), plus astrocyte/ECS membrane-mechanism sections | source located; transcription pending |
| `neuron_astrocyte_associative_memory_2025` | [Neuron-astrocyte associative-memory model](equations/models/neuron_astrocyte_associative_memory_2025.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `large_scale_network` | `bibliography_verified` | [DOI](https://doi.org/10.1073/pnas.2417788122) | not_verified | bibliography only |
| `astrocyte_place_cell_formation_2022` | [Astrocyte-dependent place-cell formation model](equations/models/astrocyte_place_cell_formation_2022.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `large_scale_network` | `bibliography_verified` | [DOI](https://doi.org/10.1007/s10827-022-00828-6) | not_verified | bibliography only |
| `polykretis_astrocytic_microdomain` | [Astrocytic microdomain local-plasticity model](equations/models/polykretis_astrocytic_microdomain.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `local_microcircuit` | `bibliography_verified` | [DOI](https://doi.org/10.1007/978-3-030-05587-5_15) | not_verified | bibliography only |
| `sequence_learning_neuronal_astrocytic_network` | [Associative neuronal-astrocytic sequence-learning network](equations/models/sequence_learning_neuronal_astrocytic_network.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `large_scale_network` | `bibliography_verified` | [DOI](https://doi.org/10.1007/978-3-030-59277-6_32) | not_verified | bibliography only |

## Equation evidence records

The unified table above preserves each row-level equation state. `second_pass_checked` remains a maintainer review state and is never treated as `independently_checked`. Located-only records do not display transcribed equations, and bibliography-only holding records do not display reconstructed source-specific equations.

## Implementation and numerical validation

| Model | Brian2 compatibility | Implementation | Numerical tests | Reference behavior | Reproduction |
| --- | --- | --- | --- | --- | --- |
| Hodgkin-Huxley conductance model | `native` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Izhikevich simple spiking-neuron model | `native` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| G-ChI astrocyte calcium and IP3 model | `possible_custom_ode` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Functional neuron-astrocyte calcium-network model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Data-driven microglial ischemic-penumbra model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Oligodendrocyte differentiation dynamics model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Wilson-Cowan excitatory-inhibitory population model | `possible_custom_ode` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Potjans-Diesmann cortical microcircuit model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Montbrio-Pazo-Roxin exact neural-mass reduction | `possible_custom_ode` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Recurrent decision-network model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Morris-Lecar excitable-membrane model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Adaptive exponential integrate-and-fire model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Tsodyks-Pawelzik-Markram dynamic-synapse model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Brunel sparse excitatory-inhibitory network | `possible_network_implementation` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Hopfield associative-memory network | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Wang-Buzsaki inhibitory gamma network | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Li-Rinzel reduced IP3-receptor calcium mechanism | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| McIntyre-Richardson-Grill myelinated-axon model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Epileptor seizure-dynamics model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Polykretis neural-astrocytic network architecture | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Halnes astrocyte-extracellular electrodiffusive model | `difficult_or_out_of_scope` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Neuron-astrocyte associative-memory model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Astrocyte-dependent place-cell formation model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Astrocytic microdomain local-plasticity model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Associative neuronal-astrocytic sequence-learning network | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |

Compatibility is a feasibility classification, not execution evidence. A passing smoke test supports `implementation_only`; it is not a paper-result reproduction.

## Screening inventory

- `bibliography_verified`: **5**
- `candidate`: **252**
- `excluded`: **1**
- `promoted`: **20**

Every requested inventory row has exactly one current screening outcome. A `candidate` row has passed title-level scope screening but still lacks source-specific evidence.

## Evidence-status definitions

- `bibliography_verified`: publication identity is verified, but equation evidence is not.
- `equation_located`: a lawful direct source and exact locator were inspected; no transcription is claimed.
- `equation_transcribed`: source equations are transcribed and registered, but review is pending.
- `second_pass_checked`: the maintainer workflow completed a second pass.
- `independently_checked`: a separate checker followed the frozen-source protocol and resolved discrepancies.
- Parameter completeness, implementation, numerical tests, reference behavior, and paper-result reproduction remain independent status dimensions.

## Canonical data and generated views

The only hand-maintained model catalogue is [models/model_catalog.csv](models/model_catalog.csv). [JSON](models/model_catalog.json), [YAML](models/model_catalog.yaml), this README, the [equation index](equations/README.md), and bibliography views are generated by `python scripts/build_tables.py`.

Every displayed equation has an audit row in [data/equations/equation_audit.csv](data/equations/equation_audit.csv). The complete requested screening scope is tracked in [references/model_screening_master.csv](references/model_screening_master.csv), with a line-level request snapshot in [references/model_screening_inventory.csv](references/model_screening_inventory.csv).

## Evidence and copyright boundary

Equation pages require a lawful source, a precise locator, a transcription type, and an audit row. The repository stores original explanatory prose and concise cited mathematics only; it does not distribute paper PDFs, publisher figures, copied tables, supplements, unlicensed third-party code, or unauthorized data. Paper access status and code-license status are recorded separately.

## Navigation

- [Equation index](equations/README.md)
- [Equation curation protocol](docs/equation_curation_protocol.md)
- [Evidence-status migration](docs/evidence_status_migration.md)
- [Independent-review protocol](docs/independent_review_protocol.md)
- [Equation notation policy](docs/equation_notation_policy.md)
- [Model scope taxonomy](docs/model_scope_taxonomy.md)
- [Cell-type pages](docs/cell_types/README.md)
- [Research gaps](docs/research_gaps.md)
- [Screening master](references/model_screening_master.csv)
- [Data dictionary](docs/data_dictionary.md)
- [Contribution guide](docs/CONTRIBUTING.md)

## Canonical catalogue coverage

- astrocyte: **1**
- astrocyte_extracellular_system: **1**
- astrocyte_relevant_calcium_mechanism: **1**
- excitable_membrane: **1**
- microglia: **1**
- mixed_neuron_astrocyte_system: **6**
- myelinated_axon: **1**
- neural_population: **8**
- neuron: **3**
- oligodendrocyte: **1**
- synapse: **1**

Neuron-microglia models, explicit oligodendrocyte-myelin networks, Schwann-cell models, neurovascular multicellular models, and other-cell categories remain evidence-gated screening items unless a source-specific canonical record says otherwise.

## Licenses and disclaimer

- Original code: Apache-2.0, see [LICENSE-CODE](LICENSE-CODE).
- Original documentation, tables, and explanations: CC BY 4.0, see [LICENSE-DOCS](LICENSE-DOCS).
- Third-party material is not relicensed; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- This repository is a literature-navigation and educational resource; see [DISCLAIMER.md](DISCLAIMER.md).

Last verified: 2026-07-23.
