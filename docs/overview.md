# Scope, classification, and use boundaries

## What the atlas answers

The unit of this atlas is a model record supported by a traceable source, not an encyclopaedia entry for a cell type. Each record must state whether it models a cell intrinsically, one cellular function, a cell population, a multicellular coupling, or only an indirect parameterisation.

| Classification | Meaning | Example | What it does not establish |
| --- | --- | --- | --- |
| `cell_intrinsic` | State variables explicitly model the cell itself | Membrane potential or intracellular Ca²⁺ | Coverage of all cell physiology |
| `cell_function` | Models one functional module | IP3-receptor Ca²⁺ dynamics | A complete cell model |
| `cell_population` | Dynamics of cell number or state distribution | Microglial populations during inflammation | Resolved single-cell mechanism |
| `coupled_multicellular` | At least two unit types are explicitly coupled | A neuron–astrocyte network | Independent validation of every unit |
| `indirect_parameterization` | A cell is folded into a parameter | Myelin parameters in a cable model | An oligodendrocyte model |

## Controlled tags

**Mathematical forms:** ODE, PDE, SDE, DDE, reaction-diffusion, Markov, Boolean, agent-based, conductance-based, compartmental, cable, population, metabolic, finite-element, hybrid, and multiscale.

**Biological scales:** molecular, signalling pathway, subcellular, single cell, cell population, multicellular network, tissue, brain region, and system level.

**Functional tags:** electrical activity, calcium signalling, ion homeostasis, transmitter release/uptake, metabolism, inflammation, migration, phagocytosis, differentiation, proliferation, myelination, conduction, vascular regulation, intercellular communication, and disease progression.

## Current coverage and limitations

The core table is a bibliographically verified starting point, not a completed systematic review. Neuronal and astrocytic modelling have mature model families. For microglia, oligodendrocytes/OPCs, and Schwann cells, cell-specific records with explicit equations and traceable parameters still need record-level screening. There are no eligible core records yet for ependymal cells, radial glia, neural stem cells, pericytes, or brain endothelial cells.

Mathematical levels must not be conflated. Hodgkin–Huxley models membrane potential and channel gating; a simplified IP3–Ca²⁺ system models a signal module; a cable equation with myelin parameters is not automatically an oligodendrocyte model; and a cytokine-population equation is not automatically a single-microglia model.
