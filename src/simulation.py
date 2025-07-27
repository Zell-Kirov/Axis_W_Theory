import pandas as pd
import matplotlib.pyplot as plt

def plot_gaia_results():
    df = pd.read_csv("data/gaia_output.csv")
    steps = df["Step"]
    stars = [col for col in df.columns if col.endswith("_TimePerceived")]

    plt.figure(figsize=(12, 6))
    for star in stars[:20]:  # Show the first 20 for readability
        plt.plot(steps, df[star], label=star, alpha=0.7)

    plt.title("Perceived Time of Gaia Stars in Axis_W")
    plt.xlabel("Universe Steps")
    plt.ylabel("Perceived Time")
    plt.legend(loc="upper left", fontsize=8)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("data/gaia_plot.png")
    plt.show()

def plot_blackhole_result():
    df = pd.read_csv("data/s_star_prediction.csv")

    plt.figure(figsize=(8, 5))
    plt.plot(df["Step"], df["S-star_W_TimePerceived"], color="black", linewidth=2)
    plt.title("Temporal Reversal Around a Supermassive Black Hole (S-star_W)")
    plt.xlabel("Universe Steps")
    plt.ylabel("Perceived Time")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("data/blackhole_plot.png")
    plt.show()

def compare_gaia_blackhole():
    gaia_df = pd.read_csv("data/gaia_output.csv")
    bh_df = pd.read_csv("data/s_star_prediction.csv")
    step = bh_df["Step"]
    
    avg_gaia = gaia_df.drop(["Step", "Universe_W"], axis=1).mean(axis=1)

    plt.figure(figsize=(10, 5))
    plt.plot(step, bh_df["S-star_W_TimePerceived"], label="S-star_W (black hole)", color="black", linewidth=2)
    plt.plot(step, avg_gaia[:len(step)], label="Gaia Average", color="skyblue", linestyle="--")
    plt.title("Comparison: Temporal Reversal vs Gaia Average")
    plt.xlabel("Steps")
    plt.ylabel("Perceived Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("data/comparison_plot.png")
    plt.show()

if __name__ == "__main__":
    plot_gaia_results()
    plot_blackhole_result()
    compare_gaia_blackhole()
