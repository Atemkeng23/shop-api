from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

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
    response = client.post(
        "/api/v1/users/register",
        json={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "password123",
        },
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Utilisateur créé avec succès"

def test_login_user():
    response = client.post(
        "/api/v1/users/login",
        json={
            "username": "newuser",
            "password": "password123",
        },
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Connexion réussie"
