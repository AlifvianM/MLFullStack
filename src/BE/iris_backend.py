from typing import Union

from fastapi import FastAPI, HTTPException, Depends
from model.schemas import IrisData
from fastapi.middleware.cors import CORSMiddleware
from model.database import SessionLocal, Base, engine
from model import models
from model.models import Iris
from sqlalchemy.orm import Session
# import crud

import pickle

models.Base.metadata.create_all(bind=engine)

# docker-compose run api alembic revision --autogenerate -m "init"
# docker-compose exec postgres psql -U alifvianmarco -d irisdb
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
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

@app.post("/predict/", response_model=dict)
async def predict(request: IrisData, db: Session = Depends(get_db)):
    model = check_model()
    print("MODEL CHECKING: OK")

    try:
        # Perform prediction using the model
        result_predict = model.predict([
            [
                request.sepal_length,
                request.petal_length,
                request.sepal_width,
                request.petal_width
            ]
        ])[0]

        print("Result Predict :", result_predict)

        # Create an instance of IrisData for the response
        data = {
            "sepal_length": request.sepal_length,
            "petal_length": request.petal_length,
            "sepal_width": request.sepal_width,
            "petal_width": request.petal_width,
            "species": result_predict.item()
        }
        print("Response Data :", data)

        # Add data to the database
        data_to_db = insert_data(db=db, iris=request, predicted_result=result_predict)

        # Return the data along with other information
        response_data = {
            "data_test": data_to_db,
            "model": str(model),
            "status": "200",
            "result": result_predict.item()
        }

        return response_data
    except ValueError as e:
        # raise HTTPException(status_code=500, detail=str(e))
        return {
            # "data_test":data,
            "model":str(model),
            "status":"500",
            "description": str(e)
        }

def insert_data(db: Session, iris: IrisData, predicted_result: int):
    print("iris =", iris)
    db_iris = Iris(
        sepal_length=iris.sepal_length,
        petal_length=iris.petal_length,
        sepal_width=iris.sepal_width,
        petal_width=iris.petal_width,
        species=predicted_result.item()
    )
    db.add(db_iris)
    db.commit()
    db.refresh(db_iris)
    print("SUCCESS")

    # Convert the Iris instance to a dictionary before returning
    iris_dict = db_iris.__dict__
    iris_dict.pop("_sa_instance_state", None)  # Remove SQLAlchemy state
    return iris_dict

