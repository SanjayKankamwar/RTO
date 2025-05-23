# scripts/analyse_vehicle_class.py

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Use non-interactive backend to avoid TclError
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File paths
CLASS_FILE = os.path.join("output", "segment_vehicle_class.csv")
PLOT_PATH = os.path.join("output", "vehicle_class_trend_plot.png")

# Load data
try:
    df = pd.read_csv(CLASS_FILE)
    print("✅ Vehicle class data loaded.")
    print(df.head())

    # Sort by count descending
    df = df.sort_values(by="Count", ascending=False)

    # Plot setup
    plt.figure(figsize=(14, 8))
    sns.barplot(data=df.head(20), x="Count", y="VehicleClass", palette="viridis")
    plt.xscale("log") # ← Use log scale
    plt.title("Top 20 Vehicle Classes by Registration Count (Log Scale)")
    plt.xlabel("Log(Number of Registrations)")
    plt.ylabel("Vehicle Class")
    plt.tight_layout()

    # Save and show
    plt.savefig(PLOT_PATH)
    plt.show()
    print(f"✅ Vehicle class trend plot saved at {PLOT_PATH}")

except Exception as e:
    print("❌ Error during analysis:", e)
