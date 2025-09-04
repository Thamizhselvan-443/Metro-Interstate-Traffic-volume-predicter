from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
app = FastAPI(title="Traffic Volume Prediction API")
try:
    model_pipeline = joblib.load('traffic_model_pipeline.joblib')
    print("Model pipeline loaded successfully.")
except FileNotFoundError:
    print("Error: Model file 'traffic_model_pipeline.joblib' not found.")
    print("Please run the Jupyter Notebook first to train and save the model.")
    model_pipeline = None


class TrafficData(BaseModel):
    holiday: str = 'None'
    temp: float = 288.28
    rain_1h: float = 0.0
    snow_1h: float = 0.0
    clouds_all: int = 40
    weather_main: str = 'Clouds'
    hour: int = 9
    day_of_week: int = 1
    month: int = 10
    is_rush_hour: int = 1

    class Config:
        schema_extra = {
            "example": {
                "holiday": "None",
                "temp": 295.15,
                "rain_1h": 0.0,
                "snow_1h": 0.0,
                "clouds_all": 75,
                "weather_main": "Clouds",
                "hour": 17,
                "day_of_week": 0,
                "month": 6,
                "is_rush_hour": 1
            }
        }


@app.get("/")
def read_root():
    """A simple endpoint to check if the API is running."""
    return {"message": "Welcome to the Traffic Prediction API. Go to /docs for details."}


@app.post("/predict")
def predict_traffic_volume(data: TrafficData):
    """
    Endpoint to predict traffic volume based on input features.
    """
    if not model_pipeline:
         return {"error": "Model not loaded. Please check API server logs."}
    input_df = pd.DataFrame([data.model_dump()])
    try:
        prediction = model_pipeline.predict(input_df)
        predicted_volume = int(prediction[0])
        return {"predicted_traffic_volume": predicted_volume}
    except Exception as e:
        return {"error": f"An error occurred during prediction: {e}"}