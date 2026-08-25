# Recurrent decision-network model

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: PMC open-access full text (PMC6674568) with equation images M1-M35.
- Source locator: Materials and Methods equations (1)-(9), Phase-plane reduction unnumbered displays, Dynamical equations equations (10)-(21), Results unnumbered stimulus displays, Simulations unnumbered noise display, Results equation (22), and Appendix unnumbered system.
- Transcription status: exact source transcription.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-25.

## Scope

- Biological cell scope: `neural_population`.
- Cell type: `neural_population`.
- Cell subtype: choice-selective and nonselective excitatory (pyramidal) populations plus a shared inhibitory (interneuron) population of a cortical decision circuit.
- Nervous-system region: `cerebral_cortex` (lateral intraparietal-like decision populations).
- Model scope: `coupled_multicellular`.
- Model scale: `population`.
- Mathematical form: `stochastic_differential_equation` (rate dynamics driven by an Ornstein-Uhlenbeck noise current); the reduced two-variable core is a deterministic system plus filtered noise.
- Interaction scope: `network_connectivity`.
- Network type: `attractor_network` (winner-take-all competition between two choice-selective populations).
- Spatial structure: `network_topology`.
- Stochasticity: `stochastic`; the deterministic mean-field core receives Ornstein-Uhlenbeck-filtered white noise.
- Plasticity scope: `none`.

## Source citation

