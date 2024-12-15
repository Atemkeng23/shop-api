from fastapi.testclient import TestClient
from api.app import app
from api.models.user import User  # Assurez-vous d'importer votre modèle User
from api.database import SessionLocal  # Pour interagir avec la base de données

client = TestClient(app)

# Utilitaire pour nettoyer la base de données
def clear_users():
    db = SessionLocal()
    db.query(User).delete()  # Efface tous les utilisateurs pour éviter les conflits d'email
    db.commit()
    db.close()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur la Shop App API"}

def test_get_products():
    response = client.get("/api/v1/produits/")
    assert response.status_code == 200

def test_create_product():
    response = client.post(
        "/api/v1/produits/",
        json={
            "name": "Test Product",
            "price": 25.0,
            "description": "Test description",
            "in_stock": True,
        },
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"

def test_register_user():
    clear_users()  # Nettoie la base de données avant d'exécuter le test
    
    response = client.post(
        "/api/v1/users/register",
        json={
            "username": "newuser",
            "email": "user@example.com",  # Changez d'email si nécessaire pour éviter les conflits
            "password": "password123",
        },
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Utilisateur créé avec succès"

def test_login_user():
    # S'assurer qu'un utilisateur existe avant de tester la connexion
    response = client.post(
        "/api/v1/users/login",
        json={
            "username": "newuser",
            "password": "password123",
        },
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Connexion réussie"
