import unittest
from src.universe import Universe

class TestUniverse(unittest.TestCase):
    def test_evolution_positive_rotation(self):
        u = Universe(rotation_w=0.1)
        initial_w = u.get_w_position()
        u.evolve(1)
        self.assertGreater(u.get_w_position(), initial_w)

    def test_evolution_negative_rotation(self):
        u = Universe(rotation_w=-0.1)
        initial_w = u.get_w_position()
        u.evolve(1)
        self.assertLess(u.get_w_position(), initial_w)

    def test_stability_zero_rotation(self):
        u = Universe(rotation_w=0.0)
        initial_w = u.get_w_position()
        u.evolve(10)
        self.assertEqual(u.get_w_position(), initial_w)

if __name__ == "__main__":
    unittest.main()
