from fastapi import FastAPI
from api.routes.produits import router as produits_router

app = FastAPI(
    title="Shop App API",
    description="API pour gérer les produits de la boutique",
    version="1.0.0"
)

# Inclure les routes
app.include_router(produits_router, prefix="/api/v1/produits", tags=["Produits"])

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur la Shop App API"}
