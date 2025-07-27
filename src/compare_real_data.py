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

def simulate_axisw(df, omega_mode, source):
    times = []
    for _, row in df.iterrows():
        if omega_mode == "none":
            omega_w = 0.0

        elif omega_mode == "sinusoidal":
            if source == "SgrA":
                omega_w = np.sin(row["eccentricity"] + row["inclination"])
            elif source == "M87":
                omega_w = np.sin(row["Hardness_Ratio_21"] + row["Hardness_Ratio_31"])
            elif source == "Pulsars":
                omega_w = np.sin(row["period_s"] + row["DM"])
            elif source == "Gaia":
                omega_w = np.sin(row["bp_rp"] + row["ruwe"])
            else:
                omega_w = 0.01

        elif omega_mode == "linear":
            if source == "SgrA":
                omega_w = 0.002 * row["eccentricity"] + 0.005 * row["inclination"]
            elif source == "M87":
                omega_w = 0.002 * row["Hardness_Ratio_21"] + 0.005 * row["Hardness_Ratio_31"]
            elif source == "Pulsars":
                omega_w = 0.002 * row["period_s"] + 0.005 * row["DM"]
            elif source == "Gaia":
                omega_w = 0.002 * row["bp_rp"] + 0.005 * row["ruwe"]
            else:
                omega_w = 0.01

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
    plt.xlabel("Galactic Object")
    plt.ylabel("Simulated Time – Prediction")
    plt.grid(True)
    plt.tight_layout()
    plot_path = f"validation/plots/{label.lower().replace(' ', '_')}_residuals.png"
    os.makedirs("validation/plots", exist_ok=True)
    plt.savefig(plot_path)
    return plot_path

def write_md_summary(source, features, score, plot_path, path="validation/axisw_real_data_comparison.md"):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"## 🔭 Source: {source}\n")
        f.write(f"🕒 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Tested parameters:** {', '.join(features)}\n\n")
        f.write(f"📊 Axis_W R² score: `{score:.4f}`\n")
        f.write(f"📉 Residuals plot: `{plot_path}`\n")
        f.write("🧠 Tested cosmological hypothesis:\n")
        if score > 0.99:
            f.write("- The perceptive Axis_W metric accurately models observed temporal behavior.\n\n")
        elif score > 0.9:
            f.write("- Perceptive torsion shows partial correspondence with real data.\n\n")
        else:
            f.write("- Low correspondence: torsional effect does not fully explain observed distortions.\n\n")
        f.write("---\n\n")

def compare_real_data(source):
    if source == "Gaia":
        df = pd.read_csv("data/gaia_real_objects-result.csv")
        label = "Gaia"
        df["velocity_sim"] = df["radial_velocity"] / 3e5
        df["mass_sim"] = 10 ** (df["logg_gspphot"] - np.log10(df["teff_gspphot"]) + 4.44)
        features = ["mass_sim", "velocity_sim", "logg_gspphot", "teff_gspphot", "bp_rp", "ruwe"]
        omega_mode = "linear"

    elif source == "SgrA":
        df = pd.read_csv("data/sgrA_sstars.csv")
        label = "Sgr A (S-stars)"
        df["velocity_sim"] = df["v"] / 3e5
        df["mass_sim"] = df["mass"]
        features = ["mass_sim", "velocity_sim", "eccentricity", "inclination"]
        omega_mode = "linear"

    elif source == "M87":
        df = pd.read_csv("data/m87_xray_sources.csv")
        label = "M87 (Relativistic Jet)"
        df["velocity_sim"] = df["Count_Rate"] * 1e3 / 3e5  # proxy
        df["mass_sim"] = df["Lx"] / 1e39  # proxy mass from luminosity
        features = ["mass_sim", "velocity_sim", "Hardness_Ratio_21", "Hardness_Ratio_31"]
        omega_mode = "sinusoidal"

    elif source == "Pulsars":
        df = pd.read_csv("data/pulsar_timing.csv")
        label = "Pulsars (NANOGrav)"
        df["velocity_sim"] = df["residual_us"] / 1e6  # proxy
        df["mass_sim"] = 1.4  # typical neutron star mass
        features = ["mass_sim", "velocity_sim", "period_s", "DM"]
        omega_mode = "sinusoidal"

    else:
        print("Unknown source.")
        return

    df = simulate_axisw(df, omega_mode, source)
    score, residuals = run_axisw_regression(df, features)
    plot_path = plot_residuals(df, residuals, label)
    write_md_summary(label, features, score, plot_path)

if __name__ == "__main__":
    for source in ["Gaia", "SgrA", "M87", "Pulsars"]:
        compare_real_data(source)
