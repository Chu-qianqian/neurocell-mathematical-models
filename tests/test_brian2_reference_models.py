"""Smoke tests for the two repository-authored Brian2 examples."""

from __future__ import annotations

import unittest

import brian2 as b2
import numpy as np

from implementations.brian2 import izhikevich_2003
from implementations.brian2 import montbrio_pazo_roxin_2015


class IzhikevichSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.first = izhikevich_2003.run_smoke()
        cls.second = izhikevich_2003.run_smoke()

    def test_execution_and_finite_states(self) -> None:
        self.assertGreater(self.first["time_ms"].size, 0)
        self.assertTrue(np.isfinite(self.first["voltage_mV"]).all())
        self.assertTrue(np.isfinite(self.first["recovery_mV"]).all())

    def test_state_ranges(self) -> None:
        self.assertGreater(float(self.first["voltage_mV"].min()), -120.0)
        self.assertLess(float(self.first["voltage_mV"].max()), 40.0)
        self.assertGreater(float(self.first["recovery_mV"].min()), -100.0)
        self.assertLess(float(self.first["recovery_mV"].max()), 100.0)

    def test_time_quantities_have_consistent_dimensions(self) -> None:
        self.assertTrue(
            b2.have_same_dimensions(izhikevich_2003.DEFAULT_DT, b2.second)
        )
        self.assertTrue(
            b2.have_same_dimensions(
                izhikevich_2003.DEFAULT_DURATION, b2.second
            )
        )

    def test_seeded_repeatability(self) -> None:
        np.testing.assert_array_equal(
            self.first["voltage_mV"], self.second["voltage_mV"]
        )
        np.testing.assert_array_equal(
            self.first["spike_times_ms"], self.second["spike_times_ms"]
        )

    def test_threshold_reset_event_occurs(self) -> None:
        self.assertGreater(self.first["spike_count"], 0)


class MPRSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.first = montbrio_pazo_roxin_2015.run_smoke()
        cls.second = montbrio_pazo_roxin_2015.run_smoke()

    def test_execution_and_finite_states(self) -> None:
        self.assertGreater(self.first["time_source_units"].size, 0)
        self.assertTrue(np.isfinite(self.first["firing_rate_state"]).all())
        self.assertTrue(np.isfinite(self.first["mean_voltage_state"]).all())

    def test_state_ranges(self) -> None:
        self.assertGreaterEqual(
            float(self.first["firing_rate_state"].min()), 0.0
        )
        self.assertLess(float(self.first["firing_rate_state"].max()), 100.0)
        self.assertLess(
            float(np.abs(self.first["mean_voltage_state"]).max()), 100.0
        )

    def test_time_quantities_have_consistent_dimensions(self) -> None:
        self.assertTrue(
            b2.have_same_dimensions(
                montbrio_pazo_roxin_2015.DEFAULT_DT, b2.second
            )
        )
        self.assertTrue(
            b2.have_same_dimensions(
                montbrio_pazo_roxin_2015.SOURCE_TIME_UNIT, b2.second
            )
        )

    def test_seeded_repeatability(self) -> None:
        np.testing.assert_array_equal(
            self.first["firing_rate_state"],
            self.second["firing_rate_state"],
        )
        np.testing.assert_array_equal(
            self.first["mean_voltage_state"],
            self.second["mean_voltage_state"],
        )


if __name__ == "__main__":
    unittest.main()
