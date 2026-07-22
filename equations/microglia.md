# Microglia: conceptual equation map

A population or state model can express the amount of cells in each state as:

$$\frac{dM_i}{dt}=\sum_{j\ne i}q_{ji}(S)M_j-\sum_{j\ne i}q_{ij}(S)M_i+P_i-D_i,$$

where $M_i$ is the amount of cells in state $i$, $q_{ij}(S)$ is a signal-dependent transition rate, and $P_i$ and $D_i$ are proliferation/recruitment and loss terms. Such a model can describe inflammatory feedback or tissue-scale change, but it is not equivalent to a molecular mechanism for one cell.

When M1/M2 is used, the number of states is only a source-specific modelling simplification; it is not the sole or complete biological classification of microglia.
