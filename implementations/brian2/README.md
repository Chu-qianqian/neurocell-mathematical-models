# Brian2 implementation-only examples

These modules are original, minimal implementations of source-audited equations. They are designed for deterministic, resource-bounded smoke tests and do not reproduce a paper figure or numerical experiment.

## Recorded environment

- Python: 3.12.13
- Brian2: 2.10.1
- NumPy: 2.5.1
- Random seed: 20260723

## Izhikevich 2003

- Module: `izhikevich_2003.py`
- Method: Euler
- Time step: 0.1 ms
- Duration: 200 ms
- Scope: one neuron with the source regular-spiking example values and threshold/reset event
- Unit mapping: the source reduced voltage convention is represented with volts in Brian2; the source input term is implemented as an effective voltage drive

## Montbrio-Pazo-Roxin 2015

- Module: `montbrio_pazo_roxin_2015.py`
- Method: fourth-order Runge-Kutta
- Time step: 0.01 source-time units
- Duration: 20 source-time units
- Scope: one Brian2 state container for the two nondimensional macroscopic ODE states
- Unit mapping: one source-time unit is mapped to 1 ms solely for Brian2 dimensional consistency

The tests check import, execution, finite states, Brian2 unit consistency during model construction, bounded state ranges, deterministic repeatability, and the Izhikevich reset event. They do not assess reference behavior or paper-result reproduction.
