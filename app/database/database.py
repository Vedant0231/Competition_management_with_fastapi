#Create connection for database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

<<<<<<< HEAD
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:vedant@localhost:5432/task1db"
=======
SQLALCHEMY_DATABASE_URL = "postgresql://[DB_USERNAME]:[DB_PASSWORD]@[DB_HOST]/[DB_NAME]"
>>>>>>> dc29a1f8876f5ef91fc1282d94e02fdc8827a3db

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
