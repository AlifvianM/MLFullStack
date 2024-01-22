from typing import Union

from fastapi import FastAPI, HTTPException, Depends
from model.schemas import IrisData
from fastapi.middleware.cors import CORSMiddleware
from model.database import SessionLocal, Base, engine
from model import models, schemas
from sqlalchemy.orm import Session
import crud

import pickle

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

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

@app.post("/predict/", response_model=schemas.IrisData)   
async def predict(request: IrisData, db:Session = Depends(get_db)):
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
        crud.create_iris(
            db=db, 
            sepal_length = data["sepal_length"],
            petal_length = data["petal_length"],
            sepal_width = data["sepal_width"],
            petal_width = data["petal_width"],
        )
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