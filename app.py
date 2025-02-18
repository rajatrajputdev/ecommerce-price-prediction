import streamlit as st
from joblib import load
from numpy import array

# Load the trained model
model = load("./resources/business.pkl")

# Streamlit App
st.title("ECommerce Earning Prediction")

st.write("Enter the user details to predict the amount he will spend.")

# Input fields
session_length = st.number_input("Avg. Session Length", min_value=0.0, max_value=50.0, step=0.1)
time_on_app = st.number_input("Time on App", min_value=0.0, max_value=50.0, step=0.1)
time_on_website = st.number_input("Time on Website", min_value=0.0, max_value=50.0, step=0.1)
membership_length = st.number_input("Length of Membership", min_value=0.0, max_value=20.0, step=0.1)

# Predict button
if st.button("Predict"):
    input_features = array([[session_length, time_on_app, time_on_website, membership_length]])
    prediction = model.predict(input_features)[0]
    st.success(f"Predicted Yearly Amount Spent: ${prediction:.2f}")
