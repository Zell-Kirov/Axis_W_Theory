class Entity:
    def __init__(self, name, position_xyz=(0, 0, 0), velocity=1.0, gravity_factor=1.0):
        """
        Represents an entity evolving in the Axis_W universe.

        :param name: Name of the entity
        :param position_xyz: Initial spatial coordinates
        :param velocity: Relative velocity along W
        :param gravity_factor: Gravitational factor influencing the perception of displacement
        """
        self.name = name
        self.position_xyz = position_xyz
        self.velocity = velocity
        self.gravity_factor = gravity_factor
        self.local_w_position = 0.0
        self.perceived_time = 0.0  # Time perceived by the entity

    def evolve_in_w(self, delta_t, rotation_w):
        """
        Evolves the entity along W based on its own velocity and the influence of the universe.

        :param delta_t: Global time step
        :param rotation_w: Global rotation of the W reference frame
        """
        if self.gravity_factor <= 0:
            raise ValueError("gravity_factor must be positive and non-zero.")

        # Composite influence: intrinsic motion + universe torsion
        effective_velocity = self.velocity * (1 / self.gravity_factor) + rotation_w
        displacement = effective_velocity * delta_t
        self.local_w_position += displacement
        self.perceived_time += displacement  # Time is measured as displacement along W

    def info(self):
        """
        Prints the current state of the entity.
        """
        print(f"👤 {self.name}")
        print(f"  📍 Spatial position (XYZ): {self.position_xyz}")
        print(f"  🚀 Intrinsic velocity in W: {self.velocity}")
        print(f"  🌌 Local gravity: {self.gravity_factor}")
        print(f"  🌀 Local W position: {self.local_w_position:.4f}")
        print(f"  ⏳ Perceived time: {self.perceived_time:.4f}")
