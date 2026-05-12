from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model = pickle.load(open("sales_p.pkl","rb"))
scaler = pickle.load(open("scaler_p.pkl","rb"))

@app.get("/")
def home():
    return {"Message" : "API is working successfully"}

@app.post("/predict")
def predict(data: dict):
    price = float(data['price'])
    stock = float(data['stock'])
    category_Clothing = float(data['category_Clothing'])
    category_Electronics = float(data['category_Electronics'])
    category_Food = float(data['category_Food'])
    category_Furniture = float(data['category_Furniture'])
    category_Sports = float(data['category_Sports'])

    columns = ['price','stock','category_Clothing','category_Electronics','category_Food','category_Furniture','category_Sports']

    input_df = pd.DataFrame([[price,stock,category_Clothing,category_Electronics,category_Food,category_Furniture,category_Sports]], columns=columns)

    input_scaled = scaler.transform(input_df)
    
    result = model.predict(input_scaled)
    return {
        'price' : price,
        'stock': stock,
        'category_Clothing' : category_Clothing,
        'category_Electronics': category_Electronics,
        'category_Food' : category_Food,
        'category_Furniture' : category_Furniture,
        'category_Sports' : category_Sports,
        "PredictedSales" : float(result[0])
    }