# 星形胶质细胞：概念性方程地图

细胞内 Ca²⁺ 模块通常以通量平衡概述：

$$\frac{dC}{dt}=J_{\mathrm{release}}(C,I,h)-J_{\mathrm{pump}}(C)+J_{\mathrm{leak}}+J_{\mathrm{in}}-J_{\mathrm{out}},$$

其中 $C$ 是胞质 Ca²⁺，$I$ 是 IP3，$h$ 是受体可用性或失活门控变量。IP3 的概念性平衡可写为：

$$\frac{dI}{dt}=J_{\mathrm{production}}-J_{\mathrm{degradation}}+J_{\mathrm{coupling}}.$$

生成、降解、受体释放、泵吸收和跨细胞耦合项分别对应不同机制假设；它们不应被误解为任意一篇论文的完整转录。空间 Ca²⁺ 波或 IP3 扩散通常还需加入 $D\nabla^2 C$ 或 $D\nabla^2 I$，从 ODE 转为 PDE/reaction-diffusion 问题。
