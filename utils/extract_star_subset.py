import pandas as pd
import re

# Load raw file
df = pd.read_csv("data/hyglike_from_athyg_v32.csv")

# Auto-detect mass column
mass_col = None
for col in df.columns:
    if re.search(r"\bmass\b", col, re.IGNORECASE):
        mass_col = col
        break

# Detect velocity components vx, vy, vz (or variants)
vx_col = next((col for col in df.columns if "vx" in col.lower()), None)
vy_col = next((col for col in df.columns if "vy" in col.lower()), None)
vz_col = next((col for col in df.columns if "vz" in col.lower()), None)

# Check detection success
if not all([mass_col, vx_col, vy_col, vz_col]):
    print("Could not automatically find all required columns.")
    print("Found:", {"mass": mass_col, "vx": vx_col, "vy": vy_col, "vz": vz_col})
    exit()

print(f"Detected columns: mass = '{mass_col}', vx = '{vx_col}', vy = '{vy_col}', vz = '{vz_col}'")

# Extract and clean subset
subset = df[[mass_col, vx_col, vy_col, vz_col]].dropna().head(100)

# Rename columns for Axis_W compatibility
subset = subset.rename(columns={
    mass_col: "mass",
    vx_col: "vx",
    vy_col: "vy",
    vz_col: "vz"
})

# Export cleaned subset
subset.to_csv("data/star_subset.csv", index=False)
print("Exported to data/star_subset.csv")
