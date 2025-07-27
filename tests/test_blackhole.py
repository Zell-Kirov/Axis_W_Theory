import unittest
from src.entity import Entity

class TestBlackholeBehavior(unittest.TestCase):
    def test_time_reversal_under_extreme_gravity(self):
        star = Entity("S-star_W", (0,0,0.1), velocity=0.8, gravity_factor=500)
        star.evolve_in_w(1, rotation_w=-0.05)
        self.assertLess(star.perceived_time, 0)

if __name__ == "__main__":
    unittest.main()