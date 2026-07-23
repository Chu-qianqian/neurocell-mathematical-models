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
