<!-- Generated from models/model_catalog.csv; do not edit by hand. -->
# 神经细胞数学模型库

[English](README.md) | 简体中文

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22078787.svg)](https://doi.org/10.5281/zenodo.22078787)

> 一个可溯源、符合版权规范的神经系统细胞数学与计算模型图谱。

本仓库是一个方程级知识库，不是论文镜像，也不收集第三方代码。它将书目核实、方程转录、维护者第二遍复核与真正独立的检查分开管理。在没有确定一手来源的情况下，模型家族的筛选条目永远不会被当作经过来源级验证的模型。

## 覆盖概况

- 规范目录记录：**25**
- 仅书目暂存记录：**9**
- 方程已定位或更强状态的记录：**16**
- 已转录、待第二遍复核的记录：**13**
- 维护者已第二遍复核的记录：**3**
- 已独立复核的记录：**0**
- 参数注册表不完整的记录：**9**
- 明确标注全文不可获取的记录：**0**
- 来源全文不可获取或尚未查验的记录：**9**
- 外部代码许可状态不明的记录：**8**
- 筛选清单行数：**278**（其中 20 条已晋升进入规范目录）

## 模型目录

| 模型 ID | 模型 | 生物学范围 | 细胞或网络类型 | 尺度 | 方程状态 | 一手文献 | 方程定位器 | 复核范围 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `hodgkin_huxley_1952` | [Hodgkin-Huxley conductance model](equations/models/hodgkin_huxley_1952.md) | `neuronal` | `neuron` / `not_applicable` | `single_cell` | `second_pass_checked` | [DOI](https://doi.org/10.1113/jphysiol.1952.sp004764) | pp. 505 and 518-519 equations (1)-(7) (15)-(16) and (26) | 维护者第二遍复核 |
| `izhikevich_2003` | [Izhikevich simple spiking-neuron model](equations/models/izhikevich_2003.md) | `neuronal` | `neuron` / `not_applicable` | `single_cell` | `second_pass_checked` | [DOI](https://doi.org/10.1109/tnn.2003.820440) | p. 1569 Section II equations (1)-(3) | 维护者第二遍复核 |
| `de_pitta_2009_gchi` | [G-ChI astrocyte calcium and IP3 model](equations/models/de_pitta_2009_gchi.md) | `glial` | `astrocyte` / `not_applicable` | `single_cell` | `second_pass_checked` | [DOI](https://doi.org/10.1007/s10867-009-9155-y) | author preprint pp. 8 and 18 equations (5) (6) and (20) | 维护者第二遍复核 |
| `postnov_2009_neuron_astrocyte` | [Functional neuron-astrocyte calcium-network model](equations/models/postnov_2009_neuron_astrocyte.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `large_scale_network` | `bibliography_verified` | [DOI](https://doi.org/10.1007/s10867-009-9156-x) | not verified | 仅书目 |
| `amato_arnold_2025_microglia` | [Data-driven microglial ischemic-penumbra model](equations/models/amato_arnold_2025_microglia.md) | `glial` | `microglia` / `not_applicable` | `population` | `bibliography_verified` | [DOI](https://doi.org/10.1016/j.mbs.2025.109549) | not verified | 仅书目 |
| `nikolov_2022_oligodendrocyte` | [Oligodendrocyte differentiation dynamics model](equations/models/nikolov_2022_oligodendrocyte.md) | `glial` | `oligodendrocyte` / `not_applicable` | `population` | `bibliography_verified` | [DOI](https://doi.org/10.3390/math10162928) | not verified | 仅书目 |
| `wilson_cowan_1972` | [Wilson-Cowan excitatory-inhibitory population model](equations/models/wilson_cowan_1972.md) | `neural_population` | `neural_population` / `firing_rate_network` | `population` | `equation_transcribed` | [DOI](https://doi.org/10.1016/s0006-3495(72)86068-5) | article p. 8, equations (7)-(8) | 已转录；待复核 |
| `potjans_diesmann_2014` | [Potjans-Diesmann cortical microcircuit model](equations/models/potjans_diesmann_2014_microcircuit.md) | `neural_population` | `neural_population` / `cortical_microcircuit` | `local_microcircuit` | `equation_transcribed` | [DOI](https://doi.org/10.1093/cercor/bhs358) | Methods equations (1)-(13) with unnumbered displays; Table 4 neuron and synapse rows (subthreshold dynamics, postsynaptic current, spiking condition) | 已转录；待复核 |
| `montbrio_pazo_roxin_2015` | [Montbrio-Pazo-Roxin exact neural-mass reduction](equations/models/montbrio_pazo_roxin_2015.md) | `neural_population` | `neural_population` / `neural_mass` | `neural_mass` | `equation_transcribed` | [DOI](https://doi.org/10.1103/physrevx.5.021028) | arXiv:1506.06581v1, Section II.B, equations (12a)-(12b) | 已转录；待复核 |
| `wong_wang_2006` | [Recurrent decision-network model](equations/models/wong_wang_2006_decision.md) | `neural_population` | `neural_population` / `attractor_network` | `population` | `equation_transcribed` | [DOI](https://doi.org/10.1523/jneurosci.3733-05.2006) | Materials and Methods equations (1)-(9) and Phase-plane reduction displays; Dynamical equations equations (10)-(21); Simulations noise display; Results stimulus displays and equation (22); Appendix system | 已转录；待复核 |
| `morris_lecar_1981` | [Morris-Lecar excitable-membrane model](equations/models/morris_lecar_1981.md) | `other_nervous_system_related` | `excitable_membrane` / `not_applicable` | `single_cell` | `equation_transcribed` | [DOI](https://doi.org/10.1016/s0006-3495(81)84782-0) | Methods, The Model, equations (1)-(2); Analysis, equations (3)-(7); Ca-accumulation perturbation, equation (8); Limit-cycle oscillations, reduced system and equations (9)-(17) | 已转录；待复核 |
| `brette_gerstner_2005_adex` | [Adaptive exponential integrate-and-fire model](equations/models/brette_gerstner_2005_adex.md) | `neuronal` | `neuron` / `not_applicable` | `single_cell` | `equation_transcribed` | [DOI](https://doi.org/10.1152/jn.00686.2005) | Methods, Adapting the aEIF model, equations (1)-(3); Table 1 aEIF parameter box (conductance-based form and reset rule) | 已转录；待复核 |
| `tsodyks_markram_1998_stp` | [Tsodyks-Pawelzik-Markram dynamic-synapse model](equations/models/tsodyks_markram_1998_stp.md) | `synaptic` | `synapse` / `not_applicable` | `subcellular` | `equation_transcribed` | [DOI](https://doi.org/10.1162/089976698300017502) | Section 2 equations (2.1)-(2.3) with unnumbered steady state; Section 3 equations (3.1)-(3.7); Section 4 equations (4.1)-(4.5); Appendix equations (A.1)-(A.4) | 已转录；待复核 |
| `brunel_2000_ei_network` | [Brunel sparse excitatory-inhibitory network](equations/models/brunel_2000_ei_network.md) | `neural_population` | `neural_population` / `spiking_network` | `large_scale_network` | `equation_transcribed` | [DOI](https://doi.org/10.1023/a:1008925309027) | Section 2 equations (1)-(2); Section 3 equations (3)-(12); Section 4 equations (13)-(27); Section 5 equations (28)-(31); Section 6 equations (32)-(33); Appendix A equations (34)-(56); Appendix B equations (57)-(66) with unnumbered displays | 已转录；待复核 |
| `hopfield_1982` | [Hopfield associative-memory network](equations/models/hopfield_1982.md) | `neural_population` | `neural_population` / `attractor_network` | `large_scale_network` | `equation_transcribed` | [DOI](https://doi.org/10.1073/pnas.79.8.2554) | pp. 2555-2556, bracketed equations [1]-[8] | 已转录；待复核 |
| `wang_buzsaki_1996_gamma` | [Wang-Buzsaki inhibitory gamma network](equations/models/wang_buzsaki_1996_gamma.md) | `neural_population` | `neural_population` / `interneuron_network` | `local_microcircuit` | `equation_transcribed` | [DOI](https://doi.org/10.1523/jneurosci.16-20-06402.1996) | Materials and Methods, equations (2.1)-(2.4) with rate expressions | 已转录；待复核 |
| `li_rinzel_1994` | [Li-Rinzel reduced IP3-receptor calcium mechanism](equations/models/li_rinzel_1994.md) | `other_nervous_system_related` | `astrocyte_relevant_calcium_mechanism` / `not_applicable` | `subcellular` | `bibliography_verified` | [DOI](https://doi.org/10.1006/jtbi.1994.1041) | not_verified | 仅书目 |
| `mrg_2002_myelinated_axon` | [McIntyre-Richardson-Grill myelinated-axon model](equations/models/mrg_2002_myelinated_axon.md) | `neuronal` | `myelinated_axon` / `not_applicable` | `multicompartment_cell` | `equation_transcribed` | [DOI](https://doi.org/10.1152/jn.00353.2001) | Appendix: general ionic current, gate kinetics, fast and persistent sodium, slow potassium, juxtaparanodal fast potassium (Fig. 9 only), and leakage currents; all displays unnumbered | 已转录；待复核 |
| `jirsa_2014_epileptor` | [Epileptor seizure-dynamics model](equations/models/jirsa_2014_epileptor.md) | `neural_population` | `neural_population` / `neural_mass` | `neural_mass` | `bibliography_verified` | [DOI](https://doi.org/10.1093/brain/awu133) | not_verified | 仅书目 |
| `polykretis_2018_neural_astrocytic_network` | [Polykretis neural-astrocytic network architecture](equations/models/polykretis_2018_neural_astrocytic_network.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `local_microcircuit` | `equation_transcribed` | [DOI](https://doi.org/10.1145/3229884.3229890) | arXiv:1807.02514v1, Methods, equations (1)-(9) | 已转录；待复核 |
| `halnes_2013_electrodiffusive_astrocyte` | [Halnes astrocyte-extracellular electrodiffusive model](equations/models/halnes_2013_electrodiffusive_astrocyte.md) | `glial` | `astrocyte_extracellular_system` / `not_applicable` | `multicompartment_cell` | `equation_transcribed` | [DOI](https://doi.org/10.1371/journal.pcbi.1003386) | Model section, Electrodiffusive formalism, equations (1)-(6); arXiv numbering matches published PMC3868551 | 已转录；待复核 |
| `neuron_astrocyte_associative_memory_2025` | [Neuron-astrocyte associative-memory model](equations/models/neuron_astrocyte_associative_memory_2025.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `large_scale_network` | `bibliography_verified` | [DOI](https://doi.org/10.1073/pnas.2417788122) | not_verified | 仅书目 |
| `astrocyte_place_cell_formation_2022` | [Astrocyte-dependent place-cell formation model](equations/models/astrocyte_place_cell_formation_2022.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `large_scale_network` | `bibliography_verified` | [DOI](https://doi.org/10.1007/s10827-022-00828-6) | not_verified | 仅书目 |
| `polykretis_astrocytic_microdomain` | [Astrocytic microdomain local-plasticity model](equations/models/polykretis_astrocytic_microdomain.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `local_microcircuit` | `bibliography_verified` | [DOI](https://doi.org/10.1007/978-3-030-05587-5_15) | not_verified | 仅书目 |
| `sequence_learning_neuronal_astrocytic_network` | [Associative neuronal-astrocytic sequence-learning network](equations/models/sequence_learning_neuronal_astrocytic_network.md) | `mixed_neuron_glia` | `mixed_neuron_astrocyte_system` / `neuron_astrocyte_network` | `large_scale_network` | `bibliography_verified` | [DOI](https://doi.org/10.1007/978-3-030-59277-6_32) | not_verified | 仅书目 |

## 方程证据记录

上表保留了每一行的方程证据状态。`second_pass_checked` 始终是维护者层面的复核状态，绝不等同于 `independently_checked`。仅"已定位"的记录不展示转录方程；仅书目的暂存记录不展示重构的来源专属方程。

## 实现与数值验证

| 模型 | Brian2 兼容性 | 实现 | 数值测试 | 参考行为 | 复现 |
| --- | --- | --- | --- | --- | --- |
| Hodgkin-Huxley conductance model | `native` | `smoke_tested` | `passed` | `qualitative_match` | `implementation_only` |
| Izhikevich simple spiking-neuron model | `native` | `smoke_tested` | `passed` | `not_assessed` | `implementation_only` |
| G-ChI astrocyte calcium and IP3 model | `possible_custom_ode` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Functional neuron-astrocyte calcium-network model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Data-driven microglial ischemic-penumbra model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Oligodendrocyte differentiation dynamics model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Wilson-Cowan excitatory-inhibitory population model | `possible_custom_ode` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Potjans-Diesmann cortical microcircuit model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Montbrio-Pazo-Roxin exact neural-mass reduction | `possible_custom_ode` | `smoke_tested` | `passed` | `not_assessed` | `implementation_only` |
| Recurrent decision-network model | `not_assessed` | `not_implemented` | `not_run` | `not_assessed` | `not_attempted` |
| Morris-Lecar excitable-membrane model | `native` | `smoke_tested` | `passed` | `qualitative_match` | `implementation_only` |
| Adaptive exponential integrate-and-fire model | `native` | `smoke_tested` | `passed` | `qualitative_match` | `implementation_only` |
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

兼容性是可行性分类，不是运行证据。通过的冒烟测试支持 `implementation_only`，但不构成对论文结果的复现。

## 筛选清单

- `bibliography_verified`: **5**
- `candidate`: **252**
- `excluded`: **1**
- `promoted`: **20**

清单中每个请求行都有且仅有一个当前筛选结论。`candidate` 表示该行已通过标题级范围筛选，但仍缺少来源级证据。

## 证据状态定义

- `bibliography_verified`：出版物身份已核实，但方程证据未核实。
- `equation_located`：已查验合法的直接来源并记录精确定位器；不声称已完成转录。
- `equation_transcribed`：来源方程已转录并登记，但复核待完成。
- `second_pass_checked`：维护者工作流完成了第二遍检查。
- `independently_checked`：由独立检查者按照冻结源协议完成检查并解决分歧。
- 参数完整性、实现、数值测试、参考行为与论文结果复现仍是相互独立的状态维度。

## 规范数据与生成视图

唯一手工维护的模型目录是 [models/model_catalog.csv](models/model_catalog.csv)。[JSON](models/model_catalog.json)、[YAML](models/model_catalog.yaml)、英文版 README、本中文版 README、[方程索引](equations/README.md)以及书目视图均由 `python scripts/build_tables.py` 生成，请勿手工编辑。

每一条展示的方程都在 [data/equations/equation_audit.csv](data/equations/equation_audit.csv) 中有对应审计行。完整筛选范围跟踪于 [references/model_screening_master.csv](references/model_screening_master.csv)，行级请求快照见 [references/model_screening_inventory.csv](references/model_screening_inventory.csv)。

## 证据与版权边界

方程页面要求合法来源、精确定位器、转录类型与审计行。仓库只保存原创解释性文字和简明引用数学式；不分发论文 PDF、出版商图表、复制表格、补充材料、许可不明第三方代码或未授权数据。论文获取状态与代码许可状态分别记录。

## 导航

- [方程索引](equations/README.md)
- [方程整理协议](docs/equation_curation_protocol.zh-CN.md)
- [证据状态迁移](docs/evidence_status_migration.md)
- [独立复核协议](docs/independent_review_protocol.md)
- [方程记法政策](docs/equation_notation_policy.md)
- [模型范围分类学](docs/model_scope_taxonomy.zh-CN.md)
- [细胞类型页面](docs/cell_types/README.md)
- [研究空白与下一步证据目标](docs/research_gaps.zh-CN.md)
- [筛选主表](references/model_screening_master.csv)
- [数据字典](docs/data_dictionary.zh-CN.md)
- [贡献指南](docs/CONTRIBUTING.zh-CN.md)

未提供中文版的文档链接指向英文原文。

## 规范目录覆盖

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

神经元-微胶质细胞模型、显式少突胶质细胞-髓鞘网络、施万细胞模型、神经血管多细胞模型及其他细胞类别仍属于受证据门控的筛选条目，除非出现来源级规范记录另有说明。

## 许可与免责声明

- 原创代码：Apache-2.0，见 [LICENSE-CODE](LICENSE-CODE)。
- 原创文档、表格与解释文字：CC BY 4.0，见 [LICENSE-DOCS](LICENSE-DOCS)。
- 第三方素材不重新授权，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
- 本仓库是文献导航与教育资源，见 [DISCLAIMER.md](DISCLAIMER.md)。

最后核验：2026-08-28。
