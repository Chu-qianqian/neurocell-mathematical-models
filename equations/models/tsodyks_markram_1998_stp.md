# Tsodyks-Pawelzik-Markram dynamic-synapse model

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: full-text PDF of the published article (MIT Press typesetting, pages 821-835, mirrored on a university course site), with every numbered equation checked against the rendered page images.
- Source locator: Section 2 equations (2.1)-(2.3) with an unnumbered steady-state display; Section 3 equations (3.1)-(3.7); Section 4 equations (4.1)-(4.5) with equation (4.4) inside the Figure 3 caption; Appendix equations (A.1)-(A.4).
- Transcription status: exact source transcription; one printed subscript inconsistency is transcribed exactly and flagged in the interpretation.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-28.

## Scope

- Biological cell scope: `synaptic`.
- Cell type: `synapse`.
- Cell subtype: neocortical interpyramidal (depressing) and pyramidal-to-interneuron (facilitating) synapses represented by a three-state (recovered/active/inactive) vesicle-resource kinetic scheme with activity-dependent utilization.
- Nervous-system region: `not_assessed` (neocortex used only as the experimental setting of the source data).
- Model scope: `cell_function`.
- Model scale: `subcellular` for the single-synapse scheme; the mean-field extension in equation (4.1) covers coupled neural populations.
- Mathematical form: `hybrid` (linear ODEs between spikes with delta-function spike-driven jumps; Poisson-averaged rate dynamics; Wilson-Cowan-type population equations).
- Interaction scope: `synaptic`.
- Network type: `firing_rate_network` for the mean-field section (4.1).
- Spatial structure: `nonspatial`.
- Stochasticity: `deterministic` at the level of the displayed equations; the derivation averages over Poisson spike trains and the source checks the resulting correlations.
- Plasticity scope: `short_term_synaptic`.

## Source citation

