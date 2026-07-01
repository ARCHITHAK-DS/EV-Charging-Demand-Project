<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=EV%20Charging%20Demand%20Forecasting&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=ARIMA%20%C2%B7%20Prophet%20%C2%B7%20Anomaly%20Detection%20%C2%B7%20Tableau&descAlignY=58&descAlign=50" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Prophet](https://img.shields.io/badge/Prophet-Forecasting-0668E1?style=for-the-badge&logoColor=white)
![ARIMA](https://img.shields.io/badge/ARIMA-Time--Series-7B61FF?style=for-the-badge&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-Live%20Dashboard-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Report-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

<br/>

### 🌐 [Live Tableau Dashboard →](https://public.tableau.com/views/EVChargingDemandForecastingTableaudashboard/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) &nbsp;·&nbsp; 📓 [View Notebook →](#) &nbsp;·&nbsp; 📄 [Project Report →](./EV_Project_Report.pdf)

<br/>

> *"Don't wait for EV congestion to happen — predict it 30 days before it does."*

</div>

---

<br/>

## 🧠 What is This?

<table>
<tr>
<td width="58%">

A **time-series forecasting system** that predicts hourly demand at EV charging stations 30 days in advance — using weather conditions, time patterns, and historical usage data.

Built using **ARIMA** and **Facebook Prophet**, with a bonus **Z-score anomaly detection engine** and a **Charging Optimization Strategy** that recommends the best station-hour slot for EV users.

**The problem it solves:** EV charging stations face unpredictable congestion during peak hours. Accurate demand forecasting enables operators to plan capacity, manage grid load, and guide users to available slots.

</td>
<td width="42%" align="center">

```
Weather + Time
      │
      ▼
  ┌────────┐     ┌──────────┐
  │  ARIMA │     │ Prophet  │
  └───┬────┘     └────┬─────┘
      └──────┬─────────┘
             ▼
      Demand Forecast
      (30 days ahead)
             │
      ┌──────┴──────┐
      ▼             ▼
  Anomaly      Optimization
  Detection    Engine
```

</td>
</tr>
</table>

<br/>

---

## 📊 Live Tableau Dashboard

<div align="center">

### 🔗 [Click to open Dashboard](https://public.tableau.com/views/EVChargingDemandForecastingTableaudashboard/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

</div>

```
Dashboard contains:
┌─────────────────────────────────────────────────────────┐
│  🟣 Demand Heatmap    → Hour × Weekday demand intensity │
│  📈 Monthly Trend     → Seasonal demand curve           │
│  ⚡ Station Compare   → Utilisation % per station       │
│  🌡️  Weather Impact   → Temp & rainfall vs demand       │
│  🔴 Anomaly Markers  → Unusual spike/drop indicators    │
└─────────────────────────────────────────────────────────┘
```

<br/>

---

## 📈 Model Results

<div align="center">

| Model | MAE | RMSE | Seasonality | Holiday Support | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---:|
| ARIMA(2,1,2) | 0.412 | 0.587 | Manual | ❌ | Baseline |
| **Prophet** | **0.298** | **0.431** | Auto ✅ | ✅ | **Winner** |

</div>

<br/>

---

## 🗺️ Dataset Overview

```
📍 5 Stations   →  MG Road · Koramangala · Whitefield (Bangalore)
                   Anna Nagar · T Nagar (Chennai)
📅 1 Year       →  Jan 2023 – Dec 2023  ·  Hourly resolution
📊 43,800 rows  →  demand_units · utilisation_pct · is_anomaly
🌡️  Weather     →  temperature_c · rainfall_mm · wind_kmh
⏰ Time Feats   →  hour · day_of_week · month · is_weekend
```

### Demand Patterns Discovered

```
Morning Peak  ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░  7 AM – 9 AM   (80% utilisation)
Afternoon     ░░░▓▓▓▓▓▓▓░░░░░░░░░░░░░░  11 AM – 1 PM  (65% utilisation)
Evening Peak  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░  5 PM – 8 PM   (90% utilisation)
Night         ░░░░░░░░░░░░░░░░░░░░░░░░  10 PM – 5 AM  (8% utilisation)
```

<br/>

---

## 🚀 Bonus Features

### 🔴 Anomaly Detection
```
Method    : Z-score per station (threshold > 3.0)
Flags     : Unusual demand spikes (equipment faults, local events)
            Unusual demand drops  (power outages, road closures)
Output    : EV_Anomaly_Report.csv — timestamp, station, z_score, demand
Evaluated : Precision-Recall classification report vs injected anomalies
```

### ⚡ Charging Optimization Engine
```
Input   : city, target_date, preferred_hours, min_availability
Output  : Top 5 station-hour slots ranked by availability %
Labels  : ⭐ Best Slot  /  ✅ Good Slot  /  🔶 Moderate
File    : EV_Optimization_Strategy.csv
Use     : EV users avoid congestion · Operators plan staffing
```

<br/>

---

## 🗂️ Project Files

```
📦 project-2-ev/
│
├── 📓 EV_Charging_Notebook.ipynb      ← Full 10-step forecasting notebook
│     ├── Step 1  : Setup & imports
│     ├── Step 2  : Load & explore data
│     ├── Step 3  : Time-series visualisation (4 charts)
│     ├── Step 4  : Weather correlation analysis
│     ├── Step 5  : ARIMA model + 30-day forecast
│     ├── Step 6  : Prophet model + components
│     ├── Step 7  : Model comparison (MAE, RMSE)
│     ├── Step 8  : 🚀 Anomaly detection (Z-score)
│     ├── Step 9  : 🚀 Charging optimization engine
│     └── Step 10 : Export all deliverables
│
├── 📊 EV_Charging_Demand.csv          ← Raw dataset (43,800 rows)
├── 📊 EV_Tableau_Ready.csv            ← Aggregated CSV — Tableau source
├── 📊 EV_Anomaly_Report.csv           ← Detected anomalies with z-scores
├── 📊 EV_Optimization_Strategy.csv    ← Best charging slots per city
├── 📈 EV_Excel_Report.xlsx            ← Station performance report
├── 📄 EV_Project_Report.pdf           ← 2-page project report
└── 📋 requirements.txt                ← Python dependencies
```

<br/>

---

## ⚙️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|:---:|:---:|:---:|
| Language | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) | Core |
| Data | ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat-square) | Cleaning & feature engineering |
| Forecasting | ![Prophet](https://img.shields.io/badge/-Prophet-0668E1?style=flat-square) | Primary forecast model |
| Forecasting | ![Statsmodels](https://img.shields.io/badge/-Statsmodels-7B61FF?style=flat-square) | ARIMA baseline model |
| Anomaly | ![Scipy](https://img.shields.io/badge/-Scipy-8CAAE6?logo=scipy&logoColor=white&style=flat-square) | Z-score detection |
| Viz | ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square) ![Seaborn](https://img.shields.io/badge/-Seaborn-4C72B0?style=flat-square) | Charts & plots |
| Dashboard | ![Tableau](https://img.shields.io/badge/-Tableau-E97627?logo=tableau&logoColor=white&style=flat-square) | Live interactive dashboard |
| Report | ![Excel](https://img.shields.io/badge/-Excel-217346?logo=microsoft-excel&logoColor=white&style=flat-square) | Business output |

</div>

<br/>

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/ev-charging-forecasting.git
cd ev-charging-forecasting

# 2. Install dependencies (Python 3.11 recommended)
pip install -r requirements.txt

# 3. Run the notebook
jupyter notebook EV_Charging_Notebook.ipynb

# Outputs generated automatically:
# → EV_Tableau_Ready.csv
# → EV_Anomaly_Report.csv
# → EV_Optimization_Strategy.csv
```

> ⚠️ **Python version note:** Use Python 3.10 or 3.11. Python 3.13 has compatibility issues with some ML packages.

<br/>

---

## 💡 Key Insights

> **1. Evening peak (5–8 PM) drives 90% utilisation** — the highest congestion window across all stations. Smart pricing during this window could shift ~20% of demand to off-peak hours.

> **2. Rainfall reduces demand by ~5%** — even light rain discourages EV usage. Weather-aware forecasting prevents over-staffing on rainy days.

> **3. Prophet captures seasonality ARIMA misses** — weekly commuter patterns and summer demand spikes are automatically detected, reducing RMSE by 26% vs ARIMA.

<br/>

---

## 🗺️ Roadmap

- [x] ARIMA time-series forecasting
- [x] Prophet seasonal forecasting
- [x] Weather feature integration
- [x] Anomaly detection (Z-score)
- [x] Charging optimization engine
- [x] Live Tableau dashboard
- [x] Excel station performance report
- [ ] Live weather API integration (Open-Meteo)
- [ ] Streamlit web app for real-time forecasting
- [ ] Multi-city expansion (Mumbai, Delhi, Hyderabad)
- [ ] Deep learning model (LSTM) comparison

<br/>

---

<div align="center">

**If this helped you, please ⭐ star the repo!**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Architha%20K-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/architha-k-a22b4539a)
[![Tableau](https://img.shields.io/badge/Tableau-Live%20Dashboard-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/views/EVChargingDemandForecastingTableaudashboard/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer&animation=fadeIn" width="100%"/>
