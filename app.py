from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model from local pickle file
model = joblib.load("model.pkl")

# Define FastAPI app
app = FastAPI(title="ML Model API with FastAPI")

# Define request schema
class InputData(BaseModel):
    area: float

# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([[data.area]])[0]
    return {"prediction": float(prediction)}
