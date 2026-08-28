# Brunel sparse excitatory-inhibitory network

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: freely accessible full-text PDF of the published article hosted by the publisher (Journal of Computational Neuroscience open archive), pages 183-208, with every numbered equation checked against the rendered page images.
- Source locator: Section 2 equations (1)-(2); Section 3 equations (3)-(12); Section 4 equations (13)-(27); Section 5 equations (28)-(31); Section 6 equations (32)-(33); Appendix A equations (34)-(56); Appendix B equations (57)-(66), plus the unnumbered displays identified by section below.
- Transcription status: exact source transcription; apparent printed slips are transcribed exactly and flagged in the interpretation.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-28.

## Scope

- Biological cell scope: `neural_population`.
- Cell type: `neural_population`.
- Cell subtype: sparse random network of leaky integrate-and-fire neurons with a fraction $N_E = 0.8N$ of excitatory and $N_I = 0.2N$ of inhibitory units (model A: identical characteristics; model B: population-specific time constants, synaptic efficacies, and delays).
- Nervous-system region: `not_assessed` (cortical anatomy used only for parameter estimates).
- Model scope: `coupled_multicellular`.
- Model scale: `large_scale_network` (analysis in the limit $N \to \infty$; simulations with 12,500 neurons).
- Mathematical form: `hybrid` (piecewise-linear membrane ODE with threshold/reset events; synaptic currents are delta-function spike trains; the analytical treatment is a Fokker-Planck diffusion equation with absorbing and resetting boundary conditions).
- Interaction scope: `network_connectivity`.
- Network type: `spiking_network` (sparse random excitatory-inhibitory connectivity).
- Spatial structure: `network_topology` (random wiring, no spatial structure).
- Stochasticity: `stochastic` (Poisson external synapses, Gaussian current fluctuations, finite-size noise).
- Plasticity scope: `none`.

## Source citation

