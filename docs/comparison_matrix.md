# 核心记录比较矩阵

| 模型 | 细胞归属 | 数学形式 | 功能 | 模型归类 | 方程状态 | 适合的后续平台 |
| --- | --- | --- | --- | --- | --- |
| Hodgkin-Huxley | neuron | ODE / conductance-based | 兴奋性、传导 | `cell_function` | 未提取 | NEURON、Brian2、Python |
| Izhikevich | neuron | ODE | 放电模式 | `cell_function` | 未提取 | Brian2、NEST、Python |
| G-ChI | astrocyte | ODE | 谷氨酸调控的 Ca²⁺/IP3 | `cell_function` | 未提取 | Python、MATLAB、Julia |
| Postnov et al. | neuron + astrocyte | ODE | 跨细胞 Ca²⁺ 信号 | `coupled_multicellular` | 未提取 | Python、MATLAB、Julia |
| Amato & Arnold | microglia | ODE | 缺血半暗带群体动力学 | `cell_population` | 未提取 | Python、MATLAB、Julia |
| Nikolov et al. | oligodendrocyte | ODE | 分化动力学 | `cell_function` | 未提取 | Python、MATLAB、Julia |

“适合的平台”只依据模型的公开数学形式类别给出技术建议，不表示该论文存在相应软件实现，更不表示已完成复现。
