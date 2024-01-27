from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv() #for running locally
# load_dotenv("src/BE/.env") #for running at docker
# "postgresql://your_postgres_user:your_postgres_password@your_postgres_container_name/your_database_name"
# DATABASE_URL = os.environ["POSTGRES_URL"]

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"

print(f"DATABASE_URL = {DATABASE_URL}, type {type(DATABASE_URL)}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()

print("CONNECTED INTO DB")