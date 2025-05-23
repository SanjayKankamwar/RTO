# 📊 Telangana RTO Automotive Market Analysis (2019–2025)
Before going forward with this download the dataset from the year 2019 to 2025(according to your preference) link :- https://data.telangana.gov.in/dataset/regional-transport-authority-vehicle-online-sales-data
A data-driven analysis of vehicle registration trends across Telangana to understand fuel adoption, manufacturer popularity, regional brand preferences, and the rise of electric vehicles. The analysis covers data from all major RTOs across the state and presents insights through 6 key KPIs.

## 🌐 Project Overview

This project aims to:

- Analyze regional trends in vehicle registrations using Telangana RTO data.
- Track fuel-type transitions (including EV surge).
- Identify top vehicle manufacturers and segment-wise preferences.
- Build 6 Key Performance Indicators (KPIs) supported by clean visualizations.
- Provide actionable insights for policy makers, automobile companies, and analysts.

## 📁 Folder Structure

```
.
├── output/                         # Final outputs (plots & processed CSVs)
│   ├── ev_adoption_by_rto.csv
│   ├── fuel_trend_plot.png
│   ├── fuel_trends.csv
│   ├── kpi6_brand_monthly_trend.csv
│   ├── kpi6_brand_monthly_trend_plot.png
│   ├── merged_rto_data.csv
│   ├── segment_fuel_type.csv
│   ├── segment_maker_model.csv
│   ├── segment_region.csv
│   ├── segment_vehicle_class.csv
│   ├── top_ev_rto_areas.csv
│   ├── top_ev_rtos_plot.png
│   ├── top_manufacturers.csv
│   ├── top_manufacturers_plot.png
│   ├── top5_brands_per_region.csv
│   ├── top5_brands_region_sample_plot.png
│   └── vehicle_class_trend_plot.png
│
├── rtocsv/                         # (Optional) Raw CSVs if any
│
├── scripts/                        # Python scripts for each KPI & preprocessing
│   ├── analyse_ev_adoption.py
│   ├── kpi_analyse_fuel_trends.py
│   ├── kpi_analyse_top_makers.py
│   ├── kpi_analyse_vehicle_class_trend.py
│   ├── kpi_brandmarkettrendovertime.py
│   ├── kpi_ev_adoption_rate.py
│   ├── kpi_top5_brands_per_region.py
│   ├── merge_rto_data.py
│   └── segment_rto_data.py
│
├── README.md                       # This file
└── requirements.txt                # Python dependencies
```

## 🛠️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/RTO.git
cd RTO
```

2. Create and activate a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) If your raw data is not pre-merged, run:

```bash
python scripts/segment_rto_data.py
python scripts/merge_rto_data.py
```

## 📈 Running the KPI Scripts

Each script in `/scripts` generates one KPI and associated outputs in `/output`:

- **KPI 1: EV Adoption Rate by RTO**
  - Script: `scripts/kpi_ev_adoption_rate.py`
  - Output: `ev_adoption_by_rto.csv`, `top_ev_rtos_plot.png`

- **KPI 2: Fuel Type Registration Trends**
  - Script: `scripts/kpi_analyse_fuel_trends.py`
  - Output: `fuel_trends.csv`, `fuel_trend_plot.png`

- **KPI 3: Vehicle Class Distribution**
  - Script: `scripts/kpi_analyse_vehicle_class_trend.py`
  - Output: `vehicle_class_trend_plot.png`

- **KPI 4: Top Vehicle Manufacturers**
  - Script: `scripts/kpi_analyse_top_makers.py`
  - Output: `top_manufacturers.csv`, `top_manufacturers_plot.png`

- **KPI 5: Top 5 Brands by Region**
  - Script: `scripts/kpi_top5_brands_per_region.py`
  - Output: `top5_brands_per_region.csv`, `top5_brands_region_sample_plot.png`

- **KPI 6: Monthly Brand Trend Over Time**
  - Script: `scripts/kpi_brandmarkettrendovertime.py`
  - Output: `kpi6_brand_monthly_trend.csv`, `kpi6_brand_monthly_trend_plot.png`

## 🧮 KPI Descriptions

1. **📍 EV Adoption by RTO Region**  
   Measures EV penetration across Telangana’s RTOs. Highlights regions like Hyderabad CZ, Medchal, and Rangareddy.

2. **⛽ Fuel Type Trends Over Years (2019–2025)**  
   Tracks petrol, diesel, hybrid, and EV vehicle trends. EVs grew 2000% since 2019.

3. **🚗 Vehicle Class Popularity**  
   Motorcycles dominate, followed by cars, tractors, and rickshaws—indicating personal mobility trends.

4. **🏭 Top Manufacturers**  
   Hero, Honda, TVS, and Bajaj top registration charts across Telangana.

5. **🌐 Top 5 Brands by Region**  
   Highlights regional preferences for manufacturers and models.

6. **📆 Brand Popularity Over Time (Monthly)**  
   Temporal trends of brand registrations—ideal for sales strategy and planning.

## 🖼️ Output Visuals

- Fuel Type Trend → `output/fuel_trend_plot.png`
- EV Regions → `output/top_ev_rtos_plot.png`
- Manufacturers → `output/top_manufacturers_plot.png`
- Vehicle Classes → `output/vehicle_class_trend_plot.png`
- Regional Brands → `output/top5_brands_region_sample_plot.png`
- Monthly Brand Trends → `output/kpi6_brand_monthly_trend_plot.png`

## 📦 Dependencies

Install all requirements with:

```bash
pip install -r requirements.txt
```

requirements.txt should include:

- pandas
- numpy
- matplotlib
- seaborn

## ✍️ Author

Developed by: Sanjay Kankamwar  
GitHub: https://github.com/SanjayKankamwar  
LinkedIn: https://www.linkedin.com/in/sanjaykankamwar

## 📜 License

This project is for academic and internal analysis use. Contact the author for commercial usage rights.
