"""
BONUS FEATURES — EV Charging Demand Forecasting
==================================================
Run this after the main notebook to add advanced capabilities.
Each function is independent — use whichever bonuses you want.
"""

import pandas as pd
import numpy as np

# ════════════════════════════════════════════════════════════════
# BONUS 1: Weather Severity Alert System
# ════════════════════════════════════════════════════════════════
def weather_demand_alert(temperature, precipitation, wind_speed):
    """
    Flags conditions likely to cause demand SPIKES so operators
    can pre-position mobile charging units or alert grid partners.
    """
    risk_score = 0
    reasons = []

    if temperature < 0:
        risk_score += 3
        reasons.append("Sub-zero temps drain EV batteries faster -> charging spike expected")
    elif temperature < 5:
        risk_score += 1
        reasons.append("Cold weather increases heating load on batteries")

    if precipitation > 5:
        risk_score += 2
        reasons.append("Heavy rain reduces walk-in traffic but increases dwell time at stations")

    if wind_speed > 35:
        risk_score += 1
        reasons.append("High wind may indicate storm system -> possible grid instability")

    if risk_score >= 4:
        level = "HIGH"
    elif risk_score >= 2:
        level = "MODERATE"
    else:
        level = "LOW"

    return {"risk_level": level, "risk_score": risk_score, "reasons": reasons}


# ════════════════════════════════════════════════════════════════
# BONUS 2: Station-Level Load Balancing Recommendation
# ════════════════════════════════════════════════════════════════
def recommend_load_balancing(station_demands: dict, total_capacity: float):
    """
    Given current demand per station, suggests which stations are
    over/under-utilized and recommends rerouting EV traffic via app notifications.

    station_demands: dict like {'STATION_1': 45.2, 'STATION_2': 12.1, ...}
    """
    avg_demand = np.mean(list(station_demands.values()))
    recommendations = []

    for station, demand in station_demands.items():
        utilization = (demand / (total_capacity / len(station_demands))) * 100
        if utilization > 90:
            recommendations.append({
                "station": station, "utilization": round(utilization, 1),
                "action": "REROUTE — Direct new arrivals to nearby underutilized stations"
            })
        elif utilization < 30:
            recommendations.append({
                "station": station, "utilization": round(utilization, 1),
                "action": "PROMOTE — Offer dynamic discount to attract more sessions"
            })
        else:
            recommendations.append({
                "station": station, "utilization": round(utilization, 1),
                "action": "OK — Operating within normal range"
            })

    return pd.DataFrame(recommendations)


# ════════════════════════════════════════════════════════════════
# BONUS 3: Carbon Offset Calculator
# ════════════════════════════════════════════════════════════════
def calculate_carbon_offset(total_kwh_charged, grid_emission_factor=0.4, petrol_emission_factor=2.31):
    """
    Estimates CO2 saved by EV charging vs equivalent petrol vehicle usage.
    grid_emission_factor: kg CO2 per kWh (varies by country grid mix)
    petrol_emission_factor: kg CO2 per liter of petrol
    Avg EV efficiency: ~6 km/kWh | Avg petrol car: ~12 km/liter
    """
    km_driven = total_kwh_charged * 6  # approx km per kWh
    petrol_liters_equivalent = km_driven / 12
    petrol_emissions = petrol_liters_equivalent * petrol_emission_factor
    ev_emissions = total_kwh_charged * grid_emission_factor
    co2_saved_kg = petrol_emissions - ev_emissions

    return {
        "total_kwh": round(total_kwh_charged, 1),
        "estimated_km_driven": round(km_driven, 1),
        "co2_saved_kg": round(co2_saved_kg, 1),
        "trees_equivalent": round(co2_saved_kg / 21, 1),  # 1 tree absorbs ~21kg CO2/year
    }


# ════════════════════════════════════════════════════════════════
# BONUS 4: Anomaly Detection (sudden demand spikes/drops)
# ════════════════════════════════════════════════════════════════
def detect_demand_anomalies(hourly_df, z_threshold=2.5):
    """
    Flags hours where demand deviated significantly from the
    expected pattern for that hour-of-day -- useful for catching
    station outages, special events, or data quality issues.
    """
    hourly_df = hourly_df.copy()
    hourly_stats = hourly_df.groupby('hour')['energy_kwh'].agg(['mean', 'std']).reset_index()
    hourly_stats.columns = ['hour', 'hour_mean', 'hour_std']

    merged = hourly_df.merge(hourly_stats, on='hour')
    merged['z_score'] = (merged['energy_kwh'] - merged['hour_mean']) / merged['hour_std']
    merged['is_anomaly'] = merged['z_score'].abs() > z_threshold
    merged['anomaly_type'] = np.where(
        merged['is_anomaly'],
        np.where(merged['z_score'] > 0, 'SPIKE', 'DROP'),
        'NORMAL'
    )

    anomalies = merged[merged['is_anomaly']][['datetime', 'energy_kwh', 'hour_mean', 'z_score', 'anomaly_type']]
    return anomalies.sort_values('z_score', key=abs, ascending=False)


# ════════════════════════════════════════════════════════════════
# DEMO — Run all bonus features on the project data
# ════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print("BONUS FEATURE 1: Weather Alert System")
    print("=" * 60)
    alert = weather_demand_alert(temperature=-3, precipitation=8, wind_speed=40)
    print(f"Risk Level: {alert['risk_level']} (score: {alert['risk_score']})")
    for r in alert['reasons']:
        print(f"  - {r}")

    print("\n" + "=" * 60)
    print("BONUS FEATURE 2: Load Balancing Recommendation")
    print("=" * 60)
    sample_demands = {
        "STATION_1": 78.5, "STATION_2": 15.2, "STATION_3": 45.1,
        "STATION_4": 92.3, "STATION_5": 22.8
    }
    lb = recommend_load_balancing(sample_demands, total_capacity=400)
    print(lb.to_string(index=False))

    print("\n" + "=" * 60)
    print("BONUS FEATURE 3: Carbon Offset Calculator")
    print("=" * 60)
    carbon = calculate_carbon_offset(total_kwh_charged=8500)
    for k, v in carbon.items():
        print(f"  {k}: {v}")

    print("\n" + "=" * 60)
    print("BONUS FEATURE 4: Anomaly Detection")
    print("=" * 60)
    hourly = pd.read_csv('/home/claude/ev_project/Hourly_Demand_Full.csv', parse_dates=['datetime'])
    anomalies = detect_demand_anomalies(hourly)
    print(f"Found {len(anomalies)} anomalies out of {len(hourly)} hours")
    print(anomalies.head(10).to_string(index=False))

    # Save anomalies to CSV
    anomalies.to_csv('/home/claude/ev_project/Demand_Anomalies.csv', index=False)
    print("\n✅ Demand_Anomalies.csv saved")
