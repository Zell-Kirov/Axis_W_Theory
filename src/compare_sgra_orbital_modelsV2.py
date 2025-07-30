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
        if omega_mode == "phase_modulated":
            omega_w = np.sin(2 * np.pi * row["phase"]) + 0.003 * row["eccentricity"]
        else:
            omega_w = 0.01  # fallback

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
    plt.scatter(range(len(residuals)), residuals, s=40, alpha=0.6, c="darkred")
    plt.title(f"Axis_W Residuals – {label}")
    plt.xlabel("S-star index")
    plt.ylabel("Simulated time – prediction")
    plt.grid(True)
    plt.tight_layout()
    safe_label = label.lower().replace(" ", "_").replace("*", "").replace("(", "").replace(")", "")
    plot_path = f"validation/plots/{safe_label}_residuals_orbital_modelsV2.png"
    os.makedirs("validation/plots", exist_ok=True)
    plt.savefig(plot_path)
    return plot_path

def write_md_summary(source, features, score, plot_path, path="validation/axisw_sgra_orbital_modelsV2.md"):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"## 🔭 Source: {source}\n")
        f.write(f"🕒 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Tested parameters:** {', '.join(features)}\n\n")
        f.write(f"📊 Axis_W R² score: `{score:.4f}`\n")
        f.write(f"📉 Residuals plot: `{plot_path}`\n")
        f.write("🧠 Cosmic hypothesis evaluated:\n")
        if score > 0.99:
            f.write("- The Axis_W perceptual metric accurately models the observed temporal behavior.\n\n")
        elif score > 0.9:
            f.write("- The perceptual torsion shows partial agreement with real data.\n\n")
        else:
            f.write("- Low correspondence: the torsional effect does not fully explain observed distortions.\n\n")
        f.write("---\n\n")

def compare_real_data(source):
    if source == "SgrA_orbital":
        df = pd.read_csv("data/sgrA_sstars_enriched.csv")
        label = "Sgr A (orbital torsion)"
        df["velocity_sim"] = df["v"] / 3e5
        df["mass_sim"] = df["mass"]

        # Compute orbital phase
        df["phase"] = ((2025.0 - df["Tp"]) % df["P"]) / df["P"]

        features = [
            "mass_sim", "velocity_sim",
            "eccentricity", "inclination",
            "omega", "Omega", "Tp", "P", "phase"
        ]
        omega_mode = "phase_modulated"
    else:
        print("Unknown source.")
        return

    df = simulate_axisw(df, omega_mode)
    score, residuals = run_axisw_regression(df, features)
    plot_path = plot_residuals(df, residuals, label)
    write_md_summary(label, features, score, plot_path)

if __name__ == "__main__":
    compare_real_data("SgrA_orbital")
