import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load("ml/model.pkl")
scaler = joblib.load("ml/scaler.pkl")

app = FastAPI(title="FinGuard Fraud Detection API")


class Transaction(BaseModel):
    features: list[float]


@app.get("/")
def home():
    return {
        "message": "FinGuard Fraud Detection API is running"
    }


@app.post("/predict")
def predict(transaction: Transaction):

    data = np.array(transaction.features).reshape(1, -1)

    data_scaled = scaler.transform(data)

    probability = model.predict_proba(data_scaled)[0][1]

    if probability < 0.30:
        risk_level = "LOW"
        decision = "APPROVE"

    elif probability < 0.70:
        risk_level = "MEDIUM"
        decision = "REVIEW"

    else:
        risk_level = "HIGH"
        decision = "BLOCK"

    return {
        "fraud_probability": round(float(probability), 4),
        "risk_level": risk_level,
        "decision": decision
    }
 	
