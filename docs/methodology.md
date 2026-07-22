# 方法学与证据规则

## 检索设计

核心检索使用细胞类型同义词与 `mathematical model`、`computational model`、`differential equation`、`calcium dynamics`、`myelination`、`inflammation`、`neurovascular coupling` 等术语组合。目标来源包括 PubMed、Europe PMC、Crossref、OpenAlex、Semantic Scholar、ModelDB、BioModels 与有明确许可证的代码仓库。

每次正式检索须保存：数据库、完整查询式、检索日期、返回数、去重规则、标题/摘要/全文筛选数以及排除原因。现阶段的 Crossref 定向检索只用于确认少量候选的书目元数据；它不是覆盖全部数据库的系统检索，故不报告 PRISMA 数量。

## 证据状态

| 字段 | 可以声明的内容 | 不能声明的内容 |
| --- | --- | --- |
| `verified` | DOI 与题名/作者/年份/期刊已与权威元数据一致 | 方程、参数、代码或生物学验证已完成 |
| `partially verified` | 已检查来源的一部分，例如摘要或元数据 | 正文方程已核验 |
| `not verified` | 尚不能确认 | 任何推断 |
| `full text unavailable` | 未取得可合法检查的全文/方法材料 | 没有方程或模型不存在 |
| `license unclear` | 外部代码许可证未确认 | 可以复制或再分发 |
| `parameters incomplete` | 公开来源未给出足够参数 | 模型不可用或无效 |

## 方程提取门槛

在模型行标记为 `extracted` 前，需记录：来源页码/章节/公式编号、状态变量、参数与单位、输入输出、初始/边界条件、求解方式、假设、适用范围和局限性。第二位审阅者或可复现脚本应再检查符号与维度。仓库中的概念性 LaTeX 式仅用于说明模型家族，不替代原文转录。

## 质量分层

- **A**：原始或经典模型来源；
- **B**：有较强应用/验证证据的模型；
- **C**：在既有模型上加入耦合、空间、随机性或疾病机制；
- **D**：探索性、预印本或参数/验证不足的来源。

该分层不使用伪造的影响因子或固定引用次数。若将来加入动态引用指标，必须记录来源和查询日期。
