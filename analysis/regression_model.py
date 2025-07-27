import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Add src/ to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from entity import Entity
from universe import Universe

def simulate_entities():
    data = []
    velocities = [0.2, 0.5, 1.0, 1.5, 2.0]
    masses = [10, 100, 1000, 10000]

    for v in velocities:
        for m in masses:
            gravity = m  # Gravity = direct mass
            entity = Entity("RegressStar", velocity=v, gravity_factor=gravity)
            universe = Universe(rotation_w=0.0)
            entity.evolve_in_w(1, universe.rotation_w)
            data.append({
                "velocity": v,
                "mass": m,
                "mass²": m ** 2,
                "gravity": gravity,
                "time": entity.perceived_time
            })

    return pd.DataFrame(data)

def run_regression(df):
    X = df[["velocity", "mass", "mass²"]]
    y = df["time"]

    model = LinearRegression()
    model.fit(X, y)

    coeffs = dict(zip(X.columns, model.coef_))
    intercept = model.intercept_

    print("Enriched Model:")
    print(f"Time ≈ {coeffs['velocity']:.4f}×velocity + {coeffs['mass']:.6f}×mass + {coeffs['mass²']:.9f}×mass² + {intercept:.4f}")

    return model, coeffs, intercept

def plot_prediction(df, model):
    os.makedirs("data", exist_ok=True)
    df["predicted_time"] = model.predict(df[["velocity", "mass", "mass²"]])

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="time", y="predicted_time", hue="velocity", style="mass", palette="viridis", s=80)
    plt.plot([df.time.min(), df.time.max()], [df.time.min(), df.time.max()], "--", color="gray")
    plt.xlabel("Actual Perceived Time")
    plt.ylabel("Predicted Time (model)")
    plt.title("Enriched Axis_W Regression")
    plt.tight_layout()
    plt.savefig("data/axisw_regression_plot.png")
    plt.show()

def plot_residuals(df):
    df["residuals"] = df["time"] - df["predicted_time"]
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="mass", y="residuals", hue="velocity", palette="coolwarm")
    plt.axhline(0, linestyle="--", color="gray")
    plt.title("Residuals of the Enriched Axis_W Model")
    plt.xlabel("Mass")
    plt.ylabel("Error (actual - predicted)")
    plt.tight_layout()
    plt.savefig("data/axisw_residuals_plot.png")
    plt.show()

def export_regression_summary(coeffs, intercept, filepath="data/regression_summary.md"):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# Summary of Enriched Axis_W Regression\n\n")
        f.write("Model fitted with quadratic effect:\n\n")
        f.write(f"**Estimated Equation:**\n\n")
        f.write(f"`Time ≈ {coeffs['velocity']:.4f} × velocity + {coeffs['mass']:.6f} × mass + {coeffs['mass²']:.9f} × mass² + {intercept:.4f}`\n\n")
        f.write("**Variables used:**\n")
        f.write("- Velocity\n")
        f.write("- Mass\n")
        f.write("- Mass² (non-linear effect)\n\n")
        f.write("**Residual Analysis:**\n")
        f.write("- Plot saved in `data/axisw_residuals_plot.png`\n")
        f.write("- If residuals are centered around zero → coherent model\n")
        f.write("- If errors increase or decrease with mass → presence of real non-linear effect\n")

if __name__ == "__main__":
    df = simulate_entities()
    model, coeffs, intercept = run_regression(df)
    plot_prediction(df, model)
    plot_residuals(df)
    export_regression_summary(coeffs, intercept)
