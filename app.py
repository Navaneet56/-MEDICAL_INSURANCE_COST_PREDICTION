import streamlit as st
import numpy as np
import pickle

# 1. Page Configuration Setup
st.set_page_config(
    page_title="Medical AI Insurance Valuation Hub",
    page_icon="🩺",
    layout="centered"
)

# 2. Premium Medical Theme
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.95)), 
                          url("https://images.unsplash.com/photo-1576091160550-2173dba999ef?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f8fafc;
    }
    .stNumberInput div div input, .stSelectbox div div select {
        background-color: rgba(30, 41, 59, 0.9) !important;
        color: #06b6d4 !important;
        border: 2px solid #334155 !important;
        border-radius: 8px;
        font-weight: bold;
    }
    label p {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #0891b2 0%, #0369a1 100%);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 14px 20px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 6px 20px rgba(8, 145, 178, 0.3);
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 15px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #06b6d4 0%, #0891b2 100%);
        box-shadow: 0 0 25px #06b6d4;
        color: #0f172a;
    }
    .valuation-box {
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-top: 30px;
        background-color: rgba(30, 41, 59, 0.8);
        border: 2px solid #06b6d4;
        color: #e2e8f0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🩺 Medical Insurance AI Premium Predictor")
st.markdown("### Automated Cost Valuation using Linear Regression")
st.write("Provide the 6 required demographic and biometric parameters below.")
st.markdown("---")

# 3. Load Saved Model Artifact
try:
    with open('medical_insurance.sav', 'rb') as f_model:
        model = pickle.load(f_model)
except FileNotFoundError:
    st.error("🚨 File Loss Error: 'medical_insurance.sav' could not be found.")
    st.stop()

st.markdown("#### Patient Metrics Profile (6 Features)")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (e.g., 19)", min_value=1, max_value=120, value=19, step=1)
    bmi = st.number_input("BMI (Body Mass Index - e.g., 27.90)", min_value=10.0, max_value=60.0, value=27.90, format="%.2f")
    children = st.number_input("Number of Children (e.g., 0)", min_value=0, max_value=10, value=0, step=1)

with col2:
    sex = st.selectbox("Sex", options=["female", "male"])
    smoker = st.selectbox("Is Smoker?", options=["yes", "no"])
    region = st.selectbox("Region", options=["southwest", "southeast", "northwest", "northeast"])

# 4. Prediction Execution
if st.button("CALCULATE PREMIUM ESTIMATE"):
    # Fix mapping variables 
    sex_encoded = 0 if sex == "female" else 1
    smoker_encoded = 0 if smoker == "yes" else 1
    
    region_mapping = {"southwest": 0, "southeast": 1, "northwest": 2, "northeast": 3}
    region_encoded = region_mapping[region]
    
    features = [float(age), float(sex_encoded), float(bmi), float(children), float(smoker_encoded), float(region_encoded)]
    input_array = np.asarray(features).reshape(1, -1)
    
    prediction = model.predict(input_array)
    estimated_cost = prediction[0]
    
    if estimated_cost < 0:
        estimated_cost = 0.0
        
    st.markdown(
        f'<div class="valuation-box">'
        f'📈 ESTIMATED ANNUAL PREMIUM:<br>'
        f'<span style="font-size: 36px; color: #06b6d4;">${estimated_cost:,.2f}</span>'
        f'</div>', 
        unsafe_allow_html=True
    )
