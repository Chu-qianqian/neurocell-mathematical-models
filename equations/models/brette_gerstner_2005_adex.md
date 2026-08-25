# Adaptive exponential integrate-and-fire model

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: public full-text PDF (course-hosted mirror of the published article), pages 3637-3642, rendered and read visually.
- Source locator: Methods, Adapting the aEIF model, equations (1)-(3); Table 1 aEIF parameter box (conductance-based form and reset rule).
- Transcription status: exact source transcription.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-25.

## Scope

- Biological cell scope: `neuronal`.
- Cell type: `neuron`.
- Cell subtype: adaptive point neuron (two-dimensional integrate-and-fire); fitted to a detailed conductance-based model of a regular-spiking pyramidal cell.
- Nervous-system region: `central_nervous_system_unspecified`.
- Model scope: `cell_function`.
- Model scale: `single_cell`.
- Mathematical form: `hybrid` (continuous two-dimensional dynamics with discrete spike-reset events).
- Interaction scope: `external_input`.
- Network type: `not_applicable`.
- Spatial structure: `nonspatial`.
- Stochasticity: `deterministic`; synaptic conductances g_e(t), g_i(t) are fluctuating (Ornstein-Uhlenbeck) inputs in the reported scenarios.
- Plasticity scope: `intrinsic`.

## Source citation

