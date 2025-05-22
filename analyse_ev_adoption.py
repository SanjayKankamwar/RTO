import pandas as pd
import os
from collections import defaultdict

chunksize = 100_000
output_dir = 'C:\\RTO\\output'
os.makedirs(output_dir, exist_ok=True)

ev_counts_by_rto = defaultdict(int)

for chunk in pd.read_csv('C:\\RTO\\output\\merged_rto_data.csv', chunksize=chunksize, low_memory=False):
    # Normalize column names
    chunk.columns = [col.strip().lower() for col in chunk.columns]
    
    # Remove duplicate columns
    chunk = chunk.loc[:, ~pd.Index(chunk.columns).duplicated(keep='first')]

    if 'fuel' not in chunk.columns or 'officecd' not in chunk.columns:
        continue

    # Normalize fuel
    chunk['fuel'] = chunk['fuel'].astype(str).str.lower()

    # Filter EV entries
    ev_chunk = chunk[chunk['fuel'].str.contains('electric|ev', na=False)]

    # Get RTO region
    ev_chunk['officecd'] = ev_chunk['officecd'].astype(str).str.upper().str.strip()

    for rto in ev_chunk['officecd'].dropna():
        ev_counts_by_rto[rto] += 1

# Create dataframe
df_top_rto = pd.DataFrame([
    {'RTO_Office': rto, 'EV_Count': count}
    for rto, count in ev_counts_by_rto.items()
])

# Sort descending
df_top_rto = df_top_rto.sort_values(by='EV_Count', ascending=False)

# Save output
df_top_rto.to_csv(os.path.join(output_dir, 'top_ev_rto_areas.csv'), index=False)
print("✔ Top EV adoption areas saved to output/top_ev_rto_areas.csv")
