def detect_emergency_risk(flood, weather, population):

    if flood > 90 and weather > 85:
        return "Critical Emergency Risk"

    elif population > 10000:
        return "High Population Exposure"

    else:
        return "Moderate Disaster Risk"