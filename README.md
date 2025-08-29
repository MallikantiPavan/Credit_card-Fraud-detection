<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/05a558a9-2fe1-45fe-bc4e-ad3da1955f80" />Credit Card Fraud Detection

🚀 A machine learning-based web application to detect fraudulent credit card transactions using Logistic Regression.
The dataset used is from the Kaggle Credit Card Fraud Detection dataset
.

🌐 Live Demo

FastAPI Backend: https://credit-card-fraud-detection-3-ijmr.onrender.com/

Streamlit Frontend: https://creditcard-fraud-detection-9wtcjqfdrxhvfvnj4xptlz.streamlit.app/

📸 Screenshots




⚙️ Tech Stack

Machine Learning: Logistic Regression (scikit-learn)

Backend: FastAPI

Frontend: Streamlit

Model Serialization: Pickle

Deployment: Render (FastAPI) & Streamlit Cloud

📂 Project Structure
Credit_card-Fraud-detection/
│── backend/
│   ├── main.py                # FastAPI app
│   ├── train.py               # Model training script
│   ├── credit.pkl             # Trained ML model
│   ├── scaler_amount.pkl      # Amount feature scaler
│   ├── scaler_time.pkl        # Time feature scaler
│   ├── requirements.txt       # Backend dependencies
│   └── start.sh               # Deployment script
│
│── frontend/
│   ├── index.py               # Streamlit app
│   └── requirements.txt       # Frontend dependencies
│
└── README.md

⚡ How It Works

User inputs transaction details (time, amount, and features V1–V28).

Data is preprocessed using trained scalers.

Logistic Regression model predicts fraud probability.

Output is displayed in Streamlit frontend and can be queried via FastAPI endpoints.

🚀 Installation & Setup
Backend (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Access at: http://127.0.0.1:8000/docs

Frontend (Streamlit)
cd frontend
pip install -r requirements.txt
streamlit run index.py


Access at: http://localhost:8501

📊 Model Details

Algorithm: Logistic Regression

Evaluation Metric: Accuracy, Precision, Recall, F1-Score

Dataset: Kaggle - Credit Card Fraud Detection

🤝 Contributing

Feel free to fork this repo and submit pull requests.