Misha Tsodyks; Klaus Pawelzik; Henry Markram. Neural Networks with Dynamic Synapses. *Neural Computation* **10**(4), 821-835 (1998). [DOI](https://doi.org/10.1162/089976698300017502). [PubMed](https://pubmed.ncbi.nlm.nih.gov/9573407/).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $x$ | fraction of resources in the recovered state | dimensionless | source-verified |
| $y$ | fraction of resources in the active state | dimensionless | source-verified |
| $z$ | fraction of resources in the inactive state | dimensionless | source-verified |
| $t_{sp}$ | arrival time of a presynaptic spike | ms | source-verified |
| $I_s(t)$ | postsynaptic current, $I_s(t) = A_{SE} y(t)$ | pA | source-verified |
| $U_{SE}$ | utilization of synaptic efficacy activated by each spike | dimensionless | source-verified |
| $U_{SE}^1$ | running value of the utilization under facilitation | dimensionless | source-verified |
| $U_{SE}^-$ | average value of $U_{SE}^1$ immediately before a spike | dimensionless | source-verified |
| $\langle x \rangle$, $\langle y \rangle$, $\langle U_{SE}^1 \rangle$, $\langle U_{SE}^- \rangle$ | Poisson-train averages of the resource fractions and utilization | dimensionless | source-verified |
| $r(t)$ | instantaneous rate of the presynaptic Poisson train | Hz | source-verified |
| $U_{SE}^{1(n)}$ | value of $U_{SE}^1$ reached upon the arrival of the $n$-th spike | dimensionless | source-verified |
| $\delta t$ | interval between the $n$-th and $(n+1)$-th spikes | ms | source-verified |
| $\lambda$ | limiting frequency of rate signaling, $\lambda \sim 1/(U_{SE}\tau_{rec})$ | Hz | source-verified |
| $\theta$ | peak frequency of the facilitating-synapse response (equation (3.6)) | Hz | source-verified |
| $\theta$ | threshold of the linear-threshold gain function (equation (4.4)); symbol reused from equation (3.6) | mV | source-verified |
| $E_r$, $I_r$ | firing rates of excitatory and inhibitory populations at site $r$ | Hz | source-verified |
| $y_{r'}^{ab}$, $y_{rr'}^{ab}$ | population-averaged active fraction for connection type $ab$ (printed with presynaptic-only index in the first term of each line of (4.1) and double index in the second term) | dimensionless | source-verified |
| $g(x)$ | monotonically increasing population response function | Hz | source-verified |
| $E$, $x$ | rate and recovered fraction of the one-population network | Hz; dimensionless | source-verified |
| $E^*$, $x^*$ | values of $E$ and $x$ at the fixed point | Hz; dimensionless | source-verified |
| $\beta$ | slope of the linear-threshold gain function, $\beta = g'(J U_{SE} x^* E^*)$ | mV$^{-1}$Hz | source-verified |
| $CV_x$, $CV_U$ | coefficients of variation of $x$ and $U^1$ | dimensionless | source-verified |
| $V$ | postsynaptic membrane potential of the passive target model used in Figure 1 | mV | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $\tau_{rec}$ | recovery time constant of the resources | ms | 800 (depressing example); 130 (facilitating examples); 600 ($ie$); 850 ($ii$) | Figure 1; Figure 4 |
| $\tau_{in}$ | inactivation time constant of active resources (printed $\tau_{inact}$ in the Figure 1 caption) | ms | 3 (depressing example); 1.5 (facilitating examples) | Section 2; Figure 1 |
| $\tau_{facil}$ | decay time constant of the facilitation factor | ms | 530 (facilitating examples); 1000 ($ie$); 400 ($ii$) | Figure 1; Figure 4 |
| $U_{SE}$ | increment of utilization per spike; coincides with $U_{SE}^1$ after the first spike | dimensionless | 0.5 (depressing example, $ee$ and $ei$); 0.03 (facilitating examples, $ii$); 0.05 ($ie$); range 0.01 to 0.05 for facilitating synapses | Section 2.1; Figures 1 and 4 |
| $A_{SE}$ | absolute synaptic strength | pA | 250 (depressing example and Figure 2); 1540 (facilitating examples) | Section 2; Figure 1 |
| $\tau_{mem}$, $R_{in}$ | membrane time constant and input resistance of the passive target in Figure 1 | ms; resistance | 40 ms and 100 Mohm (pyramidal target); 60 ms and 1 Gohm (interneuron target) | Figure 1 caption |
| $\tau$, $\tau_e$, $\tau_i$ | population time constants of the mean-field equations | ms | $\tau$ = 30 (Figure 3); $\tau_e$ = 30; $\tau_i$ = 40 (Figure 4) | Figure 3; Figure 4 |
| $J$ | effective synaptic strength of the one-population network (absorbs $\tau_{in}$) | mV/Hz | 60 | Figure 3 |
| $J_{rr'}^{ee}$, $J_{rr'}^{ei}$, $J_{rr'}^{ie}$, $J_{rr'}^{ii}$ | absolute strengths of the four connection types (strength times average connection number) | mV/Hz | 50 ($ee$); 40 ($ei$); 70 ($ie$); 19.5 ($ii$) | Section 4; Figure 4 |
| $\beta$ | gain slope of the linear-threshold response | mV$^{-1}$Hz | 0.5 | Figure 3 |
| $\theta$ | threshold of the linear-threshold response | mV | 15 | Figure 3 |
| $I_r^e$, $I_r^i$ | external inputs to the two populations | mV | 17; 15 | Figure 4 |
| $N$ | number of simulated presynaptic neurons in Figure 2 | count | 1000 | Figure 2 caption |
| stimulus frequencies | regular train and step-transition frequencies of the illustrations | Hz | 20 and 70 (Figure 1); steps 0-15-30-80 (Figure 2) | Figures 1-2 |

## Equations

These are exact source transcriptions. Numbering follows the published article; displays that the source leaves unnumbered are identified by section.

Section 2, kinetic scheme of the vesicle-resource synapse; each presynaptic spike arriving at $t_{sp}$ activates a fraction $U_{SE}$ of the recovered resources:

$$
\frac{dx}{dt} = \frac{z}{\tau_{rec}} - U_{SE} x(t_{sp} - 0) \delta(t - t_{sp})
$$

$$
\frac{dy}{dt} = -\frac{y}{\tau_{in}} + U_{SE} x(t_{sp} - 0) \delta(t - t_{sp})
$$

$$
\frac{dz}{dt} = \frac{y}{\tau_{in}} - \frac{z}{\tau_{rec}},
$$

Section 2.1, kinetic equation of the running utilization under facilitation:

$$
\frac{d U_{SE}^1}{dt} = -\frac{U_{SE}^1}{\tau_{facil}} + U_{SE} (1 - U_{SE}^1) \delta(t - t_{sp}),
$$

Section 2.1, iterative expression for the utilization reached at the $(n+1)$-th spike:

$$
U_{SE}^{1(n+1)} = U_{SE}^{1(n)} (1 - U_{SE}) \exp(-\delta t / \tau_{facil}) + U_{SE},
$$

Section 2.1, unnumbered steady-state utilization under a regular train at frequency $r$:

$$
\frac{U_{SE}}{1 - (1 - U_{SE}) \exp(-1 / r \tau_{facil})},
$$

Section 3, Poisson-averaged dynamics of the mean quantities:

$$
\frac{d \langle x \rangle}{dt} = \frac{1 - \langle x \rangle}{\tau_{rec}} - \langle U_{SE}^1 \rangle \langle x \rangle r(t)
$$

$$
\frac{d \langle U_{SE}^- \rangle}{dt} = -\frac{\langle U_{SE}^- \rangle}{\tau_{facil}} + U_{SE} (1 - \langle U_{SE}^- \rangle) r(t)
$$

$$
\langle U_{SE}^1 \rangle = \langle U_{SE}^- \rangle (1 - U_{SE}) + U_{SE},
$$

Section 3, dynamics of the averaged active fraction (the inline simplification for timescales slower than $\tau_{in}$ reads $y = r \tau_{in} U_{SE}^1 \langle x \rangle$):

$$
\frac{d \langle y \rangle}{dt} = -\frac{\langle y \rangle}{\tau_{in}} + \langle U_{SE}^1 \rangle \langle x \rangle r(t),
$$

Section 3, analytic solution for depressing synapses under arbitrary rate modulation:

$$
\langle y(t) \rangle = U_{SE} r(t) \int_{-\infty}^{t} dt' \exp\left( -\frac{t - t'}{\tau_{rec}} - \int_{t'}^{t} dt'' U_{SE} r(t'') \right),
$$

Section 3, first two terms of the expansion over the derivatives of the frequency:

$$
\frac{r}{1 + r U_{SE} \tau_{rec}} + r' \frac{r}{(1 + r U_{SE} \tau_{rec})^3} + \cdots
$$

Section 3, the utilization as a functional of the frequency for facilitating synapses (to be substituted in equation (3.3)):

$$
U_{SE}^1 = U_{SE} \int_{-\infty}^{t} dt' r(t') \exp\left( -\frac{t - t'}{\tau_{facil}} - U_{SE} \int_{t'}^{t} dt'' r(t'') \right),
$$

