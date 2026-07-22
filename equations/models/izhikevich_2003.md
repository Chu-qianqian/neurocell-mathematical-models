# Izhikevich simple spiking-neuron model

## Verification status

- Bibliography: verified against Crossref on 2026-07-22.
- Equation source inspected: author-hosted full paper PDF.
- Source locator: Izhikevich (2003), p. 1569, Section II, equations (1)-(3).
- Independent transcription check: completed against the author-hosted paper PDF.
- Full-text access status: lawful author-hosted full text inspected.

## Scope

- Cell type: phenomenological cortical and thalamic neuron types.
- Model classification: two-dimensional ODE with an event-triggered reset.
- Biological function: spiking and bursting dynamics.
- Mathematical form: hybrid ODE/reset system.
- Spatial and stochastic terms: none in the single-neuron equations.
- Timescale: milliseconds.

## Source citation

Izhikevich, E. M. Simple model of spiking neurons. *IEEE Transactions on Neural Networks* **14**, 1569-1572 (2003). [DOI](https://doi.org/10.1109/tnn.2003.820440). [Author source](https://izhikevich.org/publications/spikes.htm).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $v$ | membrane potential | mV scale | source-verified |
| $u$ | recovery variable representing potassium activation and sodium inactivation effects | source convention | source-verified |
| $I$ | synaptic or injected current | source convention | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $a$ | recovery time-scale parameter | dimensionless in source convention | typical value 0.02 | p. 1569 |
| $b$ | recovery sensitivity parameter | dimensionless in source convention | typical value 0.2 | p. 1569 |
| $c$ | post-spike voltage reset | mV | typical value -65 | p. 1569 |
| $d$ | post-spike recovery increment | dimensionless in source convention | typical value 2 | p. 1570 |

## Equations

These are exact verified transcriptions of equations (1)-(3):

$$
\frac{dv}{dt}=0.04v^2+5v+140-u+I,
\qquad
\frac{du}{dt}=a(bv-u).
$$

$$
\text{if } v\geq 30\ \mathrm{mV},\quad v\leftarrow c,\quad u\leftarrow u+d.
$$

## Term-by-term interpretation

The quadratic voltage term supplies nonlinear spike initiation. The recovery variable negatively feeds back on voltage. The reset is a hybrid event, not a continuous ionic-current equation; it returns voltage and increments recovery after the stated apex threshold.

## Inputs, outputs, and conditions

The source treats $I$ as synaptic or injected current. It provides a network example initialized with $v=-65$ and $u=bv$ and advances voltage with two 0.5-ms half steps for numerical stability. That example is a source-specific demonstration, not a prescribed universal solver.

## Assumptions and limitations

The model is phenomenological and reduces detailed channel mechanisms to two states plus reset. Parameter sets map to firing patterns but are not cell-type identity proofs.

## Reproducibility and code

The paper links an author-hosted MATLAB demonstration. It is not imported into this repository. Code license status is `license_unclear`.
