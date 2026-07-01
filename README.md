<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=00897B&height=200&section=header&text=EV%20Charging%20Forecaster&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Predict%20%C2%B7%20Optimize%20%C2%B7%20Electrify&descAlignY=58&descAlign=50" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Prophet](https://img.shields.io/badge/Prophet-Forecasting-0072B5?style=for-the-badge&logo=meta&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-Heatmap-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Report-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

<br/>

### 🌐 [Live Demo →](https://your-app-link.streamlit.app) &nbsp;&nbsp; 📓 [View Notebook →](#) &nbsp;&nbsp; 📊 [See Report →](#)

<br/>

> *"Every parked EV is a data point. This model turns those data points into a power grid that thinks ahead."*

</div>

---

<br/>

## ⚡ What is This?

<table>
<tr>
<td width="60%">

A **time-series forecasting system** that predicts hourly demand at EV charging stations — before it happens.

Built on **Prophet & ARIMA** models using weather, time, and traffic signals, it identifies peak/off-peak windows so operators can plan capacity, set dynamic pricing, and prevent the #1 complaint in EV infrastructure: **waiting in line for a charger.**

**The problem it solves:** Charging networks are built reactively. This model makes them predictive.

</td>
<td width="40%" align="center">

```
Given time + weather + traffic:

  Hour      ──┐
  Day        ──┤
  Temperature──┼──► Prophet ──► Demand (kWh)
  Rain       ──┤        │
  Wind       ──┤        └──► Peak/Off-Peak
  Traffic    ──┘              Classification
```

</td>
</tr>
</table>

<br/>

---

## 📊 Results at a Glance

<div align="center">

| Metric | Forecasting Model | Naive Baseline | Improvement |
|:---:|:---:|:---:|:---:|
| MAE | **3.51 kWh** | 5.20 kWh | 🔻 32.5% |
| RMSE | **4.36 kWh** | 6.54 kWh | 🔻 33.3% |
| MAPE | **13.9%** | 21.6% | 🔻 35.6% |

</div>

<br/>

---

## ⏰ Demand Pattern Discovered

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   🔴 PEAK HOURS        │  4 PM – 7 PM   │  Commute + EV charging │
│   ─────────────────────────────────────────────────────────────  │
│   → Recommended action: +20-30% dynamic pricing surcharge        │
│                                                                  │
│   🌙 OFF-PEAK HOURS     │  12 AM – 3 AM  │  Lowest network load  │
│   ─────────────────────────────────────────────────────────────  │
│   → Recommended action: -15-20% discount + scheduled maintenance │
│                                                                  │
│   🔋 RECOMMENDED CAPACITY │ 79.7 kWh/hr  │  95th %ile + buffer   │
│   ─────────────────────────────────────────────────────────────  │
│   → Covers 95% of demand scenarios across the network            │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

<br/>

---

## 🗂️ Project Structure

```
📦 ev-charging-demand-forecasting/
│
├── 📓 EV_Charging_Demand_Forecasting.ipynb   ← Full 11-step ML notebook
├── 🌐 app.py                                 ← Streamlit live dashboard (4 tabs)
├── 📊 EV_Excel_Report.xlsx                   ← 5-sheet Excel report
├── 📽️  EV_Presentation.pptx                  ← 8-slide portfolio deck
├── ⭐ bonus_features.py                      ← 4 bonus modules (see below)
│
├── 📁 EV_Weather_Raw_Data.csv                ← Raw per-station + weather data
├── 📁 Hourly_Demand_Full.csv                 ← Aggregated hourly demand
├── 📁 Forecast_Output.csv                    ← Predicted vs actual (30-day test)
├── 📁 Tableau_Heatmap_Data.csv               ← Ready-to-import Tableau heatmap
├── 📁 Charging_Optimization_Strategy.csv     ← Business recommendations
├── 📁 Model_Comparison.csv                   ← Forecasting model vs baseline
├── 📁 Demand_Anomalies.csv                   ← Detected anomalies (bonus output)
│
├── 🤖 ev_forecast_model.pkl                  ← Trained forecasting model
├── 📋 requirements.txt                       ← Python dependencies
└── 📄 README.md                              ← You are here
```

<br/>

---

## ⚙️ How It Works — Step by Step

```
STEP 1        STEP 2         STEP 3          STEP 4          STEP 5
  │             │              │               │               │
Merge EV    Explore         Engineer        Train Prophet    Generate
+ Weather → Time-Series  →  Cyclical    →   + ARIMA      →   Optimization
  Data        Patterns       Features        Models           Strategy
  │             │              │               │               │
Hourly      Daily/weekly    Hour & day      Compare MAE,     Peak/off-peak
aggregation  seasonality     sin/cos         RMSE, MAPE       + capacity plan
```

<br/>

---

## 🚀 Quick Start

### 1️⃣ Clone & Install

