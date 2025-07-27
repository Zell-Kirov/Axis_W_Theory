import unittest
from src.entity import Entity
from src.universe import Universe

class TestPhysicsConsistency(unittest.TestCase):

    def test_axis_w_vs_relativistic_case(self):
        """ Low gravity + moderate velocity → perceived time close to real time """
        e = Entity("RelativisticCase", velocity=0.8, gravity_factor=1.0)
        u = Universe(rotation_w=0.0)
        e.evolve_in_w(1, u.rotation_w)
        self.assertAlmostEqual(e.perceived_time, 0.8, delta=0.01)

    def test_axis_w_under_extreme_gravity(self):
        """ High gravity → perceived time slows down """
        e = Entity("BlackHoleEdge", velocity=1.0, gravity_factor=1000)
        u = Universe(rotation_w=0.0)
        e.evolve_in_w(1, u.rotation_w)
        self.assertLess(e.perceived_time, 0.01)

    def test_axis_w_under_inverse_rotation(self):
        """ Negative rotation → perceived time reversal (ΔW < 0) """
        e = Entity("TimeReverse", velocity=0.0, gravity_factor=1.0)
        u = Universe(rotation_w=-0.1)
        e.evolve_in_w(1, u.rotation_w)
        self.assertLess(e.perceived_time, 0)

    def test_time_perceived_stability(self):
        """ Checks perceived time does not jump or diverge abruptly """
        e = Entity("StableStar", velocity=0.5, gravity_factor=1.0)
        u = Universe(rotation_w=0.02)
        previous_time = 0.0
        for _ in range(10):
            e.evolve_in_w(1, u.rotation_w)
            self.assertGreaterEqual(e.perceived_time, previous_time)
            previous_time = e.perceived_time

    def test_null_motion_null_time(self):
        """ Stationary entity + no rotation = zero perceived time """
        e = Entity("FrozenParticle", velocity=0.0, gravity_factor=1.0)
        u = Universe(rotation_w=0.0)
        e.evolve_in_w(1, u.rotation_w)
        self.assertEqual(e.perceived_time, 0.0)

if __name__ == "__main__":
    unittest.main()
