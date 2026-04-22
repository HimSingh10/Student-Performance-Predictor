import streamlit as st
from predict import predict_performance

st.set_page_config(page_title="Student Predictor", page_icon="🎓")

st.title("Student Performance Predictor")

st.write("Enter details to predict performance:")
st.markdown("### Model Info")
st.write("Model: Random Forest Regressor")
st.write("R2 Score: ~0.85 (example)")

hours = st.slider("Hours Studied", 0, 12, 5)
sleep = st.slider(" Sleep Hours", 0, 12, 7)
activities = st.selectbox("Extracurricular Activities", ["Yes", "No"])

if st.button("Predict"):
    result = predict_performance(hours, sleep, activities)
    st.success(f"🎯 Predicted Performance: {result:.2f}")