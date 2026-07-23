# Model scope taxonomy

| Scope | Meaning |
| --- | --- |
| `cell_intrinsic` | A state model of one cell or a homogeneous compartment. |
| `cell_function` | A cell-relevant mechanism such as excitability, calcium handling, or differentiation. |
| `cell_population` | A model of cell-state abundances or population dynamics. |
| `coupled_multicellular` | A system coupling two or more cell classes or spatial compartments. |
| `indirect_parameterization` | A model in which a cell type appears only through a fitted or imposed parameter. |

Cell labels describe the source scope, not a claim that all cells of that class share the model.

Examples of careful classification:

- A neuron-astrocyte network is `coupled_multicellular`.
- A population microglia model is `cell_population`.
- A myelinated-axon model is `indirect_parameterization` unless it includes explicit oligodendrocyte or Schwann-cell state variables.
- A theoretical associative or neuronal-network model can be a formal model even when it has no direct experimental validation.
- A simulator, database, or experimental system is not itself a mathematical model.

## Orthogonal controlled classifications

`model_scope` is not a substitute for the controlled fields in the canonical schema:

- `biological_cell_scope` distinguishes neuronal, glial, mixed neuron-glia, neural-population, synaptic, and other nervous-system-related records.
- `model_scale` distinguishes molecular, subcellular, single-cell, multicompartment, pair, microcircuit, population, neural-mass, neural-field, large-scale-network, and whole-brain scales.
- `mathematical_form` distinguishes ODE, PDE, stochastic, difference-equation, event-driven, agent-based, probabilistic, hybrid, and other forms.
- `interaction_scope` and `network_type` describe coupling without conflating it with a spatial boundary condition.
- `spatial_structure`, `stochasticity`, and `plasticity_scope` describe independent model properties.

A source can be relevant without being a neuron or glial-cell model. For example, Morris-Lecar is classified as a neuron-relevant excitable-membrane model, and Li-Rinzel as an astrocyte-relevant calcium mechanism, rather than being relabelled as a source-specific mammalian neuron or complete astrocyte.
