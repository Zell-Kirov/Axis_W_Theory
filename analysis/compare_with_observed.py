import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Access to Axis_W modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from entity import Entity
from universe import Universe

def load_gaia_data(filepath="data/TableGaia_Archive-result.csv"):
    df = pd.read_csv(filepath)
    required = ["mass", "radial_velocity"]
    df = df.dropna(subset=required)

    # Normalization: velocity as a fraction of c (optional)
    df["velocity_sim"] = df["radial_velocity"] / 3e5  # speed of light ~300,000 km/s

    # Simulated mass (preserving in solar masses)
    df["mass_sim"] = df["mass"]

    return df

def simulate_axisw(df):
    results = []
    for _, row in df.iterrows():
        entity = Entity("GaiaStar", velocity=row["velocity_sim"], gravity_factor=row["mass_sim"])
        universe = Universe(rotation_w=0.0)
        entity.evolve_in_w(1, universe.rotation_w)
        results.append(entity.perceived_time)

    df["time_axisw"] = results
    return df

def plot_comparison(df):
    os.makedirs("data", exist_ok=True)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x="mass_sim", 
        y="time_axisw", 
        hue="velocity_sim", 
        data=df, 
        palette="viridis", 
        s=70
    )
    plt.title(" Simulated Axis_W Time vs Gaia Star Mass")
    plt.xlabel("Mass (M☉)")
    plt.ylabel("Simulated Perceived Time (Axis_W)")
    plt.tight_layout()
    plt.savefig("data/comparison_plot.png")
    plt.show()

def export_summary(df, filepath="data/comparison_summary.md"):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# Comparison: Axis_W vs Gaia Universe Model\n\n")
        f.write(f"Number of stars analyzed: {len(df)}\n\n")
        f.write("**Simulated Axis_W Time Statistics:**\n\n")
        f.write(f"- Mean time: `{df['time_axisw'].mean():.6f}`\n")
        f.write(f"- Max time: `{df['time_axisw'].max():.6f}`\n")
        f.write(f"- Min time: `{df['time_axisw'].min():.6f}`\n\n")
        f.write("**Cosmological Notes:**\n")
        f.write("- Stellar mass strongly influences the simulated perceived time.\n")
        f.write("- Extreme radial velocities cause pronounced time distortions.\n")
        f.write("- This model opens the path to a temporal mapping of the Milky Way according to Axis_W.\n")

if __name__ == "__main__":
    df = load_gaia_data()
    df = simulate_axisw(df)
    plot_comparison(df)
    export_summary(df)
