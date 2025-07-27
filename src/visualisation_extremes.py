import matplotlib.pyplot as plt
from entity import Entity
from universe import Universe

def plot_time_vs_gravity():
    gravities = [0.1, 1, 10, 100, 1000, 1e4, 1e6]
    times = []
    for g in gravities:
        star = Entity("TestG", velocity=1.0, gravity_factor=g)
        u = Universe(rotation_w=0.0)
        star.evolve_in_w(1, u.rotation_w)
        times.append(star.perceived_time)

    plt.figure(figsize=(10, 5))
    plt.plot(gravities, times, marker='o', color='firebrick')
    plt.xscale("log")
    plt.title("Perceived Time vs Gravity (log scale)")
    plt.xlabel("Gravity")
    plt.ylabel("Perceived Time")
    plt.grid(True)
    plt.savefig("data/time_vs_gravity.png")
    plt.show()

def plot_time_vs_velocity():
    velocities = [0.2, 0.5, 1.0, 1.2, 1.5, 2.0]
    times = []
    for v in velocities:
        star = Entity("TestV", velocity=v, gravity_factor=1.0)
        u = Universe(rotation_w=0.0)
        star.evolve_in_w(1, u.rotation_w)
        times.append(star.perceived_time)

    plt.figure(figsize=(10, 5))
    plt.plot(velocities, times, marker='o', color='navy')
    plt.title("Perceived Time vs Velocity")
    plt.xlabel("Velocity")
    plt.ylabel("Perceived Time")
    plt.grid(True)
    plt.savefig("data/time_vs_velocity.png")
    plt.show()

def plot_time_loop():
    star = Entity("Looper", velocity=0.2, gravity_factor=1.0)
    u = Universe(rotation_w=-0.25)
    steps, times = [], []
    for i in range(20):
        star.evolve_in_w(1, u.rotation_w)
        steps.append(i + 1)
        times.append(star.perceived_time)

    plt.figure(figsize=(10, 5))
    plt.plot(steps, times, marker='o', color='purple')
    plt.title("Time Loop Simulation (Looper)")
    plt.xlabel("Steps")
    plt.ylabel("Perceived Time")
    plt.grid(True)
    plt.savefig("data/time_loop_simulation.png")
    plt.show()

if __name__ == "__main__":
    plot_time_vs_gravity()
    plot_time_vs_velocity()
    plot_time_loop()
