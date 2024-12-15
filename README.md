# Shop App API

Bienvenue dans le projet **Shop App API**, une API RESTful développée en Python avec **FastAPI**. Ce projet vise à fournir une solution de gestion des produits pour une boutique en ligne. L'application inclut des fonctionnalités de base telles que l'affichage et la création de produits, et est déployable via un pipeline CI/CD sur Azure.

---

## **Fonctionnalités principales**
- **Récupérer la liste des produits** : Endpoint GET pour afficher tous les produits.
- **Ajouter un produit** : Endpoint POST pour créer un nouveau produit.
- **Tests unitaires** : Validation des routes principales avec Pytest.
- **Pipeline CI/CD** : Automatisation des tests, de la construction et du déploiement sur Azure.
- **Provisionnement d'infrastructure** : Création et gestion des ressources Azure via Terraform.

---

## **Technologies utilisées**
- **Langage** : Python 3.11
- **Framework** : FastAPI
- **Serveur** : Uvicorn
- **Déploiement** : Docker, Azure App Service
- **Infrastructure** : Terraform
- **Tests** : Pytest
- **Database** : Sql Alchemy

---

## **Prérequis**

### **Environnement local**
- Python 3.11
- Docker
- Terraform
- Database sql
- Postman ou cURL pour tester les endpoints.

### **Configuration de l'environnement virtuel**
Créez un environnement virtuel et installez les dépendances :
```bash
python -m venv .venv
source .venv/bin/activate # Sur Linux/Mac
.venv\Scripts\activate   # Sur Windows
pip install -r requirements.txt
```

## **Installation des dependances**
```bash
pip install -r requirements.txt
```

### **Fichiers importants**
- **`api/app.py`** : Point d'entrée principal de l'application.
- **`api/routes/produits.py`** : Routes pour la gestion des produits.
- **`api/models/product.py`** : Modèles de données pour les produits.
- **`tests/test_app.py`** : Tests unitaires.
- **`infrastructure/`** : Contient les fichiers Terraform pour provisionner les ressources Azure.

---

## **Démarrage de l'application**
Pour exécuter l'application localement :
```bash
uvicorn api.app:app --reload
```
- Application accessible sur : `http://127.0.0.1:8000`
- Documentation automatique : `http://127.0.0.1:8000/docs`

---

## **Endpoints**

### **GET /**
- Description : Endpoint par défaut.
- Réponse :
  ```json
  {
      "message": "Bienvenue sur la Shop App API"
  }
  ```

### **POST /api/v1/users/register**
- Description : Enregistrer un nouvel utilisateur.
- Corps de la requête :
  ```json
{
    "email": "user@example.com",
    "password": "password123"
}
  ```
- Réponse :
  ```json
{
    "message": "Utilisateur enregistré avec succès",
    "user": {
        "email": "user@example.com"
    }
}
  ```

### **POST /api/v1/users/login**
- Description : Connecter un utilisateur et obtenir un token JWT.
- Corps de la requête :
  ```json
{
    "email": "user@example.com",
    "password": "password123"
}
  ```
- Réponse :
  ```json
{
    "message": "Connexion réussie",
    "token": "jwt-token"
}
  ```

---

### **GET /api/v1/produits/**
- Description : Récupérer la liste des produits.
- Réponse :
  ```json
  [
      {"id": 1, "name": "Produit A", "price": 10.5},
      {"id": 2, "name": "Produit B", "price": 20.0}
  ]
  ```

### **GET /api/v1/produits/{id}**
- Description : Récupérer les informations d'un produit spécifique.
- Réponse :
  ```json
{
    "id": 1,
    "name": "Produit A",
    "description": "Description du produit A",
    "price": 10.5
}
  ```

