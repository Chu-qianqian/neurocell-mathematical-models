# McIntyre-Richardson-Grill myelinated-axon model

## Verification status

- Bibliography: verified against authoritative metadata on 2026-07-23.
- Equation source inspected: full-text PDF of the published article (Journal of Neurophysiology open archive, pages 995-1006), with every displayed equation checked against the rendered page images.
- Source locator: Appendix: general ionic-current form; gating time constant and kinetics; fast sodium current with rates; persistent sodium current with rates; slow potassium current with rates; juxtaparanodal fast potassium current with rates (used only in Fig. 9); leakage current. All appendix displays are unnumbered in the source.
- Transcription status: exact source transcription, including the printed negative denominators of the slow potassium rate exponentials (see interpretation).
- Independent transcription check: not completed.
- Full-text access status: `source_inspected`.
- Last verified: 2026-08-28.

## Scope

- Biological cell scope: `neuronal`.
- Cell type: `myelinated_axon`.
- Cell subtype: mammalian motor nerve fiber modeled as a double-cable multicompartment structure with 21 nodes of Ranvier and 20 internodes; each internode comprises 2 paranodal myelin-attachment segments (MYSA), 2 paranode main segments (FLUT), and 6 internodal segments (STIN).
- Nervous-system region: `peripheral_nervous_system`.
- Model scope: `indirect_parameterization`.
- Model scale: `multicompartment_cell`.
- Mathematical form: `ordinary_differential_equation` (Hodgkin-Huxley-style gating ODEs at the node; passive double-cable compartments).
- Interaction scope: `intrinsic`.
- Network type: `not_applicable`.
- Spatial structure: `one_dimensional`.
- Stochasticity: `deterministic`.
- Plasticity scope: `none`.

## Source citation

