from sqlalchemy.orm import Session
from model.schemas import IrisData
from model.models import Iris

def create_iris(db: Session, iris: IrisData):
    print(f"Iris : {iris}")
    db_iris = Iris(**iris)
    db.add(db_iris)
    db.commit()
    db.refresh(db_iris)
    print("REFRESH SUCCESS")
    return db_iris

def get_iris(db: Session, iris_id: int):
    return db.query(Iris).filter(Iris.id == iris_id).first()

def get_all_iris(db: Session):
    return db.query(Iris).all()