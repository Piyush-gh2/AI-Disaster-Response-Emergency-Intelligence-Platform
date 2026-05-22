from src.loader import load_data
from src.forecasting import forecast_disaster_risk
from src.risk_engine import detect_emergency_risk
from src.explainable_ai import explain_risk

def run_disaster_ai():

    df = load_data()

    prediction = forecast_disaster_risk(df)

    latest_flood = df["flood_level"].iloc[-1]
    latest_weather = df["weather_severity"].iloc[-1]
    latest_population = df["population_risk"].iloc[-1]

    risk = detect_emergency_risk(
        latest_flood,
        latest_weather,
        latest_population
    )

    explanation = explain_risk(prediction)

    return df, prediction, risk, explanation