Kong-Fatt Wong; Xiao-Jing Wang. A recurrent network mechanism of time integration in perceptual decisions. *Journal of Neuroscience* **26**(4), 1314-1328 (2006). [DOI](https://doi.org/10.1523/jneurosci.3733-05.2006). [PubMed](https://pubmed.ncbi.nlm.nih.gov/16436619/). [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6674568/).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $r_i$ | mean firing rate of excitatory population $i$ ($i$ = 1, 2 selective; 3 nonselective) | Hz | source-verified |
| $r_I$ | mean firing rate of the inhibitory population | Hz | source-verified |
| $I_{syn}$, $I_{syn,i}$ | total synaptic input current to a cell / to population $i$ | nA | source-verified |
| $S_{AMPA,i}$ | AMPA synaptic gating variable of population $i$ | dimensionless | source-verified |
| $S_{NMDA,i}$ ($S_i$) | NMDA synaptic gating variable of population $i$ | dimensionless | source-verified |
| $S_{GABA}$ | GABA synaptic gating variable of the inhibitory population | dimensionless | source-verified |
| $\psi_i$ | steady state of $S_i$ | dimensionless | source-verified |
| $F$ | steady-state rise function of the NMDA gating variable, $F(\psi_i) = \psi_i/(\tau_{NMDA}(1 - \psi_i))$ | 1/ms | source-verified |
| $x_i$ | effective synaptic input to selective population $i$ | nA | source-verified |
| $H$ | effective single-population input-output function | Hz | source-verified |
| $I_i$ | coherence-dependent stimulus input to population $i$ | nA | source-verified |
| $I_{noise,i}$ | Ornstein-Uhlenbeck-filtered noise current into population $i$ | nA | source-verified |
| $\eta_i(t)$ | Gaussian white noise with zero mean and unit variance | dimensionless | source-verified |
| $\Delta S$ | displacement of $S = (S_1, S_2)$ from the saddle steady state | dimensionless | source-verified |
| $v_1$, $v_2$ | eigenvectors of the saddle (tangents of the unstable/stable manifolds) | dimensionless | source-verified |
| $\tau_{stable}$, $\tau_{unstable}$ | positive inverse eigenvalue time constants of the saddle | ms | source-verified |
| $V_{th}$, $V_{reset}$ | spiking threshold and reset voltage of the LIF parent neuron | mV | source-verified |
| $V_{ss}$ | steady-state membrane voltage $V_L + I_{syn}/g_L$ | mV | source-verified |
| $\sigma_V$ | standard deviation of membrane-potential fluctuations | mV | source-verified |
| $\phi(I_{syn})$ | population firing-rate transfer function | Hz | source-verified |
| $c'$ | motion coherence of the random-dot stimulus | % | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $\tau_r$ | population firing-rate relaxation time constant | ms | 2 | Phase-plane reduction, step (3) |
| $\tau_{AMPA}$ | AMPA gating decay time constant | ms | 2 | Appendix parameter list |
| $\tau_{NMDA} = \tau_S$ | NMDA gating decay time constant | ms | 100 | Introduction; Appendix parameter list |
| $\tau_{GABA}$ | GABA gating decay time constant | ms | not stated | equation (7) |
| $\gamma$ | NMDA gating kinetic parameter | dimensionless | 0.641 | after equation (8) |
| $c_E$ | pyramidal-cell F-I gain factor | (V nC)$^{-1}$ | 310 | after equation (2) |
| $g_E$ | pyramidal-cell F-I noise/curvature factor | s | 0.16 | after equation (2) |
| $I_E$ | pyramidal-cell F-I threshold current (rate units) | Hz | 125 | after equation (2) |
| $c_I$ | interneuron F-I gain factor | (V nC)$^{-1}$ | 615 | after equation (2) |
| $g_I$ | interneuron F-I noise/curvature factor | s | 0.087 | after equation (2) |
| $I_I$ | interneuron F-I threshold current (rate units) | Hz | 177 | after equation (2) |
| $g_2$ | slope of the linearized interneuron response | dimensionless | 2 | after equation (9) |
| $r_0$ | intercept of the linearized interneuron response | Hz | 11.5 | after equation (9) |
| $J_{N,11} = J_{N,22}$ | recurrent NMDA self-coupling of a selective population | nA | 0.1561 (standard set); 0.2609 (appendix set) | Parameter values; Appendix |
| $J_{N,12} = J_{N,21}$ | effective NMDA cross-coupling between selective populations | nA | 0.0264 (standard set); 0.0497 (appendix set) | Parameter values; Appendix |
| $J_{A,11} = J_{A,22}$ | recurrent AMPA self-coupling of a selective population | nC | $9.9026 \times 10^{-4}$ | Parameter values |
| $J_{A,12} = J_{A,21}$ | effective AMPA cross-coupling between selective populations | nA/Hz | $6.5177 \times 10^{-5}$ | Parameter values |
| $J_{A,ext}$ | external AMPA coupling for stimulus inputs | nA/Hz | $0.2243 \times 10^{-3}$ (standard set); $5.2 \times 10^{-4}$ (appendix set) | Results; Appendix |
| $I_0$ | mean effective external input common to both populations | nA | 0.2346 (standard set); 0.3255 (appendix set) | Parameter values; Appendix |
| $\sigma_{noise}$ | standard deviation of the OU noise current | nA | 0.007 (standard set); 0.02 (appendix set) | Simulations; Appendix |
| $\theta$ | decision threshold on the firing rate | Hz | 15 | Parameter values |
| $\mu_0$ | zero-coherence stimulus strength | Hz | 30 | Results; Appendix |
| $a$ | gain of the appendix input-output function | (V nC)$^{-1}$ | 270 | Appendix parameter list |
| $b$ | threshold offset of the appendix input-output function | Hz | 108 | Appendix parameter list |
| $d$ | scale of the appendix input-output function | s | 0.154 | Appendix parameter list |
| $\tau_m$ | membrane time constant of the LIF parent model | ms | not stated | equation (1); inherited from Wang (2002) |
| $\tau_{ref}$ | refractory period of the LIF parent model | ms | not stated | equation (1) |
| $V_{th}$, $V_{reset}$ | LIF spiking threshold and reset voltage | mV | not stated | equation (1) |
| nondecision latency | fixed nondecision time added to the decision time | ms | 100 | Parameter values |

## Equations

These are exact source transcriptions. Numbering follows the published article; displays that the source leaves unnumbered are identified by section.

First-passage-time firing rate of a leaky integrate-and-fire neuron receiving noisy input, as reported before adopting the simplified fit:

$$
\tau = \phi(I_{syn}) = \left( \tau_{ref} + \tau_m \sqrt{\pi} \int_{\frac{V_{reset} - V_{ss}}{\sigma_V}}^{\frac{V_{th} - V_{ss}}{\sigma_V}} e^{u^2} \left( 1 + \mathrm{erf}(u) \right) du \right)^{-1},
$$

Simplified input-output function fitted to the LIF response (Abbott and Chance, 2005), with subscript E, I selecting pyramidal or interneuron parameters:

$$
\phi(I_{syn}) = \frac{c_{E,I} I_{syn} - I_{E,I}}{1 - \exp\left[ -g_{E,I} \left( c_{E,I} I_{syn} - I_{E,I} \right) \right]},
$$

Eleven-variable mean-field network dynamics (four population rates; three AMPA and three NMDA gating variables; one GABA gating variable), with $i = 1, 2, 3$ in the rate and AMPA/NMDA equations:

$$
\begin{aligned}
\tau_r \frac{dr_i}{dt} &= -r_i + \phi(I_{syn,i}),\\
\tau_r \frac{dr_I}{dt} &= -r_I + \phi(I_{syn,I}),\\
\frac{dS_{AMPA,i}}{dt} &= -\frac{S_{AMPA,i}}{\tau_{AMPA}} + r_i,\\
\frac{dS_{NMDA,i}}{dt} &= -\frac{S_{NMDA,i}}{\tau_{NMDA}} + (1 - S_{NMDA,i}) F(\psi(r_i)),\\
\frac{dS_{GABA}}{dt} &= -\frac{S_{GABA}}{\tau_{GABA}} + r_I,
\end{aligned}
$$

Poisson-average fit of the NMDA gating variable to presynaptic rate $r$:

$$
\psi_{Poisson} \equiv \langle S \rangle_{Poisson} = \frac{\gamma r \tau_S}{1 + \gamma r \tau_S},
$$

Linearized interneuron input-output relation:

$$
\phi(I_{syn,I}) = \frac{1}{g_2} \left( c_I I_{syn,I} - I_I \right) + r_0,
$$

Phase-plane reduction displays: NMDA gating dynamics written on the slow variable, and the adiabatic steady states of the fast AMPA and GABA gating variables (the final equality is transcribed exactly as printed; see interpretation):

$$
\begin{aligned}
\frac{dS_{NMDA,i}}{dt} &= -\frac{S_{NMDA,i}}{\tau_{NMDA}} + (1 - S_{NMDA,i}) F(\psi_i),\\
S_{i,AMPA}(t) &= \tau_{AMPA} r_i(t) = \tau_{AMPA} \phi_i(t),\\
S_{GABA}(t) &= \tau_{GABA} r_I(t) = \tau_{AMPA} \phi_I(t),
\end{aligned}
$$

Reduced two-variable dynamics for the two choice-selective populations ($S$ denotes $S_{NMDA}$, $\tau_S$ denotes $\tau_{NMDA}$):

$$
\begin{aligned}
\frac{dS_1}{dt} &= -\frac{S_1}{\tau_S} + (1 - S_1) \gamma r_1,\\
\frac{dS_2}{dt} &= -\frac{S_2}{\tau_S} + (1 - S_2) \gamma r_2,
\end{aligned}
$$

Population rates from the fitted transfer function:

$$
r_1 = \phi(I_{syn,1}), \qquad r_2 = \phi(I_{syn,2}),
$$

Total synaptic currents with effective recurrent and cross-inhibitory couplings:

$$
\begin{aligned}
I_{syn,1} &= J_{N,11} S_1 - J_{N,12} S_2 + J_{A,11} r_1 - J_{A,12} r_2 + I_0 + I_1 + I_{noise,1},\\
I_{syn,2} &= J_{N,22} S_2 - J_{N,21} S_1 + J_{A,22} r_2 - J_{A,21} r_1 + I_0 + I_2 + I_{noise,2},
\end{aligned}
$$

Rewritten form with an explicit effective input and the single-population transfer function $H$:

$$
\begin{aligned}
r_1 &= H(x_1, x_2), \qquad r_2 = H(x_2, x_1),\\
x_1 &= J_{N,11} S_1 - J_{N,12} S_2 + I_0 + I_1 + I_{noise,1},\\
x_2 &= J_{N,22} S_2 - J_{N,21} S_1 + I_0 + I_2 + I_{noise,2},
\end{aligned}
$$

Final self-contained two-variable system:

$$
\begin{aligned}
\frac{dS_1}{dt} &= G_1(S_1, S_2) = -\frac{S_1}{\tau_S} + (1 - S_1) \gamma H(x_1, x_2),\\
\frac{dS_2}{dt} &= G_2(S_2, S_1) = -\frac{S_2}{\tau_S} + (1 - S_2) \gamma H(x_2, x_1),
\end{aligned}
$$

Ornstein-Uhlenbeck noise current (white noise filtered by the AMPA time constant; $\sigma_{noise}^2$ is the noise variance and $\eta$ is Gaussian white noise with zero mean and unit variance):

$$
\tau_{AMPA} \frac{dI_{noise}(t)}{dt} = -I_{noise}(t) + \eta(t) \sqrt{\tau_{AMPA} \sigma_{noise}^2},
$$

Coherence-dependent stimulus currents favoring population 1 for $c' > 0$:

$$
I_1 = J_{A,ext} \mu_0 \left( 1 + \frac{c'}{100\%} \right), \qquad I_2 = J_{A,ext} \mu_0 \left( 1 - \frac{c'}{100\%} \right),
$$

Local linearization of the dynamics near the saddle steady state $S_{saddle}$, governing the integration time:

$$
\Delta S(t) = a_1 v_1 \exp(-t / \tau_{stable}) + a_2 v_2 \exp(t / \tau_{unstable}),
$$

Appendix form of the reduced model without AMPA at recurrent synapses (unnumbered displays; $i = 1, 2$ labels the selective populations):

$$
\begin{aligned}
\frac{dS_i}{dt} &= -\frac{S_i}{\tau_S} + (1 - S_i) \gamma H_i, \qquad H_i = \frac{a x_i - b}{1 - \exp[-d (a x_i - b)]},\\
x_1 &= J_{N,11} S_1 - J_{N,12} S_2 + I_0 + I_1 + I_{noise,1}, \qquad x_2 = J_{N,22} S_2 - J_{N,21} S_1 + I_0 + I_2 + I_{noise,2},\\
I_i &= J_{A,ext} \mu_0 \left( 1 \pm \frac{c'}{100\%} \right), \qquad \tau_{AMPA} \frac{dI_{noise,i}(t)}{dt} = -I_{noise,i}(t) + \eta_i(t) \sqrt{\tau_{AMPA} \sigma_{noise}^2},
\end{aligned}
$$

## Term-by-term interpretation

Equation (1) is the standard first-passage-time rate of a leaky integrate-and-fire neuron with Gaussian current input; the source reports it as motivation and then replaces it by the saturating rational fit of equation (2) from Abbott and Chance (2005), whose curvature is controlled by $g_{E,I}$ and whose threshold-like behavior is set by $I_{E,I}$. Equations (3)-(7) constitute the mean-field network: four Wilson-Cowan-type rate equations with the fast relaxation $\tau_r = 2$ ms, first-order AMPA and GABA gating kinetics, and NMDA gating driven by $F(\psi(r_i)) = \psi_i/(\tau_{NMDA}(1 - \psi_i))$, the algebraic steady-state form whose Poisson-average fit is equation (8); simple algebra gives $F(\psi(r)) = \gamma r$ with $\gamma = 0.641$, so NMDA gating rises linearly with presynaptic rate and decays with the 100 ms time constant that underlies slow integration. Equation (9) linearizes the interneuron response ($g_2 = 2$, $r_0 = 11.5$ Hz), which lets the shared feedback inhibition be absorbed into the effective cross-couplings: the $S_2$-dependent term of $I_{syn,1}$ is $(J_{N,E \to E} - J_{N,I \to E} J_{E \to I}) S_2 \equiv -J_{N,12} S_2$, so $J_{N,12}$, $J_{N,21}$, $J_{A,12}$, and $J_{A,21}$ are negative-effective (written with explicit minus signs in equations (14)-(15)). The phase-plane reduction clamps the nonselective population at a constant 2 Hz, linearizes inhibition, and assumes every fast variable equilibrates relative to $\tau_{NMDA}$, leaving equations (10)-(11) in which AMPA and GABA contributions enter through their steady-state proportionalities to firing rate. Equations (12)-(15) make the rates explicit functions of the synaptic currents, and equations (16)-(19) resolve the implicit mutual dependence of $r_i$ and $I_{syn,i}$ through the effective input $x_i$ and the single-population function $H$, giving the closed two-variable system (20)-(21). The unnumbered Simulations display defines the Ornstein-Uhlenbeck noise ($\sigma_{noise} = 0.007$ nA unless stated), and the unnumbered Results displays define the coherence-dependent stimulus pair. Equation (22) linearizes the flow near the saddle: residence time near the saddle scales as $\tau_{unstable} \log(1/\delta)$, which explains decision times far longer than $\tau_S$ and the longer reaction times of error trials. The psychometric fits use a Weibull form $p = 1 - 0.5 e^{-(c'/\alpha)^\beta}$ inline (fitted $\alpha = 7.2\%$, $\beta = 1.25$ for the standard parameters). In the appendix display transcribed from the phase-plane reduction, the printed final equality reads $S_{GABA}(t) = \tau_{GABA} r_I(t) = \tau_{AMPA} \phi_I(t)$; dimensional consistency with the preceding equality requires $\tau_{GABA} \phi_I$, so the printed $\tau_{AMPA}$ is flagged as an apparent typographical slip in the published text. The transcription reproduces the source exactly.

## Inputs, outputs, and conditions

- Input: stimulus currents $I_1$, $I_2$ (coherence-scaled by $c'$ around $\mu_0 = 30$ Hz), background drive $I_0$, and OU noise $I_{noise,i}$.
- Output: synaptic gating trajectories $S_1(t)$, $S_2(t)$ (equivalently $r_1(t)$, $r_2(t)$); a decision is registered when the winning rate crosses $\theta$.
- Initial conditions: `not_verified`.
- Boundary conditions: `not_applicable`; locator: not_applicable.
- Network conditions: `source_located`; locator: Materials and Methods, "Dynamical equations" paragraph after equations (14)-(15) (effective cross-couplings $-J_{N,12}$, $-J_{N,21}$, $-J_{A,12}$, $-J_{A,21}$ arise from shared feedback inhibition; architecture in Fig. 1).
- Event handling: `source_located`; locator: "Parameter values" paragraph (decision when a population reaches $\theta = 15$ Hz; reaction time adds a 100 ms nondecision latency).
- Numerical method: `source_example_located`; locator: "Simulations" paragraph (Euler method, 0.1 ms step; phase-plane and bifurcation analysis in XPPAUT).
- Stochastic input: `stochastic`; Ornstein-Uhlenbeck process with $\sigma_{noise} = 0.007$ nA (standard set).
- Simulation scale: `large_scale_network` (two-variable reduction of a circuit of about 2000 spiking neurons).

## Assumptions and limitations

The model is a mean-field reduction: synaptic driving forces are constant, membrane-potential variance is fixed, the nonselective excitatory population is clamped at 2 Hz, the interneuron response is linear, and all variables except the NMDA gating are adiabatic. The effective couplings fold shared inhibition into negative cross-couplings, so the two-variable system cannot separately identify excitation and inhibition. The standard parameters were slightly adjusted to match the reaction times of Roitman and Shadlen (2002), and the source notes the set may not be optimal. One printed equality in the reduction display carries an apparent typographical slip ($\tau_{AMPA}$ for $\tau_{GABA}$; see interpretation). The model addresses two-alternative forced-choice integration in a cortical decision circuit and is not a comprehensive account of cognition.

## Experimental support

`not assessed`. This status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`; a ModelDB entry and an author-lab code repository (xjwanglab/wong-wang-2006, MIT license) exist but have not been audited for this record.
