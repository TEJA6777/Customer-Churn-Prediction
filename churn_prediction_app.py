import streamlit as st
import pickle
import pandas as pd

# Load pre-trained models
sc = pickle.load(open('Standard scaler.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Customer Churn Prediction")

# Collecting user inputs
CreditScore = st.text_input("Enter the Credit Score")
Geography = st.selectbox("Select the Geography", ['France', 'Spain', 'Germany'])
Gender = st.selectbox("Select the Gender", ['Male', 'Female'])
Age = st.text_input("Enter the Age")
Tenure = st.text_input("Enter the Tenure")
Balance = st.text_input("Enter the Balance")
NumOfProducts = st.text_input("Enter the Number Of Products")
HasCrCard = st.selectbox("Do they have a Credit Card?", ['Yes', 'No'])
IsActiveMember = st.selectbox("Are they an Active Member?", ['Yes', 'No'])
EstimatedSalary = st.text_input("Enter the Estimated Salary")

if st.button('Predict'):
    # Transform the inputs to match the model's expected format
    try:
        CreditScore = float(CreditScore)
        Age = int(Age)
        Tenure = int(Tenure)
        Balance = float(Balance)
        NumOfProducts = int(NumOfProducts)
        EstimatedSalary = float(EstimatedSalary)
        Geography = {'France': 0, 'Spain': 1, 'Germany': 2}[Geography]
        Gender = {'Male': 1, 'Female': 0}[Gender]
        HasCrCard = 1 if HasCrCard == 'Yes' else 0
        IsActiveMember = 1 if IsActiveMember == 'Yes' else 0

        # Creating a DataFrame for the input features
        input_data = {
            'CreditScore': [CreditScore],
            'Geography': [Geography],
            'Gender': [Gender],
            'Age': [Age],
            'Tenure': [Tenure],
            'Balance': [Balance],
            'NumOfProducts': [NumOfProducts],
            'HasCrCard': [HasCrCard],
            'IsActiveMember': [IsActiveMember],
            'EstimatedSalary': [EstimatedSalary]
        }
        input_df = pd.DataFrame(input_data)

        # Scaling the features
        input_df_scaled = sc.transform(input_df)

        # Predicting with the model
        result = model.predict(input_df_scaled)[0]

        # Displaying the result
        if result == 1:
            st.header("The customer is likely to churn.")
        else:
            st.header("The customer is not likely to churn.")
    except ValueError as e:
        st.error(f"Invalid input: {e}")
