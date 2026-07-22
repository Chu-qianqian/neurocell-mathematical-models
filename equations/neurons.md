# Neurons: conceptual equation map

## Conductance-based membrane balance

A common mechanistic membrane model has the conceptual form:

$$C_m\frac{dV}{dt}=I_{\mathrm{ext}}-\sum_k \bar g_k a_k(V,t)(V-E_k).$$

Here $V$ is membrane potential, $C_m$ is membrane capacitance, $I_{\mathrm{ext}}$ is external current, and $\bar g_k$ and $E_k$ are the maximal conductance and reversal potential of channel class $k$. The factor $a_k$ represents a combination of gating variables. A gating variable often follows first-order dynamics:

$$\frac{dx}{dt}=\alpha_x(V)(1-x)-\beta_x(V)x.$$

This captures the central idea of the Hodgkin–Huxley family—current balance and channel states—not complete cellular morphology, metabolism, or network function. Specific channels, rate functions, parameters, and units must be checked in the original source.

## Low-dimensional spiking models

Low-cost neuron models often abstract dynamics into a fast variable $v$ and a slow/recovery variable $u$:

$$\frac{dv}{dt}=F(v,u)+I,\qquad \frac{du}{dt}=G(v,u).$$

Threshold and reset rules can represent spike events. FitzHugh–Nagumo, Morris–Lecar, Hindmarsh–Rose, Izhikevich, and AdEx differ in $F$, $G$, variable count, reset rules, and biological interpretation. They support comparisons of spiking phenomena and computational cost, but low-dimensional form alone does not establish ion-channel or morphological detail.
