from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://alifvianmarco:alifvianmaro@localhost:5432/irisdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
base = declarative_base()

print("CONNECTED INTO DB")

# if __name__ == '__main__':
#     # import pdb;pdb.set_trace()
#     get_db()