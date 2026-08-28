# Potjans-Diesmann cortical microcircuit model

## Verification status

- Bibliography: verified against the public PubMed record on 2026-07-23.
- Equation source inspected: PMC open-access full text of the published article (Europe PMC record PMC3920768, XML and PMC CDN equation images), with every displayed equation checked against the rendered equation images.
- Source locator: Methods, Connectivity Data equations (1)-(2); equation (3) with the physiological map; Lateral Connectivity Model equations (4)-(9) with one unnumbered display; Connectivity Data Analysis equations (10)-(11); Consistent Modifications of Target Specificity equations (12)-(13) with one unnumbered display; Table 4 neuron and synapse rows (subthreshold dynamics, postsynaptic current, spike condition).
- Transcription status: exact source transcription; two comparison operators that are missing from the PMC-rendered Table 4 equation images are transcribed as rendered and flagged in the interpretation.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-28.

## Scope

- Biological cell scope: `neural_population`.
- Cell type: `neural_population`.
- Cell subtype: four cortical layers (L2/3, L4, L5, L6), each with one excitatory (pyramidal) and one inhibitory population of leaky integrate-and-fire neurons, plus a fixed-rate Poisson thalamic population.
- Nervous-system region: `cerebral_cortex`.
- Model scope: `coupled_multicellular`.
- Model scale: `local_microcircuit` (cortical network under 1 mm^2 of surface; reference size 77,169 neurons plus 902 thalamic cells).
- Mathematical form: `hybrid` (leaky integrate-and-fire membrane ODE with fixed threshold and refractory clamp, exponential postsynaptic currents, Poisson background; the numbered equations of the article formalize the connectivity-map construction).
- Interaction scope: `network_connectivity`.
- Network type: `cortical_microcircuit`.
- Spatial structure: `network_topology` (random connections; a lateral Gaussian connectivity model is used only to reconcile maps, not in the simulations).
- Stochasticity: `stochastic` (Poisson background; Gaussian-distributed synaptic weights and delays).
- Plasticity scope: `none`.

## Source citation