### **POST /api/v1/produits/**
- Description : Ajouter un nouveau produit.
- Corps de la requête :
```json
{
    "name": "Produit C",
    "price": 30.0,
    "description": "Produit de test",
    "in_stock": true
}
- Réponse :
```json
{
    "message": "Produit ajouté avec succès",
    "product": {
        "name": "Produit C",
        "price": 30.0,
        "description": "Produit de test",
        "in_stock": true
    }
}
  ```

### **PUT /api/v1/produits/{id}**
- Description : Mettre à jour un produit existant.
- Corps de la requête :
```json
{
    "name": "Produit C modifié",
    "price": 35.0,
    "description": "Nouvelle description du produit",
    "in_stock": false
}
- Réponse :
```json
{
    "message": "Produit mis à jour avec succès",
    "product": {
        "name": "Produit C modifié",
        "price": 35.0,
        "description": "Nouvelle description du produit",
        "in_stock": false
    }
}
```

### **DELETE /api/v1/produits/{id}**
- Description : Supprimer un produit existant.
- Réponse :
```json
{
    "message": "Produit supprimé avec succès"
}
```

---

## **Tests unitaires**
Pour exécuter les tests unitaires :
```bash
pytest
```
- Exemple de résultat attendu :
  ```
  =========================== test session starts ===========================
  platform win32 -- Python 3.11.9, pytest-7.4.2
  collected 2 items

  tests/test_app.py ..                                                [100%]
  ======================== 2 passed in 1.50s =========================
  ```

# Explications des routes :
- GET / : L'endpoint par défaut retourne un message de bienvenue.
- POST /api/v1/users/register : Permet d'enregistrer un nouvel utilisateur.
- POST /api/v1/users/login : Permet à un utilisateur de se connecter et obtenir un JWT pour les requêtes sécurisées.
- GET /api/v1/produits/ : Retourne la liste de tous les produits.
- GET /api/v1/produits/{id} : Récupère les détails d'un produit spécifique.
- POST /api/v1/produits/ : Ajoute un nouveau produit à la base de données.
- PUT /api/v1/produits/{id} : Met à jour un produit existant.
- DELETE /api/v1/produits/{id} : Supprime un produit de la base de données.
---

## **Docker**

### **Construction de l'image Docker**
```bash
docker build -t shop-api .
```

### **Exécution du conteneur Docker**
```bash
docker run -p 8000:8000 shop-api
```

### **Push vers Azure Container Registry**
```bash
docker tag shop-app:latest shopapi.azurecr.io/shop-app:latest
docker push shopapi.azurecr.io/shop-app:latest
```

---

## **Pipeline CI/CD**

Le pipeline GitHub Actions est configuré pour :

1. Installé les driver OBDC 17 pour SQL server
1. Exécuter les tests via pytest.
2. Construire l'image Docker.
3. Pousser l'image vers Azure Container Registry.
4. Déployer l'application sur Azure App Service.

### **Secrets requis**
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`
- `AZURE_TENANT_ID`
- `ACR_USERNAME`
- `ACR_PASSWORD`

## **DockerFile**

```bash
// filepath: /c:/Users/User/Downloads/shop-app-api/Dockerfile
FROM python:3.11-slim

# Install ODBC libraries and gnupg
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    gnupg \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | tee /etc/apt/sources.list.d/msprod.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql17 \
    mssql-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers
COPY . .

# Exposer le port 8000
EXPOSE 8000

## Lancer l'application
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
```
---

## **Infrastructure avec Terraform**

### **Structure des fichiers Terraform**
- **`infrastructure/main.tf`** : Décrit les ressources principales, telles que Azure App Service, Azure Container Registry, et le groupe de ressources.
- **`infrastructure/variables.tf`** : Définit les variables utilisées pour paramétrer les ressources.
- **`infrastructure/provider.tf`** : Configure le fournisseur Azure pour Terraform.
- **`infrastructure/outputs.tf`** : Définit les sorties, comme les URL et identifiants des ressources créées.

### **Exemple de `main.tf`**
```hcl
resource "azurerm_resource_group" "shop_app_rg" {
  name     = "shop-app-rg"
  location = "France Central"
}

