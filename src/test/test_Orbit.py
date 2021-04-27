from unittest import TestCase
from Orbit import Orbit


class TestOrbit(TestCase):

    def create_orbit_mercury(self):
        return Orbit("mercury", 0.205630, 57_909_050, 3.38, 48.331, 29.124, 0)

    def test_get_periapsis(self):
        orbit_mercury = self.create_orbit_mercury()
        expected_periapsis = 46_001_200

        actual_periapsis = orbit_mercury.get_periapsis()

        self.assertAlmostEqual(actual_periapsis, expected_periapsis, delta = 1000)

    def test_get_apoapsis(self):
        orbit_mercury = self.create_orbit_mercury()
        expected_apoapsis = 69_816_900

        actual_apoapsis = orbit_mercury.get_apoapsis()

        self.assertAlmostEqual(actual_apoapsis, expected_apoapsis, delta = 1000)
