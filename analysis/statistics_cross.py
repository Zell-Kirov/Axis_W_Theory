import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from entity import Entity
from universe import Universe

# Generate 100 entities
data = []
for v in [0.2, 0.5, 1.0, 1.5]:
    for m in [10, 100, 1000, 10000]:
        gravity_factor = m
        entity = Entity("StatStar", velocity=v, gravity_factor=gravity_factor)
        universe = Universe(rotation_w=0.0)
        entity.evolve_in_w(1, universe.rotation_w)
        data.append({
            "velocity": v,
            "mass": m,
            "gravity": gravity_factor,
            "time": entity.perceived_time
        })

df = pd.DataFrame(data)

# Correlation matrix
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlations between Axis_W parameters")
plt.savefig("data/axisw_correlation_matrix.png")
plt.show()
