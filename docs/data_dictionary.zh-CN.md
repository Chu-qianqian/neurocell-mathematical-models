# 模型目录数据字典

[English](data_dictionary.md) | 简体中文

`models/model_catalog.csv` 是唯一手工维护的模型目录。`models/model_catalog.json`、`models/model_catalog.yaml` 以及 README 中的表格与计数均由 `python scripts/build_tables.py` 生成，不得手工编辑。原 `data/models/catalogue.csv` 子集在内容迁移完成后已删除。

完整的字段契约与受控词表定义于 `models/schema.json`。每一行都要求唯一且稳定的 `model_id`、规范的 DOI URL、被引用的方程页面、显式的证据状态与显式的实现状态。

诸如 `not_verified`、`not_assessed`、`not_run` 以及空的代码位置等取值，刻意保留了不确定性，不得凭推断填写。

重要字段组包括：

- `model_scope`：`cell_intrinsic`、`cell_function`、`cell_population`、`coupled_multicellular` 或 `indirect_parameterization`；
- `biological_cell_scope`、`cell_type`、`nervous_system_region` 与 `model_scale`：受控的生物学与尺度分类，不隐含方程验证结论；
- `mathematical_form`、`interaction_scope`、`network_type`、`spatial_structure`、`stochasticity` 与 `plasticity_scope`：受控的数学形式与相互作用分类；
- `parent_model_id` 和以分号分隔的 `related_model_ids`：来源定义的模型家族与后续扩展之间经过验证的链接；
- `network_conditions_status` 与 `network_conditions_locator`：连接结构、群体规模、拓扑或耦合证据，与空间边界条件分开保存；
- `event_handling_status` 与 `event_handling_locator`：阈值、复位、状态转移或其他事件证据，与连续动力学分开保存；
- `quality_tier`：A-D 证据等级，不是影响因子或固定引用数；
- `evidence_notes` 与 `limitations`：以策展人原创措辞记录验证边界；
- `code_available`、`code_url` 与 `code_license`：只有在逐一审查外部仓库之后才能升级；网页可访问不等于代码可再分发。
- `equation_status`：将仅书目、已定位、已转录、维护者第二遍复核与独立复核的证据状态分开；
- `brian2_compatibility`：可行性分类，不是实现可运行的证据；
- `brian2_implementation_status`、`numerical_test_status`、`reference_behavior_status` 与 `reproduction_status`：把执行证据与参考行为评估、论文结果复现分开。

独立复核的溯源信息按方程记录于 `data/equations/equation_audit.csv`，包括检查者身份与角色、日期、方法、冻结源标识符与版本、访问日期、冻结提交哈希、分歧标记、解决方式及解决日期。

宽泛的请求范围不会混入规范目录，而是单独跟踪于 `references/model_screening_master.csv`；`candidate` 结果表示该行通过了标题级范围筛选，但仍缺少来源级证据。生成的书目视图不构成第二份模型目录。
