import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
import os

st.set_page_config(page_title="Heart Risk Analyzer", page_icon="🫀", layout="wide")

# Custom CSS for Black + Red Medical Theme
st.markdown("""
<style>
    body, .stApp {
        background-image: radial-gradient(circle at top left, rgba(115, 33, 184, 0.24), transparent 24%),
                          radial-gradient(circle at bottom right, rgba(73, 0, 112, 0.28), transparent 20%),
                          linear-gradient(135deg, #12032e 0%, #2a0c4a 45%, #160420 100%);
        background-attachment: fixed;
        color: #ffffff;
    }
    .block-container {
        background-color: rgba(18, 7, 36, 0.88);
        border-radius: 24px;
        padding: 2rem 2rem 2.5rem;
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35);
    }
    h1, h2, h3, h4, h5, h6,
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6,
    label,
    .stText,
    .stMarkdown,
    .css-1r6slb0-Label,
    .css-1d391kg,
    .css-1m3r2id,
    .css-1aumxhk {
        color: #ffffff !important;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
    }
    .risk-box {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; margin-bottom: 0.25rem;'>🫀 Heart Risk Analyzer</h1>", unsafe_allow_html=True)

# Load and train model
@st.cache_resource
def load_model():
    df = pd.read_csv('heart.csv')
    
    X = df.drop('target', axis=1)
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=10)
    model.fit(X_train_scaled, y_train)
    
    return model, scaler, X.columns

model, scaler, features = load_model()

# Input Section - Split in 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Patient Details")
    age = st.slider("Age", 20, 80, 45)
    sex = st.selectbox("Gender", ["Male", "Female"])
    sex = 1 if sex == "Male" else 0
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3], help="0:Typical Angina, 1:Atypical, 2:Non-anginal, 3:Asymptomatic")
    trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)

with col2:
    st.subheader("Lab Results")
    chol = st.number_input("Cholesterol", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120?", [0, 1])
    restecg = st.selectbox("Rest ECG", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)

with col3:
    st.subheader("Stress Test")
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression", 0.0, 6.0, 1.0, step=0.1)
    slope = st.selectbox("Slope of Peak Exercise ST", [0, 1, 2])
    ca = st.selectbox("Major Vessels Colored", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

# Prediction
if st.button("🔍 Analyze Heart Risk"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    input_scaled = scaler.transform(input_data)
    
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]
    
    st.markdown("---")
    st.subheader("📊 Result")
    
    if prediction == 1:
        st.markdown(f'<div class="risk-box" style="background-color:#4B0000; color:#FF4B4B;">High Risk Detected<br>Risk Score: {probability*100:.1f}%</div>', unsafe_allow_html=True)
        st.warning("Recommendation: Please consult a cardiologist immediately. Maintain low-sodium diet and regular checkups.")
    else:
        st.markdown(f'<div class="risk-box" style="background-color:#003B00; color:#4BFF4B;">Low Risk<br>Risk Score: {probability*100:.1f}%</div>', unsafe_allow_html=True)
        st.success("Recommendation: Heart looks healthy. Keep exercising and maintain a balanced diet.")
