# scripts/kpi_ev_adoption_rate.py

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Use non-interactive backend to avoid TclError
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File paths
EV_FILE = os.path.join("output", "top_ev_rto_areas.csv")
TOTAL_FILE = os.path.join("output", "merged_rto_data.csv")  # Assuming this has total registrations

# Load EV data
ev_df = pd.read_csv(EV_FILE)
print("EV File Columns:", ev_df.columns)

# Preview EV data
print("\nTop EV RTOs:")
print(ev_df.sort_values(by="EV_Count", ascending=False).head(10))

# Load total vehicle data and compute adoption rate
try:
    total_df = pd.read_csv(TOTAL_FILE)
    print("Merged file loaded. Columns:", total_df.columns)

    # Compute total vehicle registrations per RTO
    if "OfficeCd" not in total_df.columns:
        raise KeyError("Expected 'OfficeCd' column in total vehicle data.")

    total_counts = total_df.groupby("OfficeCd").size().reset_index(name="Total_Count")

    # Merge EV and total vehicle counts
    df_merged = pd.merge(ev_df, total_counts, left_on="RTO_Office", right_on="OfficeCd", how="inner")

    # Calculate EV Adoption Rate
    df_merged["EV_Adoption_Rate"] = df_merged["EV_Count"] / df_merged["Total_Count"]

    # Save to output
    output_file = os.path.join("output", "ev_adoption_by_rto.csv")
    df_merged.to_csv(output_file, index=False)
    print(f"\n✅ EV adoption rate saved to '{output_file}'")

except Exception as e:
    print("⚠️ Could not compute EV adoption rate due to:", e)
    df_merged = ev_df.copy()  # Fallback to just EV data

# Plot: Top 10 RTOs by EV Registrations
top_rtos = ev_df.sort_values(by="EV_Count", ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_rtos, x="EV_Count", y="RTO_Office", palette="mako")
plt.title("Top 10 RTOs by EV Registrations")
plt.xlabel("EV Registration Count")
plt.ylabel("RTO Office")
plt.tight_layout()

# Save plot
plot_file = os.path.join("output", "top_ev_rtos_plot.png")
plt.savefig(plot_file)
print(f"\n📊 Plot saved to '{plot_file}'")

# Show merged data preview
if "EV_Adoption_Rate" in df_merged.columns:
    print("\n🔍 Merged EV Adoption Data (Top 10):")
    print(df_merged.sort_values(by="EV_Adoption_Rate", ascending=False).head(10).to_string())
else:
    print("\n📄 EV data preview (no adoption rate available):")
    print(df_merged.head(10).to_string())
