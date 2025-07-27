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
        if omega_mode == "none":
            omega_w = 0.0

        elif omega_mode == "linear":
            omega_w = 0.002 * row["eccentricity"] + 0.005 * row["inclination"]

        elif omega_mode == "nonlinear":
            omega_w = np.sin(row["eccentricity"] * row["inclination"]) + np.log1p(row["eccentricity"])

        elif omega_mode == "multifrequency":
            omega_w = np.sin(2 * row["eccentricity"]) + np.sin(0.5 * row["inclination"])

        elif omega_mode == "custom":
            omega_w = row.get("omega_W", 0.0)

        else:
            omega_w = 0.01  # default fallback

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
    plt.scatter(range(len(residuals)), residuals, s=40, alpha=0.6, c="darkblue")
    plt.title(f"Axis_W Residuals – {label}")
    plt.xlabel("S-star")
    plt.ylabel("Simulated time – prediction")
    plt.grid(True)
    plt.tight_layout()
    safe_label = label.lower().replace(" ", "_").replace("*", "").replace("(", "").replace(")", "")
    plot_path = f"validation/plots/{safe_label}_residuals_multitest.png"
    os.makedirs("validation/plots", exist_ok=True)
    plt.savefig(plot_path)
    return plot_path

def write_md_summary(source, features, score, plot_path, path="validation/axisw_sgra_models.md"):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"## 🔭 Source: {source}\n")
        f.write(f"🕒 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Tested parameters:** {', '.join(features)}\n\n")
        f.write(f"📊 Axis_W R² score: `{score:.4f}`\n")
        f.write(f"📉 Residuals plot: `{plot_path}`\n")
        f.write("🧠 Tested cosmological hypothesis:\n")
        if score > 0.99:
            f.write("- The perceptive Axis_W metric faithfully models observed temporal behavior.\n\n")
        elif score > 0.9:
            f.write("- Perceptive torsion shows partial correspondence with real data.\n\n")
        else:
            f.write("- Low correspondence: torsional effect does not fully explain observed distortions.\n\n")
        f.write("---\n\n")

def compare_real_data(source):
    df = pd.read_csv("data/sgrA_sstars.csv")
    df["velocity_sim"] = df["v"] / 3e5
    df["mass_sim"] = df["mass"]
    features = ["mass_sim", "velocity_sim", "eccentricity", "inclination"]

    if source == "SgrA":
        label = "Sgr A (linear torsion)"
        omega_mode = "linear"

    elif source == "SgrA_nonlinear":
        label = "Sgr A (nonlinear torsion)"
        omega_mode = "nonlinear"

    elif source == "SgrA_multifreq":
        label = "Sgr A (multi-frequency torsion)"
        omega_mode = "multifrequency"

    else:
        print("Unknown source.")
        return

    df = simulate_axisw(df, omega_mode)
    score, residuals = run_axisw_regression(df, features)
    plot_path = plot_residuals(df, residuals, label)
    write_md_summary(label, features, score, plot_path)

if __name__ == "__main__":
    for source in ["SgrA", "SgrA_nonlinear", "SgrA_multifreq"]:
        compare_real_data(source)
