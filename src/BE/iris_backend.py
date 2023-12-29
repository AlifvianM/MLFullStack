from typing import Union

from fastapi import FastAPI
from model.model import InputData
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://0.0.0.0:8502"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

def check_model():
    model_path = 'model/classifier.pkl'
    with open(model_path, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

@app.post("/predict/")   
async def predict(request: InputData):
    model = check_model()
    data = request.get_json()
    try:
        result = model.predict([
            [
                data["sepal_length"], 
                data["petal_length"],
                data["sepal_width"],
                data["petal_width"]
            ]
        ])[0]

        return {
            "data_test":data,
            "model":str(model),
            "status":"200",
            "result":int(result)
        }
    
    except ValueError as e:
        return {
            "data_test":data,
            "model":str(model),
            "status":"500",
            "description": str(e)
        }
