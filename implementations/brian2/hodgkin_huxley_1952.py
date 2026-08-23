"""Minimal Brian2 implementation of the audited Hodgkin-Huxley 1952 system."""

from __future__ import annotations

from typing import Any

import brian2 as b2
import numpy as np


RANDOM_SEED = 20260823
DEFAULT_DT = 0.02 * b2.ms
REST_DURATION = 200 * b2.ms
STIM_DURATION = 1000 * b2.ms
DRIVE_UA_PER_CM2 = 6.3
INTEGRATION_METHOD = "euler"

EQUATIONS = """
dv/dt = (i_stim - i_na - i_k - i_l)/c_m : volt
i_stim : amp/metre**2
i_na = g_na*m**3*h*(v - e_na) : amp/metre**2
i_k = g_k*n**4*(v - e_k) : amp/metre**2
i_l = g_l*(v - e_l) : amp/metre**2
dm/dt = alpha_m*(1 - m) - beta_m*m : 1
dn/dt = alpha_n*(1 - n) - beta_n*n : 1
dh/dt = alpha_h*(1 - h) - beta_h*h : 1
alpha_m = 0.1*(x + 40.0)/(1.0 - exp(-(x + 40.0)/10.0))/ms : hertz
beta_m = 4.0*exp(-(x + 65.0)/18.0)/ms : hertz
alpha_n = 0.01*(x + 55.0)/(1.0 - exp(-(x + 55.0)/10.0))/ms : hertz
beta_n = 0.125*exp(-(x + 65.0)/80.0)/ms : hertz
alpha_h = 0.07*exp(-(x + 65.0)/20.0)/ms : hertz
beta_h = 1.0/(1.0 + exp(-(x + 35.0)/10.0))/ms : hertz
x = v/mV : 1
"""

NAMESPACES = {
    "c_m": 1.0 * b2.ufarad / b2.cm**2,
    "g_na": 120.0 * b2.msiemens / b2.cm**2,
    "g_k": 36.0 * b2.msiemens / b2.cm**2,
    "g_l": 0.3 * b2.msiemens / b2.cm**2,
    "e_na": 50.0 * b2.mV,
    "e_k": -77.0 * b2.mV,
    "e_l": -54.4 * b2.mV,
}

INITIAL_V = -65.0 * b2.mV
INITIAL_M = 0.0529324852
INITIAL_N = 0.3176769141
INITIAL_H = 0.5961207535


def _crossing_times_ms(time_ms: np.ndarray, signal_mV: np.ndarray, level: float) -> np.ndarray:
    crossings = np.flatnonzero((signal_mV[:-1] < level) & (signal_mV[1:] >= level))
    return time_ms[crossings + 1]


def _make_group(drive: b2.Quantity) -> b2.NeuronGroup:
    group = b2.NeuronGroup(
        1,
        EQUATIONS,
        namespace=NAMESPACES,
        method=INTEGRATION_METHOD,
    )
    group.i_stim = drive
    group.v = INITIAL_V
    group.m = INITIAL_M
    group.n = INITIAL_N
    group.h = INITIAL_H
    return group


def run_smoke(
    *,
    seed: int = RANDOM_SEED,
    dt: b2.Quantity = DEFAULT_DT,
    rest_duration: b2.Quantity = REST_DURATION,
    stim_duration: b2.Quantity = STIM_DURATION,
    drive_uA_per_cm2: float = DRIVE_UA_PER_CM2,
) -> dict[str, Any]:
    """Run the resting-state settle and the classic 6.3 uA/cm2 stimulus."""
    b2.start_scope()
    b2.seed(seed)
    b2.defaultclock.dt = dt

    rest_group = _make_group(0.0 * b2.uamp / b2.cm**2)
    rest_state = b2.StateMonitor(rest_group, ("v",), record=True)
    b2.run(rest_duration)
    tail = int(rest_duration / dt) - int(20 * b2.ms / dt)
    rest_voltage_mV = float(np.mean(rest_state.v[0][tail:] / b2.mV))

    b2.start_scope()
    b2.seed(seed)
    b2.defaultclock.dt = dt

    stim_group = _make_group(drive_uA_per_cm2 * b2.uamp / b2.cm**2)
    stim_state = b2.StateMonitor(stim_group, ("v",), record=True)
    b2.run(stim_duration)

    voltage_mV = np.asarray(stim_state.v[0] / b2.mV, dtype=float)
    time_ms = np.asarray(stim_state.t / b2.ms, dtype=float)
    spike_times_ms = _crossing_times_ms(time_ms, voltage_mV, 0.0)

    return {
        "rest_voltage_mV": rest_voltage_mV,
        "time_ms": time_ms,
        "voltage_mV": voltage_mV,
        "spike_times_ms": spike_times_ms,
        "spike_count": int(len(spike_times_ms)),
        "mean_rate_hz": float(len(spike_times_ms) / (stim_duration / b2.second)),
        "drive_uA_per_cm2": drive_uA_per_cm2,
        "dt_ms": float(dt / b2.ms),
        "rest_duration_ms": float(rest_duration / b2.ms),
        "stim_duration_ms": float(stim_duration / b2.ms),
        "seed": seed,
        "method": INTEGRATION_METHOD,
    }
