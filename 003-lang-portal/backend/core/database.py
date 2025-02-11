from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./langportal.db"

# SQL is single threaded, so we need to set check_same_thread to False to allow multiple connections
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# This creates a base class for our models. All models will inherit from this class. Necessary for classes to become tables
Base = declarative_base()

# How we can access the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5️⃣ Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Allows dependency injection in FastAPI
    finally:
        db.close()  # Closes the session after use
