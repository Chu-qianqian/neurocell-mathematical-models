# Wang-Buzsaki inhibitory gamma network

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: author-hosted full text (X.-J. Wang lab publication page, PDF).
- Source locator: Materials and Methods, equations (2.1)-(2.4) with accompanying rate expressions.
- Transcription status: exact source transcription.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-24.

## Scope

- Biological cell scope: `neural_population`.
- Cell type: `neural_population`.
- Cell subtype: hippocampal fast-spiking GABAergic interneurons.
- Nervous-system region: `hippocampus`.
- Model scope: `coupled_multicellular`.
- Model scale: `large_scale_network`.
- Mathematical form: `ordinary_differential_equation`.
- Interaction scope: `synaptic`.
- Network type: `interneuron_network`.
- Spatial structure: `network_topology`.
- Stochasticity: `deterministic`; coupling is randomly assigned with fixed average degree.
- Plasticity scope: `none`.

## Source citation

Xiao-Jing Wang; Gyorgy Buzsaki. Gamma Oscillation by Synaptic Inhibition in a Hippocampal Interneuronal Network Model. *Journal of Neuroscience* **16**(20), 6402-6413 (1996). [DOI](https://doi.org/10.1523/jneurosci.16-20-06402.1996). [Author-hosted PDF](https://www.cns.nyu.edu/wanglab/publications/pdf/wang_buzaski1996.pdf).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $V$ | membrane potential | mV | source-verified |
| $I_{Na}$, $I_K$, $I_L$, $I_{syn}$ | sodium, potassium, leak, and synaptic current densities | mA/cm$^2$ | source-verified |
| $I_{app}$ | injected current density | mA/cm$^2$ | source-verified |
| $m$ | sodium activation, instantaneous $m_\infty = \alpha_m/(\alpha_m + \beta_m)$ | dimensionless | source-verified |
| $h$ | sodium inactivation gate | dimensionless | source-verified |
| $n$ | potassium activation gate | dimensionless | source-verified |
| $s$ | fraction of open synaptic channels | dimensionless | source-verified |
| $F(V_{pre})$ | normalized transmitter-receptor complex concentration | dimensionless | source-verified |
| $V_{pre}$ | presynaptic membrane potential | mV | source-verified |
| $t$ | time | ms | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $C_m$ | specific membrane capacitance | $\mu F/cm^2$ | 1 | equation (2.1) |
| $g_L$, $E_L$ | leak conductance and reversal | mS/cm$^2$, mV | 0.1, $-65$ | after equation (2.1) |
| $g_{Na}$, $E_{Na}$ | sodium conductance and reversal | mS/cm$^2$, mV | 35, 55 | after equation (2.2) |
| $\phi$ | temperature factor for gating kinetics | dimensionless | 5 | after equation (2.2) |
| $g_K$, $E_K$ | potassium conductance and reversal | mS/cm$^2$, mV | 9, $-90$ | after equation (2.3) |
| $g_{syn}$, $E_{syn}$ | maximal synaptic conductance and reversal | mS/cm$^2$, mV | 0.1 (typical), $-75$ | Models synapse paragraph |
| $\alpha$ | channel opening rate | 1/ms | 12 | page 6404 |
| $\beta$ | channel closing rate, $\tau_{syn} = 1/\beta$ | 1/ms | 0.1 ($\tau_{syn}$ = 10 ms) | page 6404 |
| $\theta_{syn}$ | sigmoid threshold for transmitter release | mV | 0 | Models synapse paragraph |
| $M_{syn}$ | average synaptic contacts per neuron | dimensionless | varied; about 60 needed for gamma | Random network connectivity |
| $N$ | number of cells | dimensionless | varied (e.g. 30-100) | Random network connectivity |

## Equations

These are exact source transcriptions of Materials and Methods equations (2.1)-(2.4) with the accompanying rate expressions.

Current balance of the single-compartment interneuron:

$$
C_m \frac{dV}{dt} = -I_{Na} - I_K - I_L - I_{syn} + I_{app},
$$

Transient sodium current with instantaneous activation and its rate expressions:

$$
\begin{aligned}
I_{Na} &= g_{Na} m_\infty^3 h (V - E_{Na}), \qquad m_\infty = \frac{\alpha_m}{\alpha_m + \beta_m},\\
\alpha_m(V) &= \frac{-0.1 (V + 35)}{\exp(-0.1 (V + 35)) - 1}, \qquad \beta_m(V) = 4 \exp\left(\frac{-(V + 60)}{18}\right),
\end{aligned}
$$

Sodium inactivation kinetics with its rate expressions:

$$
\begin{aligned}
\frac{dh}{dt} &= \phi \left[\alpha_h (1 - h) - \beta_h h\right],\\
\alpha_h(V) &= 0.07 \exp\left(\frac{-(V + 58)}{20}\right), \qquad \beta_h(V) = \frac{1}{\exp(-0.1 (V + 28)) + 1},
\end{aligned}
$$

Delayed-rectifier potassium current and activation kinetics with rate expressions:

$$
\begin{aligned}
I_K &= g_K n^4 (V - E_K), \qquad \frac{dn}{dt} = \phi \left[\alpha_n (1 - n) - \beta_n n\right],\\
\alpha_n(V) &= \frac{-0.01 (V + 34)}{\exp(-0.1 (V + 34)) - 1}, \qquad \beta_n(V) = 0.125 \exp\left(\frac{-(V + 44)}{80}\right),
\end{aligned}
$$

GABAergic synaptic current, first-order gating, and sigmoid release function:

$$
\begin{aligned}
I_{syn} &= g_{syn} s (V - E_{syn}), \qquad \frac{ds}{dt} = \alpha F(V_{pre}) (1 - s) - \beta s,\\
F(V_{pre}) &= \frac{1}{1 + \exp\left(\dfrac{-(V_{pre} - \theta_{syn})}{2}\right)}.
\end{aligned}
$$

## Term-by-term interpretation

Equation (2.1) is the single-compartment current balance. The sodium current uses the standard approximation that activation is instantaneous ($m = m_\infty$); the rate expressions are modified from Hodgkin-Huxley so that spikes show a shallow afterhyperpolarization (about $-15$ mV below threshold) rather than approaching $E_K$, and so that the fast-spiking frequency-current slope is steep. The factor $\phi = 5$ speeds both gating variables relative to squid. The synaptic term uses a first-order transmitter-gated channel: $F(V_{pre})$ is an instantaneous sigmoid that opens channels only for presynaptic spikes, $\alpha$ sets the fast rise, and $\beta$ the decay ($\tau_{syn} = 10$ ms), which is the key parameter for gamma-band synchronization. In the network, each cell receives on average $M_{syn}$ randomly chosen inhibitory contacts and $g_{syn}$ is divided by $M_{syn}$ so the total synaptic drive per cell is preserved when connectivity is varied.

## Inputs, outputs, and conditions

- Input: $I_{app}$ (homogeneous or Gaussian-distributed) and presynaptic spike events through $F(V_{pre})$.
- Output: membrane potential trajectories and population spike trains; network coherence index.
- Initial conditions: `not_verified`.
- Boundary conditions: `not_applicable`; locator: not_applicable.
- Network conditions: `source_located`; locator: Materials and Methods, "Random network connectivity" paragraph (random pairing with probability $p = M_{syn}/N$; $g_{syn}$ divided by $M_{syn}$).
- Event handling: `not_applicable`; locator: not_applicable.
- Numerical method: `not_verified`.
- Stochastic input: `deterministic`; connectivity is randomly assigned with fixed average degree.
- Simulation scale: `large_scale_network`.

## Assumptions and limitations

Each interneuron is a single compartment; dendritic structure is ignored. The synaptic variable $s$ is driven instantaneously by presynaptic voltage without axonal or synaptic delay, and $g_{syn}$ scaling by $M_{syn}$ keeps total drive fixed by construction. The critical connectedness value (about 60 contacts) is specific to these single-cell parameters and the gamma band. This record does not assert a paper-result reproduction.

## Experimental support

`not assessed`. This status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`; ModelDB and Open Source Brain entries exist but their license status has not been assessed.
