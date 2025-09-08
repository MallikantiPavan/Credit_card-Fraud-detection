import streamlit as st
import requests

st.title(" Credit Card Fraud Detection ")

inputs = {}


inputs["Time"] = st.number_input(" Time",0,1000)
inputs["Amount"] = st.number_input(" Amount",0,100)


with st.expander("Advanced Features (V1–V28)"):
    cols = st.columns(4)  
    for i in range(1, 29):
        col = cols[(i - 1) % 4]  
        with col:
            inputs[f"V{i}"] = st.number_input(f"V{i}",0,100)

url = "https://credit-card-fraud-detection-3-ijmr.onrender.com/amount_time"


if st.button(" Predict"):
    response = requests.post(url, json=inputs)
    if response.status_code == 200:
        result = response.json()
        
        st.success(f"Not Fraud Probability: {result['probability_not_fraud']*100:.2f}%")
        st.warning(f"fraud_Probability: {result['probability_fraud']*100:.2f}%")
        
    else:
        st.error(" Error from backend")