Nicolas Brunel. Dynamics of Sparsely Connected Networks of Excitatory and Inhibitory Spiking Neurons. *Journal of Computational Neuroscience* **8**(3), 183-208 (2000). [DOI](https://doi.org/10.1023/a:1008925309027). [PubMed](https://pubmed.ncbi.nlm.nih.gov/10809012/). The full text is freely readable on the publisher site (Journal of Computational Neuroscience open archive).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $V_i(t)$ | somatic membrane potential of neuron $i$ | mV | source-verified |
| $I_i(t)$ | synaptic current arriving at the soma of neuron $i$ | not stated (appears as $R I_i(t)$ with units of voltage) | source-verified |
| $P(V, t)$ | probability density of finding a neuron at depolarization $V$ | 1/mV | source-verified |
| $p_r(t)$ | probability that a neuron is refractory at time $t$ | dimensionless | source-verified |
| $S(V, t)$ | probability current through $V$ at time $t$ | not stated | source-verified |
| $\nu(t)$ | instantaneous network firing rate | Hz | source-verified |
| $\mu(t)$ | average part of the synaptic input $R I_i(t)$ | mV | source-verified |
| $\sigma(t)$ | magnitude of the fluctuating part of the synaptic input | mV | source-verified |
| $\eta_i(t)$ | Gaussian white noise, $\langle \eta_i(t) \rangle = 0$, $\langle \eta_i(t) \eta_j(t') \rangle = \delta_{ij} \delta(t - t')$ | not stated | source-verified |
| $\mu_l(t)$, $\mu_{ext}$ | local and external parts of the mean input | mV | source-verified |
| $\sigma_l(t)$, $\sigma_{ext}$ | local and external fluctuation amplitudes | mV | source-verified |
| $P_a(V, t)$, $p_{ra}(t)$ | depolarization density and refractory probability for population $a = E, I$ (model B) | 1/mV; dimensionless | source-verified |
| $\mu_a$, $\sigma_a$ | mean input and fluctuation amplitude for population $a$ | mV | source-verified |
| $\nu_a(t)$ | firing rate of population $a = E, I$ | Hz | source-verified |
| $P_0(V)$, $p_{r,0}$ | stationary depolarization density and refractory probability (model A) | 1/mV; dimensionless | source-verified |
| $\mu_0$, $\sigma_0$ | stationary mean input and fluctuation amplitude (model A) | mV | source-verified |
| $\nu_0$ | stationary firing rate (model A) | Hz | source-verified |
| $\mu_{0,l}$, $\sigma_{0,l}$ | stationary local (recurrent) parts of $\mu_0$ and $\sigma_0$ | mV | source-verified |
| $\mu_{a0}$, $\sigma_{a0}$, $\nu_{a0}$ | stationary inputs and rate of population $a$ (model B) | mV; mV; Hz | source-verified |
| $Q$ | rescaled depolarization distribution, $P = 2 \tau \nu_0 Q / \sigma_0$ | dimensionless | source-verified |
| $y$ | rescaled membrane potential, $y = (V - \mu_0)/\sigma_0$ | dimensionless | source-verified |
| $y_\theta$, $y_r$ | rescaled threshold and reset ordinates | dimensionless | source-verified |
| $n(t)$ | relative variation of the instantaneous rate around $\nu_0$ | dimensionless | source-verified |
| $G$ | ratio of mean local input to $\sigma_0$ (sign chosen positive for inhibitory feedback) | dimensionless | source-verified |
| $H$ | ratio of local-input variance to total variance | dimensionless | source-verified |
| $Q_0(y)$ | stationary solution of the rescaled Fokker-Planck equation | dimensionless | source-verified |
| $Q_1$, $n_1$ | first-order perturbations of $Q$ and $n$ | dimensionless | source-verified |
| $Q_1(y,t) = \exp(\lambda t) \hat{n}_1(\lambda) \hat{Q}_1(y, \lambda)$ | eigenmode decomposition of the perturbation | dimensionless | source-verified |
| $\lambda$ | eigenvalue of the linear stability problem | 1/ms | source-verified |
| $\phi_1$, $\phi_2$ | independent solutions of the homogeneous eigenmode equation (confluent hypergeometric combinations) | dimensionless | source-verified |
| $\mathrm{Wr}$ | Wronskian of $\phi_1$ and $\phi_2$ | dimensionless | source-verified |
| $\tilde{\phi}$, $\tilde{W}$, $W$ | reduced eigenfunctions and Wronskian combinations used in the eigenfrequency condition | dimensionless | source-verified |
| $\psi(y, \omega)$, $R(\omega)$, $S(y, \omega)$ | auxiliary functions of the Hopf condition (name collision with the probability current $S(V,t)$ is present in the source) | dimensionless | source-verified |
| $\omega_c$ | angular frequency on a Hopf bifurcation line ($\lambda = i \omega_c$) | 1/ms | source-verified |
| $K$ | rescaled delay, $K = D C_E \nu_{thr} = D\theta/(\tau J)$ | dimensionless | source-verified |
| $\mu_k$ | $k$-th moment of the interspike interval distribution | ms$^k$ | source-verified |
| $\mathrm{CV}$ | coefficient of variation of the interspike interval | dimensionless | source-verified |
| $\rho_i(t)$ | presence/absence indicator of a synapse from the fired neuron onto neuron $i$ | dimensionless | source-verified |
| $S(t)$ | spike-emission process of the whole network (finite-size description) | spikes/ms | source-verified |
| $\xi(t)$ | Gaussian white noise approximating the global finite-size fluctuations | not stated | source-verified |
| $\zeta(t)$, $\hat{\zeta}(\omega)$ | finite-size noise entering the rescaled Fokker-Planck equation and its Fourier transform | not stated | source-verified |
| $Z(\omega)$ | linear-response term relating $\hat{n}_1(\omega)$ to $\hat{\zeta}(\omega)$ | dimensionless | source-verified |
| $P(\omega)$ | power spectrum of the global activity | dimensionless | source-verified |
| $n_a(t)$, $n_{a1}(t)$ | relative rate fluctuation of population $a$ and its first-order part (model B) | dimensionless | source-verified |
| $G_{ab}$, $H_{ab}$ | recurrent-coupling measures of population $a$ driven by population $b$ (model B) | dimensionless | source-verified |
| $y_a$, $y_{a\theta}$, $y_{ar}$ | rescaled potential, threshold, and reset ordinates for population $a$ | dimensionless | source-verified |
| $s_a$ | population sign in the model-B linearized equation: $s_E = -1$, $s_I = 1$ | dimensionless | source-verified |
| $\hat{Q}_a(y_a, \lambda)$, $\hat{n}_a(\lambda)$ | eigenmode of population $a$ and its rate amplitude | dimensionless | source-verified |
| $\hat{Q}^p_{ab}$ | particular solution driven by population $b$ | dimensionless | source-verified |
| $A_{ab}$ | matrix entries of the model-B eigenvalue condition | dimensionless | source-verified |
| $\bar{\sigma}_a$ | square root of the normalized total input variance of population $a$ | dimensionless | source-verified |
| $\Delta\phi$ | phase lag between inhibitory and excitatory population oscillations | rad | source-verified |
| $f$ | frequency of the global oscillation | Hz | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $N$, $N_E$, $N_I$ | total, excitatory, and inhibitory neuron numbers | count | $N_E = 0.8N$, $N_I = 0.2N$; simulations $N_E = 10{,}000$, $N_I = 2{,}500$ | Section 2; Section 6 |
| $C$ | number of connections received by each neuron | count | $C = C_E + C_I + C_{ext}$ | Section 2 |
| $C_E$, $C_I$ | recurrent excitatory and inhibitory inputs per neuron | count | $C_E = \epsilon N_E$, $C_I = \epsilon N_I = \gamma C_E$; Fig. 1 $C_E = 4000$; simulations $C_E = 1000$ | Section 2; Fig. 1; Section 6 |
| $\epsilon$ | connection probability, $C_E/N_E = C_I/N_I$ | dimensionless | $\epsilon \ll 1$; simulations $\epsilon = 0.1$ | Section 2; Section 6 |
| $C_{ext}$ | external connections per neuron | count | $C_{ext} = C_E$ | Section 2 |
| $\gamma$ | ratio of inhibitory to excitatory inputs, $C_I/C_E$ | dimensionless | 0.25 | Section 2 |
| $\tau$ | membrane time constant (model A) | ms | not stated (model B value $\tau_E = 20$ ms is given) | Section 2 |
| $\tau_E$, $\tau_I$ | membrane time constants of the two populations (model B) | ms | $\tau_E = 20$; $\tau_I$ not stated | Section 2 |
| $R$ | membrane resistance | resistance | not stated | equation (1) |
| $J$ | excitatory postsynaptic potential amplitude (model A) | mV | Fig. 1: 0.2; simulations: 0.1 | Section 4.1; Section 6 |
| $J_{ij}$ | synaptic efficacy from $j$ to $i$ | mV | $J$ for excitatory (recurrent and external), $-gJ$ for inhibitory | Section 2 |
| $g$ | relative strength of inhibitory synapses (model A) | dimensionless | varied (balanced value $g = 4$) | Section 2; Fig. 1 |
| $\theta$ | firing threshold | mV | 20 | Section 2 |
| $V_r$ | reset potential | mV | 10 | Section 2 |
| $\tau_{rp}$ | refractory period | ms | 2 | Section 2 |
| $D$ | transmission delay (model A) | ms | Fig. 2: 1.5, 2, 3; Fig. 4B: uniform on [0, 3]; simulations 1.5 | Section 2; Figs. 2-4 |
| $D_{ab}$ | delay from population $b$ to population $a$ (model B) | ms | four independent delays; Fig. 6: uniform on [0, 4] | Section 2; Fig. 6 |
| $\nu_{ext}$ | external Poisson rate (model A) | Hz | expressed in units of $\nu_{thr}$ | Section 2 |
| $\nu_{E,ext}$, $\nu_{I,ext}$ | external Poisson rates of the two populations (model B) | Hz | not stated individually | Section 2 |
| $\nu_{thr}$ | external rate needed to reach threshold without feedback, $\theta/(C_E J \tau)$ | Hz | 1.25 for the Fig. 1 parameters | p. 185 inline; p. 188 display |
| $J_E$, $J_I$ | excitatory efficacies onto excitatory and inhibitory neurons (model B), $J_{EE} \equiv J_E$, $J_{IE} \equiv J_I$ | mV | $J_I$ varied in Fig. 6 | Section 2 |
| $g_E$, $g_I$ | relative inhibitory strengths $J_{EI}/J_E$ and $J_{II}/J_I$ (model B) | dimensionless | varied | Section 2 |
| Table 1 simulation points | $(g, \nu_{ext}/\nu_{thr})$ of the four simulated states A-D | dimensionless | A (3, 2); B (6, 4); C (5, 2); D (4.5, 0.9) | Fig. 7; Fig. 8 caption |

## Equations

These are exact source transcriptions. Numbering follows the published article; displays that the source leaves unnumbered are identified by section.

Section 2, integrate-and-fire membrane equation of neuron $i$:

$$
\tau \dot{V}_i(t) = -V_i(t) + R I_i(t),
$$

Section 2, synaptic current as a sum of delayed delta-function spike contributions over the $C + C_{ext}$ presynaptic neurons $j$:

$$
R I_i(t) = \tau \sum_j J_{ij} \sum_k \delta\left( t - t_j^k - D \right),
$$

Section 3, Gaussian decomposition of the synaptic current:

$$
R I_i(t) = \mu(t) + \sigma \sqrt{\tau}\, \eta_i(t),
$$

Section 3, average part of the synaptic input:

$$
\mu(t) = \mu_l(t) + \mu_{ext} \quad \text{with} \quad \mu_l(t) = C_E J (1 - \gamma g) \nu(t - D) \tau, \quad \mu_{ext} = C_E J \nu_{ext} \tau,
$$

Section 3, magnitude of the fluctuating part:

$$
\sigma^2(t) = \sigma_l^2(t) + \sigma_{ext}^2 \quad \text{with} \quad \sigma_l(t) = J \sqrt{C_E (1 + \gamma g^2) \nu(t - D) \tau}, \quad \sigma_{ext} = J \sqrt{C_E \nu_{ext} \tau},
$$

Section 3, Fokker-Planck equation for the depolarization distribution:

$$
\tau \frac{\partial P(V, t)}{\partial t} = \frac{\sigma^2(t)}{2} \frac{\partial^2 P(V, t)}{\partial V^2} + \frac{\partial}{\partial V} \left[ \left( V - \mu(t) \right) P(V, t) \right],
$$

Section 3, continuity-equation form:

$$
\frac{\partial P(V, t)}{\partial t} = -\frac{\partial S(V, t)}{\partial V},
$$

Section 3, probability current:

$$
S(V, t) = -\frac{\sigma^2(t)}{2 \tau} \frac{\partial P(V, t)}{\partial V} - \frac{\left( V - \mu(t) \right)}{\tau} P(V, t),
$$

Section 3, absorbing boundary condition at the threshold expressed as a derivative condition:

$$
\frac{\partial P}{\partial V}(\theta, t) = -\frac{2 \nu(t) \tau}{\sigma^2(t)},
$$

Section 3, derivative discontinuity at the reset potential:

$$
\frac{\partial P}{\partial V}(V_r^+, t) - \frac{\partial P}{\partial V}(V_r^-, t) = -\frac{2 \nu(t - \tau_{rp}) \tau}{\sigma^2(t)},
$$

Section 3, integrability condition at negative infinity:

$$
\lim_{V \to -\infty} P(V, t) = 0, \qquad \lim_{V \to -\infty} V P(V, t) = 0,
$$

Section 3, normalization with the refractory fraction (the second display is the source's unnumbered definition of $p_r$):

$$
\int_{-\infty}^{\theta} P(V, t)\, dV + p_r(t) = 1, \qquad p_r(t) = \int_{t - \tau_{rp}}^{t} \nu(u)\, du,
$$

Section 3, mean input to a cell of population $a = E, I$ (model B):

$$
\mu_a = C_E J_a \tau_a \left[ \nu_{a,ext} + \nu_E(t - D_{a,E}) - \gamma g_a \nu_I(t - D_{aI}) \right],
$$

Section 3, fluctuation magnitude for population $a$ (model B):

$$
\sigma_a^2 = J_a^2 C_E \tau_a \left[ \nu_{a,ext} + \nu_E(t - D_{aE}) + \gamma g_a^2 \nu_I(t - D_{aI}) \right],
$$

Section 3, coupled Fokker-Planck equations (model B):

$$
\tau_a \frac{\partial P_a(V, t)}{\partial t} = \frac{\sigma_a^2(t)}{2} \frac{\partial^2 P_a(V, t)}{\partial V^2} + \frac{\partial}{\partial V} \left[ \left( V - \mu_a(t) \right) P_a(V, t) \right], \qquad a = E, I,
$$

Section 3, threshold boundary condition (model B):

$$
\frac{\partial P_a}{\partial V}(\theta, t) = -\frac{2 \nu_a(t) \tau_a}{\sigma_a^2(t)},
$$

Section 3, reset boundary condition (model B; the numerator is printed with the plain $\tau$):

$$
\frac{\partial P_a}{\partial V}(V_r^+, t) - \frac{\partial P_a}{\partial V}(V_r^-, t) = -\frac{2 \nu_a(t - \tau_{rp}) \tau}{\sigma_a^2(t)},
$$

Section 3, integrability condition (model B):

$$
\lim_{V \to -\infty} P_a(V, t) = 0, \qquad \lim_{V \to -\infty} V P_a(V, t) = 0,
$$

Section 4.1, stationary distribution of model A (the second equality is part of the source display; $\Theta$ is the Heaviside function):

$$
P_0(V) = \frac{2 \nu_0 \tau}{\sigma_0} \exp\left( -\frac{(V - \mu_0)^2}{\sigma_0^2} \right) \times \int_{\frac{V_r - \mu_0}{\sigma_0}}^{\frac{\theta - \mu_0}{\sigma_0}} \Theta(u - V_r) e^{u^2}\, du, \qquad p_{r,0} = \nu_0 \tau_{rp},
$$

Section 4.1, stationary input moments of model A:

$$
\mu_0 = C_E J \tau \left[ \nu_{ext} + \nu_0 (1 - g \gamma) \right], \qquad \sigma_0^2 = C_E J^2 \tau \left[ \nu_{ext} + \nu_0 (1 + g^2 \gamma) \right],
$$

Section 4.1, self-consistency condition determining $\nu_0$:

$$
\frac{1}{\nu_0} = \tau_{rp} + 2 \tau \int_{\frac{V_r - \mu_0}{\sigma_0}}^{\frac{\theta - \mu_0}{\sigma_0}} du\, e^{u^2} \int_{-\infty}^{u} dv\, e^{-v^2} = \tau_{rp} + \tau \sqrt{\pi} \int_{\frac{V_r - \mu_0}{\sigma_0}}^{\frac{\theta - \mu_0}{\sigma_0}} du\, e^{u^2} \left( 1 + \mathrm{erf}(u) \right),
$$

Section 4.1, low-rate asymptotic form of equation (21):

$$
\nu_0 \tau \simeq \frac{\theta - \mu_0}{\sigma_0 \sqrt{\pi}} \exp\left( -\frac{(\theta - \mu_0)^2}{\sigma_0^2} \right),
$$

Section 4.1, unnumbered display defining the external-rate unit:

$$
\nu_{thr} = \frac{\theta}{C_E J \tau},
$$

Section 4.1.1, stationary rate in the high-activity regime:

$$
\nu_0 = \frac{1}{\tau_{rp}} \left[ 1 - \frac{\theta - V_r}{C_E J (1 - g \gamma)} \right],
$$

Section 4.1.1, linear gain in the inhibition-dominated regime:

$$
\nu_0 = \frac{\nu_{ext} - \nu_{thr}}{g \gamma - 1},
$$

Section 4.2, stationary distribution of model B (the refractory probability is printed as $p_{r,0} = \nu_{a0} \tau_{rp}$):

$$
P_{a0}(V) = \frac{2 \nu_{a0} \tau_a}{\sigma_{a0}} \exp\left( -\frac{(V - \mu_{a0})^2}{\sigma_{a0}^2} \right) \times \int_{\frac{V_r - \mu_{a0}}{\sigma_{a0}}}^{\frac{\theta - \mu_{a0}}{\sigma_{a0}}} \Theta(u - V_r) e^{u^2}\, du, \qquad p_{r,0} = \nu_{a0} \tau_{rp},
$$

Section 4.2, stationary input moments of model B (printed with plain $g$ and $g^2$ in the second line):

$$
\mu_{a0} = C_E J_a \tau_a \left[ \nu_{ext} + \nu_{E0} - g \gamma \nu_{I0} \right], \qquad \sigma_{a0}^2 = C_E J_a^2 \tau_a \left[ \nu_{ext} + \nu_{E0} + g^2 \gamma \nu_{I0} \right],
$$

Section 4.2, self-consistency condition of model B:

$$
\frac{1}{\nu_{a0}} = \tau_{rp} + 2 \tau_a \int_{\frac{V_r - \mu_{a0}}{\sigma_{a0}}}^{\frac{\theta - \mu_{a0}}{\sigma_{a0}}} du\, e^{u^2} \int_{-\infty}^{u} dv\, e^{-v^2},
$$

Section 5, rescaling of the model-A distributions:

$$
P = \frac{2 \tau \nu_0}{\sigma_0} Q, \qquad y = \frac{V - \mu_0}{\sigma_0}, \qquad \nu = \nu_0 \left( 1 + n(t) \right),
$$

Section 5, rescaled Fokker-Planck equation:

$$
\tau \frac{\partial Q}{\partial t} = \frac{1}{2} \frac{\partial^2 Q}{\partial y^2} + \frac{\partial}{\partial y} \left( y Q \right) + n(t - D) \left( G \frac{\partial Q}{\partial y} + \frac{H}{2} \frac{\partial^2 Q}{\partial y^2} \right),
$$

Section 5, measures of the recurrent interactions:

$$
G = \frac{C_E J \tau \nu_0 (g \gamma - 1)}{\sigma_0} = -\frac{\mu_{0,l}}{\sigma_0}, \qquad H = \frac{C_E J^2 \tau \nu_0 (1 + g^2 \gamma)}{\sigma_0^2} = \frac{\sigma_{0,l}^2}{\sigma_0^2},
$$

Section 5, unnumbered display fixing the rescaled threshold and reset ordinates:

$$
y_\theta = \frac{\theta - \mu_0}{\sigma_0} \quad \text{and} \quad y_r = \frac{V_r - \mu_0}{\sigma_0},
$$

Section 5, boundary conditions on the derivatives of $Q$:

$$
\frac{\partial Q}{\partial y}(y_\theta, t) = -\frac{1 + n(t)}{1 + H n(t - D)}, \qquad \frac{\partial Q}{\partial y}(y_r^+, t) - \frac{\partial Q}{\partial y}(y_r^-, t) = -\frac{1 + n(t - \tau_{rp})}{1 + H n(t - D)},
$$

Section 6.1, unnumbered finite-size decomposition displays (input from a single network spike; decomposition of connectivity and spike-emission processes; resulting input):

$$
R I_i(t) = -J \tau \rho_i(t) S(t - D), \qquad \rho_i(t) = \frac{C}{N} + \delta \rho_i(t), \quad S(t) = N \nu(t) + \delta S(t), \qquad R I_i(t) = \mu(t) - J \tau N \nu(t) \delta \rho_i(t) - J \tau \frac{C}{N} \delta S(t),
$$

Section 6.1, unnumbered display for the mean synaptic input with the Gaussian approximation of the global Poisson activity:

$$
C J \tau \nu(t) + J \sqrt{\epsilon C \nu_0 \tau} \sqrt{\tau}\, \xi(t) + \mu_{ext},
$$

Section 6.1, rescaled Fokker-Planck equation with the finite-size noise term:

$$
\tau \frac{\partial Q}{\partial t} = \frac{1}{2} \frac{\partial^2 Q}{\partial y^2} + \frac{\partial}{\partial y} \left( y Q \right) + n(t - D) \times \left( G \frac{\partial Q}{\partial y} + \frac{H}{2} \frac{\partial^2 Q}{\partial y^2} \right) + \sqrt{\epsilon \tau} H \zeta(t) \frac{\partial Q}{\partial y},
$$

Section 6.2, large-$\omega$ approximation of the power spectrum of the global activity:

$$
P(\omega) = \frac{2 \epsilon H}{\omega \tau \left( 1 - 2 H \cos(\omega D) + H^2 \right) + 2 \sqrt{\omega \tau} G \left( \cos(\omega D) - \sin(\omega D) - H \right) + 2 G^2},
$$

Appendix A.1, unnumbered displays: recurrence for the interspike-interval moments (reset ordinate $x = V_r$) with the first moment:

$$
\frac{\sigma^2}{2} \frac{d^2 \mu_k}{d x^2} + (\mu - x) \frac{d \mu_k}{d x} = -k \mu_{k-1}, \qquad \mu_1 = \frac{1}{\nu_0},
$$

Appendix A.1, unnumbered displays: second moment and coefficient of variation of the interspike interval:

$$
\mu_2 = \mu_1^2 + 2 \pi \int_{y_r}^{y_\theta} e^{x^2} dx \int_{-\infty}^{x} e^{y^2} \left( 1 + \mathrm{erf}\, y \right)^2 dy, \qquad \mathrm{CV} = 2 \pi \nu_0^2 \int_{y_r}^{y_\theta} e^{x^2} dx \int_{-\infty}^{x} e^{y^2} \left( 1 + \mathrm{erf}\, y \right)^2 dy,
$$

Appendix A.2, starting system of the excitation-dominated estimate (the source tags (34) on the first display and (35) on the mean-input line):

$$
\frac{1}{\nu_0} = \tau_{rp} + \tau \sqrt{\pi} \int_{\frac{V_r - \mu_0}{\sigma_0}}^{\frac{\theta - \mu_0}{\sigma_0}} du\, e^{u^2} \left( 1 + \mathrm{erf}(u) \right)
$$

$$
\mu_0 = C_E J \tau \left[ \nu_{ext} + \nu_0 (1 - g \gamma) \right], \qquad \sigma_0^2 = C_E J^2 \tau \left[ \nu_{ext} + \nu_0 (1 + g^2 \gamma) \right],
$$

Appendix A.2, unnumbered asymptotic chain leading to equation (23):

$$
\sqrt{\pi} e^{u^2} \left( 1 + \mathrm{erf}(u) \right) \to -\frac{1}{u},
$$

$$
\frac{1}{\nu_0} \sim \tau_{rp} - \tau [\ln u]_{\frac{V_r - \mu_0}{\sigma_0}}^{\frac{\theta - \mu_0}{\sigma_0}} \sim \tau_{rp} + \tau \ln \left( \frac{\mu_0 - \theta}{\mu_0 - V_r} \right) \sim \tau_{rp} + \tau \frac{\theta - V_r}{\mu_0},
$$

$$
\tau \frac{\theta - V_r}{\mu_0} \sim \frac{1}{\nu_0} \frac{\theta - V_r}{C_E J (1 - g \gamma)}, \qquad \nu_0 = \frac{1}{\tau_{rp}} \left[ 1 - \frac{\theta - V_r}{C_E J (1 - g \gamma)} \right],
$$

Appendix A.3, stationary solution of the rescaled problem:

$$
Q_0(y) = \begin{cases} \exp(-y^2) \int_y^{y_\theta} du \exp(u^2) & y > y_r \\ \exp(-y^2) \int_{y_r}^{y_\theta} du \exp(u^2) & y < y_r \end{cases},
$$

Appendix A.3, unnumbered definition of the linear operator (the source also defines the bracket $[f]_{y^-}^{y^+} = \lim_{\epsilon \to 0} \{f(y + \epsilon) - f(y - \epsilon)\}$ in prose):

$$
\mathcal{L}[Q] = \frac{1}{2} \frac{\partial^2 Q}{\partial y^2} + \frac{\partial}{\partial y} \left( y Q \right),
$$

Appendix A.3, linearized equation at first order:

$$
\tau \frac{\partial Q_1}{\partial t} = \mathcal{L}[Q_1] + n_1(t - D) \left( G \frac{d Q_0}{d y} + \frac{H}{2} \frac{d^2 Q_0}{d y^2} \right),
$$

Appendix A.3, linearized threshold boundary condition:

$$
Q_1(y_\theta, t) = 0, \qquad \frac{\partial Q_1}{\partial y}(y_\theta) = -n_1(t) + H n_1(t - D),
$$

Appendix A.3, linearized reset boundary condition:

$$
\left[ Q_1 \right]_{y_r^-}^{y_r^+} = 0, \qquad \left[ \frac{\partial Q_1}{\partial y} \right]_{y_r^-}^{y_r^+} = -n_1(t - \tau_{rp}) + H n_1(t - D),
$$

Appendix A.3, unnumbered eigenmode ansatz (the second line is printed with a comma in place of a product):

$$
Q_1(y, t) = \exp(\lambda t) \hat{n}_1(\lambda) \hat{Q}_1(y, \lambda), \qquad n_1(t) = \exp(\lambda t), \quad \hat{n}_1(\lambda),
$$

Appendix A.3, ordinary differential equation for the eigenmode:

$$
\lambda \tau \hat{Q}_1(y, \lambda) = \mathcal{L}[\hat{Q}_1]\,(y, \lambda) + e^{-\lambda D} \left( G \frac{d Q_0}{d y} + \frac{H}{2} \frac{d^2 Q_0}{d y^2} \right),
$$

Appendix A.3, unnumbered boundary conditions of the eigenmode problem (both pairs are printed at $y_\theta$ and the last exponential is printed as $\exp(-\lambda \tau)$):

$$
\hat{Q}_1(y_\theta, \lambda) = 0, \quad \frac{\partial \hat{Q}_1}{\partial y}(y_\theta) = -1 + H \exp(-\lambda D),
$$

$$
\hat{Q}_1(y_\theta, \lambda) = 0, \quad \frac{\partial \hat{Q}_1}{\partial y}(y_\theta) = -\exp(-\lambda \tau_{rp}) + H \exp(-\lambda \tau),
$$

Appendix A.3, general solution of the eigenmode equation:

$$
\hat{Q}_1(y, \lambda) = \begin{cases} \alpha_1^+(\lambda) \phi_1(y, \lambda) + \beta_1^+(\lambda) \phi_2(y, \lambda) + \hat{Q}_1^p(y, \lambda) & y > y_r \\ \alpha_1^-(\lambda) \phi_1(y, \lambda) + \beta_1^-(\lambda) \phi_2(y, \lambda) + \hat{Q}_1^p(y, \lambda) & y < y_r \end{cases},
$$

Appendix A.3, particular solution:

$$
\hat{Q}_1^p(y, \lambda) = e^{-\lambda D} \left( \frac{G}{1 + \lambda \tau} \frac{d Q_0(y)}{d y} + \frac{H}{2 (2 + \lambda \tau)} \frac{d^2 Q_0(y)}{d y^2} \right),
$$

Appendix A.3, first homogeneous solution (confluent hypergeometric function $M$):

$$
\phi_1(y, \lambda) = M\left[ (1 - \lambda \tau)/2,\, 1/2,\, -y^2 \right],
$$

Appendix A.3, second homogeneous solution:

$$
\phi_2(y, \lambda) = \frac{\sqrt{\pi}}{\Gamma\left( \frac{1 + \lambda \tau}{2} \right)} M\left( \frac{1 - \lambda \tau}{2}, \frac{1}{2}, -y^2 \right) + \frac{\sqrt{\pi}}{\Gamma\left( \frac{\lambda \tau}{2} \right)} 2 y M\left( 1 - \frac{\lambda \tau}{2}, \frac{3}{2}, -y^2 \right),
$$

Appendix A.3, Wronskian of the two homogeneous solutions:

$$
\mathrm{Wr}(\phi_1, \phi_2) \equiv \phi_1 \phi_2' - \phi_1' \phi_2 = \frac{2 \sqrt{\pi}}{\Gamma(\lambda/2)} \exp(-y^2),
$$

Appendix A.3, unnumbered reduced functions used by the eigenfrequency condition:

$$
\tilde{\phi} = \frac{\phi_2}{\mathrm{Wr}}, \qquad \tilde{W}(y_\theta) = \frac{\hat{Q}_1^p \phi_2' - \hat{Q}_1^{p'} \phi_2}{\mathrm{Wr}}(y_\theta), \qquad W(y_r) = \left[ \frac{\hat{Q}_1^p \phi_2' - \hat{Q}_1^{p'} \phi_2}{\mathrm{Wr}} \right]_{y_r^-}^{y_r^+},
$$

