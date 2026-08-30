# Data-driven microglial ischemic-penumbra model

## Verification status

- Bibliography: verified against Crossref and PubMed on 2026-08-30.
- Equation source inspected: author-submitted arXiv full text, version 1.
- Source locator: arXiv:2404.10915v1, Results and Conclusions, equations (4)-(5).
- Transcription status: exact source transcription; maintainer second pass and independent review are pending.
- Full-text access status: lawful author-submitted full text inspected on 2026-08-30.

## Scope

- Cell type: ischemic-penumbra microglial population.
- Model classification: deterministic, data-driven two-state ODE.
- Biological function: post-ischemic M1/M2 microglial cell dynamics.
- Mathematical form: ordinary differential equation.
- Spatial and stochastic terms: no spatial term or stochastic forcing is displayed in the reported ODE.
- Timescale: days.

## Source citation

Amato, S. and Arnold, A. Data-driven modeling and prediction of microglial cell dynamics in the ischemic penumbra. *Mathematical Biosciences* **390**, 109549 (2025). [DOI](https://doi.org/10.1016/j.mbs.2025.109549). The inspected lawful author manuscript is [arXiv:2404.10915v1](https://arxiv.org/abs/2404.10915v1).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $M1(t)$ | detrimental M1 microglial cell count | source count convention | source-verified |
| $M2(t)$ | beneficial M2 microglial cell count | source count convention | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $\theta_1$ | constant term in the M1 equation | source count per source time | 32.9650 | equation (4) |
| $\theta_2$ | M1 coefficient in the M1 equation | inverse source time | -0.1377 | equation (4) |
| $\theta_3$ | M2 coefficient in the M1 equation | inverse source time | 0.3157 | equation (4) |
| $\theta_4$ | constant term in the M2 equation | source count per source time | 70.3415 | equation (5) |
| $\theta_5$ | M1 coefficient in the M2 equation | inverse source time | -0.1569 | equation (5) |
| $\theta_6$ | M2 coefficient in the M2 equation | inverse source time | 0.0217 | equation (5) |

## Equations

The reported sparse SINDy result is transcribed exactly from equations (4)-(5):

$$
\begin{aligned}
\dot{M1}(t) &= \theta_1 + \theta_2 M1(t) + \theta_3 M2(t)
             = 32.9650 - 0.1377M1(t) + 0.3157M2(t),\\
\dot{M2}(t) &= \theta_4 + \theta_5 M1(t) + \theta_6 M2(t)
             = 70.3415 - 0.1569M1(t) + 0.0217M2(t).
\end{aligned}
$$

## Term-by-term interpretation

Each derivative is an affine function of the two observed phenotype-specific counts. The source reports that the candidate library included constant, linear, and quadratic terms, but only the constant and linear terms were active in this fitted system. The coefficients are source-specific identification results, not universal phenotype-transition rates.

## Inputs, outputs, and conditions

- Input: observed M1 and M2 cell-count time series from mouse middle-cerebral-artery-occlusion studies; no external forcing term appears in equations (4)-(5).
- Output: predicted M1 and M2 counts.
- Initial conditions: `not_verified`; the displayed result does not prescribe a universal initial state.
- Boundary conditions: `not_applicable`; the ODE has no spatial domain.
- Network conditions: `not_applicable`; no cell-network topology is defined by the reported two-state system.
- Event handling: `not_applicable`.
- Numerical method: `source_example_located`; arXiv:2404.10915v1, Methodology, Forecast Predictions, reports MATLAB `ode15s` over $[0,50]$ days for forward simulations.
- Stochastic input: `deterministic` for the displayed ODE; uncertainty quantification is a separate parameter-estimation procedure.

## Assumptions and limitations

The model is fitted to a compiled mouse ischemic-penumbra data set and treats M1 and M2 as two count states. It does not identify molecular mechanisms, spatial recruitment, or nonlinear cell-cell interactions. The source explicitly cautions that longer-horizon biological relevance remains uncertain.

## Experimental support

`not assessed`. Source data inform the fitted model, but this curation does not claim an independent experimental validation or reproduction.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`.
