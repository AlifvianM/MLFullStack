from typing import Union

from fastapi import FastAPI
from model import InputData
import pickle

app = FastAPI()


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
