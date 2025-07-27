import unittest
from src.entity import Entity
from src.universe import Universe

class TestExtremeConditions(unittest.TestCase):

    def test_infinite_gravity(self):
        """ Infinite gravity → perceived time tends toward zero """
        e = Entity("SingularityStar", velocity=1.0, gravity_factor=1e12)
        u = Universe(rotation_w=0.0)
        e.evolve_in_w(1, u.rotation_w)
        self.assertLess(e.perceived_time, 1e-6)

    def test_zero_gravity(self):
        """ Zero gravity (non-physical) → should raise an error """
        e = Entity("ZeroGravityStar", velocity=1.0, gravity_factor=0.0)
        u = Universe(rotation_w=0.01)
        with self.assertRaises(ValueError):
            e.evolve_in_w(1, u.rotation_w)

    def test_superluminal_velocity(self):
        """ Velocity > 1 (relativistically invalid) → should be handled or rejected """
        e = Entity("FasterThanLight", velocity=1.5, gravity_factor=1.0)
        u = Universe(rotation_w=0.0)
        e.evolve_in_w(1, u.rotation_w)
        self.assertGreater(e.perceived_time, 1.0)

    def test_micro_delta_t(self):
        """ Microscopic time step → checks the engine’s granularity """
        e = Entity("MicroTick", velocity=0.5, gravity_factor=1.0)
        u = Universe(rotation_w=0.01)
        e.evolve_in_w(1e-6, u.rotation_w)
        self.assertAlmostEqual(e.perceived_time, (0.5 + 0.01) * 1e-6, delta=1e-8)

    def test_time_loop_simulation(self):
        """ Time reversal loop → checks if entity returns to origin """
        e = Entity("Looper", velocity=0.2, gravity_factor=1.0)
        u = Universe(rotation_w=-0.25)
        for _ in range(10):
            e.evolve_in_w(1, u.rotation_w)
        self.assertLess(e.local_w_position, 0)
        self.assertLess(e.perceived_time, 0)

if __name__ == "__main__":
    unittest.main()