Appendix A.3, eigenfrequency equation:

$$
\tilde{\phi}(y_\theta) \left( 1 - H e^{-\lambda D} \right) - \tilde{\phi}(y_r) \left( e^{-\lambda \tau_{rp}} - H e^{-\lambda D} \right) = \tilde{W}(y_\theta) - \tilde{W}(y_r),
$$

Appendix A.3, Hopf form with $\lambda = i \omega_c$:

$$
1 - H e^{-i \omega_c D} - R(\omega_c) \left[ e^{-i \omega_c \tau_{rp}} - H e^{-i \omega_c D} \right] = S(y_\theta, \omega_c) - R(\omega_c) S(y_r, \omega_c),
$$

Appendix A.3, unnumbered ratio definition of the auxiliary function $\psi$:

$$
\psi(y, \omega) = \frac{\phi_2'(y, \omega)}{\phi_2(y, \omega)},
$$

Appendix A.3, unnumbered definitions of the remaining auxiliary functions:

$$
R(\omega) = \frac{\tilde{\phi}(y_r, \omega)}{\tilde{\phi}(y_\theta, \omega)} = \exp\left( y_r^2 - y_\theta^2 + \int_{y_\theta}^{y_r} \psi(y, \omega)\, dy \right), \qquad S(y, \omega) = e^{-i \omega D} \left[ G \frac{-\psi(y, \omega) - 2 y}{1 + i \omega} + H \frac{y \psi(y, \omega) - 2 (1 - y^2)}{2 + i \omega} \right],
$$

Appendix A.3, large-$y$ and/or large-$\omega$ asymptotics of $\psi$:

$$
\psi(y, \omega) \sim -y + \sqrt{y^2 + 2 i \omega} + O(1/y, 1/\sqrt{\omega})
$$

$$
\sim -y + |y| \quad \text{for } |y| \ll \sqrt{\omega}
$$

$$
\sim -y + (1 + i) \sqrt{\omega} \quad \text{for } \sqrt{\omega} \ll |y|,
$$

Appendix A.3, high-frequency form of the Hopf condition:

$$
e^{i \omega_c \delta} - H = (i - 1) \frac{G - H y_\theta}{\sqrt{\omega_c}},
$$

Appendix A.3, unnumbered real conditions on $G$ and $H$ implied by the high-frequency root:

$$
G = \sqrt{\omega_c} \sin(\omega_c D), \qquad H = \sin(\omega_c D) + \cos(\omega_c D),
$$

Appendix A.3, unnumbered first branch solution and the stationary-rate estimate used with it:

$$
\omega_c \sim \frac{\pi \tau}{2 D}, \qquad G \sim \sqrt{\frac{\pi \tau}{2 D}}, \qquad H \sim 1, \qquad \nu_0 \sim \frac{\nu_{ext} - \nu_{thr}}{g \gamma - 1},
$$

Appendix A.3, approximate instability line in the plane $(\nu_{ext}/\nu_{thr}, g)$ with the unnumbered definition of $K$ printed below it:

$$
\frac{\nu_{ext}}{\nu_{thr}} = 1 + \frac{\pi}{4 K} \frac{g (1 + g) \gamma}{g \gamma - 1} + \sqrt{ \frac{\pi^2}{16 K^2} \left( \frac{g (1 + g) \gamma}{g \gamma - 1} \right)^2 + \frac{\pi}{2 K} }, \qquad K = D C_E \nu_{thr} = \frac{D \theta}{\tau J},
$$

Appendix A.3, unnumbered second family of solutions:

$$
\omega_c \sim \frac{2 \pi k \tau}{D}, \qquad G \sim -(1 - H) \sqrt{\frac{2 \pi k \tau}{D}},
$$

Appendix A.4, unnumbered replacement for a wide distribution of delays $P(D)$:

$$
\int P(D) e^{-\lambda D} d\, D,
$$

Appendix A.5, Fourier-domain eigenmode equation with the finite-size noise:

$$
i \omega \tau \hat{Q}_1(y, \omega) = \mathcal{L}[\hat{Q}_1]\,(y, \omega) + e^{-i \omega D} \hat{n}_1(\omega) \times \left( G \frac{d Q_0}{d y} + \frac{H}{2} \frac{d^2 Q_0}{d y^2} \right) + \sqrt{\epsilon \tau} H \hat{\zeta}(\omega) \frac{d Q_0}{d y},
$$

Appendix A.5, unnumbered floating display for the linear-response term (printed between rules with $\lambda$ exponents although the surrounding Fourier analysis uses $\omega$):

$$
Z(\omega) = \frac{\tilde{W}_r(y_\theta) - \tilde{W}_r(y_r)}{\tilde{\phi}(y_\theta) (1 - H e^{-\lambda D}) - \tilde{\phi}(y_r) (e^{-\lambda \tau_{rp}} - H e^{-\lambda D}) - \tilde{W}(y_\theta) + \tilde{W}(y_r)},
$$

Appendix A.5, unnumbered boundary conditions of the Fourier problem (both pairs are printed at $y_\theta$ and the final exponential is printed as $\exp(-\omega_c \delta)$):

$$
\hat{Q}_1(y_\theta, \omega) = 0, \quad \frac{\partial \hat{Q}_1}{\partial y}(y_\theta) = \hat{n}_1(\omega) \left[ -1 + H \exp(-i \omega D) \right],
$$

$$
\hat{Q}_1(y_\theta, \omega) = 0, \quad \frac{\partial \hat{Q}_1}{\partial y}(y_\theta) = \hat{n}_1(\omega) \left[ -\exp(-i \omega \tau_{rp}) + H \exp(-\omega_c \delta) \right],
$$

Appendix A.5, solution of the Fourier problem:

$$
\hat{Q}_1(y, \omega) = \begin{cases} \alpha_1^+ \phi_1(y, i \omega) + \beta_1^+ \phi_2(y, i \omega) + \hat{n}_1(\omega) \hat{Q}_1^p(y, i \omega) + \hat{\zeta} \hat{R}_1^p(y, i \omega) & y > y_r \\ \alpha_1^- \phi_1(y, i \omega) + \beta_1^- \phi_2(y, i \omega) + \hat{n}_1(\omega) \hat{Q}_1^p(y, i \omega) + \hat{\zeta} \hat{R}_1^p(y, i \omega) & y < y_r \end{cases},
$$

Appendix A.5, particular solution driven by the finite-size noise:

$$
\hat{R}_1^p(y, i \omega) = \frac{\sqrt{\epsilon \tau} H}{1 + i \omega \tau} \frac{d Q_0(y)}{d y},
$$

Appendix A.5, unnumbered linear relation between the Fourier transforms of the global activity and the finite-size noise:

$$
\hat{n}_1(\omega) = Z(\omega) \hat{\zeta}(\omega),
$$

Appendix A.5, unnumbered Wronskian combinations built from $\hat{R}_1^p$:

$$
\tilde{W}_r(y_\theta) = \frac{\hat{R}_1^p \phi_2' - \hat{R}_1^{p'} \phi_2}{\mathrm{Wr}}(y_\theta), \qquad W_r(y_r) = \left[ \frac{\hat{R}_1^p \phi_2' - \hat{R}_1^{p'} \phi_2}{\mathrm{Wr}} \right]_{y_r^-}^{y_r^+},
$$

