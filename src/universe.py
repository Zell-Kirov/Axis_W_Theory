import numpy as np

class Universe:
    def __init__(self, size=(100, 100, 100), rotation_w=0.01):
        """
        Initializes a universe with X, Y, Z dimensions.
        W is implicit as the temporal displacement axis.
        """
        self.size_x, self.size_y, self.size_z = size
        self.rotation_w = rotation_w  # Global rotation in the W axis (rad/s)
        self.time_position_w = 0.0    # Current position of the universe in W

    def evolve(self, delta_t):
        """
        Evolves the universe along W over elapsed time.
        """
        self.time_position_w += self.rotation_w * delta_t

    def get_w_position(self):
        """
        Returns the universe's current position in W.
        """
        return self.time_position_w

    def display_structure(self):
        """
        Displays the universe's parameters.
        """
        print(f"Dimensions: X={self.size_x}, Y={self.size_y}, Z={self.size_z}")
        print(f"W Rotation: {self.rotation_w} rad/s")
        print(f"Current position in W: {self.time_position_w}")