# Research gaps and expansion priorities

## Evidence maturity

Neuronal model families are the most mature, with ion-channel, spiking, compartmental, and cable frameworks plus broad simulator ecosystems. Astrocytic Ca²⁺/IP3, extracellular K⁺, transmitter, and neurovascular-coupling models differ greatly across scales and cannot be reduced to a single Li–Rinzel or De Young–Keizer family. Microglial, oligodendrocyte/OPC, and Schwann-cell records often sit at population, injury, regeneration, or myelin-function levels; they must not be mislabelled as complete cell-intrinsic models.

## Current key gaps

1. Core records do not yet contain source equation locations, units, or independent transcription checks.
2. Microglial models should not use M1/M2 dichotomy as the only modern framework; sources using it must record its scope and limitations.
3. Oligodendrocyte/OPC records must distinguish lineage/differentiation equations from work that only changes myelinated-cable parameters.
4. Explicit, parameterised Schwann-cell models may be relatively sparse and require systematic screening of peripheral-nerve injury, Wallerian degeneration, regeneration, and tissue-engineering literature.
5. Ependymal, radial-glia, neural-stem-cell, pericyte, and brain-endothelial records have not reached the core-record gate.
6. Code provenance, licenses, and experimental validation require record-level auditing; public access alone does not confer reuse rights.

## Platform guidance

Brian2 is suitable for original neuron-spiking, synaptic, and simplified coupled examples. NEURON is more suitable for compartmental, cable, and conduction questions. Spatial Ca²⁺, diffusion, and vascular/tissue problems usually require PDE, finite-element, or reaction-diffusion tools. Cell migration, phagocytosis, or lineage-state transitions may fit agent-based, state-transition, or hybrid models. Every implementation must be labelled either as an original approximation/teaching implementation or a validated reproduction.

## Next priority

Obtain lawfully reviewable equation locations and variable definitions for the six existing records first. Then expand neurons, astrocytes, microglia, oligodendrocytes/OPCs, and Schwann cells with the recorded queries. Only candidates meeting the evidence gate may enter the core catalogue.
