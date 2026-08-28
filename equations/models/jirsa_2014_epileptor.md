# Epileptor seizure-dynamics model

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: HAL author copy of the published Brain article (amu.hal.science/hal-03626097, Brain 2014, 137, 2210-2230, with the supplementary information appended), with every displayed equation checked against the rendered page images.
- Source locator: The Epileptor section, complete five-variable system with the integral coupling function g and the piecewise functions f1 and f2 together with the parameter-value line (all displays unnumbered in the source); Supplementary Information 3, Alternative formulation of Epileptor equations (six-variable form with the dummy variable u).
- Transcription status: exact source transcription of the HAL author copy; one printed discrepancy relative to the Brain version of record (the branch inequalities of f2) is transcribed exactly and flagged in the interpretation.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-28.

## Scope

- Biological cell scope: `neural_population`.
- Cell type: `neural_population`.
- Cell subtype: phenomenological neural-mass seizure system composed of two coupled ensembles: a fast subsystem (x1, y1) generating interictal spikes and seizure discharges, a spike-wave subsystem (x2, y2), and the slow permittivity variable z that moves the system between normal and seizure states.
- Nervous-system region: `central_nervous_system_unspecified`.
- Model scope: `cell_population`.
- Model scale: `neural_mass`.
- Mathematical form: `hybrid` (deterministic ODE core driven by additive Gaussian white noise; piecewise-defined nonlinearities).
- Interaction scope: `population_coupling`.
- Network type: `neural_mass`.
- Spatial structure: `nonspatial`.
- Stochasticity: `stochastic` (linear additive Gaussian white noise on each equation).
- Plasticity scope: `none`.

## Source citation

