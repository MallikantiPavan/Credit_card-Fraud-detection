from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pandas as pd
import joblib

app=FastAPI()

model=joblib.load('credit.pkl')
scalar_time=joblib.load('scaler_time.pkl')
scalar_amount=joblib.load('scaler_amount.pkl')
class Credit(BaseModel):
    Time: float
    Amount: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
@app.get("/")
def index():
    return {"message":"Hello world"}

@app.post('/amount_time')
def amount_time(trans:Credit):
    df=pd.DataFrame([trans.dict()])
    df['Time']=scalar_time.transform(df[['Time']]).ravel()
    df['Amount']=scalar_amount.transform(df[['Amount']]).ravel()
    feature_order = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
    df = df[feature_order]
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0]   

    return {
        "prediction": "Fraud" if prediction == 1 else "Not Fraud",
        "probability_fraud": round(probability[1], 4),
        "probability_not_fraud": round(probability[0], 4)
}


