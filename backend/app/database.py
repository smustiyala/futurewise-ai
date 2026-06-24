from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

# Load environment variables from the .env file.
load_dotenv()

# Retrieve database connection string.
DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine used to communicate with PostgreSQL.
engine = create_engine(DATABASE_URL)

# Create database session factory.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class inherited by all database models.
Base = declarative_base()


def get_db():
    """
    Dependency used by FastAPI endpoints to obtain
    a database session.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()