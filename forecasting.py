from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_disaster_risk(df):

    df["t"] = range(1, len(df)+1)

    X = df[["t"]]
    y = df["flood_level"]

    model = LinearRegression()
    model.fit(X, y)

    next_region = np.array([[len(df)+1]])

    prediction = model.predict(next_region)

    return prediction[0]