# Halnes astrocyte-extracellular electrodiffusive model

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: author-submitted arXiv LaTeX source (v2).
- Source locator: Model section, "Electrodiffusive formalism", equations (1)-(6).
- Transcription status: exact source transcription from the LaTeX source.
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-24.

## Scope

- Biological cell scope: `glial`.
- Cell type: `astrocyte_extracellular_system`.
- Cell subtype: astrocyte and extracellular-space ion transport.
- Nervous-system region: `central_nervous_system_unspecified`.
- Model scope: `coupled_multicellular`.
- Model scale: `multicompartment_cell`.
- Mathematical form: `partial_differential_equation`.
- Interaction scope: `astrocyte_extracellular`.
- Network type: `not_applicable`.
- Spatial structure: `one_dimensional`.
- Stochasticity: `deterministic`.
- Plasticity scope: `none`.

## Source citation

Geir Halnes; Ivar Ostby; Klas H. Pettersen; Stig W. Omholt; Gaute T. Einevoll. Electrodiffusive Model for Astrocytic and Neuronal Ion Concentration Dynamics. *PLOS Computational Biology* (2013). [DOI](https://doi.org/10.1371/journal.pcbi.1003386). [arXiv:1304.7782v2](https://arxiv.org/abs/1304.7782).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $c_{kn}$ | concentration of ion species $k$ in domain $n$ ($n \in \{I, E\}$) | mol/m$^3$ | source-verified |
| $j_{kM}$ | transmembrane flux density of species $k$, positive from $I$ to $E$ | mol/(m$^2$ s) | source-verified |
| $j_{kn}$ | axial flux density of species $k$ in domain $n$ | mol/(m$^2$ s) | source-verified |
| $v_n$ | electric potential in domain $n$ | volt | source-verified |
| $v_M$ | membrane potential, defined as $v_I - v_E$ | volt | source-verified |
| $x$ | position along the one-dimensional cable | metre | source-verified |
| $t$ | time | second | source-verified |
| $O_M$ | membrane area per tissue volume | 1/metre | source-verified |
| $a_I$ | tissue volume fraction of the intracellular $I$-domain | dimensionless | source-verified |
| $a_E$ | tissue volume fraction of the extracellular $E$-domain | dimensionless | source-verified |
| $\Delta x$ | segment length | metre | source-verified |
| $l$ | cable length | metre | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $D_k$ | diffusion constant of species $k$ in dilute solution | m$^2$/s | parameters_incomplete | equation (4) |
| $\lambda_n$ | tortuosity factor of domain $n$ | dimensionless | parameters_incomplete | equation (4) |
| $z_k$ | valence of ion species $k$ | dimensionless | parameters_incomplete | equation (4) |
| $\psi$ | thermal voltage, $\psi = RT/F$ | volt | parameters_incomplete | equation (4) and source definition of $\psi$ |
| $f(\cdot)$ | membrane-mechanism function (channels, pumps, cotransporters) | source convention | parameters_incomplete | equation (5) |

## Equations

These are exact source transcriptions of equations (1)-(6) of the Model section.

Segment particle conservation for the intracellular domain:

$$
-O_M \Delta x\, j_{kM}(x,t) + a_I j_{kI}(x-\Delta x/2,t) - a_I j_{kI}(x+\Delta x/2,t) = a_I \Delta x\, \frac{\partial c_{kI}(x,t)}{\partial t},
$$

Continuity equation for the intracellular domain:

$$
\frac{\partial j_{kI}(x,t)}{\partial x} + \frac{O_M}{a_I} j_{kM}(x,t) + \frac{\partial c_{kI}(x,t)}{\partial t} = 0,
$$

Continuity equation for the extracellular domain:

$$
\frac{\partial j_{kE}(x,t)}{\partial x} - \frac{O_M}{a_E} j_{kM}(x,t) + \frac{\partial c_{kE}(x,t)}{\partial t} = 0,
$$

Generalized Nernst-Planck axial flux density:

$$
j_{kn}(x,t) = -\frac{D_k}{\lambda_n^{2}}\frac{\partial c_{kn}(x,t)}{\partial x}
- \frac{D_k z_k}{\lambda_n^{2} \psi} c_{kn}(x,t) \frac{\partial v_{n}(x,t)}{\partial x},
$$

General membrane-mechanism flux closure:

$$
j_{kM}(x,t) = f\big(c_{kI}(x,t),\, c_{kE}(x,t),\, v_M(x,t),\, \tilde{m}_1(x,t),\, \tilde{m}_2(x,t),\, \dots\big),
$$

Sealed-end boundary conditions:

$$
j_{kn}(0,t) = j_{kn}(l,t) = 0.
$$

## Term-by-term interpretation

Equations (1)-(3) state particle conservation: transmembrane exchange with the membrane area element $O_M \Delta x$ and axial inflow/outflow through the segment boundaries change the local concentration. Equation (4) splits each axial flux into a diffusion term driven by concentration gradients and an electrical-migration term driven by potential gradients; the tortuosity $\lambda_n$ reduces the effective diffusivity and $\psi = RT/F$ converts potential gradients into migration drives. Equation (5) leaves the membrane mechanisms general: any closure must return the transmembrane flux from the membrane potential, both adjacent concentrations, and local mechanism states $\tilde{m}_i$. Equation (6) seals the cable ends so that no flux enters or leaves the system longitudinally.

## Inputs, outputs, and conditions

- Input: not verified; the source later adds locally electroneutral external ion input terms to the continuity equations.
- Output: concentration fields $c_{kn}(x,t)$ and potentials $v_n(x,t)$.
- Initial conditions: `not_verified`.
- Boundary conditions: `source_example_located`; sealed-end condition, equation (6).
- Network conditions: `not_applicable`; locator: not_applicable.
- Event handling: `not_applicable`; locator: not_applicable.
- Numerical method: `source_example_located`.
- Stochastic input: `deterministic`.
- Simulation scale: `multicompartment_cell`.

## Assumptions and limitations

The formalism assumes one-dimensional macroscopic transport in a two-domain (ICS cable plus ECS coating) geometry, quasi-electroneutral bulk domains with the charge-symmetry condition across the membrane, and a membrane closure $f(\cdot)$ that must be supplied separately. The transcribed equations cover the general formalism only; the astrocyte-specific membrane mechanisms used in the paper's simulations are separate and not transcribed here. This record does not assert a paper-result reproduction.

## Experimental support

`not assessed`. This status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`; a ModelDB entry exists but its license status has not been assessed.