Section 3, peak frequency of the facilitating response:

$$
\theta = 1 / \tau_{facil} + \sqrt{2 / \tau_{facil}^2 + \frac{1 + U_{SE}}{U_{SE} \tau_{rec} \tau_{facil}}} \approx 1 / \sqrt{U_{SE} \tau_{rec} \tau_{facil}},
$$

Section 3, low-frequency regime in which the postsynaptic signal reflects the rate amplified by $U_{SE}^1$:

$$
I_s \sim r(t) \int_{-\infty}^{t} dt' r(t') \exp(-(t - t') / \tau_{facil}),
$$

Section 4, coarse-grained mean-field equations for two interconnected subpopulations (excitatory pyramidal and inhibitory interneuron) at each site $r$; the two lines are one numbered display split by a page break, and the printed $y$ indices are transcribed exactly:

$$
\begin{aligned}
\tau_e \frac{d E_r}{dt} &= -E_r + g\left( \sum_{r'} J_{rr'}^{ee} y_{r'}^{ee} - J_{rr'}^{ei} y_{rr'}^{ei} + I_r^e \right)\\
\tau_i \frac{d I_r}{dt} &= -I_r + g\left( \sum_{r'} J_{rr'}^{ie} y_{r'}^{ie} - J_{rr'}^{ii} y_{rr'}^{ii} + I_r^i \right),
\end{aligned}
$$

Section 4.1, one-population reduction (the factor $\tau_{in}$ is absorbed into $J$):

$$
\tau \frac{d E}{dt} = -E(t) + g(J U_{SE} x(t) E(t))
$$

$$
\frac{dx}{dt} = -U_{SE} E(t) x(t) + \frac{1 - x(t)}{\tau_{rec}},
$$

Section 4.1, fixed-point equation:

$$
E = g\left( \frac{J U_{SE} E}{1 + E U_{SE} \tau_{rec}} \right),
$$

Figure 3 caption, linear-threshold response function used in the one-population illustration:

$$
g(x) = \begin{cases} 0 & \text{if } x < \theta \\ \beta (x - \theta) & \text{if } x > \theta \end{cases},
$$

Section 4.1, stability matrix of the fixed point (eigenvalues must have negative real parts):

$$
\left( \begin{array}{cc} \frac{\beta J U_{SE} x^* - 1}{\tau} & \frac{\beta J U_{SE} E^*}{\tau} \\ -U_{SE} x^* & -U_{SE} E^* - \frac{1}{\tau_{rec}} \end{array} \right),
$$

Appendix, factorization approximation underlying the mean-field derivation:

$$
\langle x U_{SE}^1 \rangle = \langle x \rangle \langle U_{SE}^1 \rangle,
$$

Appendix, Cauchy-Schwarz bound on the relative error of the factorization ($U^1$ abbreviates $U_{SE}^1$):

$$
\frac{\left| \langle x U^1 \rangle - \langle x \rangle \langle U^1 \rangle \right|}{\langle x \rangle \langle U^1 \rangle} \le CV_x CV_U,
$$

Appendix, stationary coefficient of variation of the utilization:

$$
CV_U^2 = \frac{r \tau_{facil} (1 - U)^2}{2 (1 + r \tau_{facil})^2 (1 + U r \tau_{facil} (1 - U/2))},
$$

Appendix, coefficient of variation of the recovered fraction under the same approximation:

$$
CV_x^2 = \frac{r \tau_{rec} \langle (U^1)^2 / 2 \rangle}{1 + r \tau_{rec} \langle U^1 (1 - U^1 / 2) \rangle},
$$

## Term-by-term interpretation

Equation (2.1) is a three-state kinetic scheme: each spike moves a fraction $U_{SE}$ of the recovered resource $x(t_{sp} - 0)$ (the pre-spike value) into the active state $y$, which decays with $\tau_{in}$, and the inactive pool $z$ recovers with $\tau_{rec}$; the presynaptic current is the inline relation $I_s(t) = A_{SE} y(t)$, so $A_{SE}$ is the maximal attainable synaptic strength. Equation (2.2) adds facilitation by making the utilization itself a dynamic variable $U_{SE}^1$ that jumps by $U_{SE}(1 - U_{SE}^1)$ per spike and decays with $\tau_{facil}$, interpreted as calcium-channel kinetics. Equation (2.3) is the exact between-spike iteration, and the following unnumbered display gives its fixed point for a regular train, showing explicitly how facilitation makes the effective utilization frequency-dependent; facilitation is marked for small $U_{SE}$ (roughly 0.01 to 0.05 for pyramidal-to-interneuron synapses) and absent for large $U_{SE}$.

Equations (3.1) average (2.1) and (2.2) over Poisson spike trains: the recovered fraction decays through usage $\langle U_{SE}^1 \rangle \langle x \rangle r(t)$, and the pre-spike utilization obeys a closed nonlinear equation with the post-spike reconstruction $\langle U_{SE}^1 \rangle = \langle U_{SE}^- \rangle(1 - U_{SE}) + U_{SE}$. Depressing synapses keep $U_{SE}^1$ fixed and use only the first equation. Equation (3.2) governs the mean active fraction; for timescales slower than $\tau_{in}$ it reduces to the algebraic $y = r \tau_{in} U_{SE}^1 \langle x \rangle$ (inline in the source). Equation (3.3) integrates the depressing case exactly, equation (3.4) expands it in rate derivatives (the transmitted signal decomposes into a rate term saturating at the limiting frequency $\lambda \sim 1/(U_{SE}\tau_{rec})$ plus a transient term proportional to $r'$ that dominates at high frequency), equation (3.5) is the corresponding functional for facilitating synapses, equation (3.6) locates the peak of the facilitating tuning curve, and equation (3.7) is the low-frequency limit in which the response is a $\tau_{facil}$-windowed convolution of the rate amplified by $U_{SE}^1$.

Equation (4.1) embeds the synaptic dynamics into Wilson-Cowan-type population equations: each connection type $ab \in \{ee, ei, ie, ii\}$ contributes its own population-averaged active fraction computed from equations (3.1)-(3.2), so synaptic efficacy becomes a dynamic state variable of the network. The printed display shows an apparent typographical inconsistency flagged here and transcribed exactly: the excitatory terms of both lines carry $y_{r'}^{ee}$ and $y_{r'}^{ie}$ with the presynaptic index only, while the inhibitory terms carry $y_{rr'}^{ei}$ and $y_{rr'}^{ii}$ with both indices, although the surrounding prose defines $y_{rr'}^{ee}$ for each connection $rr'$. Equations (4.2)-(4.3) reduce the system to one excitatory population, whose fixed point always exists and saturates because of depression; the one-population figures use the linear-threshold gain (4.4) with $\theta = 15$ mV and $\beta = 0.5$ mV$^{-1}$Hz, and the 2x2 matrix (4.5) determines fixed-point stability (the phase diagram of Figure 3B separates the parameter region in which the fixed point exists but is unstable from the stable region; dampened oscillations precede steady state because of the synaptic variable). The appendix quantifies the factorization (A.1) behind the mean-field closure through the Cauchy-Schwarz bound (A.2) and the variances (A.3)-(A.4): for the experimentally derived parameter sets the relative error stays below about 5 percent at all frequencies, exceeding 10 percent only for short $\tau_{facil}$ and large $U$ where facilitation disappears. The symbol $\theta$ is used by the source both for the peak frequency (3.6) and for the gain threshold (4.4).

## Inputs, outputs, and conditions

- Input: presynaptic spike train $\{t_{sp}\}$ (single synapse) or population rate $r(t)$ / external inputs $I_r^e$, $I_r^i$ (mean-field sections).
- Output: postsynaptic current $I_s(t)$ (single synapse); population rates $E_r(t)$, $I_r(t)$ with dynamic synaptic efficacies (network).
- Initial conditions: `not_verified` (Figures 1-3 start from rest; not stated explicitly).
- Boundary conditions: `not_applicable`.
- Network conditions: `source_located`; locator: Section 4 (uniform connections within each subpopulation; $J_{rr'}^{ab}$ denotes absolute strength times the average number of connections of type $ab$ between populations at $r$ and $r'$; refractoriness ignored).
- Event handling: `source_located`; locator: Section 2, equations (2.1)-(2.2) (each presynaptic spike at $t_{sp}$ produces delta-function jumps: $U_{SE} x(t_{sp}-0)$ moves from $x$ to $y$, and $U_{SE}(1 - U_{SE}^1)$ raises $U_{SE}^1$).
- Numerical method: `not_verified`; locator: Figures 1-2 (population simulations of 1000 Poisson spike trains using the full model (2.1); passive membrane $\tau_{mem} \dot V = -V + R_{in} I_{syn}(t)$ in Figure 1; no integrator named).
- Stochastic input: `deterministic` for the displayed equations; the derivation assumes Poisson presynaptic trains with rate $r(t)$ (Section 3).
- Simulation scale: `subcellular` single-synapse traces; 1000-neuron presynaptic populations for the mean-field comparison of Figure 2; two-population networks of Section 4.2 (Figures 4A-4B, with and without $J^{ii}$).

## Assumptions and limitations

The scheme is phenomenological: resources are either recovered, active, or inactive, with a single recovery and inactivation constant per synapse, and facilitation enters only through $U_{SE}^1$. The Poisson averaging of Section 3 assumes no statistical dependence between the spike-emission probability and the state variables; the appendix shows this factorization (A.1) holds to within about 5 percent for the neocortical parameter sets and degrades for short $\tau_{facil}$ and large $U_{SE}$. The mean-field equations ignore neuronal refractoriness, and the population response function $g$ is left generic (linear-threshold only in the illustrations). The one printed inconsistency in equation (4.1) is propagated unchanged. Update-order conventions of later implementations are outside the scope of this transcription.

## Experimental support

`not assessed`. The source cites its experimental basis (Markram and Tsodyks, 1996; Thomson and Deuchars, 1994; Markram et al., in press) and compares the stationary facilitating tuning curve with one recorded pyramidal-to-interneuron connection (Figure 1D), but no quantitative validation status is recorded here; this status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`; a ModelDB entry (model 3815) and a Brian2 documentation example reproduce this model but have not been audited for this record.
