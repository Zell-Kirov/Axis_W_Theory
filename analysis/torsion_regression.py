import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from entity import Entity
from universe import Universe

def load_data(filepath="data/gaia_universe_observed-result.csv"):
    df = pd.read_csv(filepath)
    df["velocity_sim"] = df["radial_velocity"] / 3e5
    df["mass_sim"] = df["mass"]
    df = df.dropna(subset=[
        "mass_sim", 
        "velocity_sim", 
        "eccentricity", 
        "inclination", 
        "logg", 
        "teff", 
        "r_env_r_star"
    ])
    print(f"✅ Remaining objects after filtering: {len(df)}")
    print(df[["mass_sim", "velocity_sim", "eccentricity", "inclination", "logg", "teff", "r_env_r_star"]].isnull().sum())

    return df

def simulate_axisw(df):
    axisw_times = []
    for _, row in df.iterrows():
        e = Entity("TestObj", velocity=row["velocity_sim"], gravity_factor=row["mass_sim"])
        u = Universe(rotation_w=0.0)
        e.evolve_in_w(1, u.rotation_w)
        axisw_times.append(e.perceived_time)
    df["time_axisw"] = axisw_times
    return df

def run_regression(df, features):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    X = df[features]
    y = df["time_axisw"]
    model.fit(X, y)
    predictions = model.predict(X)
    score = r2_score(y, predictions)
    df["axisw_predicted"] = predictions
    df["residual"] = y - predictions
    return df, score

def plot_residuals(df, features, score):
    os.makedirs("data", exist_ok=True)
    plt.figure(figsize=(9, 6))
    sns.scatterplot(x="mass_sim", y="residual", hue="eccentricity", palette="mako", data=df, s=70)
    plt.title(f"📉 Axis_W Residuals vs Mass (R² Score: {score:.3f})")
    plt.xlabel("Mass (M☉)")
    plt.ylabel("Model Residual (simulated time - torsion prediction)")
    plt.tight_layout()
    plt.savefig("data/axisw_torsion_residuals.png")
    plt.show()

def export_summary(df, score, path="data/torsion_summary.md"):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# 🌀 Torsion Regression – Axis W\n\n")
        f.write(f"Number of tested objects: {len(df)}\n")
        f.write(f"R² score of the regression: `{score:.4f}`\n\n")
        f.write("**Included variables:**\n")
        f.write("- Mass\n- Radial velocity\n- Orbital eccentricity\n- Inclination\n")
        f.write("- Surface gravity (logg)\n- Temperature (teff)\n- Envelope-to-radius ratio (indirect torsion)\n\n")
        f.write("**Interpretation:**\n")
        f.write("- A high score suggests distortions in W-space correlate with these geometric parameters.\n")
        f.write("- Objects with high eccentricity or inclination tend to deviate more strongly from the GR model.\n")
        f.write("- This opens the door to interpreting a perceptive cosmological torsion.\n")

if __name__ == "__main__":
    features = ["mass_sim", "velocity_sim", "eccentricity", "inclination", "logg", "teff", "r_env_r_star"]
    df = load_data()
    df = simulate_axisw(df)
    df, score = run_regression(df, features)
    plot_residuals(df, features, score)
    export_summary(df, score)
