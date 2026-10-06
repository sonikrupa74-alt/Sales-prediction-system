# 📊 Sales Prediction System

A machine learning web application that predicts product sales using historical sales data, pricing, quantity, discounts, marketing spend, region, product category, and date-related features.

## 🚀 Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Missing value and duplicate handling
- Date feature engineering
- One-hot encoding
- Multiple regression model comparison
- Random Forest hyperparameter tuning
- Overfitting analysis
- Real-time predictions using FastAPI
- Frontend and backend integration
- Deployment using Render

## 🤖 Machine Learning

Models evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- Tuned Random Forest Regressor

### 🏆 Final Model

**Tuned Random Forest Regressor**

| Metric | Score |
|---|---:|
| MAE | ₹33,363.97 |
| RMSE | ₹68,549.66 |
| R² Score | 0.823 |

The Random Forest model was tuned to reduce overfitting and improve generalization.

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- HTML
- CSS
- JavaScript
- Joblib
- Render

## 🔄 ML Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
EDA
   ↓
Feature Engineering
   ↓
One-Hot Encoding
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Comparison
   ↓
Hyperparameter Tuning
   ↓
Final Random Forest Model
   ↓
FastAPI
   ↓
Frontend
```

## 🔌 API

### Endpoint

```text
POST /predict
```

### Input

```json
{
  "Date": "2026-10-07",
  "Product": "Laptop",
  "Category": "Electronics",
  "Region": "West",
  "Quantity": 10,
  "Unit_Price": 45000,
  "Discount_Percent": 5,
  "Marketing_Spend": 15000
}
```

### Output

```json
{
  "PredictedSales": 356909.0552048532
}
```

## 🌐 Live Demo

**Frontend:** https://sales-frontend-w8u6.onrender.com

**Backend:** https://sales-backend-dil3.onrender.com

**GitHub:** https://github.com/sonikrupa74-alt/Sales-prediction-system

## 📁 Project Structure

```text
Sales-prediction-system/
│
├── sales_backend/
│   ├── app.py
│   ├── model.ipynb
│   ├── sales_prediction.csv
│   ├── sales_prediction_model.pkl
│   ├── sales_features.pkl
│   └── requirements.txt
│
├── sales_frontend/
│
├── README.md
└── .gitignore
```

## ▶️ Run Locally

```bash
git clone https://github.com/sonikrupa74-alt/Sales-prediction-system.git
cd Sales-prediction-system/sales_backend
pip install -r requirements.txt
uvicorn app:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 🎯 Project Outcome

An end-to-end machine learning system that performs data preprocessing, model training, model evaluation, prediction, API integration, and deployment for real-time sales prediction.
