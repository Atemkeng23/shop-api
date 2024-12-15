# api/app.py
from fastapi import FastAPI
from api.routes.produits import router as produits_router
from api.routes.users import router as users_router  # Ajoutez cette ligne
from api.database import Base, engine

# Créer les tables dans la base de données
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Shop App API",
    description="API pour gérer les produits de la boutique",
    version="1.0.0",
)

# Inclure les routeurs pour les produits et les utilisateurs
app.include_router(produits_router, prefix="/api/v1/produits", tags=["Produits"])
app.include_router(users_router, prefix="/api/v1/users", tags=["Utilisateurs"])

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur la Shop App API"}
