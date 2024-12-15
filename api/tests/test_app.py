import os
from fastapi.testclient import TestClient
from api.app import app
from api.models.user import User  # Ensure you import your User model
from api.database import SessionLocal, engine, Base  # Import the database and engine

# Set the environment variable to 'test'
os.environ["ENVIRONMENT"] = "test"

client = TestClient(app)

# Utility to clear the users table
def clear_users():
    db = SessionLocal()
    db.query(User).delete()  # Clear all users to avoid email conflicts
    db.commit()
    db.close()

# Before each test, reset the database
def setup_db():
    Base.metadata.create_all(bind=engine)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur la Shop App API"}