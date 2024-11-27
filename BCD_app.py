import joblib
import streamlit as st
import numpy as np

# Load the trained model
model = joblib.load("c:\\Users\\mjsid\\OneDrive\\Documents\\Python_Programs\\adaboost_model.pkl")

# Streamlit app
st.title('Breast Cancer Diagnosis')

# Feature names for clarity (for user-facing labels)
features = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area',
    'mean smoothness', 'mean compactness', 'mean concavity',
    'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error',
    'smoothness error', 'compactness error', 'concavity error',
    'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area',
    'worst smoothness', 'worst compactness', 'worst concavity',
    'worst concave points', 'worst symmetry', 'worst fractal dimension'
]

# Input fields for features
input_data = []
for feature in features:
    input_data.append(st.number_input(feature, value=0.0, step=0.0001, format="%.8f"))

# Prediction button
if st.button('Predict'):
    # Convert input data to numpy array
    input_array = np.array(input_data).reshape(1, -1)

    # Make predictions
    prediction = model.predict(input_array)

    # Display the prediction
    if prediction[0] == 0:
        st.success("🎉 **Prediction: Benign**", icon="✅")
    else:
        st.error("⚠️ **Prediction: Malignant**", icon="❌")