Appendix A.5, rewritten form of the linear-response term:

$$
Z(\omega) = \left( \frac{\sqrt{\epsilon \tau} H}{1 + i \omega \tau} \right) \frac{-\psi(y_\theta, \omega) - 2 y_\theta - R(\omega) \left( -\psi(y_r, \omega) - 2 y_r \right)}{1 - H e^{-i \omega D} - R(\omega) \left[ e^{-i \omega \tau_{rp}} - H e^{-i \omega D} \right] - S(y_\theta, \omega) + R(\omega) S(y_r, \omega)},
$$

Appendix A.5, power spectrum of the global activity:

$$
P(\omega) = Z(\omega) Z(-\omega),
$$

Appendix A.5, large-$\omega$ form of the power spectrum:

$$
P(\omega) = \frac{2 \epsilon H}{\omega \tau \left( 1 - 2 H \cos(\omega D) + H^2 \right) + 2 \sqrt{\omega \tau} G \left( \cos(\omega D) - \sin(\omega D) - H \right) + 2 G^2},
$$

Appendix B, unnumbered model-B rescaling definition:

$$
P_a = \frac{2 \tau_a \nu_{a0}}{\sigma_{a0}} Q_a, \quad a = E, I,
$$

Appendix B, unnumbered model-B recurrent-coupling definitions ($G_{aI}$ shown with its companion):

