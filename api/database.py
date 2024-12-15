from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus
import os
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Determine if we are in test or production mode
is_test = os.getenv("ENVIRONMENT") == "test"  # You can set this environment variable for tests

# Database settings for SQL Server (production)
password = "P@ssword123!"
encoded_password = quote_plus(password)
SQLALCHEMY_DATABASE_URL = (
    f"mssql+pyodbc://adminuser:{encoded_password}@shop-sql-server-api.database.windows.net:1433/shop-database?driver=ODBC+Driver+17+for+SQL+Server"
)

# Database settings for SQLite (test)
SQLALCHEMY_DATABASE_URL_TEST = "sqlite:///:memory:"  # SQLite in-memory for tests

# Choose the database URL based on the environment
DATABASE_URL = SQLALCHEMY_DATABASE_URL_TEST if is_test else SQLALCHEMY_DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if is_test else {})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()