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
    assert len(response.json()) > 0