Viktor K. Jirsa; William C. Stacey; Pascale P. Quilichini; Anton I. Ivanov; Christophe Bernard. On the nature of seizure dynamics. *Brain* **137**(8), 2210-2230 (2014). [DOI](https://doi.org/10.1093/brain/awu133). [PubMed](https://pubmed.ncbi.nlm.nih.gov/24919973/). Equations inspected in the HAL open-archive author copy [hal-03626097](https://amu.hal.science/hal-03626097).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $x_1$ | fast ensemble position variable (interictal spikes and seizure discharges) | dimensionless | source-verified |
| $y_1$ | fast ensemble velocity variable | dimensionless | source-verified |
| $z$ | slow permittivity variable controlling seizure onset and offset | dimensionless | source-verified |
| $x_2$ | spike-wave subsystem position variable | dimensionless | source-verified |
| $y_2$ | spike-wave subsystem velocity variable | dimensionless | source-verified |
| $f_1(x_1, x_2)$ | piecewise nonlinearity of the fast subsystem | dimensionless | source-verified |
| $f_2(x_1, x_2)$ | piecewise nonlinearity of the spike-wave subsystem (written $f_2(x_2)$ in the alternative formulation) | dimensionless | source-verified |
| $g(x_1)$ | low-pass integral coupling function of $x_1$ | dimensionless | source-verified |
| $\tau$ | integration variable of the integral coupling function (symbol reuse with the time constants $\tau_0$, $\tau_1$, $\tau_2$ is present in the source) | dimensionless | source-verified |
| $u$ | dummy variable replacing the integral in the alternative formulation | dimensionless | source-verified |
| $I_{rest1}$, $I_{rest2}$ | resting input currents of the two ensembles | dimensionless | source-verified |
| $x_0$ | excitability parameter (z shift) of the fast subsystem | dimensionless | source-verified |
| $y_0$ | position parameter of the fast subsystem nullclines | dimensionless | source-verified |
| $\tau_0$, $\tau_1$, $\tau_2$ | characteristic time scales of the permittivity variable, ensemble 1, and ensemble 2, with hierarchy $\tau_0 \gg \tau_1 \gg \tau_2$ | dimensionless | source-verified |
| $\gamma$ | decay rate of the low-pass coupling function | dimensionless | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $x_0$ | excitability parameter | dimensionless | -1.6 | The Epileptor, parameter line |
| $y_0$ | fast-subsystem nullcline parameter | dimensionless | 1 | The Epileptor, parameter line |
| $\tau_0$ | permittivity time scale | dimensionless | 2857 | The Epileptor, parameter line |
| $\tau_1$ | ensemble-1 time scale (equal to 1 and omitted from the equations) | dimensionless | 1 | The Epileptor, parameter line and following prose |
| $\tau_2$ | ensemble-2 time scale | dimensionless | 10 | The Epileptor, parameter line |
| $I_{rest1}$ | resting input to ensemble 1 | dimensionless | 3.1 | The Epileptor, parameter line |
| $I_{rest2}$ | resting input to ensemble 2 | dimensionless | 0.45 | The Epileptor, parameter line |
| $\gamma$ | low-pass coupling decay rate (1/gamma = 100, much larger than tau_2) | dimensionless | 0.01 | The Epileptor, parameter line; Supplementary Information 3 |
| noise variances | variance of the additive Gaussian white noise on each equation, first and second subsystems | dimensionless | 0.025; 0.25 | The Epileptor, following prose |
| piecewise constants | constants of f1 and f2 | dimensionless | 5 (y-dynamics); 3; 0.6; 4; 0.002 (integral weight); 0.3; 3.5; -0.25; 6 | The Epileptor, equations |
| initial conditions | initial state for the numerical simulation | dimensionless | x1 = 0; y1 = 5; z = 3; x2 = 0; y2 = 0 | The Epileptor, following prose |

## Equations

These are exact source transcriptions. All displays are unnumbered in the source; the first four are given under the heading "The Epileptor" (main text) and the last under "Alternative formulation of Epileptor equations" (Supplementary Information 3).

Main text, complete system of the Epileptor equations:

$$
\begin{aligned}
\dot{x}_1 &= y_1 - f_1(x_1, x_2) - z + I_{rest1}\\
\dot{y}_1 &= y_0 - 5x_1^2 - y_1\\
\dot{z} &= \frac{1}{\tau_0}\left(4(x_1 - x_0) - z\right)\\
\dot{x}_2 &= -y_2 + x_2 - x_2^3 + I_{rest2} + 0.002 g(x_1) - 0.3(z - 3.5)\\
\dot{y}_2 &= \frac{1}{\tau_2}\left(-y_2 + f_2(x_1, x_2)\right)
\end{aligned}
$$

Main text, integral coupling function:

$$
g(x_1) = \int_{t_0}^{t} e^{-\gamma(t-\tau)} x_1(\tau) d\tau
$$

Main text, piecewise nonlinearity of the fast subsystem:

$$
f_1(x_1, x_2) = \begin{cases} x_1^3 - 3x_1^2 & \text{if } x_1 < 0 \\ (x_2 - 0.6(z-4)^2) x_1 & \text{if } x_1 \geq 0 \end{cases}
$$

Main text, piecewise nonlinearity of the spike-wave subsystem (branch senses exactly as printed in the HAL copy; see interpretation):

$$
f_2(x_1, x_2) = \begin{cases} 0 & \text{if } x_2 < -0.25 \\ 6(x_2 + 0.25) & \text{if } x_2 \geq -0.25 \end{cases}
$$

Main text, parameter-value line as printed:

$$
x_0 = -1.6; \quad y_0 = 1; \quad \tau_0 = 2857; \quad \tau_1 = 1; \quad \tau_2 = 10; \quad I_{rest1} = 3.1; \quad I_{rest2} = 0.45; \quad \gamma = 0.01.
$$

Supplementary Information 3, alternative formulation with the dummy variable u (the source notes that all parameters and functions are as in the main text, and that u acts as a low-pass filter because 1/gamma = 100 is much larger than tau_2):

$$
\begin{aligned}
\dot{x}_1 &= y_1 - f_1(x_1, x_2) - z + I_{rest1}\\
\dot{y}_1 &= y_0 - 5x_1^2 - y_1\\
\dot{z} &= \frac{1}{\tau_0}\left(4(x_1 - x_0) - z\right)\\
\dot{x}_2 &= -y_2 + x_2 - x_2^3 + I_{rest2} + 2u - 0.3(z - 3.5)\\
\dot{y}_2 &= \frac{1}{\tau_2}\left(-y_2 + f_2(x_2)\right)\\
\dot{u} &= -\gamma(u - 0.1 x_1)
\end{aligned}
$$

## Term-by-term interpretation

The Epileptor is a phenomenological five-variable system constructed from experimentally constrained bifurcations: seizure onset is a saddle-node (fold) bifurcation and seizure offset a homoclinic bifurcation, defining the fold/homoclinic (square-wave bursting) class. The fast subsystem (x1, y1) follows a Hindmarsh-Rose-like form whose piecewise nonlinearity f1 switches between a cubic branch for x1 < 0 and a line with slope modulated by (x2 - 0.6(z-4)^2) for x1 >= 0; this z-dependent slope is the linear inhibition coupling from ensemble 2 to ensemble 1. The permittivity variable z integrates 4(x1 - x0) slowly (tau0 = 2857): it accumulates during fast activity, drives the offset through the -z term in the x1 equation, and and biases the second subsystem via the -0.3(z - 3.5) term. The spike-wave subsystem (x2, y2) is an excitable system near a saddle-node on invariant circle bifurcation, with piecewise f2 providing the negative-feedback coupling from ensemble 1 to ensemble 2 that biases it toward preictal spikes. The term 0.002 g(x1) is a low-pass filtered excitatory coupling of the fast spikes into the second subsystem; in steady state g(x1) with gamma = 0.01 corresponds to 100 times the filtered value of x1, which is why the alternative formulation writes 2u with u the low-pass state. The alternative formulation of Supplementary Information 3 introduces u as the dummy state, making the system six-dimensional; it writes the spike-wave feedback as f2(x2) without the x1 argument. The time constant tau1 = 1 never appears explicitly. The printed f2 branches of the HAL copy read 0 for x2 < -0.25 and 6(x2 + 0.25) for x2 >= -0.25; the published Brain version of record prints the opposite branch assignment (0 for x2 >= -0.25 and a2(x2 + 0.25) with a2 = 6 for x2 < -0.25), which is the reading consistent with the spike-wave subsystem dynamics used in the paper's simulations; the transcription preserves the HAL print and flags the difference. Noise is added to each equation as linear additive Gaussian white noise (variance 0.025 for the first subsystem and 0.25 for the second), integrated with the Euler-Maruyama method.

## Inputs, outputs, and conditions

- Input: resting currents $I_{rest1}$, $I_{rest2}$ and additive Gaussian white noise on each equation.
- Output: time courses of $x_1 + x_2$ mimicking the local field potential; seizure onset, evolution, and offset governed by the permittivity variable $z$.
- Initial conditions: `source_example_located`; locator: The Epileptor, following prose (x1 = 0; y1 = 5; z = 3; x2 = 0; y2 = 0).
- Boundary conditions: `not_applicable`.
- Network conditions: `not_verified` (the article discusses coupled and large-scale Epileptor networks in prose and in later work, but no coupling display is given in the manuscript).
- Event handling: `not_applicable`.
- Numerical method: `source_example_located`; locator: The Epileptor, following prose (Euler-Maruyama method for the stochastic equations).
- Stochastic input: `stochastic` (additive Gaussian white noise, zero mean; variance 0.025 first subsystem, 0.25 second subsystem).
- Simulation scale: `neural_mass` (single Epileptor unit; the field potential is approximated by x1 + x2).

## Assumptions and limitations

The Epileptor is phenomenological: the state variables are not direct biological/biophysical measurements, the fast subsystem abstracts spike-generating currents, the permittivity variable abstracts the slow metabolic processes that control seizure onset and offset, and the piecewise switches are chosen for structural stability rather than fitted to single-channel data. The parameters were chosen to match the experimental data of the in vitro immature hippocampus model and the interspike-interval and DC-shift signatures analyzed in the article. The state variables are neural-mass variables and the model is not a molecular or single-cell account of epilepsy. The f2 branch-sense discrepancy between the HAL author copy and the Brain version of record is flagged in the interpretation, and the HAL print is propagated unchanged in the displayed equations.

## Experimental support

`not assessed`. The article validates model predictions against in vitro and in vivo recordings (DC shift at seizure onset, logarithmic interspike-interval scaling at offset across mouse, zebrafish, and human seizures), but no quantitative validation status is recorded here; this status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`; the Epileptor ships with The Virtual Brain platform and community reimplementations exist, but none has been audited for this record.
