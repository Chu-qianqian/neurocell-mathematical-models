# Hodgkin-Huxley conductance model

## Verification status

- Bibliography: verified against Crossref on 2026-07-22.
- Equation source inspected: publisher-accessible article and Physiome model record.
- Source locator: Hodgkin and Huxley (1952), pp. 505 and 518-519, equations (1)-(7), (15)-(16), and (26); Physiome record 0155 identifies the rate-law page.
- Maintainer second-pass check: completed against the cited article's summary of equations.
- Independent transcription check: not documented; no independent checker evidence is recorded.
- Full-text access status: lawful publisher-accessible source inspected.

## Scope

- Cell type: squid giant axon membrane.
- Model classification: conductance-based ODE; one-dimensional cable extension is also given in the source.
- Biological function: voltage-clamp membrane current and action-potential conduction.
- Mathematical form: nonlinear ODE system with voltage-dependent transition rates.
- Spatial and stochastic terms: no stochastic term; the source derives a cable PDE separately.
- Timescale: milliseconds at the source reference temperature.

## Source citation

Hodgkin, A. L. and Huxley, A. F. A quantitative description of membrane current and its application to conduction and excitation in nerve. *The Journal of Physiology* **117**, 500-544 (1952). [DOI](https://doi.org/10.1113/jphysiol.1952.sp004764). [Persistent source](https://physoc.onlinelibrary.wiley.com/doi/10.1113/jphysiol.1952.sp004764).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $V$ | membrane potential displacement from rest | mV | source-verified |
| $I$ | total membrane current density | microampere per square centimetre | source-verified |
| $m,h,n$ | sodium activation, sodium inactivation, and potassium activation variables | dimensionless | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| $C_M$ | membrane capacitance per area | microfarad per square centimetre | parameters_incomplete | source equation (26) |
| $\bar g_K,\bar g_{Na},g_l$ | maximal potassium, sodium, and leak conductance densities | millimho per square centimetre | parameters_incomplete | source equation (26) and Table 3 |
| $V_K,V_{Na},V_l$ | reversal-potential displacements | mV | parameters_incomplete | source equation (26) |

## Equations

The following is an exact source transcription with a maintainer second-pass check:

$$
I=C_M\frac{dV}{dt}+\bar g_K n^4(V-V_K)+\bar g_{Na}m^3h(V-V_{Na})+g_l(V-V_l).
$$

The gating equations are exact source transcriptions with a maintainer second-pass check; $x$ is $n$, $m$, or $h$ with its respective source rates:

$$
\frac{dx}{dt}=\alpha_x(V)(1-x)-\beta_x(V)x.
$$

The page does not reproduce the six voltage-rate expressions because their values, reference voltage convention, and temperature scaling should be curated together from the same source table.

## Term-by-term interpretation

The capacitive term changes membrane voltage. Potassium, sodium, and leak terms are conductance times driving force. The gates describe voltage-dependent activation or inactivation; their products scale the sodium and potassium conductances.

## Inputs, outputs, and conditions

Input is prescribed total current density $I$ in the voltage-clamp formulation. Outputs are $V$ and the gates. Resting-state initialization, source parameter values, and numerical method are recorded as `parameters_incomplete` in the registry; the source also presents a numerical cable calculation.

## Assumptions and limitations

This is a squid giant-axon membrane model with a specific voltage and temperature convention. It is not a universal neuron model and does not represent morphology, synaptic chemistry, or channel stochasticity.

## Reproducibility and code

The [Physiome record 0155](https://www.imagwiki.nibib.nih.gov/physiome/jsim/models/webmodel/NSR/hodgkinhuxley1952) was inspected during the maintainer workflow. That comparison is not represented as an independent check because no independent checker record is available. No third-party code is included here; code license status is `license_unclear`.