$$
G_{aE} = \frac{\sqrt{C_E \tau_a} \nu_{E0}}{\sqrt{\nu_{a,ext} + \nu_{E0} + g_a^2 \gamma \nu_{I0}}},
$$

$$
G_{aI} = \frac{g_a \gamma \sqrt{C_E \tau_a} \nu_{I0}}{\sqrt{\nu_{a,ext} + \nu_{E0} + g_a^2 \gamma \nu_{I0}}}, \quad a = E, I,
$$

Appendix B, unnumbered model-B variance-share definitions:

$$
H_{aE} = \frac{\nu_{E0}}{\nu_{a,ext} + \nu_{E0} + g_a^2 \gamma \nu_{I0}},
$$

$$
H_{aI} = \frac{g_a^2 \gamma \nu_{E0}}{\nu_{a,ext} + \nu_{E0} + g_a^2 \gamma \nu_{I0}}, \quad a = E, I,
$$

Appendix B, unnumbered model-B ordinates and rate fluctuation:

$$
y_a = \frac{V - \mu_{a0}}{\sigma_{a0}}, \quad y_{a\theta} = \frac{\theta - \mu_{a0}}{\sigma_{a0}}, \quad y_{ar} = \frac{V_r - \mu_{a0}}{\sigma_{a0}}, \quad \nu_a = \nu_{a0} (1 + n_a(t)), \quad a = E, I,
$$

