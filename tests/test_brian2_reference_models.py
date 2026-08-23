"""Smoke tests for the two repository-authored Brian2 examples."""

from __future__ import annotations

import unittest

import brian2 as b2
import numpy as np

from implementations.brian2 import brette_gerstner_2005_adex
from implementations.brian2 import hodgkin_huxley_1952
from implementations.brian2 import izhikevich_2003
from implementations.brian2 import montbrio_pazo_roxin_2015
from implementations.brian2 import morris_lecar_1981


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


class HodgkinHuxley1952Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = hodgkin_huxley_1952.run_smoke()

    def test_resting_potential_near_minus_65_mV(self) -> None:
        self.assertAlmostEqual(self.result["rest_voltage_mV"], -65.0, delta=0.5)

    def test_repetitive_firing_at_classic_drive(self) -> None:
        self.assertGreaterEqual(self.result["spike_count"], 40)
        self.assertLessEqual(self.result["spike_count"], 70)
        self.assertAlmostEqual(self.result["mean_rate_hz"], 54.0, delta=10.0)

    def test_voltage_excursions_finite_and_bounded(self) -> None:
        voltage = self.result["voltage_mV"]
        self.assertTrue(np.isfinite(voltage).all())
        self.assertGreater(float(voltage.max()), 20.0)
        self.assertGreater(float(voltage.min()), -90.0)

    def test_seeded_repeatability(self) -> None:
        second = hodgkin_huxley_1952.run_smoke()
        np.testing.assert_array_equal(
            self.result["voltage_mV"], second["voltage_mV"]
        )
        np.testing.assert_array_equal(
            self.result["spike_times_ms"], second["spike_times_ms"]
        )


class MorrisLecar1981Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = morris_lecar_1981.run_smoke()

    def test_sustained_limit_cycle_amplitude(self) -> None:
        self.assertGreater(self.result["late_peak_to_peak"], 0.4)

    def test_recovery_variable_bounded_in_unit_interval(self) -> None:
        recovery = self.result["recovery_state"]
        self.assertTrue(np.isfinite(recovery).all())
        self.assertGreaterEqual(float(recovery.min()), 0.0)
        self.assertLessEqual(float(recovery.max()), 1.0)

    def test_repetitive_oscillations_above_threshold(self) -> None:
        self.assertGreaterEqual(self.result["spike_count"], 80)
        self.assertLessEqual(self.result["spike_count"], 220)
        self.assertAlmostEqual(self.result["mean_rate_hz"], 48.0, delta=15.0)

    def test_seeded_repeatability(self) -> None:
        second = morris_lecar_1981.run_smoke()
        np.testing.assert_array_equal(
            self.result["voltage_state"], second["voltage_state"]
        )


class BretteGerstner2005AdExTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = brette_gerstner_2005_adex.run_smoke()

    def test_adapting_spike_train_present(self) -> None:
        self.assertGreaterEqual(self.result["spike_count"], 10)
        self.assertLessEqual(self.result["spike_count"], 40)

    def test_isi_lengthens_under_constant_drive(self) -> None:
        ratio = self.result["last_isi_ms"] / self.result["first_isi_ms"]
        self.assertGreater(ratio, 1.5)

    def test_voltage_finite_and_bounded(self) -> None:
        voltage = self.result["voltage_mV"]
        self.assertTrue(np.isfinite(voltage).all())
        self.assertLess(float(voltage.max()), 20.0)
        self.assertGreater(float(voltage.min()), -90.0)

    def test_seeded_repeatability(self) -> None:
        second = brette_gerstner_2005_adex.run_smoke()
        np.testing.assert_array_equal(
            self.result["voltage_mV"], second["voltage_mV"]
        )


if __name__ == "__main__":
    unittest.main()