Romain Brette; Wulfram Gerstner. Adaptive Exponential Integrate-and-Fire Model as an Effective Description of Neuronal Activity. *Journal of Neurophysiology* **94**(5), 3637-3642 (2005). [DOI](https://doi.org/10.1152/jn.00686.2005). [PubMed](https://pubmed.ncbi.nlm.nih.gov/16014787/).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $V$ | membrane potential | mV | source-verified |
| $w$ | adaptation variable (a current) | nA | source-verified |
| $I$ | synaptic current | nA | source-verified |
| $f(V)$ | passive-plus-spike function of the voltage equation | nA | source-verified |
| $g_e(t)$, $g_i(t)$ | fluctuating excitatory and inhibitory synaptic conductances | nS | source-verified |
| $V_{peak}$ | voltage at which a spike is triggered | mV | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $C$ | membrane capacitance | pF | 281 | Table 1, aEIF parameters |
| $g_L$ | leak conductance | nS | 30 | Table 1, aEIF parameters |
| $E_L$ | leak (resting) potential | mV | $-70.6$ | Table 1, aEIF parameters |
| $V_T$ | threshold potential | mV | $-50.4$ (alternative estimate $-50.7$) | Table 1; Parameter fitting text |
| $\Delta_T$ | slope factor | mV | 2 (alternative estimate 2.2) | Table 1; Parameter fitting text |
| $\tau_w$ | adaptation time constant | ms | 144 | Table 1, aEIF parameters |
| $a$ | subthreshold adaptation level | nS | 4 | Table 1, aEIF parameters |
| $b$ | spike-triggered adaptation increment | nA | 0.0805 | Table 1, aEIF parameters |
| $V_r$ | reset value of $V$ after a spike | mV | $E_L$ ($-70.6$) | Table 1 aEIF box; Methods text |
| $V_{peak}$ | spike-triggering voltage | mV | 20 | Methods, after equation (1) |
| $E_e$ | excitatory (AMPA) reversal potential | mV | 0 | Methods, Detailed neuron model |
| $E_i$ | inhibitory (GABA$_A$) reversal potential | mV | $-75$ | Methods, Detailed neuron model |

## Equations

These are exact source transcriptions of the rendered PDF pages. Numbering follows the published article.

Adaptive integrate-and-fire voltage equation:

$$
C \frac{dV}{dt} = f(V) - w + I,
$$

Exponential spike mechanism combined with linear leak:

$$
f(V) = -g_L(V - E_L) + g_L \Delta_T \exp\left(\frac{V - V_T}{\Delta_T}\right),
$$

Adaptation current:

$$
\tau_w \frac{dw}{dt} = a(V - E_L) - w,
$$

Conductance-based form with fluctuating synaptic conductances and the spike-reset rule, as given in the Table 1 aEIF parameter box:

$$
\begin{aligned}
C \frac{dV}{dt} &= -g_L(V - E_L) + g_L \Delta_T \exp\left(\frac{V - V_T}{\Delta_T}\right) - g_e(t)(V - E_e) - g_i(t)(V - E_i) - w\\
\tau_w \frac{dw}{dt} &= a(V - E_L) - w\\
\text{At spike time } (V > 20 \text{ mV}): \quad V &\rightarrow E_L,\quad w \rightarrow w + b
\end{aligned}
$$

## Term-by-term interpretation

Equation (1) is the current-balance form: the model is an integrate-and-fire neuron whose spike mechanism is folded into $f(V)$. Equation (2) defines $f(V)$ as the sum of a linear leak toward $E_L$ and an exponential activation term that diverges as $V$ approaches $V_T$ from below; the slope factor $\Delta_T$ controls the sharpness of the threshold, and in the limit $\Delta_T \rightarrow 0$ the model reduces to a standard integrate-and-fire neuron with threshold $V_T$. Formally the exponential model "spikes" when $V$ diverges; operationally the source triggers a spike at $V_{peak} = 20$ mV, which only shifts spike times by a fraction of a millisecond. Equation (3) is a first-order adaptation current toward $a(V - E_L)$: $a$ sets subthreshold adaptation, and at each firing time $w$ is increased by $b$ (spike-triggered adaptation); high reset values ($V_r > V_T$) induce bursting, large $b$ gives strong spike-frequency adaptation, and high $a$ yields subthreshold oscillations. The Table 1 box restates the model with explicit fluctuating synaptic conductances $g_e(t)$, $g_i(t)$ (reversal potentials $E_e = 0$ mV, $E_i = -75$ mV, Ornstein-Uhlenbeck processes of the input scenarios) and states the reset rule: after a spike, integration restarts from $V_r = E_L$ and $w$ gains $b$. The parameter-fitting protocol additionally uses the linear far-from-threshold relation $I = (g_L + a)(V - E_L)$ and the inversion $w = -C\,dV/dt - g_L(V - E_L) + I$; these are estimation formulas rather than model equations and are recorded here inline. The fitted values reproduce the reference detailed model's spikes with 2-ms precision in 96% of cases; the alternative estimation route gives $V_T = -50.7$ mV and $\Delta_T = 2.2$ mV.

## Inputs, outputs, and conditions

- Input: synaptic current $I$ or, in the conductance-based form, fluctuating conductances $g_e(t)$, $g_i(t)$ with reversals $E_e$, $E_i$ (Table 1 scenario values; time constants $\tau_e = 2.728$ ms, $\tau_i = 10.49$ ms).
- Output: membrane potential trajectory $V(t)$ and spike times; adaptation current $w(t)$.
- Initial conditions: `not_verified`.
- Boundary conditions: `not_applicable`; locator: not_applicable.
- Network conditions: `not_applicable`; locator: not_applicable.
- Event handling: `source_located`; locator: Table 1 aEIF box and Methods text (spike triggered when $V > V_{peak} = 20$ mV; $V \rightarrow E_L$, $w \rightarrow w + b$; integration restarted from $V_r = E_L$).
- Numerical method: `not_verified` (source states simulations were done with MATLAB; no integration step reported).
- Stochastic input: `deterministic`; the conductance inputs of the reported scenarios are Ornstein-Uhlenbeck fluctuating processes.
- Simulation scale: `single_cell`.

## Assumptions and limitations

The aEIF model is a phenomenological point-neuron abstraction: spike initiation is compressed into an exponential nonlinearity and adaptation into a single first-order current, with no biophysical channel variables. Its parameters were fitted to artificial data from one detailed regular-spiking pyramidal-cell model, and the source notes that fitting to bursting neurons might be harder. The spike threshold $V_{peak} = 20$ mV is an operational convention whose exact value is not critical. This record does not assert a paper-result reproduction.

## Experimental support

`not assessed`. This status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `smoke_tested`; Brian2 reference implementation in `implementations/brian2/brette_gerstner_2005_adex.py`.
- Numerical tests: `passed` (repository unit tests).
- Reference behavior: `qualitative_match` (adaptation ratio reported in the repository smoke test).
- Reproduction: `implementation_only`; no paper-result reproduction is claimed.
- External code license: `not_assessed`; a ModelDB entry (153635) exists but has not been audited for this record.
