"""Chinese localization resources for generated views.

This module is the single designated home for Simplified Chinese
repository-authored text. Every other repository location remains
English-only per scripts/validate_language.py.
"""

from __future__ import annotations


REVIEW_LABELS_ZH = {
    "independently_checked": "已记录独立复核",
    "second_pass_checked": "维护者第二遍复核",
    "equation_transcribed": "已转录；待复核",
    "equation_located": "已定位来源；待转录",
    "bibliography_verified": "仅书目",
}

MODEL_HEADERS_ZH = (
    "| 模型 ID | 模型 | 生物学范围 | 细胞或网络类型 | 尺度 | 方程状态 | 一手文献 | 方程定位器 | 复核范围 |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
)

IMPL_HEADERS_ZH = (
    "| 模型 | Brian2 兼容性 | 实现 | 数值测试 | 参考行为 | 复现 |",
    "| --- | --- | --- | --- | --- | --- |",
)

EMPTY_TABLE_ZH = "当前没有满足该证据状态的记录。"

SWITCHER_LINE_EN = "English | [简体中文](README.zh-CN.md)"

NAV_SUFFIXES_ZH = {
    "equation_curation_protocol": "[中文](docs/equation_curation_protocol.zh-CN.md)",
    "model_scope_taxonomy": "[中文](docs/model_scope_taxonomy.zh-CN.md)",
    "research_gaps": "[中文](docs/research_gaps.zh-CN.md)",
    "data_dictionary": "[中文](docs/data_dictionary.zh-CN.md)",
    "contributing": "[中文](docs/CONTRIBUTING.zh-CN.md)",
}


def render_zh_readme(
    s: dict,
    coverage: str,
    screening_summary: str,
    generated_notice: str,
    model_table_zh: str,
    implementation_table_zh: str,
    doi_badge: str,
) -> str:
    records = s["records"]
    statuses = s["statuses"]
    latest = s["latest"]
    return f"""<!-- {generated_notice} -->
# 神经细胞数学模型库

[English](README.md) | 简体中文

{doi_badge}

> 一个可溯源、符合版权规范的神经系统细胞数学与计算模型图谱。

本仓库是一个方程级知识库，不是论文镜像，也不收集第三方代码。它将书目核实、方程转录、维护者第二遍复核与真正独立的检查分开管理。在没有确定一手来源的情况下，模型家族的筛选条目永远不会被当作经过来源级验证的模型。

## 覆盖概况

- 规范目录记录：**{len(records)}**
- 仅书目暂存记录：**{statuses["bibliography_verified"]}**
- 方程已定位或更强状态的记录：**{s["equation_located_or_beyond"]}**
- 已转录、待第二遍复核的记录：**{statuses["equation_transcribed"]}**
- 维护者已第二遍复核的记录：**{statuses["second_pass_checked"]}**
- 已独立复核的记录：**{statuses["independently_checked"]}**
- 参数注册表不完整的记录：**{s["parameters_incomplete"]}**
- 明确标注全文不可获取的记录：**{s["full_text_unavailable"]}**
- 来源全文不可获取或尚未查验的记录：**{s["uninspected_full_text"]}**
- 外部代码许可状态不明的记录：**{s["license_unclear"]}**
- 筛选清单行数：**{len(s["screening"])}**（其中 {s["promoted_screening"]} 条已晋升进入规范目录）

## 模型目录

{model_table_zh}

## 方程证据记录

上表保留了每一行的方程证据状态。`second_pass_checked` 始终是维护者层面的复核状态，绝不等同于 `independently_checked`。仅"已定位"的记录不展示转录方程；仅书目的暂存记录不展示重构的来源专属方程。

## 实现与数值验证

{implementation_table_zh}

兼容性是可行性分类，不是运行证据。通过的冒烟测试支持 `implementation_only`，但不构成对论文结果的复现。

## 筛选清单

{screening_summary}

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

{coverage}

神经元-微胶质细胞模型、显式少突胶质细胞-髓鞘网络、施万细胞模型、神经血管多细胞模型及其他细胞类别仍属于受证据门控的筛选条目，除非出现来源级规范记录另有说明。

## 许可与免责声明

- 原创代码：Apache-2.0，见 [LICENSE-CODE](LICENSE-CODE)。
- 原创文档、表格与解释文字：CC BY 4.0，见 [LICENSE-DOCS](LICENSE-DOCS)。
- 第三方素材不重新授权，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
- 本仓库是文献导航与教育资源，见 [DISCLAIMER.md](DISCLAIMER.md)。

最后核验：{latest}。
"""
