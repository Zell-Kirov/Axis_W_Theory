import matplotlib.pyplot as plt
import numpy as np
import os
from entity import Entity
from universe import Universe

def plot_mass_velocity_time():
    # Create "data" folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Reduced grid for readability: 7x7 points
    masses = np.logspace(0, 3, num=7)       # from 1 to 1000 (log scale)
    velocities = np.linspace(0.1, 2.0, num=7)

    M, V = np.meshgrid(masses, velocities)
    T = np.zeros_like(M)

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            mass = M[i, j]
            velocity = V[i, j]

            gravity_factor = mass  # Gravity = direct mass
            entity = Entity(name="SimStar", velocity=velocity, gravity_factor=gravity_factor)
            universe = Universe(rotation_w=0.0)
            entity.evolve_in_w(delta_t=1, rotation_w=universe.rotation_w)
            T[i, j] = entity.perceived_time

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(
        M, V, T,
        cmap='viridis',
        edgecolor='k',
        alpha=0.9,
        rstride=1,
        cstride=1
    )

    ax.set_title("Perceived Time vs Mass × Velocity (Axis_W)")
    ax.set_xlabel("Mass")
    ax.set_ylabel("Velocity")
    ax.set_zlabel("Perceived Time")
    ax.set_xlim(left=1)
    ax.set_xscale('log')
    fig.colorbar(surf, shrink=0.5, aspect=10)

    plt.savefig("data/time_mass_velocity_3D.png")
    plt.show()

if __name__ == "__main__":
    plot_mass_velocity_time()
