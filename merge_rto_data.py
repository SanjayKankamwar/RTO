import pandas as pd
import os

# Define folder path for reading CSVs
folder_path = os.path.join("..", "rtocsv")

# Get all CSV files
all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]

# Read all CSVs into a list
df_list = [pd.read_csv(f, low_memory=False) for f in all_files]

# Merge into one DataFrame
df = pd.concat(df_list, ignore_index=True)
print("Columns in merged DataFrame:", df.columns.tolist())


# ✅ Clean the merged data
df.dropna(subset=['fuel', 'makerName', 'modelDesc', 'vehicleClass', 'OfficeCd'], inplace=True)

df['fuel'] = df['fuel'].str.strip().str.upper()
df['makerName'] = df['makerName'].str.strip().str.title()
df['modelDesc'] = df['modelDesc'].str.strip().str.title()
df['vehicleClass'] = df['vehicleClass'].str.strip().str.title()
df['OfficeCd'] = df['OfficeCd'].astype(str).str.strip().str.upper()

df['Maker_Model'] = df['makerName'] + ' ' + df['modelDesc']


# Show some preview
print("Total cleaned records:", len(df))
print(df.head())

# Save the final cleaned + merged CSV
output_path = os.path.join("..", "output", "merged_rto_data.csv")
df.to_csv(output_path, index=False)
print(f"Merged CSV saved at: {output_path}")
