import streamlit as st
import requests
import numpy as np

st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")

st.title("💳 Credit Card Fraud Detection")

inputs = {}

inputs["Time"] = st.number_input("After how many seconds did the transaction happen from first transaction:", 0, 1000000,1000)
inputs["Amount"] = st.number_input("Transaction Amount ($):", 0, 1000000,10000)

for i in range(1, 29):
    inputs[f"V{i}"] = np.random.uniform(-3, 3)

url = "https://credit-card-fraud-detection-3-ijmr.onrender.com/amount_time"


if st.button("🔍 Predict"):
    response = requests.post(url, json=inputs)
    if response.status_code == 200:
        result = response.json()
        prob_not_fraud = result['probability_not_fraud']
        prob_fraud = result['probability_fraud']

        if prob_not_fraud > prob_fraud:
            
            st.markdown(
                f"""
                <div style='background-color: #2ecc71; padding: 10px; border-radius: 8px; color: white; font-weight: bold;'>
                    ✅ Transaction is likely <u>NOT fraudulent</u><br>
                    Not Fraud Probability: {prob_not_fraud*100:.2f}%
                </div>
                """, unsafe_allow_html=True
            )
        
        else:
            st.markdown(
                f"""
                <div style='background-color: red; padding: 10px; border-radius: 8px; color: black; font-weight: bold;'>
                    ⚠️ Suspicious Transaction Detected<br>
                    Fraud Probability: {prob_fraud*100:.2f}%
                </div>
                """, unsafe_allow_html=True
            )
    else:
        st.error("❌ Error from backend. Please try again.")

image_url = "https://imgs.search.brave.com/lqaTaLamS5uiGiap3NgfAgnEFWflOukYU9_OAEAIkR8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cHJlbWl1bS1waG90/by9iYW5rLXN5c3Rl/bS1jb25jZXB0LXdp/dGgtYmxhY2stZGVi/aXQtY2FyZHMtZGFy/ay1iYWNrZ3JvdW5k/XzY3MDE0Ny0yOTI5/My5qcGc_c2VtdD1h/aXNfaHlicmlkJnc9/NzQwJnE9ODA"

pic = f"""
<style>
.stApp {{
    background-image: url("{image_url}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""
st.markdown(pic, unsafe_allow_html=True)
