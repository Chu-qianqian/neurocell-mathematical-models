# Wilson-Cowan excitatory-inhibitory population model

## Verification status

- Bibliography: verified against PubMed, the publisher DOI record, and PMC on 2026-07-23.
- Equation source inspected: lawful PMC page scan of the primary article.
- Source locator: Wilson and Cowan (1972), article p. 8, equations (7)-(8).
- Transcription status: equation transcribed with equivalent notation and an explicit mapping.
- Independent transcription check: not completed.
- Full-text access status: source inspected through PMC.

## Scope

- Cell type: localized excitatory and inhibitory neuron populations.
- Model classification: neuronal population model.
- Model scope: `cell_population`.
- Biological function: coarse-grained excitatory-inhibitory population activity.
- Mathematical form: coupled nonlinear ordinary differential equations.
- Spatial and stochastic terms: the displayed system is temporally coarse grained and non-spatial; later spatial extensions are outside this record.
- Scale: population.
- Timescale: source time-constant convention.

## Source citation

Wilson, H. R. and Cowan, J. D. Excitatory and Inhibitory Interactions in Localized Populations of Model Neurons. *Biophysical Journal* **12**, 1-24 (1972). [DOI](https://doi.org/10.1016/S0006-3495(72)86068-5). [PubMed](https://pubmed.ncbi.nlm.nih.gov/4332108/). [PMC record](https://pmc.ncbi.nlm.nih.gov/articles/PMC1484078/).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $E$ | coarse-grained excitatory population activity | source activity convention | source-verified |
| $I$ | coarse-grained inhibitory population activity | source activity convention | source-verified |
| $P(t),Q(t)$ | external inputs to the excitatory and inhibitory populations | source input convention | source-verified |

The source uses overbars for the coarse-grained activities. This page maps $\bar E\mapsto E$ and $\bar I\mapsto I$ for readability.

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $\tau_E,\tau_I$ | excitatory and inhibitory population time constants | source time convention | parameters_incomplete | article p. 8, equations (7)-(8) |
| $r_E,r_I$ | refractory activity factors | source convention | parameters_incomplete | article p. 8, equations (7)-(8) |
| $k_E,k_I$ | coarse-graining scale factors | source convention | parameters_incomplete | article p. 8, equations (7)-(8) |
| $c_1,c_2,c_3,c_4$ | within- and cross-population coupling coefficients | source convention | parameters_incomplete | article p. 8, equations (7)-(8) |

## Equations

The following is an equivalent-notation transcription of source equations (7)-(8):

$$
\begin{aligned}
\tau_E\frac{dE}{dt}
  &= -E + (1-r_E E)\,S_E\!\left(k_E c_1 E-c_2 k_I I+k_E P(t)\right),\\
\tau_I\frac{dI}{dt}
  &= -I + (1-r_I I)\,S_I\!\left(k_I c_3 E-c_4 k_I I+k_I Q(t)\right).
\end{aligned}
$$

The symbol mapping preserves the source coefficient order. The complete source parameter sets and sigmoid definitions have not yet been registered, so the record remains `parameters_incomplete`.

## Term-by-term interpretation

The negative terms describe decay of coarse-grained activity. The factors $(1-r_EE)$ and $(1-r_II)$ reduce the available population by the refractory fraction. $S_E$ and $S_I$ map weighted recurrent, cross-population, and external inputs to new activity.

## Inputs, outputs, and conditions

Inputs are $P(t)$ and $Q(t)$. Outputs are the coarse-grained activities $E(t)$ and $I(t)$. The source discusses a low-background state and later phase-plane parameter sets, but initial conditions and numerical methods are not registered here. Boundary conditions are not applicable to this temporal ODE record.

## Assumptions and limitations

The variables represent coarse-grained population activity, not individual-neuron membrane voltage or molecular state. The displayed temporal system does not reproduce the later spatial extension. No claim is made that it represents a specific brain region, every oscillation frequency, or explicit PV, SST, VIP, or other transcriptomic cell classes.

## Experimental support

The source compares qualitative population-response behavior with physiological observations. This record does not claim parameter fitting to a modern cell-type-resolved dataset.

## Reproducibility and code

No implementation is included or executed. Brian2 compatibility is classified as `possible_custom_ode`; this is a feasibility assessment only. Code-license status is `license_unclear`, numerical tests were not run, reference behavior was not assessed, and paper results were not reproduced.
