import streamlit as st
#import pickle
import joblib
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        #data = pickle.load(file)
        data = joblib.load(file)
        return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States of America",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "India",
        "Canada",
        "France",
        "Brazil",
        "Spain",
        "Netherlands",
        "Australia",
        "Italy",
        "Poland",
        "Sweden",
        "Russian Federation",
        "Switzerland",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )
