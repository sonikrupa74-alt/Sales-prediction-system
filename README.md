# Sales Prediction System

A Machine Learning based Sales Prediction System that predicts sales using product, category, region, quantity, price, discount, marketing spend, and date features.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- HTML
- CSS
- JavaScript
- Render

## ML Workflow

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- One-Hot Encoding
- Train-Test Split
- Model Comparison
- Random Forest Hyperparameter Tuning

## Models Used

- Linear Regression
- Decision Tree
- Random Forest
- XGBoost
- Tuned Random Forest

### Final Model

**Tuned Random Forest**

- MAE: ₹33,363.97
- RMSE: ₹68,549.66
- R² Score: 0.823

## API

FastAPI is used to serve real-time sales predictions.

### Endpoint

`POST /predict`

### Live Project

Frontend: https://sales-frontend-w8u6.onrender.com

Backend: https://sales-backend-dil3.onrender.com

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
