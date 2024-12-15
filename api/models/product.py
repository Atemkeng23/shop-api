# api/models/product.py
from sqlalchemy import Column, Integer, String, Float, Boolean
from api.database import Base
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Modèle SQLAlchemy
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), index=True)  # Limitation de la longueur
    price = Column(Float)
    description = Column(String)  # `VARCHAR(max)` n'est pas problématique ici car pas indexé
    in_stock = Column(Boolean)

# Modèles Pydantic
class ProductBase(BaseModel):
    name: str
    price: float
    description: str
    in_stock: bool

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True  # Permet de convertir les objets SQLAlchemy en Pydantic
