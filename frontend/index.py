import streamlit as st
import requests
import numpy as np

st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")

st.title("💳 Credit Card Fraud Detection")

inputs = {}

inputs["Time"] = st.number_input("After how many seconds did the transaction happen from first transaction:", 0, 1000000)
inputs["Amount"] = st.number_input("Transaction Amount ($):", 0, 1000000)

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

st.markdown("""
<style>
st.image("https://imgs.search.brave.com/04uU9w39NIkfP548tZBgj41CtYddh0eq-arJ1uajYL0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAyMS8w/Ny8xMC8xNi8wNC9j/cmVkaXQtY2FyZC02/NDAxNzg2XzY0MC5w/bmc
</style>
""")
