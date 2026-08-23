"""Minimal Brian2 implementation of the Morris-Lecar 1981 membrane model.

Dimensionless type-I parameterization following Ermentrout (1996),
"Type I membranes, phase resetting curves, and synchrony".
"""

from __future__ import annotations

from typing import Any

import brian2 as b2
import numpy as np


RANDOM_SEED = 20260823
DEFAULT_DT = 0.05 * b2.ms
DEFAULT_DURATION = 3000 * b2.ms
DRIVE_I_APP = 0.08
INTEGRATION_METHOD = "euler"

EQUATIONS = """
dv/dt = (i_app + g_l*(v_l - v) + g_k*w*(v_k - v) - g_ca*m_inf*(v - v_ca))/ms : 1
dw/dt = phi*cosh((v - v_3)/(2.0*v_4))*(w_inf - w)/ms : 1
m_inf = 0.5*(1.0 + tanh((v - v_1)/v_2)) : 1
w_inf = 0.5*(1.0 + tanh((v - v_3)/v_4)) : 1
i_app : 1
"""

NAMESPACES = {
    "g_l": 0.5,
    "g_k": 2.0,
    "g_ca": 1.33,
    "v_l": -0.5,
    "v_k": -0.7,
    "v_ca": 1.0,
    "v_1": -0.01,
    "v_2": 0.15,
    "v_3": 0.1,
    "v_4": 0.145,
    "phi": 1.0 / 3.0,
}


def _crossing_times_ms(time_ms: np.ndarray, signal: np.ndarray, level: float) -> np.ndarray:
    crossings = np.flatnonzero((signal[:-1] < level) & (signal[1:] >= level))
    return time_ms[crossings + 1]


def run_smoke(
    *,
    seed: int = RANDOM_SEED,
    dt: b2.Quantity = DEFAULT_DT,
    duration: b2.Quantity = DEFAULT_DURATION,
    i_app: float = DRIVE_I_APP,
) -> dict[str, Any]:
    """Run one type-I limit-cycle example above the saddle-node threshold."""
    b2.start_scope()
    b2.seed(seed)
    b2.defaultclock.dt = dt

    neuron = b2.NeuronGroup(
        1,
        EQUATIONS,
        namespace=NAMESPACES,
        method=INTEGRATION_METHOD,
    )
    neuron.i_app = i_app
    neuron.v = -0.45
    neuron.w = 0.05

    state = b2.StateMonitor(neuron, ("v", "w"), record=True)
    b2.run(duration)

    voltage = np.asarray(state.v[0], dtype=float)
    recovery = np.asarray(state.w[0], dtype=float)
    time_ms = np.asarray(state.t / b2.ms, dtype=float)
    spike_times_ms = _crossing_times_ms(time_ms, voltage, 0.25)
    tail = len(voltage) // 2
    return {
        "time_ms": time_ms,
        "voltage_state": voltage,
        "recovery_state": recovery,
        "late_peak_to_peak": float(voltage[tail:].max() - voltage[tail:].min()),
        "spike_times_ms": spike_times_ms,
        "spike_count": int(len(spike_times_ms)),
        "mean_rate_hz": float(len(spike_times_ms) / (duration / b2.second)),
        "i_app": i_app,
        "dt_ms": float(dt / b2.ms),
        "duration_ms": float(duration / b2.ms),
        "seed": seed,
        "method": INTEGRATION_METHOD,
    }
