"""Minimal Brian2 implementation of the audited Izhikevich 2003 system."""

from __future__ import annotations

from typing import Any

import brian2 as b2
import numpy as np


RANDOM_SEED = 20260723
DEFAULT_DT = 0.1 * b2.ms
DEFAULT_DURATION = 200 * b2.ms
INTEGRATION_METHOD = "euler"


def run_smoke(
    *,
    seed: int = RANDOM_SEED,
    dt: b2.Quantity = DEFAULT_DT,
    duration: b2.Quantity = DEFAULT_DURATION,
) -> dict[str, Any]:
    """Run one regular-spiking parameter example as implementation evidence."""
    b2.start_scope()
    b2.seed(seed)
    b2.defaultclock.dt = dt
    equations = """
    dv/dt = (0.04/mV*v**2 + 5*v + 140*mV - u + drive)/ms : volt
    du/dt = a*(b*v - u)/ms : volt
    drive : volt
    a : 1
    b : 1
    c : volt
    d : volt
    """
    neuron = b2.NeuronGroup(
        1,
        equations,
        threshold="v >= 30*mV",
        reset="v = c; u += d",
        method=INTEGRATION_METHOD,
    )
    neuron.a = 0.02
    neuron.b = 0.2
    neuron.c = -65 * b2.mV
    neuron.d = 8 * b2.mV
    neuron.drive = 10 * b2.mV
    neuron.v = -65 * b2.mV
    neuron.u = neuron.b * neuron.v

    state = b2.StateMonitor(neuron, ("v", "u"), record=True)
    spikes = b2.SpikeMonitor(neuron)
    b2.run(duration)
    return {
        "time_ms": np.asarray(state.t / b2.ms, dtype=float),
        "voltage_mV": np.asarray(state.v[0] / b2.mV, dtype=float),
        "recovery_mV": np.asarray(state.u[0] / b2.mV, dtype=float),
        "spike_times_ms": np.asarray(spikes.t / b2.ms, dtype=float),
        "spike_count": int(spikes.count[0]),
        "dt_ms": float(dt / b2.ms),
        "duration_ms": float(duration / b2.ms),
        "seed": seed,
        "method": INTEGRATION_METHOD,
    }
