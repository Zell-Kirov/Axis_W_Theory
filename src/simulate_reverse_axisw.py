import matplotlib.pyplot as plt 
from entity import Entity
from universe import Universe

def simulate_entity(name, velocity, mass, omega_w, steps=20):
    e = Entity(name, velocity=velocity, gravity_factor=mass)
    u = Universe(rotation_w=omega_w)
    times = []
    for _ in range(steps):
        e.evolve_in_w(1, u.rotation_w)
        times.append(e.perceived_time)
    return times

# Normal entity: forward perception
forward_times = simulate_entity("Forward", velocity=0.003, mass=2.0, omega_w=0.01)

# Inverted entity: reverse perception
reverse_times = simulate_entity("Reverse", velocity=0.003, mass=2.0, omega_w=-0.01)

# Display both time trajectories
plt.figure(figsize=(10, 6))
plt.plot(range(len(forward_times)), forward_times, label="Forward (ω_W > 0)", marker="o")
plt.plot(range(len(reverse_times)), reverse_times, label="Reverse (ω_W < 0)", marker="o")
plt.xlabel("Evolution steps")
plt.ylabel("Perceived time")
plt.title("Axis_W Simulation: Perceived Time vs ω_W")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("validation/plots/axisw_reverse_time_simulation.png")
plt.show()
