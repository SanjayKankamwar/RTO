import pandas as pd
import os

# Load data
df = pd.read_csv('c:/RTO/output/merged_rto_data.csv', low_memory=False)

# Ensure output directory exists
os.makedirs('../output', exist_ok=True)

# 1. Segment by Fuel Type
fuel_segment = df['fuel'].value_counts().reset_index()
fuel_segment.columns = ['FuelType', 'Count']
fuel_segment.to_csv('../output/segment_fuel_type.csv', index=False)

# 2. Segment by Maker & Model
maker_model_segment = df.groupby(['makerName', 'modelDesc']).size().reset_index(name='Count')
maker_model_segment.to_csv('../output/segment_maker_model.csv', index=False)

# 3. Segment by Body Type
# Segment by Vehicle Class (body type equivalent)
if 'vehicleClass' in df.columns:
    body_segment = df['vehicleClass'].value_counts().reset_index()
    body_segment.columns = ['VehicleClass', 'Count']
    body_segment.to_csv('../output/segment_vehicle_class.csv', index=False)
else:
    print("⚠️ 'vehicleClass' column not found. Skipping body type segmentation.")


# 4. Segment by Region (OfficeCd)
region_segment = df['OfficeCd'].value_counts().reset_index()
region_segment.columns = ['OfficeCd', 'Count']
region_segment.to_csv('../output/segment_region.csv', index=False)

# 5. Top 5 Performing Brands per Region
top_brands = df.groupby(['OfficeCd', 'makerName'])['modelDesc'].count().reset_index(name='Count')
top_brands_sorted = top_brands.sort_values(['OfficeCd', 'Count'], ascending=[True, False])
top5_brands_per_region = top_brands_sorted.groupby('OfficeCd').head(5)
top5_brands_per_region.to_csv('../output/top5_brands_per_region.csv', index=False)

print("✅ Segmentation completed and CSVs saved in '../output/' folder.")