```bash
git clone https://github.com/your-username/ev-charging-demand-forecasting.git
cd ev-charging-demand-forecasting
pip install -r requirements.txt
```

### 2️⃣ Run the Notebook

```bash
jupyter notebook EV_Charging_Demand_Forecasting.ipynb
```

> Run all cells top to bottom. Uses synthetic data by default — swap in real data from [Kaggle EV datasets](https://www.kaggle.com/datasets?search=ev+charging) or [Open-Meteo](https://open-meteo.com) for production use.

### 3️⃣ Launch the Dashboard

```bash
streamlit run app.py
```

🎉 Opens at `http://localhost:8501` with 4 interactive tabs: Live Predictor, Demand Heatmap, Forecast Accuracy, Optimization Strategy.

### 4️⃣ Run Bonus Features

```bash
python bonus_features.py
```

<br/>

---

## 🌟 Bonus Features

```
┌─────────────────────── 4 Advanced Modules ────────────────────────┐
│                                                                    │
│  🌧️  Weather Severity Alert System                                │
│      Flags conditions likely to cause demand SPIKES               │
│      (sub-zero temps, heavy rain, high wind) → pre-position units │
│                                                                    │
│  ⚖️  Station-Level Load Balancing                                  │
│      Detects over/under-utilized stations in real time            │
│      → reroute traffic via app notifications automatically        │
│                                                                    │
│  🌍  Carbon Offset Calculator                                      │
│      Converts kWh charged → CO2 saved vs petrol vehicles          │
│      → 8,500 kWh charged = 6,417 kg CO2 saved = 305 trees/year    │
│                                                                    │
│  🔎  Anomaly Detection Engine                                      │
│      Z-score based detection of demand spikes/drops               │
│      → catches station outages, special events, data errors       │
│      → found 77 anomalies across 8,784 hours of data              │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

<br/>

---

## 🌐 Dashboard Features

```
┌────────────────────── Glassmorphism UI (Teal Theme) ──────────────────┐
│                                                                       │
│  📈  Live Predictor     →  6 inputs (time, weather, traffic) → kWh   │
│                                                                       │
│  📊  Demand Heatmap     →  Day × Hour matrix, interactive colormap   │
│                                                                       │
│  🔍  Forecast Accuracy  →  30-day actual vs predicted with CI bands  │
│                                                                       │
│  💡  Optimization Tab   →  Strategy table + actionable recommendations│
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

<br/>

---

## 📦 Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|:---:|:---:|:---:|
| Language | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) | Core |
| Data | ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat-square) | Merging & aggregation |
| Forecasting | ![Prophet](https://img.shields.io/badge/-Prophet-0072B5?style=flat-square) | Seasonality + regressors |
| Baseline | ![ARIMA](https://img.shields.io/badge/-ARIMA-FF6F00?style=flat-square) | Statistical comparison |
| Validation | ![Sklearn](https://img.shields.io/badge/-Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white&style=flat-square) | MAE, RMSE, MAPE |
| Viz | ![Tableau](https://img.shields.io/badge/-Tableau-E97627?logo=tableau&logoColor=white&style=flat-square) | Heatmap dashboard |
| App | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square) | Web UI |
| Report | ![Excel](https://img.shields.io/badge/-Excel-217346?logo=microsoft-excel&logoColor=white&style=flat-square) | Business output |

</div>

<br/>

---

## 📈 Key Business Insights

> **1. Cold weather is a hidden demand driver**
> Temperatures below 0°C correlate with measurable charging spikes — EV batteries lose efficiency in cold, drivers charge more often. Most operators don't plan for this.

> **2. The grid has a rush hour**
> 4–7 PM accounts for the highest sustained demand window — overlapping with commute traffic and home-charging habits. Off-peak pricing here could shift 15-20% of load.

> **3. Naive forecasting underestimates risk by 35%**
> A simple "same time last week" baseline misses weather and traffic effects entirely — the Prophet-style model's MAPE improvement directly translates to fewer under-provisioned stations.

<br/>

---

## 🗺️ Roadmap / Extensions

- [x] Prophet + ARIMA forecasting models
- [x] Day × Hour demand heatmap
- [x] Streamlit live dashboard (4 tabs)
- [x] Charging optimization strategy
- [x] Weather severity alerts
- [x] Load balancing recommendations
- [x] Carbon offset calculator
- [x] Anomaly detection engine
- [ ] Real-time API integration (live weather + traffic feeds)
- [ ] Multi-station individual forecasting (vs network aggregate)
- [ ] Reinforcement learning for dynamic pricing optimization
- [ ] Mobile app push notifications for load balancing

<br/>

---

## 👤 About

<div align="center">

**Built as part of a Data Science Portfolio Project**

If you found this useful, please ⭐ star the repo!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/architha-k-a22b4539a)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username)

</div>

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=00897B&height=120&section=footer&animation=fadeIn" width="100%"/>
