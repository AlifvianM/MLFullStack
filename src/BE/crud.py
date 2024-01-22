from sqlalchemy.orm import Session
from model.schemas import IrisData
from model.models import Iris

def create_iris(db: Session, user: IrisData):
    db_iris = Iris(
        sepal_length = user.sepal_length,
        petal_length = user.petal_length,
        sepal_width = user.sepal_width,
        petal_width = user.petal_width,    
    )
    db.add(db_iris)
    db.commit()
    db.refresh(db_iris)
    return db_iris