Appendix B, rescaled Fokker-Planck equations for the two populations (the perturbation is printed as $\nu_b(t - D_{ab})$):

$$
\tau_a \frac{\partial Q_a}{\partial t} = \mathcal{L}[Q_a] + \sum_{b = E, I} \nu_b(t - D_{ab}) \times \left( s_b G_{ab} \frac{\partial Q_a}{\partial y_a} + \frac{H_{ab}}{2} \frac{\partial^2 Q_a}{\partial y_a^2} \right),
$$

Appendix B, threshold boundary condition (model B):

$$
Q_a(y_{a\theta}, t) = 0, \qquad \frac{\partial Q_a}{\partial y_a}(y_{a\theta}, t) = -\frac{1 + n_a(t)}{1 + H_{aE} n_E(t - D_{aE}) + H_{aI} n_I(t - D_{aI})},
$$

Appendix B, reset boundary condition (model B):

$$
\left[ Q_a \right]_{y_{ar}^-}^{y_{ar}^+} = 0, \qquad \left[ \frac{\partial Q_a}{\partial y_a} \right]_{y_{ar}^-}^{y_{ar}^+} = -\frac{1 + n_a(t - \tau_{rp})}{1 + H_{aE} n_E(t - D_{aE}) + H_{aI} n_I(t - D_{aI})},
$$

Appendix B, linearized equation at first order (the perturbation is printed as $n_{a1}(t - D_{ab})$):

$$
\tau_a \frac{\partial Q_{a1}}{\partial t} = \mathcal{L}[Q_{a1}] + \sum_{b = E, I} n_{a1}(t - D_{ab}) \times \left( s_b G_{ab} \frac{d Q_{a0}}{d y_a} + \frac{H_{ab}}{2} \frac{d^2 Q_{a0}}{d y_a^2} \right),
$$

Appendix B, linearized threshold boundary condition:

$$
Q_{a1}(y_{a\theta}, t) = 0, \qquad \frac{\partial Q_{a1}}{\partial y_a}(y_{a\theta}) = -n_{a1}(t) + \sum_{b = E, I} H_{ab} n_{b1}(t - D_{ab}),
$$

Appendix B, linearized reset boundary condition:

$$
\left[ Q_{a1} \right]_{y_{ar}^-}^{y_{ar}^+} = 0, \qquad \left[ \frac{\partial Q_{a1}}{\partial y_a} \right]_{y_{ar}^-}^{y_{ar}^+} = -n_{a1}(t - \tau_{rp}) + \sum_{b = E, I} H_{ab} n_{b1}(t - D_{ab}),
$$

Appendix B, unnumbered eigenmode ansatz:

$$
Q_{a1}(y_a, t) = \exp(\lambda t) \hat{Q}_a(y_a, \lambda), \qquad n_{a1}(t) = \exp(\lambda t) \hat{n}_a(\lambda),
$$

Appendix B, ordinary differential equation for the eigenmodes (printed with $e^{-\lambda D_b}$, $\hat{n}_b$, $s_b G_b$, $H_b$, and an extra $\sqrt{\tau_a}$ factor):

$$
\lambda \tau_a \hat{Q}_a(y, \lambda) = \mathcal{L}[\hat{Q}_a]\,(y_a, \lambda) + \sum_b e^{-\lambda D_b} \times \hat{n}_b \left( s_b G_b \sqrt{\tau_a} \frac{d Q_{a0}}{d y_a} + \frac{H_b}{2} \frac{d^2 Q_{a0}}{d y_a^2} \right),
$$

Appendix B, unnumbered boundary conditions of the model-B eigenmode problem (both pairs are printed at $y_{a\theta}$, the first sum is printed with $H_b \exp(-\lambda D_b)$, and the conditions carry a stray time argument $t$):

$$
\hat{Q}_a(y_{a\theta}, t) = 0, \quad \frac{\partial \hat{Q}_a}{\partial y_a}(y_{a\theta}) = -\hat{n}_a + \sum_b H_b \hat{n}_b \exp(-\lambda D_b),
$$

$$
\hat{Q}_a(y_{a\theta}, t) = 0, \quad \frac{\partial \hat{Q}_a}{\partial y_a}(y_{a\theta}) = -\hat{n}_a \exp(-\lambda \tau_{rp}) + \sum_b H_{ab} \hat{n}_b \exp(-\lambda D_{ab}),
$$

Appendix B, general solution of the model-B eigenmode equation:

$$
\hat{Q}_a(y_a, \lambda) = \begin{cases} \alpha_a^+(\lambda) \phi_1(y_a, \lambda) + \beta_a^+(\lambda) \phi_2(y_a, \lambda) + \hat{Q}_a^p(y_a, \lambda) & y_a > y_{ar} \\ \alpha_a^-(\lambda) \phi_1(y_a, \lambda) + \beta_a^-(\lambda) \phi_2(y_a, \lambda) + \hat{Q}_a^p(y_a, \lambda) & y_a < y_{ar} \end{cases},
$$

Appendix B, particular solution as a sum over driving populations:

$$
\hat{Q}_a^p(y_a, \lambda) = \sum_b \hat{Q}_{ab}^p(y_a, \lambda) \hat{n}_b,
$$