Tobias C. Potjans; Markus Diesmann. The cell-type specific cortical microcircuit: relating structure and activity in a full-scale spiking network model. *Cerebral Cortex* **24**(3), 785-806 (2014). [DOI](https://doi.org/10.1093/cercor/bhs358). [PubMed](https://pubmed.ncbi.nlm.nih.gov/23203991/). Open access (Creative Commons Attribution Non-Commercial License); PMC record [PMC3920768](https://europepmc.org/article/MED/23203991).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $C_a$ | connection probability of the anatomical map | dimensionless | source-verified |
| $C_p$ | connection probability of the physiological map (hit-rate weighted average) | dimensionless | source-verified |
| $K$ | number of synapses participating in a connection | count | source-verified |
| $N^{pre}$, $N^{post}$ | neuron numbers of the pre- and postsynaptic populations | count | source-verified |
| $R_i$ | hit rate (detected connections over tested pairs) of experiment $i$ | dimensionless | source-verified |
| $Q_i$ | number of tested pairs in experiment $i$ | count | source-verified |
| $C(r)$ | lateral connectivity model, a 2D Gaussian in distance $r$ | dimensionless | source-verified |
| $C_0$ | peak connection probability of the lateral model (zero distance) | dimensionless | source-verified |
| $\sigma$ | lateral spread of the lateral connectivity model | mm | source-verified |
| $r_a$, $r_p$ | sampling radii of the anatomical and physiological experiments | mm | source-verified |
| $\tilde{C}_a$ | global mean of the (modified) anatomical connectivity map | dimensionless | source-verified |
| $\bar{C}_p$ | global mean of the physiological connectivity map | dimensionless | source-verified |
| $\bar{\tilde{C}}_a$ | anatomical map mean used in the model-referenced form of equation (9) | dimensionless | source-verified |
| $r_m$ | radius of the simulated network model | mm | source-verified |
| $C_m$ | mean connection probability of the model (symbol collision with membrane capacitance $C_m$ of Table 5 is present in the source) | dimensionless | source-verified |
| $\zeta$ | discrepancy index of a connection between the two maps | dimensionless | source-verified |
| $T$ | target specificity of a projection | dimensionless | source-verified |
| $\Delta$ | fraction of synapses targeting excitatory neurons | dimensionless | source-verified |
| $N^{post=e}$, $N^{post=i}$ | neuron numbers of the excitatory and inhibitory target populations | count | source-verified |
| $V(t)$ | membrane potential of an integrate-and-fire neuron | mV | source-verified |
| $t^*$ | spike time stamp of the last emitted action potential | ms | source-verified |
| $I(t)$ | input current to the neuron (synaptic and background) | pA | source-verified |
| $I_{syn}(t)$ | exponential postsynaptic current of weight $w$ | pA | source-verified |
| $V$ | membrane potential | mV | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $N$ (populations) | population sizes of L2/3e, L2/3i, L4e, L4i, L5e, L5i, L6e, L6i, Th | count | 20683; 5834; 21915; 5479; 4850; 1065; 14395; 2948; 902 | Table 5 |
| $k_{ext}$ (reference) | external inputs per neuron, layer-specific | count | 1600; 1500; 2100; 1900; 2000; 1900; 2900; 2100 | Table 5 |
| $k_{ext}$ (layer independent) | alternative uniform external input setting | count | 2000; 1850; 2000; 1850; 2000; 1850; 2000; 1850 | Table 5 |
| $\nu_{bg}$ | background spike rate per external synapse | Hz | 8 | Table 5 |
| external inputs (anatomical estimate) | thalamic / gray matter / other white matter inputs per excitatory neuron in L2/3, L4, L5, L6 | count | 0/93/0/47; 534/353/389/79; 1072/1665/1609/2790; totals 1606/2111/1997/2915 | Table 3 |
| $w \pm \delta w$ | excitatory synaptic strength | pA | 87.8 ± 8.8 | Table 5 |
| $g$ | relative inhibitory synaptic strength | dimensionless | −4 | Table 5 |
| $d_e \pm \delta d_e$ | excitatory synaptic delay | ms | 1.5 ± 0.75 | Table 5 |
| $d_i \pm \delta d_i$ | inhibitory synaptic delay | ms | 0.8 ± 0.4 | Table 5 |
| $\tau_m$ | membrane time constant | ms | 10 | Table 5 |
| $\tau_{ref}$ | absolute refractory period | ms | 2 | Table 5 |
| $\tau_{syn}$ | postsynaptic current time constant | ms | 0.5 | Table 5 |
| $C_m$ | membrane capacitance | pF | 250 | Table 5 |
| $V_{reset}$ | reset potential | mV | −65 | Table 5 |
| $\theta$ | fixed firing threshold | mV | −50 | Table 5 |
| $\nu_{th}$ | thalamic firing rate during the input period | Hz | 15 | Table 5 |
| EPSP calibration | excitatory postsynaptic potential amplitude, rise time, width | mV; ms | 0.15; 1.6; 8.8 | Methods, Synaptic Plasticity paragraph |
| connectivity overrides | L4e to L2/3e excitatory strength doubled; L2/3i to L5e and L4i to L2/3i probabilities set to 0.2 | dimensionless | as stated | Methods; Haeusler and Maass (2007) |
| simulation step size | computation step size (delays drawn as multiples) | ms | 0.1 (per repository reference implementation; not stated in the article) | not stated in article |

## Equations

These are exact source transcriptions. Numbering follows the published article; displays that the source leaves unnumbered are identified by section.

Methods, Connectivity Data, connection probability from the number of synapses $K$ (multiple contacts allowed; synapses randomly distributed):

$$
C_a = \frac{K}{N^{pre}\, N^{post}},
$$

Methods, the often-used first-order Taylor approximation of equation (1), valid for small $K/(N^{pre} N^{post})$:

$$
C_a = 1 - \left( 1 - \frac{1}{N^{pre}\, N^{post}} \right)^{K}.
$$

Methods, physiological map connection probability as the hit-rate weighted average over experiments:

$$
C_p = \frac{\sum_i R_i Q_i}{\sum_j Q_j},
$$

Methods, Lateral Connectivity Model, Gaussian lateral connectivity profile with lateral distance $r$:

$$
C(r) = C_0 \exp\left( \frac{-r^2}{2 \sigma^2} \right),
$$

Methods, lateral model prediction for the anatomical map with sampling radius $r_a$:

$$
C_a = \frac{2 \pi C_0 \sigma^2}{\pi r_a^2} \left[ 1 - \exp\left( \frac{-r_a^2}{2 \sigma^2} \right) \right],
$$

Methods, lateral model prediction for the physiological map with sampling radius $r_p$:

$$
C_p = \frac{2 \pi C_0 \sigma^2}{\pi r_p^2} \left[ 1 - \exp\left( \frac{-r_p^2}{2 \sigma^2} \right) \right].
$$

Methods, unnumbered consistency condition stating that both maps share the same underlying lateral connectivity:

$$
\frac{\pi r_a^2 C_a}{1 - \exp(-r_a^2/2\sigma^2)} = \frac{\pi r_p^2 C_p}{1 - \exp(-r_p^2/2\sigma^2)},
$$

Methods, lateral spread solved numerically from the consistency condition:

$$
\sigma = r_p \left[ -2 \ln \left( 1 - \frac{\pi r_p^2 C_p}{\tilde{C}_a} \right) \right]^{-1/2},
$$

Methods, peak amplitude of the lateral model:

$$
C_0 = \frac{\tilde{C}_a}{2 \pi \sigma^2}.
$$

Methods, mean connection probability of the model at network radius $r_m$ (three chained equalities as printed):

$$
C_m = \frac{1}{\pi r_m^2} \int_0^{r_m} \int_0^{2 \pi} C(r) r \, dr \, d\varphi = \frac{2}{r_m^2} C_0 \sigma^2 \left[ 1 - \exp\left( \frac{-r_m^2}{2 \sigma^2} \right) \right] = \frac{\bar{\tilde{C}}_a}{\pi r_m^2} \left[ 1 - \left( 1 - \frac{\pi r_p^2 \bar{C}_p}{\tilde{C}_a} \right)^{r_m^2 / r_p^2} \right],
$$

Methods, Connectivity Data Analysis, discrepancy index of a connection:

$$
\zeta = \frac{\max(C_a', C_p')}{\min(C_a', C_p')} = \frac{\max(C_a / \bar{C}_a, C_p / \bar{C}_p)}{\min(C_a / \bar{C}_a, C_p / \bar{C}_p)},
$$

Methods, target specificity of a projection:

$$
T = \frac{C^{post=e} - C^{post=i}}{C^{post=e} + C^{post=i}},
$$

Methods, equation determining the excitatory-target synapse fraction $\Delta$ under a requested target specificity (exact, in terms of connection probabilities):

$$
2T = \left( 1 - \frac{1}{N^{post=i} N^{pre}} \right)^{(1-\Delta)K} (1 + T) - \left( 1 - \frac{1}{N^{post=e} N^{pre}} \right)^{\Delta K} (1 - T).
$$

Methods, unnumbered first-order Taylor solution for $\Delta$:

$$
\Delta = \frac{(1 + T) N^{post=e}}{(1 - T) N^{post=i} + (1 + T) N^{post=e}}.
$$

Methods, revised connection probabilities after imposing a target specificity:

$$
C^{post=i(e)} = \left( \frac{1 - T}{1 + T} \right)^{+(-)1} C^{post=e(i)}.
$$

Table 4, neuron and synapse model, subthreshold dynamics (the condition is rendered "if (t t$^*$ + $\tau_{ref}$)" in the PMC equation image; see interpretation):

$$
\frac{dV}{dt} = -\frac{V}{\tau_m} + \frac{I(t)}{C_m} \ \text{if} \ (t\, t^* + \tau_{ref})
$$

Table 4, synapse model, exponential postsynaptic current:

$$
I_{syn}(t) = w e^{-t/\tau_{syn}},
$$

Table 4, spiking condition (rendered "$V(t-)\theta \wedge V(t+) \geq \theta$" in the PMC equation image; see interpretation):

$$
V(t-)\, \theta \wedge V(t+) \geq \theta,
$$

## Term-by-term interpretation

Equation (1) converts the synapse count $K$ reported by the anatomical map into a connection probability under random synapse placement with multiple contacts allowed; equation (2) is its often-used first-order Taylor expansion, valid for sparse connectivity. Equation (3) pools patch-clamp pair measurements into a physiologically estimated connection probability, weighting each experiment's hit rate $R_i$ by its number of tested pairs $Q_i$. Equations (4)-(6) and the unnumbered consistency condition constitute the lateral connectivity reconciliation: an underlying Gaussian profile $C(r)$ sampled within cylinders of radii $r_a$ (anatomy) and $r_p$ (physiology) predicts the measured means $C_a$ and $C_p$; equating the two predictions yields the consistency condition, whose numerical solution gives the spread $\sigma$ (equation (7)) and peak $C_0$ (equation (8)). Equation (9) then gives the model's mean connection probability $C_m$ at the simulated network radius $r_m$ in three chained forms, the last expressed purely through the experimentally accessible quantities $\bar{\tilde{C}}_a$, $r_p$, and $\bar{C}_p$; individual connection probabilities of a map are rescaled by the ratio $C_m$ over the map's global mean. Equation (10) defines the discrepancy index $\zeta$ after global rescaling, and equation (11) the target specificity $T$ of a projection onto the excitatory and inhibitory populations of a target layer. Equation (12) is the exact nonlinear condition determining the fraction $\Delta$ of a projection's synapses that must target excitatory neurons to realize a requested $T$, using equation (1) inside the target-specificity definition; its first-order Taylor solution is the unnumbered display for $\Delta$, and equation (13) gives the revised pair of connection probabilities consistent with $T$. The L4e to L2/3e strength doubling and the fixed 0.2 probabilities for L2/3i to L5e and L4i to L2/3i are applied during map compilation.

Table 4 presents the network model in Nordlie et al. (2009) format: eight integrate-and-fire cortical populations plus a fixed-rate Poisson thalamic population; random pairwise connection drawing (binomially distributed in- and out-degrees); fixed weights and delays drawn from Gaussian distributions. The subthreshold row reads, in the PMC-rendered equation image, $\frac{dV}{dt} = -V/\tau_m + I(t)/C_m$ "if (t t$^*$ + $\tau_{ref}$)" with the alternative "V(t) = V$_{reset}$"; the comparison operator between $t$ and $t^* + \tau_{ref}$ is absent from the rendered image. Likewise the spiking-condition image renders "$V(t-)\theta \wedge V(t+) \geq \theta$" without the operator between $V(t-)$ and $\theta$. Both rows follow the standardized Nordlie schema, in which the subthreshold equation integrates only outside the refractory period, $t > t^* + \tau_{ref}$ (otherwise the potential is clamped at $V_{reset}$), and a spike is emitted when $V(t-) < \theta \wedge V(t+) \geq \theta$; the transcription preserves the rendered form exactly and flags the missing operators as an artifact of the PMC figure rendering rather than a source typographical slip. The exponential current $I_{syn}(t) = w e^{-t/\tau_{syn}}$ uses $\tau_{syn} = 0.5$ ms; weights and delays are Gaussian ($w = 87.8 \pm 8.8$ pA; delays $1.5 \pm 0.75$ ms excitatory, $0.8 \pm 0.4$ ms inhibitory, constrained positive and to multiples of the computation step size, sign change prohibited); inhibitory strengths are scaled by $g = -4$; all excitatory synapses are calibrated to 0.15 mV EPSP amplitude (rise 1.6 ms, width 8.8 ms); the thalamic input rate is 15 Hz during the stimulus period, and the spontaneous background is an 8 Hz Poisson process per external synapse.

## Inputs, outputs, and conditions

- Input: independent fixed-rate Poisson background spike trains to every cortical neuron ($k_{ext}$ synapses at $\nu_{bg} = 8$ Hz; layer-specific totals per Table 3), plus thalamic pulses (15 Hz for the input period) to L4 and L6.
- Output: spike activity and membrane potentials of sampled neurons in every population; population firing rates (Table 6), CV of interspike intervals, and synchrony measures.
- Initial conditions: `not_verified`.
- Boundary conditions: `not_applicable`.
- Network conditions: `registered`; locator: Table 5 connectivity matrix (connection probabilities between all population pairs, 8 by 9 including thalamus) and Methods connectivity-map construction, equations (1)-(13).
- Event handling: `registered`; locator: Table 4, spiking condition and reset rule (threshold $\theta = -50$ mV, reset to $V_{reset} = -65$ mV, absolute refractory period $\tau_{ref} = 2$ ms).
- Numerical method: `source_example_located`; locator: Methods (delays drawn as multiples of the computation step size; NEST simulation infrastructure; reference network of 77,169 cortical neurons).
- Stochastic input: `stochastic` (Poisson background; Gaussian weights and delays).
- Simulation scale: `local_microcircuit` (1 mm^2 of cortical surface; reference parameterization in Table 5; robustness checks with constant-DC background and layer-independent inputs).

## Assumptions and limitations

The microcircuit abstracts each layer to two homogeneous populations of point neurons with exponential synapses and no plasticity; cell-type specificity beyond the excitatory/inhibitory split, dendritic morphology, and neuromodulation are outside the model. The connectivity map is compiled from data across species and areas (mostly rodent), with explicit target-specificity amendments (Table 2) where measurements are missing; the lateral connectivity model is used only to reconcile the two experimental maps, and simulations use laterally uniform connectivity. The comparison operators missing from the two PMC-rendered Table 4 equations are flagged in the interpretation and the standard Nordlie-format reading is stated. Layer- and cell-type-specific structure does not establish molecular cell identity or a universal cortical circuit.

## Experimental support

`not assessed`. Table 6 of the source compares simulated layer-specific spontaneous and evoked rates with in vivo electrophysiology (de Kock et al. 2007; Sakata and Harris 2009; Hromadka et al. 2008; de la Rocha et al. 2008, among others); no quantitative validation status is recorded here; this status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`; the reference implementation is distributed with NEST (the article's simulations used NEST), and community reimplementations exist, but none has been audited for this record.
