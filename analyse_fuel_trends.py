import pandas as pd
import os
from collections import defaultdict

chunksize = 100_000
output_dir = 'C:\\RTO\\output'
os.makedirs(output_dir, exist_ok=True)

# Containers to count fuel and engine size trends
fuel_trends = defaultdict(lambda: defaultdict(int))  # fuel_type -> year -> count
engine_trends = defaultdict(lambda: defaultdict(int))  # engine_size_bucket -> year -> count

for chunk in pd.read_csv('C:\\RTO\\output\\merged_rto_data.csv', chunksize=chunksize, low_memory=False):
    # Normalize column names
    chunk.columns = [col.strip().lower() for col in chunk.columns]
    
    # Remove duplicate columns
    chunk = chunk.loc[:, ~pd.Index(chunk.columns).duplicated(keep='first')]
    
    if 'fuel' not in chunk.columns or 'fromdate' not in chunk.columns:
        continue

    # Normalize fuel column
    chunk['fuel'] = chunk['fuel'].astype(str).str.lower().str.strip()
    
    # Parse registration date to get year
    chunk['fromdate'] = pd.to_datetime(chunk['fromdate'], errors='coerce')
    chunk = chunk.dropna(subset=['fromdate'])
    chunk['year'] = chunk['fromdate'].dt.year
    
    # Process fuel types per year
    for _, row in chunk.iterrows():
        fuel = row['fuel']
        year = row['year']
        fuel_trends[fuel][year] += 1
    
    # Engine size: check if engine size column is present
    engine_col_candidates = ['engine_size', 'cc', 'displacement', 'enginesize']
    engine_col = None
    for col in engine_col_candidates:
        if col in chunk.columns:
            engine_col = col
            break
    
    if engine_col:
        chunk[engine_col] = pd.to_numeric(chunk[engine_col], errors='coerce')
        chunk = chunk.dropna(subset=[engine_col])
        
        # Define buckets
        bins = [0, 500, 1000, 1500, 2000, 3000, 5000, 10000]
        labels = ['0-500cc', '501-1000cc', '1001-1500cc', '1501-2000cc', '2001-3000cc', '3001-5000cc', '5000+cc']
        
        chunk['engine_size_bucket'] = pd.cut(chunk[engine_col], bins=bins, labels=labels, right=True)
        
        for _, row in chunk.iterrows():
            bucket = row['engine_size_bucket']
            year = row['year']
            if pd.notna(bucket):
                engine_trends[bucket][year] += 1

# Convert fuel trends to DataFrame
records_fuel = []
for fuel_type, years_dict in fuel_trends.items():
    for year, count in years_dict.items():
        records_fuel.append({'Fuel_Type': fuel_type, 'Year': year, 'Count': count})
df_fuel_trends = pd.DataFrame(records_fuel).sort_values(['Fuel_Type', 'Year'])

# Convert engine size trends to DataFrame (check if not empty)
records_engine = []
for bucket, years_dict in engine_trends.items():
    for year, count in years_dict.items():
        records_engine.append({'Engine_Size_Bucket': bucket, 'Year': year, 'Count': count})
df_engine_trends = pd.DataFrame(records_engine)

if not df_engine_trends.empty:
    df_engine_trends = df_engine_trends.sort_values(['Engine_Size_Bucket', 'Year'])
    df_engine_trends.to_csv(os.path.join(output_dir, 'engine_size_trends.csv'), index=False)
    print("✔ Engine size trend analysis saved.")
else:
    print("⚠️ No engine size data found; skipping saving engine_size_trends.csv")

# Always save fuel trends
df_fuel_trends.to_csv(os.path.join(output_dir, 'fuel_trends.csv'), index=False)
print("✔ Fuel trend analysis saved.")