Appendix B, per-link particular solution:

$$
\hat{Q}_{ab}^p(y_a, \lambda) = e^{-\lambda D_{ab}} \left( \frac{s_b G_{ab}}{1 + \lambda \tau_a} \frac{d Q_{a0}(y_a)}{d y_a} + \frac{H_{ab}}{2 (2 + \lambda \tau_a)} \frac{d^2 Q_{a0}(y_a)}{d y_a^2} \right),
$$

Appendix B, linear system for the two rate amplitudes:

$$
A_{EE} \hat{n}_E + A_{EI} \hat{n}_I = 0, \qquad A_{IE} \hat{n}_E + A_{II} \hat{n}_I = 0,
$$

Appendix B, matrix entry for matching populations:

$$
A_{aa} = \tilde{\phi}(y_{a\theta}) - \tilde{\phi}(y_{ar}) e^{-\lambda \tau_{rp}} - H_{aa} e^{-\lambda D_{aa}} \left[ \tilde{\phi}(y_{a\theta}) - \tilde{\phi}(y_{ar}) \right] - \tilde{W}_{aa}(y_{a\theta}) + \tilde{W}_{aa}(y_{ar}),
$$

Appendix B, matrix entry for distinct populations:

$$
A_{ab} = -H_{ab} e^{-\lambda D_{ab}} \left[ \tilde{\phi}(y_{a\theta}) - \tilde{\phi}(y_{ar}) \right] - \tilde{W}_{ab}(y_{a\theta}) + \tilde{W}_{ab}(y_{ar}), \quad a \neq b,
$$

Appendix B, unnumbered Wronskian combinations of the model-B particular solutions:

$$
\tilde{W}_{ab}(y_\theta) = \frac{\hat{Q}_{ab}^p \phi_2' - \hat{Q}_{ab}^{p'} \phi_2}{\mathrm{Wr}}(y_\theta), \qquad W(y_r) = \left[ \frac{\hat{Q}_{ab}^p \phi_2' - \hat{Q}_{ab}^{p'} \phi_2}{\mathrm{Wr}} \right]_{y_r^-}^{y_r^+},
$$

Appendix B, eigenvalue condition:

$$
\det(A) = A_{EE} A_{II} - A_{IE} A_{EI} = 0,
$$

Appendix B, unnumbered population-amplitude relation on the bifurcation line:

$$
\hat{n}_I = -\frac{A_{EE}}{A_{EI}} \hat{n}_E,
$$

Appendix B, symmetric-population simplification of the Hopf condition (stated for $g_I = g_E \equiv g$, $\nu_{E,ext} = \nu_{I,ext} \equiv \nu_{ext}$, $D_{EE} + D_{II} = D_{EI} + D_{IE}$, and $\omega_c \gg y_r^2, y_\theta^2$; the signs $s_E = -1$, $s_I = 1$ are introduced before equation (57)):

$$
1 - \sum_a H_{aa} e^{-i \omega_c D_{aa}} = (i - 1) \sum_{aa} e^{-i \omega_c D_{aa}} \frac{s_a G_{aa}}{\sqrt{\omega_c}},
$$

Appendix B, unnumbered population ratio in the symmetric case:

$$
\hat{n}_I = \exp \left[ i \omega_c (D_{EI} - D_{II}) \right] \hat{n}_E,
$$

Appendix B, inhibition-dominated limit (any parameters, $\nu_I \gg \nu_E$, $\omega_c \gg y_r^2, y_\theta^2$) and the resulting frequency estimate:

$$
1 - H_{II} e^{-i \omega_c D_{II}} = (i - 1) e^{-i \omega_c D_{II}} \frac{G_{II}}{\sqrt{\omega_c}}, \qquad f \sim \frac{\pi}{2 D_{II}},
$$

Appendix B, oscillatory behavior of the excitatory population:

$$
\hat{n}_E = \exp \left( -i \frac{\pi}{2} \frac{D_{EI}}{D_{II}} \right) \left[ \frac{g_I \bar{\sigma}_E - g_E \bar{\sigma}_I + i g_E \bar{\sigma}_I}{g_I \bar{\sigma}_E} \right] \hat{n}_I,
$$

Appendix B, unnumbered definition of $\bar{\sigma}_a$:

$$
\bar{\sigma}_a = \sqrt{\nu_{a,ext} + \nu_{E0} + g_a^2 \gamma \nu_{I0}},
$$

Appendix B, phase lag between interneurons and excitatory cells (general inhibition-dominated form):

$$
\Delta \phi = \frac{\pi}{2} \frac{D_{EI}}{D_{II}} + \mathrm{Arctg} \left( \frac{g_E \bar{\sigma}_I}{g_E \bar{\sigma}_I - g_I \bar{\sigma}_E} \right),
$$

Appendix B, phase lag in the symmetric case ($g_E = g_I$, $\nu_{E,ext} = \nu_{I,ext}$):

$$
\Delta \phi = \omega_c (D_{EI} - D_{II}),
$$

## Term-by-term interpretation

Equations (1)-(2) define the network: a leaky integrate-and-fire membrane with membrane time constant $\tau$ and resistance $R$, driven by delayed delta-function spike contributions whose efficacy is $J_{ij} = J$ for excitatory (recurrent and external) synapses and $-gJ$ for inhibitory ones; a spike arriving at $t_j^k + D$ acts instantaneously, so $J$ is the peak postsynaptic potential. The threshold/reset rule (spike at $\theta$, reset to $V_r$ after refractory period $\tau_{rp}$) is stated in prose after equation (2) and is not written as a display. Equations (3)-(5) implement the diffusion approximation: when each neuron receives many small inputs ($J \ll \theta$), the current splits into a mean part proportional to the delayed rate $\nu(t - D)$ and a Gaussian fluctuation whose variance counts excitatory, inhibitory, and external Poisson arrivals. Equations (6)-(8) convert the stochastic membrane equation into a Fokker-Planck equation, a continuity form, and the probability current whose value at $\theta$ is the instantaneous rate $\nu(t) = S(\theta, t)$. Equations (9)-(12) are the absorbing threshold condition, the reset derivative jump carrying neurons that exit the refractory state, integrability at $-\infty$, and normalization including the refractory fraction $p_r(t)$. Equations (13)-(18) repeat the construction for model B, where each population $a$ has its own time constant $\tau_a$, efficacy $J_a$, inhibitory strength $g_a$, external rate $\nu_{a,ext}$, and delays $D_{ab}$; the two Fokker-Planck equations couple only through the delayed rates in $\mu_a$ and $\sigma_a$.

Equation (19) is the stationary distribution: a Gaussian factor times an integral of $e^{u^2}$ truncated by the Heaviside function $\Theta(u - V_r)$, which keeps the integral finite through the upper limit $(\theta - \mu_0)/\sigma_0$ and implements the reset floor. Equation (20) gives the stationary input moments and equation (21) the self-consistency condition (mean first-passage time of a diffusion-model integrate-and-fire neuron), whose low-rate asymptotics is (22); the unnumbered $\nu_{thr} = \theta/(C_E J \tau)$ defines the external-rate unit (the same quantity appears inline on p. 185 as $\theta/(J C_E \tau)$). Equations (23) and (24) are the leading-$1/C_E$ estimates of the stationary rate in the excitation-dominated and inhibition-dominated regimes; the gain $1/(g\gamma - 1)$ of (24) explains the quasi-linear rate curves of Fig. 1B. Equations (25)-(27) repeat equations (19)-(21) for the two model-B populations. Equation (28) rescales $P$, $V$, and $\nu$ around the stationary state; equation (29) shows that the perturbation $n(t - D)$ enters through two recurrent-strength measures $G$ and $H$ of equation (30) ($G$ is positive when inhibition dominates), and equation (31) transports the boundary conditions to $y_\theta$ and $y_r$. The stability boundaries of the phase diagrams of Fig. 2 are the Hopf lines obtained from the eigenfrequency equation (46) (or its Hopf form (47)); the saddle-node lines come from the stationary system (20)-(21). The three qualitative branches are analyzed via the asymptotics (48)-(50) and the high-frequency root (51): fast delay-controlled oscillations with $G \sim \sqrt{\tau/D}$ and $f \sim 1/4D$ (Section 5.1.1), slow membrane-controlled oscillations near $\nu_{ext} \sim \nu_{thr}$ (Section 5.1.2), and very fast $k/D$ oscillations near the balanced point $g = 4$ (Section 5.1.3), with an approximate instability line given after (51) in terms of $K = D\theta/(\tau J)$. A wide delay distribution (Appendix A.4) drastically expands the stability region of the asynchronous state (Fig. 4), and removing the external noise leaves it almost unchanged (Section 5.3), so irregularity is an intrinsic effect of the random wiring.

