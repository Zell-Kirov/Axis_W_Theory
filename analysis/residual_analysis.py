import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your Axis_W engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from entity import Entity
from universe import Universe

def load_data(filepath="data/TableGaia_Archive-result.csv"):
    df = pd.read_csv(filepath)
    df = df.dropna(subset=["mass", "radial_velocity", "mag_g"])

    df["velocity_sim"] = df["radial_velocity"] / 3e5  # velocity normalization
    df["mass_sim"] = df["mass"]  # solar mass → Axis_W engine

    return df

def simulate_axisw(df):
    times = []
    for _, row in df.iterrows():
        entity = Entity("GaiaObj", velocity=row["velocity_sim"], gravity_factor=row["mass_sim"])
        universe = Universe(rotation_w=0.0)
        entity.evolve_in_w(1, universe.rotation_w)
        times.append(entity.perceived_time)

    df["time_axisw"] = times
    return df

def compute_residuals(df, observed_col="mag_g"):
    # Residual = simulation - observed value
    df["residual"] = df["time_axisw"] - df[observed_col]
    return df

def plot_residuals(df):
    os.makedirs("data", exist_ok=True)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x="mass_sim",
        y="residual",
        hue="velocity_sim",
        palette="viridis",
        s=70,
        data=df
    )
    plt.title("Residuals (Axis_W - observed magnitude) vs Mass")
    plt.xlabel("Mass (M☉)")
    plt.ylabel("Simulated time residual - observed magnitude")
    plt.tight_layout()
    plt.savefig("data/axisw_residuals_plot_real.png")
    plt.show()

def export_residual_stats(df, filepath="data/residual_summary_real.md"):
    mean_res = df["residual"].mean()
    std_res = df["residual"].std()
    max_res = df["residual"].max()
    min_res = df["residual"].min()

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# Axis_W Residual Analysis\n\n")
        f.write(f"Number of objects: {len(df)}\n\n")
        f.write(f"- Mean residual: `{mean_res:.4f}`\n")
        f.write(f"- Residual standard deviation: `{std_res:.4f}`\n")
        f.write(f"- Max residual: `{max_res:.4f}`\n")
        f.write(f"- Min residual: `{min_res:.4f}`\n\n")
        f.write("**Quick interpretation:**\n")
        f.write("- A residual close to 0 indicates good agreement.\n")
        f.write("- Large deviations suggest atypical entities or Axis_W structure to refine.\n")

if __name__ == "__main__":
    df = load_data()
    df = simulate_axisw(df)
    df = compute_residuals(df, observed_col="mag_g")
    plot_residuals(df)
    export_residual_stats(df)
