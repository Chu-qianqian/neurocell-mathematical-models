# Morris-Lecar excitable-membrane model

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: PMC scanned-page full text (PMC1327511), journal pages 193-213.
- Source locator: Methods, The Model, equations (1)-(2); Analysis, equations (3)-(7); Ca-accumulation perturbation, equation (8); Limit-cycle oscillations, unnumbered reduced system and equations (9)-(17).
- Transcription status: exact source transcription.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-25.

## Scope

- Biological cell scope: `other_nervous_system_related`.
- Cell type: `excitable_membrane`.
- Cell subtype: space-clamped patch of barnacle (*Balanus nubilus*) giant muscle fiber sarcolemma with EGTA-perfused interior.
- Nervous-system region: `not_assessed`.
- Model scope: `cell_function`.
- Model scale: `single_cell`.
- Mathematical form: `ordinary_differential_equation` (two- or three-dimensional conductance-based system; deterministic).
- Interaction scope: `external_input`.
- Network type: `not_applicable`.
- Spatial structure: `nonspatial` (space-clamped membrane patch; a two-patch cleft variant is discussed but not part of the core model).
- Stochasticity: `deterministic`.
- Plasticity scope: `none`.

## Source citation

C. Morris; H. Lecar. Voltage oscillations in the barnacle giant muscle fiber. *Biophysical Journal* **35**(1), 193-213 (1981). [DOI](https://doi.org/10.1016/s0006-3495(81)84782-0). [PubMed](https://pubmed.ncbi.nlm.nih.gov/7260316/). [PMC scanned full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC1327511/).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $V$ | membrane potential | mV | source-verified |
| $I$ | applied current density | $\mu A/cm^2$ | source-verified |
| $I_L$, $I_{Ca}$, $I_K$ | leak, calcium, and potassium current densities | $\mu A/cm^2$ | source-verified |
| $M$ | fraction of open Ca$^{++}$ channels | dimensionless | source-verified |
| $N$ | fraction of open K$^+$ channels | dimensionless | source-verified |
| $M_\infty(V)$, $N_\infty(V)$ | steady-state open fractions of Ca$^{++}$ and K$^+$ channels | dimensionless | source-verified |
| $\lambda_M(V)$, $\lambda_N(V)$ | voltage-dependent opening rate constants | 1/s | source-verified |
| $\mu$ | generic gating variable ($M$ or $N$) in the single-conductance system | dimensionless | source-verified |
| $V_i$ | equilibrium potential for conductance $i$ ($V_L$, $V_{Ca}$, or $V_K$) | mV | source-verified |
| $R$ | nonlinear calcium driving-force function | mV | source-verified |
| $[Ca^{++}]_i$, $[Ca^{++}]_o$ | internal and external Ca$^{++}$ concentrations | mM | source-verified |
| $f_1(V,N)$, $f_2(V,N)$ | vector field of the reduced $V$,$N$ system | mV/ms, 1/ms | source-verified |
| $V_s$, $N_s$ | singular-point coordinates of the reduced system | mV, dimensionless | source-verified |
| $V_{min}$, $V_{max}$ | bounding voltages of the trapping rectangle | mV | source-verified |
| $p$ | eigenvalue of the system linearized about the singular point | 1/ms | source-verified |
| $\bar{g}$ | equivalent conductance at the operating point, $g_L + g_K N + g_{Ca} M$ | mmho/cm$^2$ | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $C$ | membrane capacitance | $\mu F/cm^2$ | 20 | List of abbreviations; Figure 2, 6, 9, and 11 captions |
| $g_L$ | leak conductance | mmho/cm$^2$ | 2 (Figures 6, 9, 11); 3 (Figure 2, Ca$^{++}$-free condition) | Figure captions |
| $g_{Ca}$ | calcium conductance | mmho/cm$^2$ | 4 (Figures 6 solid, 9, 11); 0 in Ca$^{++}$-free condition | Figure captions |
| $g_K$ | potassium conductance | mmho/cm$^2$ | 8 (Figures 6 solid, 9, 11); 12 (Figure 6 broken line) | Figure captions |
| $\hat{g}_{Ca}$ | conductance constant for the nonlinear $I_{Ca}$ | mmho/cm$^2$ | not stated | List of abbreviations; equation (6) |
| $V_L$ | leak equilibrium potential | mV | $-50$ | Figure captions |
| $V_{Ca}$ | calcium equilibrium potential | mV | 100 | Figure captions |
| $V_K$ | potassium equilibrium potential | mV | $-70$ | Figure captions |
| $V_1$ | potential of $M_\infty = 0.5$ | mV | 0 (Figure 6); 10 (Figure 9); $-1$ (Figure 11) | Figure captions |
| $V_2$ | reciprocal slope of $M_\infty$ voltage dependence | mV | 15 | Figure captions |
| $V_3$ | potential of $N_\infty = 0.5$ | mV | 10 (Figures 6, 11); $-1$ (Figures 2, 9) | Figure captions |
| $V_4$ | reciprocal slope of $N_\infty$ voltage dependence | mV | 10 (Figure 6); 14.5 (Figures 2, 9, 11) | Figure captions |
| $\bar{\lambda}_M$ | maximum Ca$^{++}$-channel opening rate | 1/s | 1.0 (Figure 6 solid); 6 (Figure 6 broken line); 0.1 (Figures 9, 11) | Figure captions |
| $\bar{\lambda}_N$ | maximum K$^+$-channel opening rate | 1/s | 0.1 (Figure 6); 1/15 (Figures 2, 9, 11) | Figure captions |
| $K$ | accumulation-layer constant for intracellular Ca$^{++}$ | cm$^{-1}$ | chosen for a 1 $\mu$m accumulating compartment; numeric value not stated | text after equation (8); List of abbreviations |
| $F$ | Faraday constant | C/mol | standard physical constant | List of abbreviations continuation |
| 12.5 | voltage scale in the electrodiffusion driving force | mV | 12.5 | equation (7) |

## Equations

These are exact source transcriptions of the scanned pages. Numbering follows the published article; unnumbered displays are identified by section.

Membrane behavior of the equivalent circuit (Fig. 1) with two noninactivating conductances. The leak term is transcribed exactly as printed; see the interpretation for a note on this line:

$$
\begin{aligned}
I &= C \dot{V} + g_L(V_L) + g_{Ca} M(V - V_{Ca}) + g_K N(V - V_K)\\
\dot{M} &= \lambda_M(V)\left[M_\infty(V) - M\right]\\
\dot{N} &= \lambda_N(V)\left[N_\infty(V) - N\right],
\end{aligned}
$$

Sigmoid steady states and bell-shaped rate constants of the two conductances:

$$
\begin{aligned}
M_\infty(V) &= 1/2\left\{1 + \tanh\left[(V - V_1)/V_2\right]\right\}\\
\lambda_M(V) &= \bar{\lambda}_M \cosh\left[(V - V_1)/2V_2\right]\\
N_\infty(V) &= 1/2\left\{1 + \tanh\left[(V - V_3)/V_4\right]\right\}\\
\lambda_N(V) &= \bar{\lambda}_N \cosh\left[(V - V_3)/2V_4\right],
\end{aligned}
$$

Generalized single-conductance system ($\mu$ is $M$ or $N$; subscript $i$ is Ca or K):

$$
\begin{aligned}
I &= C \dot{V} + g_L(V - V_L) + g_i \mu(V - V_i)\\
\dot{\mu} &= \lambda(V)\left[\mu_\infty(V) - \mu\right],
\end{aligned}
$$

Nullclines of the single-conductance system:

$$
\begin{aligned}
(\dot{V} = 0 \text{ nullcline})\quad V(\mu) &= (I + g_L V_L + g_i \mu V_i)/(g_L + g_i \mu),\\
(\mu = 0 \text{ nullcline})\quad \mu(V) &= \mu_\infty(V),
\end{aligned}
$$

Extreme values of the $\dot{V} = 0$ nullcline:

$$
V(0) = (I + g_L V_L)/g_L, \qquad V(1) = (I + g_L V_L + g_i V_i)/(g_L + g_i),
$$

Nonlinear instantaneous calcium current with a concentration-dependent driving force:

$$
I_{Ca} = -\hat{g}_{Ca} M R(V, [Ca^{++}]_i, [Ca^{++}]_o),
$$

Electrodiffusion form of the driving-force function:

$$
R(V, [Ca^{++}]_i, [Ca^{++}]_o) = \frac{V\left\{1 - ([Ca^{++}]_i/[Ca^{++}]_o)\exp\left(V/12.5\right)\right\}}{\left\{1 - \exp\left(V/12.5\right)\right\}},
$$

Calcium-accumulation perturbation of the all-Ca$^{++}$ system (steady-state $M_\infty$ substituted for $M(t)$):

$$
\begin{aligned}
\frac{dV}{dt} &= C^{-1}\left\{I - g_L(V - V_L) + \hat{g}_{Ca} M_\infty(V) V R(V, [Ca^{++}]_i, [Ca^{++}]_o)\right\},\\
\frac{d[Ca^{++}]_i}{dt} &\simeq K\left\{(CF)^{-1}\hat{g}_{Ca} M_\infty(V) V R(V, [Ca^{++}]_i, [Ca^{++}]_o)\right\},
\end{aligned}
$$

Reduced $V$,$N$ system with instantaneous calcium activation ($M = M_\infty(V)$), following the terminology of FitzHugh (1969):

$$
\begin{aligned}
I &= C \frac{dV}{dt} + g_L(V - V_L) + g_{Ca} M_\infty(V)(V - V_{Ca}) + g_K N(V - V_K),\\
\frac{dN}{dt} &= \lambda_N(V)\left(N_\infty(V) - N\right),
\end{aligned}
$$

Bounding rectangle of the reduced system in the $V$,$N$ phase plane:

$$
V_{min} = \frac{g_L V_L + g_K V_K + I}{g_L + g_K} < V < \frac{g_L V_L + g_{Ca} V_{Ca} + I}{g_L + g_{Ca}} = V_{max},
$$

Singular point of the reduced system (the leak term is transcribed exactly as printed; see the interpretation):

$$
N_s = N_\infty(V_s) = \frac{I - g_L(V_s - V_K) - g_{Ca} M_\infty(V_s)(V_s - V_{Ca})}{g_K(V_s - V_K)},
$$

General second-order form of the reduced system and the characteristic equation of its linearization about $S$:

$$
\dot{V} = f_1(V, N), \qquad \dot{N} = f_2(V, N),
$$

$$
p^2 - \left(\frac{\partial f_1}{\partial V} + \frac{\partial f_2}{\partial N}\right)_s p + \left(\frac{\partial f_1}{\partial V}\frac{\partial f_2}{\partial N} - \frac{\partial f_2}{\partial V}\frac{\partial f_1}{\partial N}\right)_s = 0,
$$

Necessary condition for an unstable singular point (both roots positive or with positive real part):

$$
\begin{aligned}
\left(\frac{\partial f_1}{\partial V} + \frac{\partial f_2}{\partial N}\right)_s &> 0\\
\left(\frac{\partial f_1}{\partial V}\frac{\partial f_2}{\partial N} - \frac{\partial f_2}{\partial V}\frac{\partial f_1}{\partial N}\right)_s &> 0,
\end{aligned}
$$

Explicit conductance inequalities for a stable limit cycle, obtained by substituting the partial derivatives of the reduced system:

$$
\begin{aligned}
g_{Ca}\left(\frac{\partial M_\infty}{\partial V}\right)_s(V_{Ca} - V_s) &> g_L + g_K N_s + g_{Ca} M_\infty(V_s) + C\lambda_N(V_s),\\
g_{Ca}\left(\frac{\partial M_\infty}{\partial V}\right)_s(V_{Ca} - V_s) &< g_L + g_K N_s + g_{Ca} M_\infty(V_s) + g_K\left(\frac{\partial N_\infty}{\partial V}\right)_s(V_s - V_K),
\end{aligned}
$$

The same inequalities rewritten with the equivalent conductance $\bar{g} = g_L + g_K N + g_{Ca} M$:

$$
(\bar{g} + C\lambda_N)_s < \left[g_{Ca}\frac{\partial M_\infty}{\partial V}(V_{Ca} - V)\right]_s < \left[\bar{g} + g_K\frac{\partial N_\infty}{\partial V}(V - V_K)\right]_s,
$$

Condition for complex roots (damped oscillatory transients about a stable focus):

$$
\left(\frac{\partial f_1}{\partial V} + \frac{\partial f_2}{\partial N}\right)_s^2 - 4\left(\frac{\partial f_1}{\partial V}\frac{\partial f_2}{\partial N} - \frac{\partial f_2}{\partial V}\frac{\partial f_1}{\partial N}\right)_s < 0,
$$

## Term-by-term interpretation

Equation (1) is the current balance of the space-clamped membrane patch plus first-order gating kinetics for the two noninactivating conductances; the leak term is printed as $g_L(V_L)$, which is dimensionally inconsistent with the parallel $g(V - V_{eq})$ form of the Ca$^{++}$ and K$^+$ terms, and equation (3) of the same paper writes the leak correctly as $g_L(V - V_L)$, so the printed equation (1) is flagged as an apparent typographical slip for $g_L(V - V_L)$; the transcription reproduces the source exactly. Equation (2) fixes both conductances to two parameters each: a sigmoid steady state set by $(V_1, V_2)$ or $(V_3, V_4)$ and a voltage-dependent opening rate that peaks ($\bar{\lambda}$) at the half-activation voltage because of the cosh form. Equations (3)-(5) analyze each conductance in isolation: the $\dot{V} = 0$ nullcline is bilinear in $\mu$, spanning $V(0)$ (no active conductance) to $V(1)$ (fully activated); when $V_i < V_L$ (all-K$^+$) only one singular point exists, whereas $V_i > V_L$ (all-Ca$^{++}$) permits three, which underlies plateau bistability. Equations (6)-(7) replace the linear calcium driving force by an electrodiffusion (Goldman-type) expression $R$ with a 12.5 mV voltage scale, improving the fit of the all-Ca$^{++}$ plateau. Equation (8) appends a slow intracellular Ca$^{++}$ accumulation variable (compartment thickness 1 $\mu$m, constant $K$, Faraday constant $F$) whose buildup lowers $\hat{g}_{Ca}$ effectively and terminates the plateau, modelling repolarization. The reduced $V$,$N$ system sets $M = M_\infty(V)$ instantaneously, justified by Tikhonov's theorem since Ca$^{++}$ activation is much faster than K$^+$ activation; equation (10) gives the trapping rectangle, equation (11) the unique singular point (its numerator leak term is printed as $V_K$ where $V_L$ is required by the current balance; another apparent typographical slip, transcribed exactly), and equations (12)-(14) the Poincare-Bendixson argument: an unstable singular point inside the rectangle yields a stable limit cycle. Equations (15)-(16) translate the instability condition into conductance-parameter inequalities: the negative dynamic conductance of the inward Ca$^{++}$ current, $g_{Ca}(\partial M_\infty/\partial V)(V_{Ca} - V)$, must exceed the restorative conductances but stay below their sum plus the K$^+$ reactive term, so oscillation requires a balance between $I_{Ca}$ and $I_K$. Equation (17) is the complex-root (underdamped) condition, interpreted through the equivalent parallel resonant circuit.

## Inputs, outputs, and conditions

- Input: applied current density $I$ (constant steps in the reported experiments and computations).
- Output: membrane potential $V(t)$ and gating trajectories $M(t)$, $N(t)$; damped or sustained voltage oscillations, plateaus, and bistability depending on parameters.
- Initial conditions: `source_example_located`; locator: Figure 2 caption ($V(0) = -50$, $N(0) = N_\infty(-50)$); resting potential taken as $-50$ mV in Figure 6.
- Boundary conditions: `not_applicable`; locator: not_applicable (space-clamped patch, no spatial domain).
- Network conditions: `not_applicable`; locator: not_applicable.
- Event handling: `not_applicable`; locator: not_applicable.
- Numerical method: `source_example_located`; locator: Methods, numerical-integration paragraph (MLAB program, NIH, Knott 1979, Geary-Nordsieck-type algorithm as printed "Geary-Nordseick").
- Stochastic input: `deterministic`.
- Simulation scale: `single_cell`.

## Assumptions and limitations

The model is a space-clamped, two-conductance (plus leak) reduction: gating kinetics are first-order with instantaneous linear instantaneous current-voltage relations except where the nonlinear Ca$^{++}$ driving force is used; no inactivation is included, and slow processes such as Ca$^{++}$ accumulation are treated only as a perturbation system in equation (8). Parameter values were drawn from the voltage-clamp literature and the authors' own data and are deliberately varied rather than fitted; the source notes the extant voltage-clamp data are variable. Two printed equations carry apparent typographical slips (leak term of equation (1); leak subscript of equation (11)), which are transcribed exactly and flagged. The source models barnacle muscle fiber and is used as a neuron-relevant excitable-membrane model, not as a universal mammalian neuron subtype.

## Experimental support

`not assessed`. This status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `smoke_tested`; Brian2 reference implementation in `implementations/brian2/morris_lecar_1981.py`.
- Numerical tests: `passed` (repository unit tests).
- Reference behavior: `qualitative_match` (Type-I excitability with limit-cycle firing in the repository smoke test).
- Reproduction: `implementation_only`; no paper-result reproduction is claimed.
- External code license: `not_assessed`.