resource "azurerm_container_registry" "shop_app_acr" {
  name                = "shopappacr"
  resource_group_name = azurerm_resource_group.shop_app_rg.name
  location            = azurerm_resource_group.shop_app_rg.location
  sku                 = "Basic"
}

resource "azurerm_app_service" "shop_app_service" {
  name                = "shop-app-service"
  location            = azurerm_resource_group.shop_app_rg.location
  resource_group_name = azurerm_resource_group.shop_app_rg.name
  app_service_plan_id = azurerm_app_service_plan.shop_app_plan.id

  site_config {
    always_on = true
    linux_fx_version = "DOCKER|shopappacr.azurecr.io/shop-app:latest"
  }
}

resource "azurerm_app_service_plan" "shop_app_plan" {
  name                = "shop-app-plan"
  location            = azurerm_resource_group.shop_app_rg.location
  resource_group_name = azurerm_resource_group.shop_app_rg.name
  sku {
    tier = "Basic"
    size = "B1"
  }
}
```

### **Commandes Terraform**
1. Initialiser Terraform :
   ```bash
   terraform init
   ```

2. Planifier les changements :
   ```bash
   terraform plan
   ```

3. Appliquer les changements :
   ```bash
   terraform apply
   ```

---

## **Déploiement sur Azure**
Une fois les secrets configurés, le pipeline déploiera automatiquement l'application. L'API sera accessible sur l'URL publique de votre Azure App Service.

---

## **Gestio de la base de données**
- Nous avons utilisé un base de donnée Sql Alchemy
  
1. Ajout de la connection sur la base de donnée
    ```bash
   from sqlalchemy import create_engine
   from sqlalchemy.orm import declarative_base, sessionmaker
   from urllib.parse import quote_plus
   import os
   import logging

  logging.basicConfig()
  logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

  # Determine if we are in test or production mode
  is_test = os.getenv("ENVIRONMENT") == "test"  # You can set this environment variable for     tests

  # Database settings for SQL Server (production)
  password = "P@ssword123!"
  encoded_password = quote_plus(password)
  SQLALCHEMY_DATABASE_URL = (
    f"mssql+pyodbc://adminuser:{encoded_password}@shop-sql-server-        api.database.windows.net:1433/shop-database?driver=ODBC+Driver+17+for+SQL+Server"
  )

  # Database settings for SQLite (test)
  SQLALCHEMY_DATABASE_URL_TEST = "sqlite:///:memory:"  # SQLite in-memory for tests

  # Choose the database URL based on the environment
  DATABASE_URL = SQLALCHEMY_DATABASE_URL_TEST if is_test else SQLALCHEMY_DATABASE_URL

  # Create the SQLAlchemy engine
  engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if is_test     else {})

  SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  Base = declarative_base()

  # Function to get the database session
  def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
   ```
2. Implémenter une gestion des utilisateurs avec authentification.
  pour cette implementation nous avons crée un user.py dans les model et ajouter des route pour le login et le registration des User.

- models/user.py
   ```bash
   // filepath: /c:/Users/User/Downloads/shop-app-api/api/models/user.py
  from sqlalchemy import Column, Integer, String
  from api.database import Base

  class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
   ```
- routes/user.py
   ```bash
   // filepath: /c:/Users/User/Downloads/shop-app-api/api/routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api.models.user import User
from pydantic import BaseModel
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}
   ```
  

3. Ajouter des tests d'intégration.
Pour des tests d'intégration nous avons crée un fichier test dans le repertoire tests
  - tests/test_integration.py
   ```bash
     // filepath: /c:/Users/User/Downloads/shop-app-api/api/tests/test_integration.py
from fastapi.testclient import TestClient
from api.app import app
from api.database import Base, engine, SessionLocal
from api.models.user import User
import pytest

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_register_user(setup_database):
    response = client.post("/register", json={"username": "testuser", "email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_login_user(setup_database):
    response = client.post("/login", json={"username": "testuser", "password": "password"})
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"
   ```
---

## **Références**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/)
- [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/)
- [Terraform Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)

