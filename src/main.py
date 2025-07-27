from universe import Universe
from entity import Entity
import csv

def run_cosmic_experiment():
    # Create the universe (inverted rotation = test)
    universe = Universe(size=(100, 100, 100), rotation_w=0.02)

    # Create entities
    entities = [
        Entity("Gwen", position_xyz=(10, 20, 30), velocity=1.0, gravity_factor=1.0),
        Entity("Nova", position_xyz=(50, 60, 70), velocity=1.0, gravity_factor=3.0),
        Entity("Singularis", position_xyz=(0, 0, 0), velocity=1.0, gravity_factor=1000.0),
        Entity("Tachyon", position_xyz=(5, 5, 5), velocity=5.0, gravity_factor=1.0),
        Entity("Inverse", position_xyz=(99, 99, 99), velocity=1.0, gravity_factor=1.0),
    ]

    # Initialize CSV file
    with open('data/output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ['Step', 'Universe_W'] + [f'{e.name}_TimePerceived' for e in entities]
        writer.writerow(header)

        print("Starting Axis_W cosmic simulation")
        print("-" * 60)

        # Simulation loop
        for step in range(10):
            delta_t = 1
            universe.evolve(delta_t)

            row = [step + 1, universe.get_w_position()]

            print(f"\nSTEP {step + 1} — W = {universe.get_w_position():.4f}")
            for entity in entities:
                entity.evolve_in_w(delta_t, universe.rotation_w)
                entity.info()
                row.append(round(entity.perceived_time, 4))

            # Save data
            writer.writerow(row)

if __name__ == "__main__":
    run_cosmic_experiment()
