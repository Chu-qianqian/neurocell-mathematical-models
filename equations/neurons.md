# 神经元：概念性方程地图

## Conductance-based membrane balance

常见机制性膜模型可写成概念形式：

$$C_m\frac{dV}{dt}=I_{\mathrm{ext}}-\sum_k \bar g_k a_k(V,t)(V-E_k).$$

其中 $V$ 为膜电位，$C_m$ 为膜电容，$I_{\mathrm{ext}}$ 为外加电流，$\bar g_k$ 与 $E_k$ 分别为第 $k$ 类通道的最大电导与反转电位，$a_k$ 表示门控变量的组合。门控变量常按一阶动力学演化：

$$\frac{dx}{dt}=\alpha_x(V)(1-x)-\beta_x(V)x.$$

这说明 Hodgkin–Huxley 家族的核心是电流平衡和通道状态，而不是完整细胞形态、代谢或网络功能。具体通道、速率函数、参数与单位必须以原文为准。

## 低维放电模型

低成本神经元模型常把动力学概括为快变量 $v$ 与慢/恢复变量 $u$：

$$\frac{dv}{dt}=F(v,u)+I,\qquad \frac{du}{dt}=G(v,u).$$

阈值与重置规则可描述放电事件。FitzHugh–Nagumo、Morris–Lecar、Hindmarsh–Rose、Izhikevich 和 AdEx 在 $F$、$G$、变量数量、重置规则及生物解释上不同。它们适合比较放电现象与计算成本，但不能仅凭低维形式推出离子通道或细胞形态细节。
