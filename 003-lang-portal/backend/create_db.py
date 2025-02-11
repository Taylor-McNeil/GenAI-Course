from backend.core.database import engine, Base  # Import database setup
from backend.models import models


# Create tables in the database
def create_database():
    print("Creating database and tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")


if __name__ == "__main__":
    create_database()