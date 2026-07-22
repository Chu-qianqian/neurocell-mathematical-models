# 贡献指南

请通过分支和 Pull Request 提交更改。不得添加论文 PDF、出版社图表、补充材料或无明确可复用许可证的外部代码。

新增模型记录需提供：原始持久标识符、目标细胞、数学形式、模型归类、分类依据，以及书目/方程/实现三种独立状态。若信息不足，请先加入 `references/screening_candidates.csv`，不要把候选直接升级为核心记录。

提交前运行：

```text
python scripts/validate_catalogue.py
python scripts/build_tables.py
python scripts/validate_references.py
python scripts/validate_links.py
```

只有在来源、公式位置、变量/参数与许可证均可审计时，才可把记录升级为更高证据状态。请用自己的语言总结原文，引用原始论文，并明确任何不确定性。
