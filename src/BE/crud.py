from sqlalchemy.orm import Session
from BE.model import schemas

from model import models

def create_iris(db: Session, user: schemas.InputData):
    db_iris = models.Iris(
        sepal_length = user.sepal_length,
        petal_length = user.petal_length,
        sepal_width = user.sepal_width,
        petal_width = user.petal_width,    
    )
    db.add(db_iris)
    db.commit()
    db.refresh(db_iris)
    return db_iris