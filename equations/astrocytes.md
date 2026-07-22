# Astrocytes: conceptual equation map

An intracellular Ca²⁺ module is often summarised by a flux balance:

$$\frac{dC}{dt}=J_{\mathrm{release}}(C,I,h)-J_{\mathrm{pump}}(C)+J_{\mathrm{leak}}+J_{\mathrm{in}}-J_{\mathrm{out}},$$

where $C$ is cytosolic Ca²⁺, $I$ is IP3, and $h$ is receptor availability or an inactivation gate. A conceptual IP3 balance is:

$$\frac{dI}{dt}=J_{\mathrm{production}}-J_{\mathrm{degradation}}+J_{\mathrm{coupling}}.$$

Production, degradation, receptor release, pump uptake, and intercellular-coupling terms encode different mechanistic assumptions; they must not be read as the complete transcription of any particular paper. Spatial Ca²⁺ waves or IP3 diffusion may add $D\nabla^2 C$ or $D\nabla^2 I$, converting an ODE into a PDE/reaction-diffusion problem.
