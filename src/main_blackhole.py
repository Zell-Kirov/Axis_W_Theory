from universe import Universe
from entity import Entity
import csv

def simulate_blackhole_prediction(steps=20, delta_t=1):
    print("🕳️ Initializing the Axis_W universe around Sgr A*")
    
    # Reversed rotation to test ΔW < 0
    universe = Universe(rotation_w=-0.05)

    # 🌠 Fictional entity S-star_W in a tight orbit
    s_star = Entity(
        name="S-star_W",
        position_xyz=(0, 0, 0.1),  # Very close to the center
        velocity=0.8,              # Moderate speed
        gravity_factor=500.0       # Extreme gravity
    )

    with open("data/s_star_prediction.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Step", "Universe_W", "S-star_W_TimePerceived"])

        for step in range(steps):
            universe.evolve(delta_t)
            s_star.evolve_in_w(delta_t, universe.rotation_w)

            print(f"Step {step + 1} | W = {universe.get_w_position():.4f} | Perceived time: {s_star.perceived_time:.4f}")

            writer.writerow([step + 1, universe.get_w_position(), round(s_star.perceived_time, 6)])

if __name__ == "__main__":
    simulate_blackhole_prediction()
