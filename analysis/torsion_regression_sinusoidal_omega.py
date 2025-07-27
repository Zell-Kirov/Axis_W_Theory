import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from entity import Entity
from universe import Universe

def load_data(filepath="data/gaia_universe_observed-result.csv"):
    df = pd.read_csv(filepath)
    df["velocity_sim"] = df["radial_velocity"] / 3e5
    df["mass_sim"] = df["mass"]
    df["omega_W"] = np.sin(df["eccentricity"] + df["inclination"])
    df = df.dropna(subset=[
        "mass_sim", "velocity_sim", "eccentricity", "inclination", "logg", "teff", "r_env_r_star"
    ])
    return df

def simulate_axisw(df):
    axisw_times = []
    for _, row in df.iterrows():
        e = Entity("Star", velocity=row["velocity_sim"], gravity_factor=row["mass_sim"])
        u = Universe(rotation_w=row["omega_W"])
        e.evolve_in_w(1, u.rotation_w)
        axisw_times.append(e.perceived_time)
    df["time_axisw"] = axisw_times
    return df

def run_dual_regression(df):
    features_no_omega = ["mass_sim", "velocity_sim", "eccentricity", "inclination", "logg", "teff", "r_env_r_star"]
    features_with_omega = features_no_omega + ["omega_W"]

    X1 = pd.DataFrame(SimpleImputer().fit_transform(df[features_no_omega]), columns=features_no_omega)
    X2 = pd.DataFrame(SimpleImputer().fit_transform(df[features_with_omega]), columns=features_with_omega)
    y = df["time_axisw"]

    model1 = RandomForestRegressor(n_estimators=100, random_state=42).fit(X1, y)
    model2 = RandomForestRegressor(n_estimators=100, random_state=42).fit(X2, y)

    pred1 = model1.predict(X1)
    pred2 = model2.predict(X2)

    score1 = r2_score(y, pred1)
    score2 = r2_score(y, pred2)
    improvement = score2 - score1

    df["residual_omega"] = y - pred2

    return score1, score2, improvement, df

def plot_residuals(df, score2):
    os.makedirs("data", exist_ok=True)
    plt.figure(figsize=(9, 6))
    plt.scatter(df["omega_W"], df["residual_omega"], s=50, c="purple", alpha=0.5)
    plt.title(f"Cosmic Torsion vs Axis_W Residual (R² = {score2:.4f})")
    plt.xlabel("Cosmic Torsion ω_W")
    plt.ylabel("Residual (simulated time – prediction)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("data/omegaW_sinusoidal_residuals_plot.png")
    plt.show()

def export_summary_sinusoidal(score1, score2, improvement, path="data/omega_sinusoidal_summary.md"):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# 🌗 Impact of Sinusoidal Cosmic Torsion\n\n")
        f.write("**Model used:**\n")
        f.write("`ω_W = sin(eccentricity + inclination)`\n\n")
        f.write(f"📊 R² score without ω_W: `{score1:.4f}`\n")
        f.write(f"📊 R² score with ω_W: `{score2:.4f}`\n")
        f.write(f"🔍 Improvement brought by ω_W: `{improvement:.4f}`\n\n")
        f.write("**Analysis:**\n")
        if improvement > 0.0005:
            f.write("- Sinusoidal cosmic torsion influences the perceptual metric.\n")
            f.write("- This wave pattern might reflect a cyclic topology in W-space.\n")
        else:
            f.write("- The sinusoidal effect remains marginal in this dataset.\n")
            f.write("- Larger or more targeted variations could reveal perceptual impact.\n")
        f.write("- See `omega_sinusoidal_residuals_plot.png` for visual impact.\n")

if __name__ == "__main__":
    df = load_data()
    df = simulate_axisw(df)
    s1, s2, gain, df = run_dual_regression(df)
    plot_residuals(df, s2)
    export_summary_sinusoidal(s1, s2, gain)
