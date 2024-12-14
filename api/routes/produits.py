from fastapi import APIRouter
from api.models.product import Product

router = APIRouter()

# Exemple de données en mémoire
fake_products = [
    {"id": 1, "name": "Produit A", "price": 10.5},
    {"id": 2, "name": "Produit B", "price": 20.0},
]

@router.get("/")
def get_products():
    return fake_products

@router.post("/")
def create_product(product: Product):
    new_product = product.dict()
    fake_products.append(new_product)
    return {"message": "Produit ajouté avec succès", "product": new_product}
