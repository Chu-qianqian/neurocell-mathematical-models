# 神经系统细胞数学模型图谱

> 一个以中文为主、可追溯且版权合规的神经元与神经胶质细胞数学/计算模型导航库。

本项目整理**能够由明确数学形式表示**的神经系统细胞模型及其来源。它不是论文全文镜像、不是第三方代码集合，也不把“提及某细胞”误作“建立该细胞模型”。模型名、变量名与原始论文标题保留英文，以便与原始来源对应。

## 项目目的

- 将模型的细胞范围、数学形式、生物学功能、证据层级和可复现状态分开记录；
- 为后续的方程逐条核验、参数提取和原创最小实现提供稳定数据接口；
- 明确区分细胞本体模型、单一功能模型、细胞群体模型、跨细胞耦合模型及仅参数化表示；
- 不上传受版权保护的论文 PDF、图表、补充材料或许可证不明的第三方代码。

## 当前核心版本

目前已纳入 **6 条书目信息已核验的种子记录**：神经元 2、星形胶质细胞 1、神经元—星形胶质耦合 1、小胶质细胞 1、少突胶质细胞 1。它们的 DOI、作者、年份与期刊均已对照 Crossref；但方程逐项核验、参数转录、外部代码许可证评估和可执行复现尚未完成，均不会被提前声称为完成。

| Cell type | Model | Mathematical form | Function simulated | Original paper | Code | License | Reproducibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Neuron | Hodgkin-Huxley conductance model | ODE / conductance-based | 膜兴奋性与动作电位 | [Hodgkin & Huxley (1952)](https://doi.org/10.1113/jphysiol.1952.sp004764) | 未评估 | 未评估 | 仅书目核验 |
| Neuron | Izhikevich simple spiking-neuron model | ODE | 放电动力学 | [Izhikevich (2003)](https://doi.org/10.1109/tnn.2003.820440) | 未评估 | 未评估 | 仅书目核验 |
| Astrocyte | G-ChI model | ODE | 谷氨酸调控的 Ca²⁺/IP3 动力学 | [De Pittà et al. (2009)](https://doi.org/10.1007/s10867-009-9155-y) | 未评估 | 未评估 | 仅书目核验 |
| Mixed neuron–glia | Functional neuron-astrocyte calcium-network model | ODE | 神经元—星形胶质 Ca²⁺ 信号 | [Postnov et al. (2009)](https://doi.org/10.1007/s10867-009-9156-x) | 未评估 | 未评估 | 仅书目核验 |
| Microglia | Ischemic-penumbra dynamics model | ODE | 缺血半暗带中的细胞动力学 | [Amato & Arnold (2025)](https://doi.org/10.1016/j.mbs.2025.109549) | 未评估 | 未评估 | 仅书目核验 |
| Oligodendrocyte | Differentiation dynamics model | ODE | 少突胶质细胞分化 | [Nikolov et al. (2022)](https://doi.org/10.3390/math10162928) | 未评估 | 未评估 | 仅书目核验 |

完整的机器可读种子目录在 [data/models/catalogue.csv](data/models/catalogue.csv)；与提示词兼容的扩展目录在 [models/model_catalog.csv](models/model_catalog.csv)。候选文献不会自动进入核心模型总表，见 [references/screening_candidates.csv](references/screening_candidates.csv)。

## 收录与不收录标准

**收录门槛**：稳定来源可定位；文献明确提出或使用细胞相关的数学/计算模型；数学形式能分类；并且书目、方程、实现与许可证状态分开标记。

**不收录为模型记录**：无模型的实验论文、仅有综述结论的条目、无法定位来源的说法、只把髓鞘或胶质细胞当作未说明参数的模型、以及许可证不明而被复制的第三方代码。尚未核验方程的文献只进入候选筛选队列。

## 导航

- [总体范围与分类](docs/overview.md)
- [方法学与证据分层](docs/methodology.md)
- [比较矩阵](docs/comparison_matrix.md)
- [研究空白](docs/research_gaps.md)
- [细胞类型页面](docs/cell_types/README.md)
- [方程阅读入口](equations/README.md)
- [检索策略](references/search_strategy.md)
- [字段词典](docs/data_dictionary.md)
- [贡献指南](docs/CONTRIBUTING.md)

## 模型分类

分类标签覆盖数学形式（ODE、PDE、SDE、reaction-diffusion、conductance-based、agent-based、hybrid 等）、生物尺度（分子至系统级）和功能（电活动、钙信号、炎症、髓鞘形成、血流调节等）。每条记录还要求区分：`cell_intrinsic`、`cell_function`、`cell_population`、`coupled_multicellular` 或 `indirect_parameterization`。这些是策展分类，不替代原作者的表述。

## 文献质量与核验层级

`A`、`B`、`C`、`D` 分别表示基础/经典、重要应用、耦合或扩展、探索性来源；它们不等同于期刊影响因子或固定引用次数。实际的证据状态使用 `verified`、`partially verified`、`not verified`、`full text unavailable`、`license unclear`、`code unavailable` 和 `parameters incomplete`。当前种子记录均为**书目信息 verified、方程 not verified**。

## 如何引用与贡献

请同时引用本仓库版本和原始论文；仓库元数据见 [CITATION.cff](CITATION.cff)。贡献前请阅读 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)，并提供可定位的原始来源、核验说明以及代码许可证信息。

## 许可证与免责声明

- 原创代码：Apache-2.0，见 [LICENSE-CODE](LICENSE-CODE)。
- 原创文档、表格和解释：CC BY 4.0，见 [LICENSE-DOCS](LICENSE-DOCS)。
- 第三方材料不被重新授权，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
- 本项目只做文献导航和教育性总结；请阅读 [DISCLAIMER.md](DISCLAIMER.md)。

最近更新：2026-07-22（核心版；详见每条记录的 `last_verified`）。
