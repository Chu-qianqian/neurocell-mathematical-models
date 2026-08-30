# Core-record comparison matrix

| Model | Cell scope | Mathematical form | Function | Model classification | Equation state | Suggested future platform |
| --- | --- | --- | --- | --- | --- |
| Hodgkin-Huxley | neuron | ODE / conductance-based | Excitability and conduction | `cell_function` | `second_pass_checked` | NEURON, Brian2, Python |
| Izhikevich | neuron | ODE | Spiking patterns | `cell_function` | `second_pass_checked` | Brian2, NEST, Python |
| G-ChI | astrocyte | ODE | Glutamate-regulated Ca²⁺/IP3 | `cell_function` | `second_pass_checked` | Python, MATLAB, Julia |
| Postnov et al. | neuron + astrocyte | ODE | Coupled Ca²⁺ signalling | `coupled_multicellular` | `bibliography_verified` | Python, MATLAB, Julia |
| Amato & Arnold | microglia | ODE | Ischemic-penumbra population dynamics | `cell_population` | `bibliography_verified` | Python, MATLAB, Julia |
| Nikolov et al. | oligodendrocyte | ODE | Differentiation dynamics | `cell_function` | `bibliography_verified` | Python, MATLAB, Julia |

The canonical catalogue is the authoritative source for evidence status. Suggested platforms are technical recommendations based on the public formalism category. They do not establish that a paper has an implementation in that platform or that reproduction has been completed.
