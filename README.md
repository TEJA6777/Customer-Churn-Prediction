# 🔍 Customer Churn Prediction with Streamlit Web App

This project uses machine learning to predict whether a customer will churn (leave) or not. It includes a **user-friendly Streamlit web application** where you can enter customer details and get real-time predictions.

---

## 🎯 Objective

Identify customers who are likely to churn using predictive analytics so that businesses can take proactive steps to retain them.

---

## 🧾 General Description

Customer churn is one of the most critical problems for subscription-based businesses and service industries. This project addresses churn prediction using historical customer data.

We trained multiple machine learning models, evaluated them, selected the best-performing one, and built an interactive web application for real-time predictions. The app enables business users to easily identify high-risk customers without any technical expertise.

---

## 🔄 Project Workflow

```mermaid
graph TD;
    A[Data Collection] --> B[Data Preprocessing];
    B --> C[Model Training & Evaluation];
    C --> D[Model Selection];
    D --> E[Streamlit App Development];
    E --> F[Deployment];


## 🖼️ Web App Interface

### 📥 Input Fields

Users provide the following customer attributes:

| Feature             | Description                                  |
|---------------------|----------------------------------------------|
| Credit Score        | Numeric score indicating creditworthiness    |
| Geography           | Country (France, Spain, Germany)             |
| Gender              | Male / Female                                |
| Age                 | Age of the customer                          |
| Tenure              | Number of years as a customer                |
| Balance             | Current bank balance                         |
| Num of Products     | Products the customer is subscribed to       |
| Has Credit Card     | Whether customer has a credit card           |
| Active Member       | Whether customer is actively engaged         |
| Estimated Salary    | Customer’s annual salary                     |

<img src="images/form_inputs.png" width="700"/>
<sub>🧾 *Form interface where users enter customer details.*</sub>

---

### 🔄 Output: Prediction Result

Based on the provided data, the model returns:

#### ✅ Not Likely to Churn
<img src="images/not_churn.png" width="700"/>
<sub>Green output when customer is predicted to stay.</sub>

#### ⚠️ Likely to Churn
<img src="images/likely_churn.png" width="700"/>
<sub>Red output when customer is predicted to churn.</sub>

---

## 🧠 Models & Accuracy

We tested 10 algorithms — top performers:

| Model          | Accuracy | Precision | Recall | F1 Score |
|----------------|----------|-----------|--------|----------|
| GBDT           | 0.8625   | 0.7588    | 0.4402 | 0.5572   |
| XGBoost        | 0.8625   | 0.7783    | 0.4198 | 0.5455   |
| Random Forest  | 0.8620   | 0.7407    | 0.4580 | 0.5660   |

---

## 💻 Run It Locally

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction

pip install -r requirements.txt

streamlit run churn_prediction_app.py
