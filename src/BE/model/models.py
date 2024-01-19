from sqlalchemy import String, Boolean, Integer, Column, text, TIMESTAMP, Float
from database import base
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


class Iris(base):
    __tablename__ = "iris"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    sepal_length = Column(Float, nullable=False)
    petal_length = Column(Float, nullable=False)
    sepal_width = Column(Float, nullable=False)
    petal_width = Column(Float, nullable=False)