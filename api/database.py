from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import os
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Détermine si on est en mode test ou production
is_test = os.getenv("ENVIRONMENT") == "test"  # Vous pouvez définir cette variable d'environnement pour les tests

# Paramètres de la base de données SQL Server (production)
password = "P@ssword123!"
encoded_password = quote_plus(password)
SQLALCHEMY_DATABASE_URL = (
    f"mssql+pyodbc://adminuser:{encoded_password}@shop-sql-server-mm5ysr.database.windows.net:1433/shop-database?driver=ODBC+Driver+17+for+SQL+Server"
)

# Paramètres de la base de données SQLite (test)
SQLALCHEMY_DATABASE_URL_TEST = "sqlite:///:memory:"  # SQLite en mémoire pour les tests

# Choisir l'URL de la base de données selon l'environnement
DATABASE_URL = SQLALCHEMY_DATABASE_URL_TEST if is_test else SQLALCHEMY_DATABASE_URL

# Créer l'engine SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if is_test else {})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Fonction pour obtenir la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

