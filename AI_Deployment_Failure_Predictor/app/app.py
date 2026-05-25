
import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="AI Deployment Failure Predictor")

st.title("AI Deployment Failure Predictor")

st.write("Predict whether a deployment/build may fail using ML.")

build_duration = st.slider("Build Duration (minutes)", 1, 60, 20)
error_count = st.slider("Error Count", 0, 20, 2)
failed_tests = st.slider("Failed Tests", 0, 15, 1)
cpu_usage = st.slider("CPU Usage (%)", 0, 100, 50)
memory_usage = st.slider("Memory Usage (%)", 0, 100, 50)
previous_status = st.selectbox("Previous Build Status", ["Success", "Failed"])
deployment_frequency = st.slider("Deployments Per Week", 1, 10, 3)

prev = 1 if previous_status == "Failed" else 0

model = joblib.load("../models/deployment_failure_model.pkl")

features = np.array([[
    build_duration,
    error_count,
    failed_tests,
    cpu_usage,
    memory_usage,
    prev,
    deployment_frequency
]])

if st.button("Predict Deployment Risk"):
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("High Risk: Deployment Likely to Fail")
        st.write("Suggestions:")
        st.write("- Reduce failed test cases")
        st.write("- Optimize CPU/memory usage")
        st.write("- Fix dependency issues")
    else:
        st.success("Low Risk: Deployment Likely to Succeed")
