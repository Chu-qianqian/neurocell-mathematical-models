# Hopfield associative-memory network

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: PNAS scan PDF (PMC346238 copy) with text layer; equations verified against rendered page images of pages 2555-2556.
- Source locator: bracketed equations [1]-[8].
- Transcription status: exact source transcription.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-24.

## Scope

- Biological cell scope: `neural_population`.
- Cell type: `neural_population`.
- Cell subtype: binary McCulloch-Pitts-style neurons with symmetric couplings.
- Nervous-system region: `not_assessed`.
- Model scope: `cell_population`.
- Model scale: `large_scale_network`.
- Mathematical form: `difference_equation`.
- Interaction scope: `network_connectivity`.
- Network type: `attractor_network`.
- Spatial structure: `network_topology`.
- Stochasticity: `deterministic`; update order is asynchronous with a stochastic mean processing time 1/W.
- Plasticity scope: `long_term_synaptic`; synapses are set by a Hebbian storage prescription.

## Source citation

J. J. Hopfield. Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences* **79**(8), 2554-2558 (1982). [DOI](https://doi.org/10.1073/pnas.79.8.2554). [PMC346238](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC346238/).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $V_i$ | state of neuron $i$ (0 = not firing, 1 = firing at maximum rate) | dimensionless | source-verified |
| $T_{ij}$ | strength of the connection made to neuron $i$ from neuron $j$ | dimensionless | source-verified |
| $U_i$ | fixed threshold of neuron $i$ | dimensionless | source-verified |
| $V^s$ | stored nominal memory state $s$, $s = 1 \cdots n$ | dimensionless | source-verified |
| $H^{s'}_j$ | effective field on neuron $j$ when the state of the system is $V^{s'}$ | dimensionless | source-verified |
| $E$ | energy of a network state with symmetric $T_{ij}$ | arbitrary units | source-verified |
| $\Delta E$ | energy change due to a change $\Delta V_i$ | arbitrary units | source-verified |
| $N$ | number of neurons | dimensionless | source-verified |
| $n$ | number of stored states | dimensionless | source-verified |
| $W$ | mean attempt rate of the asynchronous state updates | 1/time | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $U_i$ | thresholds | dimensionless | 0 unless otherwise stated | page 2555, after equation [1] |
| $T_{ii}$ | self-coupling constraint | dimensionless | 0 | page 2555, after equation [2] |
| memory capacity | number of simultaneously remembered states before severe recall error | dimensionless | about $0.15\,N$ | page 2556, simulation summary |

## Equations

These are exact source transcriptions of bracketed equations [1]-[8].

Asynchronous threshold update rule:

$$
V_i \to 1 \ \ \text{if} \ \ \sum_{j \neq i} T_{ij} V_j > U_i; \qquad V_i \to 0 \ \ \text{if} \ \ \sum_{j \neq i} T_{ij} V_j < U_i,
$$

Hebbian storage prescription for $n$ nominal states:

$$
T_{ij} = \sum_s (2V_i^s - 1)(2V_j^s - 1), \qquad T_{ii} = 0,
$$

Effective-field decomposition:

$$
\sum_j T_{ij} V_j^{s'} = \sum_s (2V_i^s - 1)\left[\sum_j V_j^{s'} (2V_j^s - 1)\right] \equiv H_j^{s'},
$$

Pseudo-orthogonality of stored states:

$$
\sum_j T_{ij} V_j^{s'} \approx \langle H_i^{s'} \rangle \approx (2V_i^{s'} - 1)\, N/2,
$$

Input signal to a cell:

$$
\sum_j T_{ij} V_j,
$$

General Hebbian synapse modification:

$$
\Delta T_{ij} = [V_i(t) V_j(t)]_{\text{average}},
$$

Energy function for symmetric $T_{ij} = T_{ji}$:

$$
E = -\frac{1}{2} \sum_{i \neq j} \sum T_{ij} V_i V_j,
$$

Energy change due to a single-neuron update:

$$
\Delta E = -\Delta V_i \sum_{j \neq i} T_{ij} V_j.
$$

## Term-by-term interpretation

Equation [1] is the asynchronous threshold update: each neuron randomly re-evaluates its state against the weighted input from all other neurons. Equation [2] writes the couplings as a normalized outer product of the stored binary states, with self-couplings removed. Equations [3]-[4] show that the weighted input at a stored state is, up to zero-mean crosstalk noise, proportional to the stored bit itself, which makes stored states stable under [1]. Equation [5] defines the synaptic input signal. Equation [6] is the general Hebbian modification from which prescription [2] is a special case. Equations [7]-[8] define a Lyapunov (energy) function for symmetric couplings; because every accepted update in [1] lowers $E$, the dynamics flows to local minima that serve as retrieved memories.

The paper's statistical analysis equations ([9], entropic measure of wandering; [10], Gaussian bit-error probability) are simulation-analysis tools rather than model equations and are deliberately not transcribed here.

## Inputs, outputs, and conditions

- Input: an initial binary state vector representing partial knowledge of a stored state.
- Output: the attractor state reached under asynchronous updates of equation [1].
- Initial conditions: `not_verified`.
- Boundary conditions: `not_applicable`; locator: not_applicable.
- Network conditions: `source_example_located`; symmetric couplings $T_{ij} = T_{ji}$ with $T_{ii} = 0$, pages 2555-2556.
- Event handling: `source_example_located`; asynchronous random-order updates at mean rate $W$, page 2555.
- Numerical method: `source_example_located`; Monte Carlo simulations with $N = 30$ and $N = 100$, page 2556.
- Stochastic input: `deterministic`; update order is asynchronous with a stochastic mean processing time.
- Simulation scale: `large_scale_network`.

## Assumptions and limitations

The energy argument of equations [7]-[8] requires symmetric couplings; the paper discusses the stochastic asymmetry case separately. Stored-state stability in [4] holds only up to crosstalk noise from the $s \neq s'$ terms, which bounds the capacity near $0.15\,N$. This record does not assert a paper-result reproduction.

## Experimental support

`not assessed`. This status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`.
