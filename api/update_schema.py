from .database import engine, Base
from .models.user import User

# Drop all tables (if you want to start fresh)
Base.metadata.drop_all(bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

print("Database schema updated successfully.")