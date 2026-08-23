"""Minimal Brian2 implementation of the adaptive exponential integrate-and-fire
model (Brette and Gerstner 2005), using the regular-spiking adaptation fit."""

from __future__ import annotations

from typing import Any

import brian2 as b2
import numpy as np


RANDOM_SEED = 20260823
DEFAULT_DT = 0.05 * b2.ms
DEFAULT_DURATION = 1000 * b2.ms
DRIVE_PA = 800.0
INTEGRATION_METHOD = "exponential_euler"

EQUATIONS = """
dv/dt = (g_l*(e_l - v) + g_l*delta_t*exp((v - v_t)/delta_t) - w + i_stim)/c : volt
dw/dt = (a*(v - e_l) - w)/tau_w : amp
i_stim : amp
"""

NAMESPACES = {
    "c": 281.0 * b2.pfarad,
    "g_l": 30.0 * b2.nsiemens,
    "e_l": -70.6 * b2.mV,
    "v_t": -50.4 * b2.mV,
    "delta_t": 2.0 * b2.mV,
    "tau_w": 144.0 * b2.ms,
    "a": 4.0 * b2.nsiemens,
    "b": 80.5 * b2.pamp,
    "v_r": -70.6 * b2.mV,
}

RESET = "v = v_r; w = w + b"


def run_smoke(
    *,
    seed: int = RANDOM_SEED,
    dt: b2.Quantity = DEFAULT_DT,
    duration: b2.Quantity = DEFAULT_DURATION,
    drive_pA: float = DRIVE_PA,
) -> dict[str, Any]:
    """Run one adapting regular-spiking example under a constant drive."""
    b2.start_scope()
    b2.seed(seed)
    b2.defaultclock.dt = dt

    neuron = b2.NeuronGroup(
        1,
        EQUATIONS,
        namespace=NAMESPACES,
        threshold="v >= 0*mV",
        reset=RESET,
        method=INTEGRATION_METHOD,
    )
    neuron.i_stim = drive_pA * b2.pamp
    neuron.v = NAMESPACES["e_l"]
    neuron.w = 0.0 * b2.amp

    state = b2.StateMonitor(neuron, ("v", "w"), record=True)
    spikes = b2.SpikeMonitor(neuron)
    b2.run(duration)

    spike_times_ms = np.asarray(spikes.t / b2.ms, dtype=float)
    isis_ms = np.diff(spike_times_ms)
    return {
        "time_ms": np.asarray(state.t / b2.ms, dtype=float),
        "voltage_mV": np.asarray(state.v[0] / b2.mV, dtype=float),
        "adaptation_mV_to_nA": np.asarray(state.w[0] / (b2.mV * b2.nA), dtype=float),
        "spike_times_ms": spike_times_ms,
        "spike_count": int(len(spike_times_ms)),
        "first_isi_ms": float(isis_ms[0]) if len(isis_ms) else float("nan"),
        "last_isi_ms": float(isis_ms[-1]) if len(isis_ms) else float("nan"),
        "drive_pA": drive_pA,
        "dt_ms": float(dt / b2.ms),
        "duration_ms": float(duration / b2.ms),
        "seed": seed,
        "method": INTEGRATION_METHOD,
    }
