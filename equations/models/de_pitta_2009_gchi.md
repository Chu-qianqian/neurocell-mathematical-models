# G-ChI astrocyte calcium and IP3 model

## Verification status

- Bibliography: verified against Crossref on 2026-07-22.
- Equation source inspected: author-posted arXiv preprint corresponding to the journal article.
- Source locator: De Pittà et al. (2009) preprint, pp. 8, 18, equations (5), (6), and (20); equation (19) defines the glutamate-dependent production term.
- Maintainer second-pass check: completed against the inspected preprint.
- Independent transcription check: not documented; no independent checker evidence is recorded.
- Full-text access status: lawful author-posted preprint inspected; journal metadata verified separately.

## Scope

- Cell type: glutamate-responsive astrocyte.
- Model classification: intracellular calcium and IP3 ODE model.
- Biological function: glutamate-regulated calcium oscillations and pulsations.
- Mathematical form: three-state nonlinear ODE system.
- Spatial and stochastic terms: no spatial or stochastic term in the curated system.
- Timescale: source concentration-rate convention.

## Source citation

De Pittà, M., Goldberg, M., Volman, V., Berry, H. and Ben-Jacob, E. Glutamate regulation of calcium and IP3 oscillating and pulsating dynamics in astrocytes. *Journal of Biological Physics* **35**, 383-411 (2009). [DOI](https://doi.org/10.1007/s10867-009-9155-y). [Author preprint](https://arxiv.org/abs/0912.3057).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $C$ | cytosolic calcium concentration | micromolar | source-verified |
| $h$ | IP3-receptor inactivation variable | dimensionless | source-verified |
| $I$ | intracellular IP3 concentration | micromolar | source-verified |
| $\gamma$ | extracellular glutamate concentration | micromolar | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $v_{ER},r_C,r_L$ | pump, channel, and leak rate scales | source rate units | parameters_incomplete | equations (1)-(5) and source table |
| $K_{ER},K_\pi,K_R,K_p$ | Hill or affinity constants | source concentration units | parameters_incomplete | equations (1), (17)-(19) and source table |
| $v_\delta,v_\beta$ | PLC-delta and PLC-beta IP3 production scales | source rate units | parameters_incomplete | equations (7)-(8), (15), (19) |

## Equations

The following is an equivalent notation with a documented mapping and a maintainer second-pass check against source equations (5), (6), and (20). $J_{\mathrm{chan}}$, $J_{\mathrm{leak}}$, and $J_{\mathrm{pump}}$ denote the source flux expressions in equations (1)-(5); $v_{\mathrm{glu}}$ is source equation (19).

$$
\frac{dC}{dt}=J_{\mathrm{chan}}(C,h,I)+J_{\mathrm{leak}}(C)-J_{\mathrm{pump}}(C),
\qquad
\frac{dh}{dt}=\frac{h_\infty(C,I)-h}{\tau_h(C,I)}.
$$

$$
\frac{dI}{dt}=v_{\mathrm{glu}}(\gamma,C)+v_\delta(C,I)-v_{3K}(C,I)-v_{5P}(I).
$$

For the transcription mapping, $v_{\mathrm{glu}}$ is the source's PLC-beta production term, $v_\delta$ is PLC-delta production, and $v_{3K}$ and $v_{5P}$ are the two source degradation terms. The source's Hill-function parameterization and full parameter table are not yet fully registered; therefore the record remains `parameters_incomplete`.

## Term-by-term interpretation

Calcium changes through IP3-receptor release, ER leak, and SERCA uptake. The gate relaxes toward its calcium- and IP3-dependent steady state. IP3 receives glutamate-driven and endogenous production and loses mass through 3-kinase and 5-phosphatase routes.

## Inputs, outputs, and conditions

Input is extracellular glutamate $\gamma$; outputs are $C$, $h$, and $I$. Initial conditions, parameter-set selection, and numerical method are `not verified` at registry level for this curated page.

## Assumptions and limitations

The system is a cell-averaged intracellular model. It does not by itself represent astrocyte morphology, intercellular diffusion, or a universal astrocyte calcium mechanism.

## Reproducibility and code

No third-party code is included. Code license status is `license_unclear`.
