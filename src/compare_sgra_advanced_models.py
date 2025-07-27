import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.impute import SimpleImputer
from datetime import datetime

from entity import Entity
from universe import Universe

def simulate_axisw(df, omega_mode):
    times = []
    for _, row in df.iterrows():
        if omega_mode == "precession_modulated":
            omega_w = 0.002 * row["omega"] + 0.003 * row["Omega"]

        elif omega_mode == "velocity_modulated":
            omega_w = 0.004 * row["v"] / 3e5 + 0.002 * row["eccentricity"]

        elif omega_mode == "gravity_comparison":
            omega_w = 0.002 * row["eccentricity"] + 0.005 * row["inclination"]

        else:
            omega_w = 0.01  # fallback constant

        e = Entity("Obj", velocity=row["velocity_sim"], gravity_factor=row["mass_sim"])
        u = Universe(rotation_w=omega_w)
        e.evolve_in_w(1, u.rotation_w)
        times.append(e.perceived_time)

    df["time_axisw"] = times
    return df

def run_axisw_regression(df, features):
    imputer = SimpleImputer(strategy="mean")
    X = pd.DataFrame(imputer.fit_transform(df[features]), columns=features)
    y = df["time_axisw"]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    y_pred = model.fit(X, y).predict(X)
    score = r2_score(y, y_pred)
    residuals = y - y_pred
    return score, residuals

def plot_residuals(df, residuals, label):
    plt.figure(figsize=(9, 6))
    plt.scatter(range(len(residuals)), residuals, s=40, alpha=0.6, c="darkgreen")
    plt.title(f"Axis_W Residuals – {label}")
    plt.xlabel("S-star")
    plt.ylabel("Simulated Time – Prediction")
    plt.grid(True)
    plt.tight_layout()
    safe_label = label.lower().replace(" ", "_").replace("*", "").replace("(", "").replace(")", "")
    plot_path = f"validation/plots/{safe_label}_residuals_advanced_models.png"
    os.makedirs("validation/plots", exist_ok=True)
    plt.savefig(plot_path)
    return plot_path

def write_md_summary(source, features, score, plot_path, path="validation/axisw_sgra_advanced_models.md"):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"## 🔭 Source: {source}\n")
        f.write(f"🕒 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Tested parameters:** {', '.join(features)}\n\n")
        f.write(f"📊 Axis_W R² score: `{score:.4f}`\n")
        f.write(f"📉 Residuals plot: `{plot_path}`\n")
        f.write("🧠 Tested cosmological hypothesis:\n")
        if score > 0.99:
            f.write("- The perceptive Axis_W metric faithfully models the observed temporal behavior.\n\n")
        elif score > 0.9:
            f.write("- Perceptive torsion shows partial correspondence with real data.\n\n")
        else:
            f.write("- Low correspondence: torsional effect does not fully explain observed distortions.\n\n")
        f.write("---\n\n")

def compare_real_data(source):
    df = pd.read_csv("data/sgrA_sstars.csv")
    df["velocity_sim"] = df["v"] / 3e5
    df["mass_sim"] = df["mass"]

    if source == "SgrA_precession":
        label = "Sgr A (precession-modulated torsion)"
        features = ["mass_sim", "velocity_sim", "omega", "Omega"]
        omega_mode = "precession_modulated"

    elif source == "SgrA_velocity":
        label = "Sgr A (velocity-modulated torsion)"
        features = ["mass_sim", "velocity_sim", "v", "eccentricity"]
        omega_mode = "velocity_modulated"

    elif source == "SgrA_gravity":
        label = "Sgr A (GRAVITY comparison torsion)"
        features = ["mass_sim", "velocity_sim", "eccentricity", "inclination"]
        omega_mode = "gravity_comparison"

    else:
        print("Unknown source.")
        return

    df = simulate_axisw(df, omega_mode)
    score, residuals = run_axisw_regression(df, features)
    plot_path = plot_residuals(df, residuals, label)
    write_md_summary(label, features, score, plot_path)

if __name__ == "__main__":
    for source in ["SgrA_precession", "SgrA_velocity", "SgrA_gravity"]:
        compare_real_data(source)
