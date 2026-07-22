# 检索策略与筛选协议

**协议版本：** 0.2

**种子检索日期：** 2026-07-22

**目的：** 识别神经系统细胞的数学/计算模型；该核心版不是已完成的系统综述或临床证据综合。

## 数据库与使用顺序

1. Crossref：核对 DOI、题名、作者、年份和期刊；
2. PubMed / Europe PMC：发现生物医学原始文献与可合法阅读的全文；
3. OpenAlex / Semantic Scholar：辅助发现引用链，动态指标必须标注来源和日期；
4. ModelDB、BioModels、Open Source Brain 与 GitHub：只用于寻找模型/代码位置，外部代码需另行核验许可证；
5. bioRxiv、medRxiv、arXiv：补充预印本，不替代同行评议证据。

## 概念组与查询模板

每个数据库保存完整查询式、日期、结果数、去重规则、筛选决定与永久链接。基础模板为：

```text
(cell-type synonym) AND ("mathematical model" OR "computational model"
OR "differential equation" OR ODE OR PDE OR stochastic)
AND (process synonym)
```

| 范围 | 优先查询示例 |
| --- | --- |
| Neuron | `(neuron OR neuronal) AND ("mathematical model" OR ODE OR "conductance-based")` |
| Astrocyte | `(astrocyte OR astroglia) AND (calcium OR Ca2+ OR IP3) AND (model OR equations)` |
| Microglia | `(microglia OR microglial) AND (activation OR inflammation OR chemotaxis) AND (model OR ODE OR PDE)` |
| Oligodendrocyte / OPC | `(oligodendrocyte OR OPC OR NG2) AND (differentiation OR myelination OR migration) AND (model OR equations)` |
| Schwann cell | `("Schwann cell") AND (myelination OR regeneration OR "Wallerian degeneration") AND (model OR simulation)` |
| Neurovascular cells | `(pericyte OR "brain endothelial" OR "neurovascular unit") AND (model OR equations)` |

## 筛选规则

1. 先按 DOI、规范化题名和年份去重；
2. 标题/摘要初筛剔除明显无数学模型的论文；
3. 书目以 Crossref、PubMed 或出版社页核对；
4. 只有在可合法检查的正文、方法、补充材料、模型数据库或代码中确证方程/算法存在时，才升级方程证据；
5. 模型实现和许可证核查是独立步骤；“公开网页”不等于可复用代码；
6. 无法确认时保留 `not verified`、`full text unavailable`、`license unclear` 或 `parameters incomplete`，不凭猜测填补。

## 当前种子轮的边界

当前轮仅完成 6 条核心记录的 Crossref 书目核对，并为 5 个经典候选建立了筛选队列。它没有进行多数据库穷尽检索，也未报告 PRISMA 计数；任何“覆盖全面”的陈述均应等后续正式检索日志完成后再作出。
