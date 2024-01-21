from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ["POSTGRES_URL"]

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
base = declarative_base()

print("CONNECTED INTO DB")

# if __name__ == '__main__':
#     # import pdb;pdb.set_trace()
#     get_db()