Cameron C. McIntyre; Andrew G. Richardson; Warren M. Grill. Modeling the Excitability of Mammalian Nerve Fibers: Influence of Afterpotentials on the Recovery Cycle. *Journal of Neurophysiology* **87**(2), 995-1006 (2002). [DOI](https://doi.org/10.1152/jn.00353.2001). [PubMed](https://pubmed.ncbi.nlm.nih.gov/11826063/). The full text is freely readable on the publisher site (Journal of Neurophysiology open archive).

## Variables

| Symbol | Meaning | Units | Source status |
| --- | --- | --- | --- |
| $V_m$ | transmembrane potential of a compartment | mV | source-verified |
| $I_{ion}$ | ionic current of a compartment in the general form | mA/cm$^2$ | source-verified |
| $g_{ion}$ | maximum conductance of the individual ion channel type (density) | S/cm$^2$ | source-verified |
| $E_{ion}$ | reversal potential of the ion species | mV | source-verified |
| $\omega$ | generic gating variable (activation or inactivation) ranging from 0 to 1 | dimensionless | source-verified |
| $\alpha_\omega$, $\beta_\omega$ | forward and backward voltage-dependent rate constants of a gate | 1/ms | source-verified |
| $\tau_\omega$ | time constant of gate $\omega$ | ms | source-verified |
| $m$, $h$ | activation and inactivation gates of the fast sodium channel | dimensionless | source-verified |
| $p$ | activation gate of the persistent sodium channel | dimensionless | source-verified |
| $s$ | activation gate of the slow potassium channel | dimensionless | source-verified |
| $n$ | activation gate of the juxtaparanodal fast potassium channel | dimensionless | source-verified |
| $I_{Naf}$ | fast sodium current (nodal) | mA/cm$^2$ | source-verified |
| $I_{Nap}$ | persistent sodium current (nodal) | mA/cm$^2$ | source-verified |
| $I_{Ks}$ | slow potassium current (nodal) | mA/cm$^2$ | source-verified |
| $I_{Kf}$ | juxtaparanodal fast potassium current (used only in Fig. 9) | mA/cm$^2$ | source-verified |
| $I_{Lk}$ | leakage current | mA/cm$^2$ | source-verified |
| $E_{Na}$, $E_K$, $E_{Lk}$ | sodium, potassium, and leakage reversal potentials | mV | source-verified |

## Parameters

| Parameter | Meaning | Units | Value/range | Provenance |
| --- | --- | --- | --- | --- |
| fiber diameter | modeled fiber diameters | um | 5.7; 7.3; 8.7; 10.0; 11.5; 12.8; 14.0; 15.0; 16.0 | Table 1 |
| node-node separation | internodal distance per diameter | um | 500; 750; 1000; 1150; 1250; 1350; 1400; 1450; 1500 | Table 1 |
| myelin lamellae | number of myelin lamellae per diameter | count | 80; 100; 110; 120; 130; 135; 140; 145; 150 | Table 1 |
| node geometry | node length and diameter | um | length 1; diameter 1.9 to 5.5 | Table 1 |
| MYSA geometry | MYSA length, diameter, periaxonal space width | um | length 3; diameter as node; space width 0.002 to 0.004 | Table 1 |
| $c_n$ | nodal membrane capacitance | uF/cm$^2$ | 2 | Table 2 |
| $c_i$ | internodal axolemma capacitance | uF/cm$^2$ | 2 | Table 2 |
| $c_m$ | myelin capacitance (per lamella, 2 membranes per lamella) | uF/cm$^2$ | 0.1 | Table 2 |
| $\rho_a$ | axoplasmic resistivity | ohm-cm | 70 | Table 2 |
| $\rho_p$ | periaxonal resistivity | ohm-cm | 70 | Table 2 |
| $g_m$ | myelin conductance | S/cm$^2$ | 0.001 | Table 2 |
| $g_a$ | MYSA conductance | S/cm$^2$ | 0.001 | Table 2 |
| $g_f$ | FLUT conductance | S/cm$^2$ | 0.0001 | Table 2 |
| $g_i$ | STIN conductance | S/cm$^2$ | 0.0001 | Table 2 |
| $g_{Naf}$ | maximum nodal fast Na conductance (2000 channels/um$^2$ at 15 pS) | S/cm$^2$ | 3.0 | Table 2; Appendix |
| $g_{Ks}$ | maximum nodal slow K conductance (100 channels/um$^2$ at 8 pS) | S/cm$^2$ | 0.08 | Table 2; Appendix |
| $g_{Nap}$ | maximum persistent Na conductance | S/cm$^2$ | 0.01 | Table 2 |
| $g_{Lk}$ | nodal leakage conductance | S/cm$^2$ | 0.007 | Table 2 |
| $E_{Na}$ | sodium Nernst potential | mV | 50.0 | Table 2 |
| $E_K$ | potassium Nernst potential | mV | -90.0 | Table 2 |
| $E_{Lk}$ | leakage reversal potential | mV | -90.0 | Table 2 |
| $V_{rest}$ | resting potential | mV | -80.0 | Table 2 |
| temperature | membrane dynamics derived for | degC | 36 | Appendix |
| extracellular medium | anisotropic point-source medium, longitudinal/transverse resistivity | ohm-cm | 300; 1200 | Methods, Simulation procedure |
| integration | NEURON v4.3, backward Euler, time step | ms | 0.001-0.005 | Methods |
| juxtaparanodal $g_{Kf}$ | fast K conductance for the Fig. 9 variant | S/cm$^2$ | not stated in the article | Appendix |

## Equations

These are exact source transcriptions. All appendix displays are unnumbered in the source; the transcription preserves the printed bracket, brace, and exponent conventions.

Appendix, general form of the ionic currents:

$$
I_{ion} = g_{ion}(V_m - E_{ion})
$$

Appendix, time constant of a gating parameter $\omega$:

$$
\tau_\omega = 1 / (\alpha_\omega + \beta_\omega)
$$

Appendix, kinetics of a gating parameter $\omega$:

$$
d\omega/dt = \alpha_\omega (1 - \omega) - \beta_\omega \omega
$$

Appendix, fast sodium current:

$$
I_{Naf} = g_{Naf} * m^3 * h * (V_m - E_{Na})
$$

Appendix, fast sodium activation rate:

$$
\alpha_m = [6.57 * (V_m + 20.4)]/\{1 - e^{[-(V_m+20.4)/10.3]}\}
$$

Appendix, fast sodium inactivation rate:

$$
\beta_m = \{0.304 * [-(V_m + 25.7)]\}/\{1 - e^{[(V_m+25.7)/9.16]}\}
$$

Appendix, fast sodium inactivation gate forward rate:

$$
\alpha_h = \{0.34 * [-(V_m + 114)]\}/\{1 - e^{[(V_m+114)/11]}\}
$$

Appendix, fast sodium inactivation gate backward rate:

$$
\beta_h = 12.6/\{1 + e^{[-(V_m+31.8)/13.4]}\}
$$

Appendix, persistent sodium current:

$$
I_{Nap} = g_{Nap} * p^3 * (V_m - E_{Na})
$$

Appendix, persistent sodium activation rate:

$$
\alpha_p = [0.0353 * (V_m + 27)]/\{1 - e^{[-(V_m+27)/10.2]}\}
$$

Appendix, persistent sodium backward rate:

$$
\beta_p = \{0.000883 * [-(V_m + 34)]\}/\{1 - e^{[(V_m+34)/10]}\}
$$

Appendix, slow potassium current:

$$
I_{Ks} = g_{Ks} * s * (V_m - E_K)
$$

Appendix, slow potassium activation rate (printed with negative denominators in the exponents):

$$
\alpha_s = 0.3/\{1 + e^{[(V_m+53)/-5]}\}
$$

Appendix, slow potassium backward rate (printed with a negative denominator in the exponent):

$$
\beta_s = 0.03/\{1 + e^{[(V_m+90)/-1]}\}
$$

Appendix, juxtaparanodal fast potassium current (used only in Fig. 9):

$$
I_{Kf} = g_{Kf} * n^4 * (V_m - E_K)
$$

Appendix, juxtaparanodal fast potassium activation rate:

$$
\alpha_n = [0.0462 * (V_m + 83.2)]/\{1 - e^{[-(V_m+83.2)/1.1]}\}
$$

Appendix, juxtaparanodal fast potassium backward rate:

$$
\beta_n = \{0.0824 * [-(V_m + 66)]\}/\{1 - e^{[(V_m+66)/10.5]}\}
$$

Appendix, leakage current:

$$
I_{Lk} = g_{Lk}(V_m - E_{Lk})
$$

## Term-by-term interpretation

The model is a double-cable multicompartment axon (21 nodes, 20 internodes; each internode split into 2 MYSA, 2 FLUT, and 6 STIN segments) in which the nodal membrane carries fast Na, persistent Na, slow K, and leakage conductances in parallel with the nodal capacitance, while every internodal segment carries a myelin layer (conductance in parallel with capacitance) over an axolemmal layer. The appendix gives the membrane dynamics: the general Ohmic driving-force form multiplies each maximum conductance by Hodgkin-Huxley gating variables; each gate follows first-order kinetics with the voltage-dependent rates tabulated above. The fast sodium gate pair (m activation, h inactivation) with the rates driven by 6.57, 0.304, 0.34, and 12.6 determines spike generation; slowing the h kinetics and hyperpolarizing the m-h curve relative to Richardson et al. (2000) raised conduction velocity and the strength-duration time constant. The persistent sodium gate p (no inactivation), with maximum conductance 0.01 S/cm^2 localized at the node, produces the slow inward charge that augments passive internodal discharge and generates the depolarizing afterpotential (DAP). The slow potassium gate s (g_Ks = 0.08 S/cm^2) generates the hyperpolarizing afterpotential (AHP). The juxtaparanodal fast potassium current I_Kf is an additional variant used only in Fig. 9 (its conductance density is not stated in the article). The leakage term closes the nodal current balance.

Printed-slip notes: the two slow potassium rate expressions are printed with negative denominators inside the exponentials, e^{[(V_m+53)/-5]} and e^{[(V_m+90)/-1]}, which are algebraically equivalent to e^{[-(V_m+53)/5]} and e^{[-(V_m+90)/1]}; the transcription reproduces the printed form. The rate constants are given in ms units consistent with the 36 degree C temperature at which the dynamics were derived; alterations in the time constants of m or h are implemented by scaling both the alpha and beta components by the listed percentages.

## Inputs, outputs, and conditions

- Input: intracellular current clamp at a mid-axon node, or extracellular point-source stimulation computed in an infinite homogeneous anisotropic medium (longitudinal resistivity 300 ohm-cm, transverse 1200 ohm-cm) with equivalent intracellular currents.
- Output: action potential and afterpotential shape (DAP of about 15 ms and AHP of about 80 ms, diameter-dependent), strength-duration relationship, current-distance relationship, conduction velocity, recovery cycle, and threshold electrotonus.
- Initial conditions: `not_verified` (models start at rest; $V_{rest} = -80$ mV is listed in Table 2).
- Boundary conditions: `not_applicable` (sealed ends of the finite fiber are implied by the compartment structure; not stated explicitly).
- Network conditions: `not_applicable`.
- Event handling: `not_applicable` (spike detection is implicit in the threshold crossing; no reset rule is displayed).
- Numerical method: `source_example_located`; locator: Methods (NEURON v4.3, backward Euler implicit integration, time step 0.001-0.005 ms).
- Stochastic input: `deterministic`.
- Simulation scale: `multicompartment_cell` (21 nodes plus 20 internodes of 10 segments each; nine fiber diameters 5.7-16 um).

## Assumptions and limitations

The model imposes an idealized myelin electrical structure (per-lamella capacitance and conductance scaled by lamella number) and an explicit paranode-node geometry derived from cat, rat, and human measurements, but it does not represent myelinating-glial dynamics. The persistent Na and slow K kinetics were tuned to reproduce ensemble experimental benchmarks (strength-duration, current-distance, conduction velocity, afterpotential shape, excitability modulation) rather than fitted to single-channel data of these poorly characterized channels. The source notes that time-constant modifications are implemented by scaling alpha and beta components equally. The juxtaparanodal fast K conductance density used in Fig. 9 is not stated in the article.

## Experimental support

`not assessed`. The source compares model action potential and afterpotentials with intra-axonal recordings from rat (David et al. 1995) and cat (Blight and Someya 1985) and recovery-cycle data of human motor axons, but no quantitative validation status is recorded here; this status is separate from bibliography and equation evidence.

## Reproducibility and code

- Repository implementation: `not_implemented`.
- Numerical tests: `not_run`.
- Reference behavior: `not_assessed`.
- Reproduction: `not_attempted`.
- External code license: `not_assessed`; the authors distributed NEURON files on request, and a ModelDB entry exists, but neither has been audited for this record.
