# 模型范围分类学

[English](model_scope_taxonomy.md) | 简体中文

| 范围 | 含义 |
| --- | --- |
| `cell_intrinsic` | 单个细胞或同质区室的状态模型。 |
| `cell_function` | 细胞相关机制，如兴奋性、钙调控或分化。 |
| `cell_population` | 细胞状态丰度或群体动力学模型。 |
| `coupled_multicellular` | 耦合两类或多类细胞、或多个空间区室的系统。 |
| `indirect_parameterization` | 某细胞类型仅通过拟合或强加参数出现的模型。 |

细胞标签描述的是来源范围，并不声称该类别的所有细胞都共享该模型。

谨慎分类的示例：

- 神经元-星形胶质细胞网络属于 `coupled_multicellular`。
- 群体层面的微胶质细胞模型属于 `cell_population`。
- 有髓轴突模型属于 `indirect_parameterization`，除非它包含显式的少突胶质细胞或施万细胞状态变量。
- 理论性联想记忆或神经元网络模型即使没有直接实验验证，也可以是形式化数学模型。
- 模拟器、数据库或实验系统本身不是数学模型。

## 正交的受控分类

`model_scope` 不能替代规范模式中的受控字段：

- `biological_cell_scope` 区分神经元、胶质、混合神经元-胶质、神经群体、突触及其他神经系统相关记录。
- `model_scale` 区分分子、亚细胞、单细胞、多室、成对、微回路、群体、神经质量、神经场、大规模网络和全脑尺度。
- `mathematical_form` 区分 ODE、PDE、随机、差分方程、事件驱动、基于智能体、概率、混合及其他形式。
- `interaction_scope` 与 `network_type` 描述耦合关系，不与空间边界条件混为一谈。
- `spatial_structure`、`stochasticity` 与 `plasticity_scope` 描述相互独立的模型属性。

一个来源可以与本库相关而同时不是神经元或胶质细胞模型。例如，Morris-Lecar 被归类为神经元相关的可兴奋膜模型，Li-Rinzel 被归类为星形胶质细胞相关的钙机制模型，而不是被重新标记为特定来源的哺乳动物神经元模型或完整星形胶质细胞模型。
