# Montbrio-Pazo-Roxin exact neural-mass reduction

## Verification status

- Bibliography: verified against the publisher DOI record and arXiv on 2026-07-23.
- Equation source inspected: author-submitted arXiv version 1.
- Source locator: arXiv:1506.06581v1, Section II.B, equations (12a)-(12b).
- Transcription status: exact source transcription.
- Independent transcription check: not completed.
- Full-text access status: lawful author-submitted full text inspected.

## Scope

- Cell type: heterogeneous spiking-neuron population.
- Model classification: exact macroscopic reduction of the source QIF network.
- Model scope: `cell_population`.
- Biological function: population firing-rate and mean-voltage dynamics.
- Mathematical form: two coupled nonlinear ordinary differential equations.
- Spatial and stochastic terms: no spatial or stochastic term in the displayed macroscopic system.
- Scale: population.
- Timescale: source nondimensional convention.

## Source citation

Montbrió, E., Pazó, D. and Roxin, A. Macroscopic Description for Networks of Spiking Neurons. *Physical Review X* **5**, 021028 (2015). [DOI](https://doi.org/10.1103/PhysRevX.5.021028). [arXiv:1506.06581v1](https://arxiv.org/abs/1506.06581).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $r$ | instantaneous population firing rate | inverse source time | source-verified |
| $v$ | population mean membrane potential | source voltage convention | source-verified |
| $I(t)$ | common time-dependent external input | source current convention | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $\Delta$ | half-width of the Lorentzian excitability distribution | source convention | parameters_incomplete | Section II.B, equation (12a) |
| $\bar\eta$ | center of the excitability distribution | source convention | parameters_incomplete | Section II.B, equation (12b) |
| $J$ | mean-field coupling strength | source convention | parameters_incomplete | Section II.B, equation (12b) |

## Equations

These are exact source transcriptions of equations (12a)-(12b):

$$
\begin{aligned}
\dot r &= \frac{\Delta}{\pi}+2rv,\\
\dot v &= v^2+\bar\eta+Jr+I(t)-\pi^2r^2.
\end{aligned}
$$

## Term-by-term interpretation

$\Delta/\pi$ reflects the width of quenched excitability heterogeneity. The $2rv$ term couples firing rate and mean voltage. In the voltage equation, $\bar\eta$, $Jr$, and $I(t)$ provide mean excitability, recurrent input, and external forcing, while $-\pi^2r^2$ is the macroscopic feedback associated with spike generation and reset.

## Inputs, outputs, and conditions

Input is $I(t)$; outputs are $r(t)$ and $v(t)$. The source reports Euler simulations with a fixed time step for network comparisons, but this repository has not implemented or rerun that source simulation protocol. Initial conditions are not registered. Boundary conditions are not applicable to the displayed temporal ODE.

## Assumptions and limitations

The exact reduction applies to the source network of all-to-all coupled QIF neurons in the thermodynamic limit with quenched excitability drawn from a Lorentzian distribution. It is not an exact reduction for arbitrary spiking-neuron families, finite sparse networks, or arbitrary heterogeneity distributions.

## Experimental support

The source provides a theoretical derivation and comparisons with simulations of the underlying QIF network. This is not direct biological validation.

## Reproducibility and code

The repository provides an [original Brian2 implementation-only example](../../implementations/brian2/montbrio_pazo_roxin_2015.py). It maps one nondimensional source-time unit to 1 ms for Brian2 dimensional consistency and uses Python 3.12.13, Brian2 2.10.1, NumPy 2.5.1, seed 20260723, fourth-order Runge-Kutta integration, a 0.01-source-unit time step, and a 20-source-unit duration.

Passing smoke tests establish execution, finite states, bounded ranges, deterministic repeatability, and Brian2 unit consistency. The chosen parameter point is a bounded implementation test, not a source demonstration parameter set. Reference behavior was not assessed, and no paper result was reproduced.
