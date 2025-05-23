# scripts/analyse_fuel_trends.py

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Use non-interactive backend to avoid TclError
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
FUEL_TRENDS_FILE = os.path.join("output", "fuel_trends.csv")
PLOT_PATH = os.path.join("output", "fuel_trend_plot.png")

# Load data
try:
    df = pd.read_csv(FUEL_TRENDS_FILE)
    print("✅ Fuel trends data loaded.")

    # Preview
    print(df.head())

    # Replace unknown fuel type (-1) with "unknown"
    df["Fuel_Type"] = df["Fuel_Type"].replace("-1", "unknown")

    # Plot setup
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df, x="Year", y="Count", hue="Fuel_Type", marker="o", palette="tab10")

    plt.title("Fuel Type Registration Trends Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Registrations")
    plt.legend(title="Fuel Type")
    plt.grid(True)
    plt.tight_layout()

    # Save and show plot
    plt.savefig(PLOT_PATH)
    plt.show()
    print(f"✅ Trend plot saved at {PLOT_PATH}")

except Exception as e:
    print("❌ Error during analysis:", e)
