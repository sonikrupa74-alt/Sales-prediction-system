from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load model and features
model = joblib.load("sales_prediction_model.pkl")
features = joblib.load("sales_features.pkl")


@app.get("/")
def home():
    return {
        "Message": "Sales Prediction API is working successfully"
    }


@app.post("/predict")
def predict(data: dict):

    date = pd.to_datetime(data["Date"])

    quantity = float(data["Quantity"])
    unit_price = float(data["Unit_Price"])
    discount = float(data["Discount_Percent"])
    marketing_spend = float(data["Marketing_Spend"])

    product = data["Product"]
    category = data["Category"]
    region = data["Region"]

    # Date features
    year = date.year
    month = date.month
    day = date.day
    day_of_week = date.dayofweek

    # Create input
    input_df = pd.DataFrame([{
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Discount_Percent": discount,
        "Marketing_Spend": marketing_spend,
        "Year": year,
        "Month": month,
        "Day": day,
        "DayOfWeek": day_of_week,
        "Product": product,
        "Category": category,
        "Region": region
    }])

    # Convert categorical columns
    input_df = pd.get_dummies(
        input_df,
        columns=["Product", "Category", "Region"],
        drop_first=True
    )

    # Match training columns
    input_df = input_df.reindex(
        columns=features,
        fill_value=0
    )

    # Predict
    prediction = model.predict(input_df)

    return {
        "PredictedSales": float(prediction[0])
    }