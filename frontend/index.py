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

image_url = "https://imgs.search.brave.com/9mv0tVFTX3z-I5r9adoHbB1k0jHg1VjIFCAkHL33wxY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTE4/MzEyMzgxL3Bob3Rv/L2JhbmstY3JlZGl0/LWNhcmRzLWJsdWUt/YW5kLWdvbGQuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPVVM/THF3dTZ6TllDdWpR/TlNHYWpHUUhEU2VO/OHo5UGhtR1RaYWht/a3JjVk09"

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
