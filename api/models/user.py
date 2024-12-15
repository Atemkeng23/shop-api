from sqlalchemy import Column, Integer, String
from api.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)  # Ensure the type is supported for indexing
    email = Column(String(255), unique=True, index=True)  # Change to VARCHAR(255) to ensure it can be indexed
    hashed_password = Column(String)