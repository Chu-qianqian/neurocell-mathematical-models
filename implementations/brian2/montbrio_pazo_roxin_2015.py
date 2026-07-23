"""Minimal Brian2 implementation of the audited MPR 2015 mean-field ODE."""

from __future__ import annotations

from typing import Any

import brian2 as b2
import numpy as np


RANDOM_SEED = 20260723
DEFAULT_DT = 0.01 * b2.ms
DEFAULT_DURATION = 20 * b2.ms
SOURCE_TIME_UNIT = 1 * b2.ms
INTEGRATION_METHOD = "rk4"


def run_smoke(
    *,
    seed: int = RANDOM_SEED,
    dt: b2.Quantity = DEFAULT_DT,
    duration: b2.Quantity = DEFAULT_DURATION,
) -> dict[str, Any]:
    """Run a bounded nondimensional example without claiming paper reproduction."""
    b2.start_scope()
    b2.seed(seed)
    b2.defaultclock.dt = dt
    equations = """
    dr/dt = (Delta/pi + 2*r*v)/source_time : 1
    dv/dt = (v**2 + eta_bar + J*r + drive - pi**2*r**2)/source_time : 1
    Delta : 1
    eta_bar : 1
    J : 1
    drive : 1
    """
    population = b2.NeuronGroup(
        1,
        equations,
        method=INTEGRATION_METHOD,
        namespace={"source_time": SOURCE_TIME_UNIT},
    )
    population.Delta = 0.5
    population.eta_bar = -2.0
    population.J = 1.0
    population.drive = 0.0
    population.r = 0.1
    population.v = -1.0

    state = b2.StateMonitor(population, ("r", "v"), record=True)
    b2.run(duration)
    return {
        "time_source_units": np.asarray(
            state.t / SOURCE_TIME_UNIT, dtype=float
        ),
        "firing_rate_state": np.asarray(state.r[0], dtype=float),
        "mean_voltage_state": np.asarray(state.v[0], dtype=float),
        "dt_source_units": float(dt / SOURCE_TIME_UNIT),
        "duration_source_units": float(duration / SOURCE_TIME_UNIT),
        "seed": seed,
        "method": INTEGRATION_METHOD,
    }
