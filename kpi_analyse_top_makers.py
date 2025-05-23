import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File paths
MERGED_FILE = os.path.join("output", "merged_rto_data.csv")
OUTPUT_CSV = os.path.join("output", "top_manufacturers.csv")
OUTPUT_PLOT = os.path.join("output", "top_manufacturers_plot.png")

try:
    # Load data
    df = pd.read_csv(MERGED_FILE, low_memory=False)
    print("✅ Merged RTO data loaded.")

    # Choose best available manufacturer column
    columns = ["Manufacturer_Name", "makerName"]
    valid_col = None
    for col in columns:
        if col in df.columns and df[col].notna().sum() > 100:
            valid_col = col
            break

    if not valid_col:
        raise ValueError("No valid manufacturer column found.")

    print(f"ℹ️ Using manufacturer column: {valid_col}")

    # Clean manufacturer data
    df[valid_col] = df[valid_col].fillna("Unknown").astype(str).str.strip()
    df[valid_col] = df[valid_col].replace("", "Unknown")

    # Count registrations
    top_makers = df[valid_col].value_counts().reset_index()
    top_makers.columns = ["Manufacturer", "Registration_Count"]

    # Save output
    top_makers.to_csv(OUTPUT_CSV, index=False)
    print(f"📁 Saved top manufacturers to: {OUTPUT_CSV}")

    # Plot top 20
    plt.figure(figsize=(14, 8))
    sns.barplot(data=top_makers.head(20), x="Registration_Count", y="Manufacturer", palette="rocket")
    plt.title("Top 20 Manufacturers by Vehicle Registrations")
    plt.xlabel("Number of Registrations")
    plt.ylabel("Manufacturer")
    plt.tight_layout()
    plt.savefig(OUTPUT_PLOT)
    print(f"📊 Saved plot to: {OUTPUT_PLOT}")
except Exception as e:
    print("❌ Error generating KPI 4:", e)
