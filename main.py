import pandas as pd
import numpy as np
import streamlit as st
import pickle
from sklearn import *

# Importing data
df = pickle.load(open('df.pkl', 'rb'))
model = pickle.load(open('xgbr.pkl', 'rb'))

# Title & Header
st.title('Calories Prediction')
st.header('Enter details to predict the calories you burnt')

# Selecting input components
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.slider('Age', 10, 80, 25)
height = st.slider('Height (cm)', 120, 220, 170)
weight = st.slider('Weight (kg)', 30, 150, 70)
duration = st.slider('Workout Duration (minutes)', 1, 120, 30)
heartrate = st.slider('Heart Rate', 40, 200, 100)
body_temp = st.number_input('Body Temperature (°C)', min_value=30.0, max_value=45.0, value=37.0)

# Predict Button
if st.button("Predict the calories"):

    # Encode Gender
    gender_value = 1 if gender == 'Male' else 0

    # Prepare input data
    input_data = pd.DataFrame([[
        gender_value, age, height, weight, duration, heartrate, body_temp
    ]], columns=[
        'Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'
    ])

    # Prediction
    prediction = model.predict(input_data)[0]

    # Output
    st.success(f'Predicted Burnt Calories: {prediction:.2f}')



