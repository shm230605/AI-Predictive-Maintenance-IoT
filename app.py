import streamlit as st
import pandas as pd
import joblib
import time

model = joblib.load("models/model.pkl")

st.title("🏭 AI Predictive Maintenance Dashboard")

# LIVE METRICS PANEL
st.subheader("📊 Live Machine Metrics")

temp = st.slider("Temperature", 20, 120, 50)
vib = st.slider("Vibration", 0.0, 5.0, 1.0)
curr = st.slider("Current", 5, 30, 10)

col1, col2, col3 = st.columns(3)

col1.metric("Temperature", temp, "+2°C")
col2.metric("Vibration", vib, "+0.3")
col3.metric("Current", curr, "-0.5")

if st.button("Predict Failure"):
    data = pd.DataFrame([[temp, vib, curr]],
                        columns=["temperature","vibration","current"])

    pred = model.predict(data)[0]

    if pred == 1:
        st.error("⚠ MACHINE FAILURE LIKELY")
    else:
        st.success("✅ MACHINE HEALTHY")

# AUTO REFRESH SIMULATION
st.subheader("🔄 Real-Time Simulation")

placeholder = st.empty()

for i in range(10):
    fake_temp = temp + (i * 0.5)
    fake_vib = vib + (i * 0.1)

    placeholder.write(f"""
    Temperature: {fake_temp}
    Vibration: {fake_vib}
    Status: {"FAILURE" if fake_vib > 2 else "NORMAL"}
    """)

    time.sleep(1)