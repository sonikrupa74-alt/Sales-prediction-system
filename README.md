# 📊 Sales Prediction System

A machine learning web application that predicts product sales based on historical sales data, pricing, quantity, discounts, marketing spend, region, product category, and date-related features.

## 🚀 Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Missing value and duplicate handling
- Date feature engineering
- One-hot encoding for categorical features
- Multiple regression model comparison
- Random Forest hyperparameter tuning
- Overfitting analysis
- Real-time predictions through FastAPI
- Frontend and backend integration
- Deployment using Render

## 🤖 Machine Learning

The following models were evaluated:

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

The Random Forest model was tuned by controlling tree depth and minimum samples required for splitting and leaf nodes to reduce overfitting and improve generalization.

## 🛠️ Tech Stack

**Machine Learning:** Python, Pandas, NumPy, Scikit-learn, XGBoost

**Backend:** FastAPI

**Frontend:** HTML, CSS, JavaScript

**Deployment:** Render

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
