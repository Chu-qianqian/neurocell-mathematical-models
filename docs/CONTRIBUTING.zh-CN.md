# 贡献指南

[English](CONTRIBUTING.md) | 简体中文

请通过分支和拉取请求提交变更。不要添加论文 PDF、出版商图表、补充材料，或没有明确可复用许可的外部代码。原创代码采用 Apache-2.0；原创文档和策展人创建的表格采用 CC BY 4.0。

新的模型记录需要一手持久标识符、目标细胞类型、数学形式、模型分类、支持该分类的证据，以及相互分开的书目/方程/实现状态。当信息不足时，请将来源添加到 `references/model_screening_master.csv`，而不是直接晋升到核心目录。

提交前请运行：

```text
python scripts/validate_catalogue.py
python scripts/build_tables.py
python scripts/build_tables.py
python scripts/validate_references.py
python scripts/validate_equations.py
python scripts/validate_links.py
python scripts/validate_language.py
python -m unittest discover -s tests -v
git diff --check
```

只有可审计的来源、方程定位器、变量/参数和许可信息才能升级记录的证据状态。请用自己的话总结来源，引用原始论文，并显式保留不确定性。数值测试、参考行为和论文结果复现必须作为相互独立的结论记录。
