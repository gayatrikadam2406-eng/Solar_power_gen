import streamlit as st
import pandas as pd
import joblib

st.title("Solar Power Prediction")

# Debug: Show current directory
st.write("Current Directory:", os.getcwd())
st.write("Files in Directory:", os.listdir())

# Load model safely
try:
    model = joblib.load("solar_model.pkl")
    encoder = joblib.load("label_encoder.pkl")
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# Inputs
temperature = st.number_input("Average Temperature (Day)", -10.0, 50.0)
wind_speed = st.number_input("Average Wind Speed (Day)", 0.0, 50.0)
sky_cover = st.number_input("Sky Cover", 0, 10)
distance_noon = st.number_input("Distance to Solar Noon", 0.0, 1.0)

# Safe selectbox
if "Is Daylight" in encoder:
    is_daylight = st.selectbox("Is Daylight", encoder["Is Daylight"].classes_)
else:
    is_daylight = st.selectbox("Is Daylight", ["Yes", "No"])

df = pd.DataFrame({
    "Average Temperature (Day)": [temperature],
    "Average Wind Speed (Day)": [wind_speed],
    "Sky Cover": [sky_cover],
    "Distance to Solar Noon": [distance_noon],
    "Is Daylight": [is_daylight]
})

if st.button("Predict"):

    try:
        for col in encoder.keys():
            if col in df.columns:
                df[col] = encoder[col].transform(df[col])

        prediction = model.predict(df)

        st.success(f"Predicted Power Generated: {round(prediction[0], 2)}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