Equations (32)-(33) and the Appendix A.5 system quantify finite-size effects: the sparse wiring contributes two stochastic terms, a private Gaussian white noise of magnitude $\sigma \sqrt{\tau}$ and a global noise $\sqrt{\epsilon C \nu_0 \tau} \sqrt{\tau}\, \xi(t)$ from the Poisson fluctuation of the total spike count. The global noise enters the rescaled equation (32) as $\sqrt{\epsilon \tau} H \zeta(t) \partial Q / \partial y$, producing (i) a damped oscillatory autocorrelation of the global activity in the asynchronous irregular state, with spectrum $P(\omega) = Z(\omega) Z(-\omega)$ of equations (55) and (33)/(56), whose peak amplitude is linear in $\epsilon$ (Fig. 9), and (ii) phase diffusion of the global oscillation beyond the Hopf lines, with a coherence time linear in $N/C$. Appendix A.1 supplies the interspike-interval moments and the CV of the asynchronous states (Fig. 1C: CV near zero for $g < 4$, jumping above 2 near $g = 4$, approaching 1 at very low rates). Appendix B generalizes the linear stability to model B; equation (65) is the two-population eigenvalue condition, and the phase-lag results follow from the ratio $\hat{n}_I / \hat{n}_E$ on the bifurcation line: in the fast symmetric case the lag is $\omega_c (D_{EI} - D_{II})$, controlled by the inhibitory delays.

Printed slips flagged (transcribed exactly as printed above): equation (17) carries the plain $\tau$ in the numerator where the parallel equation (16) has $\tau_a$; the second pair of boundary conditions printed after equations (40) and (52) repeats the threshold argument $y_\theta$ where the reset argument $y_r$ is required by equations (39) and (58)-(59), and their last exponentials read $\exp(-\lambda \tau)$ and $\exp(-\omega_c \delta)$ where the parallel structure requires $\exp(-\lambda D)$ and $\exp(-i \omega D)$; the unnumbered ansatz line prints $n_1(t) = \exp(\lambda t), \hat{n}_1(\lambda)$ with a comma instead of the product written on the preceding line; the prose homogeneous equation on p. 202 reads $(1 - \lambda) \phi = 0$ while p. 203 reads $(1 - \lambda \tau) \phi = 0$, the latter being consistent with equation (40); the floating $Z(\omega)$ display of Appendix A.5 is printed with $\lambda$ exponents although the surrounding Fourier analysis uses $\omega$; the model-B definitions print $H_{aI} = g_a^2 \gamma \nu_{E0}/(\cdot)$ where the denominator bookkeeping of equations (58)-(59) requires $\nu_{I0}$ in the numerator; equation (57) is printed with the unperturbed rate $\nu_b(t - D_{ab})$ where the perturbation $n_b(t - D_{ab})$ is required by the parallel equation (29); equation (60) is printed with $n_{a1}(t - D_{ab})$ where the $b$-sum requires $n_{b1}$ (as in equations (61)-(62)); and equation (63) with its boundary conditions is printed with the abbreviations $D_b$, $G_b$, $H_b$ and an extra $\sqrt{\tau_a}$ factor where equations (60)-(62) and the particular solution following equation (64) carry $D_{ab}$, $G_{ab}$, $H_{ab}$ without the factor. The repetition of the power-spectrum approximation as both equation (33) (Section 6.2) and equation (56) (Appendix A.5) is present in the source, as is the symbol reuse of $S$ for both the probability current $S(V, t)$ and the Hopf auxiliary $S(y, \omega)$ and of $R$ for both the membrane resistance and the auxiliary $R(\omega)$.

## Inputs, outputs, and conditions

- Input: external Poisson rates $\nu_{ext}$ (model A) or $\nu_{E,ext}$, $\nu_{I,ext}$ (model B) on $C_{ext}$ synapses per neuron.
- Output: stationary rates $\nu_0$, $\nu_{a0}$ and CV of the asynchronous states; stability boundaries (saddle-node and Hopf lines) of the phase diagram in the plane $(g, \nu_{ext})$; frequency and phase of the global oscillation; finite-size spectrum of the global activity.
- Initial conditions: `not_verified`.
- Boundary conditions: `registered`; locator: equations (9)-(11) for model A, (16)-(18) for model B, (31) rescaled, (58)-(59) for model B rescaled, with the eigenmode conditions after equations (40), (52), and (63).
- Network conditions: `source_located`; locator: Section 2 (each neuron receives $C = C_E + C_I + C_{ext}$ inputs with $C_E = \epsilon N_E$, $C_I = \gamma C_E$, $C_{ext} = C_E$; fixed in-degree sparse wiring with $\epsilon \ll 1$; PSP amplitudes $J$ and $-gJ$; single delay $D$ or four delays $D_{ab}$; independent Poisson processes on external synapses).
- Event handling: `source_located`; locator: Section 2, after equation (2) (spike emitted when $V_i$ reaches $\theta$; depolarization reset to $V_r$ after a refractory period $\tau_{rp}$ during which the potential is insensitive to stimulation).
- Numerical method: `not_verified`; locator: Sections 4.1 and 6 (stationary equations "solved numerically"; simulations of Fig. 8 report instantaneous rates in 0.1 ms bins; no integrator is named).
- Stochastic input: `stochastic` (Poisson external synapses approximated by Gaussian fluctuations; intrinsic stochasticity of the random wiring persists without external noise, Section 5.3).
- Simulation scale: `large_scale_network` (12,500 neurons: $N_E = 10{,}000$, $N_I = 2{,}500$, $\epsilon = 0.1$, $J = 0.1$ mV, $C_E = 1000$, $D = 1.5$ ms). The four simulated states are A $(g, \nu_{ext}/\nu_{thr}) = (3, 2)$ strongly synchronized regular; B $(6, 4)$ fast oscillation with irregular singles; C $(5, 2)$ asynchronous irregular; D $(4.5, 0.9)$ slow oscillation at very low rates. Table 1 compares simulation and theory in the inhibition-dominated regimes: B firing 60.7 Hz vs 55.8 Hz and global 180 Hz vs 190 Hz; C firing 37.7 Hz vs 38.0 Hz; D firing 5.5 Hz vs 6.5 Hz and global 22 Hz vs 29 Hz.

## Assumptions and limitations

The analytical results rest on the diffusion approximation (many small inputs per membrane time constant, $J \ll \theta$), on neglecting input correlations beyond the shared instantaneous rate ($C/N \to 0$), and on a single synaptic time scale, the delay $D$; the source itself notes that realistic synapses add rise and decay times whose role is left open. The calculations do not describe states with correlations beyond a common $\nu(t)$, so the strongly synchronized state A is outside their scope even though the analysis predicts the transition toward it. The mean-field description is exact only for $N \to \infty$; finite-size corrections are computed to first order in $\epsilon = C/N$. Parameter estimates borrow cortical anatomy ($N_E = 0.8N$, fixed in-degree sparsity) without asserting a universal cortical circuit. The printed slips listed in the interpretation are propagated unchanged.

## Experimental support

`not assessed`. The source discusses qualitative correspondences with hippocampal and cortical field-and-unit recordings (Section 7.1), including fast sharp-wave-like and slow gamma-like oscillation bands, but no quantitative validation status is recorded here; this status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`; a ModelDB entry (model 42020) and several community reimplementations are associated with this paper but have not been audited for this record.
