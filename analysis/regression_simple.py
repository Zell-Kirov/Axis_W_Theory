import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from entity import Entity
from universe import Universe

def simulate_entities():
    data = []
    velocities = [0.2, 0.5, 1.0, 1.5, 2.0]
    masses = [10, 100, 1000, 10000]

    for v in velocities:
        for m in masses:
            gravity = m
            entity = Entity("RegressStar", velocity=v, gravity_factor=gravity)
            universe = Universe(rotation_w=0.0)
            entity.evolve_in_w(1, universe.rotation_w)
            data.append({
                "velocity": v,
                "mass": m,
                "gravity": gravity,
                "time": entity.perceived_time
            })

    return pd.DataFrame(data)

def run_regression(df):
    X = df[["velocity", "mass"]]
    y = df["time"]

    model = LinearRegression()
    model.fit(X, y)

    coeffs = dict(zip(X.columns, model.coef_))
    intercept = model.intercept_

    print("Fitted linear model:")
    print(f"Perceived time ≈ {coeffs['velocity']:.4f} × velocity + {coeffs['mass']:.6f} × mass + {intercept:.4f}")

    return model, coeffs, intercept

def plot_model(df, model):
    os.makedirs("data", exist_ok=True)
    df["predicted_time"] = model.predict(df[["velocity", "mass"]])

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="time", y="predicted_time", hue="velocity", style="mass", palette="viridis", s=80)
    plt.plot([df.time.min(), df.time.max()], [df.time.min(), df.time.max()], "--", color="gray")
    plt.xlabel("Actual perceived time")
    plt.ylabel("Model-estimated time")
    plt.title("Linear Regression - Axis_W")
    plt.tight_layout()
    plt.savefig("data/axisw_regression_plot_simple.png")
    plt.show()

def export_regression_summary(coeffs, intercept, filepath="data/regression_summary_simple.md"):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# Axis_W Linear Regression Summary\n\n")
        f.write("Linear model fitted on 20 simulated entities:\n\n")
        f.write(f"**Estimated Equation:**\n\n")
        f.write(f"`Perceived time ≈ {coeffs['velocity']:.4f} × velocity + {coeffs['mass']:.6f} × mass + {intercept:.4f}`\n\n")
        f.write("**Coefficients:**\n\n")
        f.write(f"- Velocity: `{coeffs['velocity']:.4f}`\n")
        f.write(f"- Mass: `{coeffs['mass']:.6f}`\n")
        f.write(f"- Intercept: `{intercept:.4f}`\n\n")
        f.write("**Quick interpretation:**\n")
        f.write("- Velocity increases perceived time in Axis_W\n")
        f.write("- Mass (i.e., gravity) decreases it\n")
        f.write("- The model is linear, with no interaction effects\n")

if __name__ == "__main__":
    df = simulate_entities()
    model, coeffs, intercept = run_regression(df)
    plot_model(df, model)
    export_regression_summary(coeffs, intercept)
