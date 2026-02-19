# Solar_power_gen
import streamlit as st import pandas as pd import joblib  # Load model model = joblib.load("solar_model.pkl")  st.title("Solar Power Prediction")  st.write("Enter the required details below:")
