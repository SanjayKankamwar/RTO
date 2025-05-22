# Telangana RTO Vehicle Registration Analysis (2019–2025)

This project analyzes vehicle registration data from the Regional Transport Offices (RTOs) in Telangana, India. The focus is on extracting insights related to:

- Fuel type adoption trends
- Electric vehicle (EV) adoption by region
- Engine capacity preferences across years
- Popular makers and models by region

---

## 📊 Objective

To assist stakeholders in understanding the transformation of the automotive market in Telangana, especially in the context of increasing EV adoption and changing engine and fuel preferences.

---

## 📂 Scripts Overview

| Script Name | Purpose |
|------------|---------|
| `merge_rto_data.py` | Merges raw RTO CSV files and performs initial cleaning (standardizing columns, dropping nulls, formatting strings). |
| `analyse_fuel_trends.py` | Analyzes fuel-type trends and engine capacity preferences from 2019 to 2025. |
| `analyse_ev_adoption.py` | Identifies regions with the highest EV adoption based on registration data. |
| `segment_rto_data.py` | Segments the dataset by fuel type, vehicle class, maker/model, region, and top brands per region. |

Each script reads from a cleaned merged dataset and exports analytical outputs (CSV files) for visualization and decision-making.

---

## 📁 Folder Structure
RTO/
├── scripts/
│ ├── merge_rto_data.py
│ ├── analyse_fuel_trends.py
│ ├── analyse_ev_adoption.py
│ └── segment_rto_data.py
├── output/ ← (Not pushed to GitHub)
├── rtocsv/ ← (Not pushed to GitHub)


Only the `scripts/` directory is version controlled on this repository.

---

## 📌 Dataset Source

The vehicle registration data is publicly available at the Telangana Government open data portal:

🔗 [https://data.telangana.gov.in/dataset/regional-transport-authority-vehicle-online-sales-data](https://data.telangana.gov.in/dataset/regional-transport-authority-vehicle-online-sales-data)

---

## 🛠️ Tools Used

- Python (Pandas, NumPy, Matplotlib)
- Git for version control
- CSV-based storage for analytics output

---

## 🧠 Key Insights

- Electric vehicles have seen a significant uptick since 2020.
- Urban and semi-urban regions show the fastest EV adoption (e.g., RT, UN RTO codes).
- Petrol remains dominant, but alternative fuels like CNG and hybrids are emerging.
- EVs dominate the sub-1000cc engine segment due to their lightweight and economical build.

---

## 📬 Contact

For questions or collaboration, feel free to reach out to:

**Sanjay Kankamwar**  
📧 sanjaykankamwar6008@gmail.com
📍 VIIT Pune

---


