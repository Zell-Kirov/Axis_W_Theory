import unittest
from src.entity import Entity

class TestEntity(unittest.TestCase):
    def test_time_perceived_low_gravity(self):
        e = Entity("TestLowG", (0,0,0), velocity=1.0, gravity_factor=0.1)
        e.evolve_in_w(1, rotation_w=0.01)
        self.assertGreater(e.perceived_time, 0)

    def test_time_perceived_high_gravity(self):
        e = Entity("TestHighG", (0,0,0), velocity=1.0, gravity_factor=1000)
        e.evolve_in_w(1, rotation_w=0.01)
        self.assertAlmostEqual(e.perceived_time, 0, delta=0.015)

    def test_negative_gravity(self):
        e = Entity("TestNegativeG", (0,0,0), velocity=1.0, gravity_factor=-10)
        with self.assertRaises(ValueError):
            e.evolve_in_w(1, rotation_w=0.01)

    def test_zero_velocity(self):
        e = Entity("TestZeroV", (0,0,0), velocity=0.0, gravity_factor=1.0)
        e.evolve_in_w(1, rotation_w=0.01)
        self.assertEqual(e.perceived_time, 0.01)

if __name__ == "__main__":
    unittest.main()
