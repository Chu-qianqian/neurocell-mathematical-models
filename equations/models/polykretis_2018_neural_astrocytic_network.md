# Polykretis neural-astrocytic network architecture

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: author-submitted arXiv v1 PDF; equations verified against a rendered page image and text extraction.
- Source locator: Methods section, equations (1)-(9).
- Transcription status: exact source transcription.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-24.

## Scope

- Biological cell scope: `mixed_neuron_glia`.
- Cell type: `mixed_neuron_astrocyte_system`.
- Cell subtype: perisynaptic astrocytic microdomains with postsynaptic LIF neurons.
- Nervous-system region: `central_nervous_system_unspecified`.
- Model scope: `coupled_multicellular`.
- Model scale: `local_microcircuit`.
- Mathematical form: `ordinary_differential_equation`.
- Interaction scope: `neuron_astrocyte`.
- Network type: `neuron_astrocyte_network`.
- Spatial structure: `multicompartment`.
- Stochasticity: `deterministic`.
- Plasticity scope: `none`.

## Source citation

Christina Polykretis; Konstantinos P. Michmizos. Astrocytic calcium waves modulate synchronous neuronal activity in a biologically constrained neural network. *ACM ICONS* (2018). [DOI](https://doi.org/10.1145/3229884.3229890). [arXiv:1807.02514v1](https://arxiv.org/abs/1807.02514).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $I$ | $IP_3$ concentration | source convention | source-verified |
| $I_\beta$ | agonist-dependent $IP_3$ production | source convention | source-verified |
| $I_\delta$ | agonist-independent $IP_3$ production | source convention | source-verified |
| $I_{3K}$ | $IP_3$ degradation by the first enzyme | source convention | source-verified |
| $I_{5P}$ | $IP_3$ degradation by the second enzyme | source convention | source-verified |
| $C$ | intracellular Calcium concentration | $\mu M$ | source-verified |
| $J_{bal}$ | Calcium-balancing flux (Hill form) | $\mu M/s$ | source-verified |
| $J_{chan}$ | cytosolic Calcium increase from ER release | source convention | source-verified |
| $J_{leak}$ | Calcium leakage from the ER | source convention | source-verified |
| $J_{pump}$ | SERCA uptake back into the ER | source convention | source-verified |
| $h$ | gating variable of ER-release channels | dimensionless | source-verified |
| $h_\infty$ | steady-state value of $h$ | dimensionless | source-verified |
| $\tau_h$ | time constant of $h$ | source convention | source-verified |
| $J_{RyR}$ | Ryanodine-receptor calcium release flux | source convention | source-verified |
| $C_{ER}$ | Calcium concentration in the ER | $\mu M$ | source-verified |
| $I_{astro}$ | Calcium-dependent astrocytic output amplitude | $\mu A/cm^2$ | source-verified |
| $w$ | transformed astrocytic Calcium variable | dimensionless | source-verified |
| $\Theta$ | Heaviside function | dimensionless | source-verified |
| $I_{SIC}$ | slow inward current | source convention | source-verified |
| $I_{total}$ | total current driving postsynaptic neurons | source convention | source-verified |
| $I_{basal}$ | basal presynaptic current | source convention | source-verified |
| $t$ | time since the last Calcium peak | source convention | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $v_{bal}$ | maximal rate of Calcium depletion | $\mu M/s$ | 0.5 | equation (2) |
| $K_{bal}$ | Calcium affinity of the balancing mechanism | $\mu M$ | 2 | equation (2) |
| $k_1, k_2$ | Ryanodine-receptor constants | source convention | parameters_incomplete | equation (5); fit to Bezprozvany et al. data |
| $K_d$ | Ryanodine-receptor dissociation constant | source convention | parameters_incomplete | equation (5); fit to Bezprozvany et al. data |
| $2.11$ | SIC amplitude coefficient | $\mu A/cm^2$ | 2.11 | equation (6) |
| $196.11$ | Calcium offset in $w$ | nM | 196.11 | equation (7) |
| $\tau^{SIC}_{rise}$ | SIC rise time constant | $ms$ | 50 | equation (8) |
| $\tau^{SIC}_{decay}$ | SIC decay time constant | $ms$ | 300 | equation (8) |
| $n$ | biexponential normalization constant | dimensionless | $6 \cdot 6^{0.2}/5$ | equation (8) |
| $R$ | LIF membrane resistance | $G\Omega$ | 0.6 | Methods, postsynaptic neuron description |
| $C_m$ | LIF membrane capacitance | $pF$ | 100 | Methods, postsynaptic neuron description |

## Equations

These are exact source transcriptions of Methods equations (1)-(9).

$IP_3$ dynamics in the perisynaptic process (C1):

$$
\dot{I} = I_\beta + I_\delta - I_{3K} - I_{5P},
$$

Calcium balancing in ER-free compartments (C1, C2):

$$
J_{bal} = -v_{bal}\, \frac{C^2}{C^2 + K_{bal}^2},
$$

ER calcium regulation and channel gating in compartments (C3, C4):

$$
\begin{aligned}
\dot{C} &= J_{chan} + J_{leak} - J_{pump},\\
\dot{h} &= \frac{h_\infty - h}{\tau_h}
\end{aligned}
$$

Ryanodine-sensitive ER release in compartments (C5, C6):

$$
J_{RyR} = \left(k_1 + k_2\, \frac{C^3}{C^3 + K_d^3}\right)(C_{ER} - C)
$$

Calcium-dependent astrocytic output:

$$
\begin{aligned}
I_{astro} &= 2.11\, \frac{\mu A}{cm^2}\, ln(w)\, \Theta(ln\, w)\\
w &= [Ca^{2+}]/nM - 196.11
\end{aligned}
$$

Slow inward current activated at every Calcium peak (exponents as printed in the source):

$$
I_{SIC}(t) = I_{astro}\, ([Ca^{2+}_{peak}])^{-n} \cdot n \cdot \left(exp\left(\frac{t}{\tau^{SIC}_{decay}}\right) - exp\left(\frac{t}{\tau^{SIC}_{rise}}\right)\right)
$$

Total current driving the postsynaptic LIF neurons:

$$
I_{total} = I_{basal} + I_{SIC}
$$

## Term-by-term interpretation

Equation (1) follows the De Pitta et al. $IP_3$ description: agonist-driven and basal production balanced by two degradation enzymes. Equation (2) clamps Calcium in compartments without ER using a Hill-form depletion term. Equations (3)-(4) are the standard ER calcium balance with an $IP_3$-dependent channel gate. Equation (5) adds Ryanodine-sensitive release with a calcium-dependent opening coefficient. Equations (6)-(8) map astrocytic Calcium peaks to slow inward currents through an experimentally fit log-amplitude with Heaviside gating and a normalized biexponential kernel; the source prints positive exponents in equation (8), and the transcription preserves them as printed. Equation (9) closes the neuron-astrocyte-neuron loop by injecting the SIC on top of a basal current into LIF neurons.

## Inputs, outputs, and conditions

- Input: presynaptic facilitation-depression model output feeding $I_\beta$ in equation (1).
- Output: postsynaptic LIF spike trains driven by $I_{total}$.
- Initial conditions: `not_verified`.
- Boundary conditions: `not_applicable`; locator: not_applicable.
- Network conditions: `not_applicable`; locator: not_applicable.
- Event handling: `source_example_located`; SIC injection is event-locked to Calcium concentration peaks, Methods, equation (8) description.
- Numerical method: `not_verified`.
- Stochastic input: `deterministic`.
- Simulation scale: `local_microcircuit`.

## Assumptions and limitations

The transcribed block covers the per-compartment astrocyte ODEs and the neuron-astrocyte-neuron coupling current. The full network architecture (compartment connectivity, LIF population sizes, and simulation protocol) is described in the source but is not transcribed here. Parameters $k_1$, $k_2$, and $K_d$ are stated to be fit to Bezprozvany et al. data without numerical values in the Methods text. This record does not assert a paper-result reproduction.

## Experimental support

`not assessed`. This status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`.
