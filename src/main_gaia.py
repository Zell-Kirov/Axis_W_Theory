from gaia_import import fetch_gaia_sample, gaia_to_entities
from universe import Universe
import csv

def simulate_gaia_entities(steps=20, delta_t=1):
    print("Loading Gaia stars...")
    df = fetch_gaia_sample(limit=50)  # You can increase this to 100+ if needed
    entities = gaia_to_entities(df)
    universe = Universe(rotation_w=0.02)

    print(f"{len(entities)} stars ready for Axis_W simulation")

    with open('data/gaia_output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ['Step', 'Universe_W'] + [f"{e.name}_TimePerceived" for e in entities]
        writer.writerow(header)

        for step in range(steps):
            universe.evolve(delta_t)
            row = [step + 1, universe.get_w_position()]

            print(f"\nSTEP {step + 1} — W = {universe.get_w_position():.4f}")
            for entity in entities:
                entity.evolve_in_w(delta_t, universe.rotation_w)
                print(f"{entity.name}: ⏳ Perceived time = {entity.perceived_time:.4f}")
                row.append(round(entity.perceived_time, 4))

            writer.writerow(row)

if __name__ == "__main__":
    simulate_gaia_entities()
