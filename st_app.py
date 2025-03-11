import streamlit as st
import pandas as pd
import sys
from pcosdiagnosis.utils.main_utils.utils import load_object
from pcosdiagnosis.utils.ml_utils.model.estimator import NetworkModel

# Load the preprocessor and model
try:
    preprocessor = load_object("final_model/preprocessor.pkl")
    final_model = load_object("final_model/model.pkl")
    network_model = NetworkModel(preprocessor=preprocessor, model=final_model)
except Exception as e:
    st.error(f"Error loading model or preprocessor: {e}")
    sys.exit(1)

# Streamlit app
st.title("PCOS Prediction App")

# Patient name input
patient_name = st.text_input("Enter Patient Name")

# File uploader
uploaded_file = st.file_uploader("Upload the health report (CSV file)", type="csv")

if uploaded_file is not None and patient_name:
    try:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Ensure the DataFrame has only one row
        if len(df) != 1:
            st.error("The CSV file must contain exactly one data point.")
        else:
            # Ensure the input data has the same column names as the training data
            training_columns = preprocessor.named_steps['imputer'].feature_names_in_
            df = df.reindex(columns=training_columns)
            # Preprocess the data
            try:
                processed_data = preprocessor.transform(df)
            except Exception as e:
                st.error(f"Error preprocessing data: {e}")
                sys.exit(1)

            # Make prediction
            try:
                y_pred = network_model.predict(processed_data)
                y_prob = network_model.predict_proba(processed_data)  # Get probability estimates

                # Display the prediction result
                st.write(f"Prediction for {patient_name}:")
                if y_pred[0] == 1:
                    st.write(f"{patient_name}, you have a high likelihood of having PCOS with a probability of {y_prob[0][1]:.2f}.")
                else:
                    st.write(f"{patient_name}, you have a low likelihood of having PCOS with a probability of {y_prob[0][0]:.2f}.")

            except Exception as e:
                st.error(f"Error making prediction: {e}")
                sys.exit(1)

    except Exception as e:
        st.error(f"Error reading CSV file: {e}")

