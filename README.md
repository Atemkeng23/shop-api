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

---

## **Prérequis**

### **Environnement local**
- Python 3.11
- Docker
- Terraform
- Postman ou cURL pour tester les endpoints.

### **Configuration de l'environnement virtuel**
Créez un environnement virtuel et installez les dépendances :
```bash
python -m venv .venv
source .venv/bin/activate # Sur Linux/Mac
.venv\Scripts\activate   # Sur Windows
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

### **GET /api/v1/produits/**
- Description : Récupérer la liste des produits.
- Réponse :
  ```json
  [
      {"id": 1, "name": "Produit A", "price": 10.5},
      {"id": 2, "name": "Produit B", "price": 20.0}
  ]
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
  ```
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

---

## **Docker**

### **Construction de l'image Docker**
```bash
docker build -t shop-app:latest .
```

### **Exécution du conteneur Docker**
```bash
docker run -p 8000:8000 shop-app:latest
```

### **Push vers Azure Container Registry**
```bash
docker tag shop-app:latest shopapi.azurecr.io/shop-app:latest
docker push shopapi.azurecr.io/shop-app:latest
```

---

## **Pipeline CI/CD**

Le pipeline GitHub Actions est configuré pour :
1. Exécuter les tests unitaires.
2. Construire l'image Docker.
3. Pousser l'image vers Azure Container Registry.
4. Déployer l'application sur Azure App Service.

### **Secrets requis**
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`
- `AZURE_TENANT_ID`
- `ACR_USERNAME`
- `ACR_PASSWORD`

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
  location = "East US"
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

## **Améliorations possibles**
- Ajouter une connexion à une base de données (SQLite, PostgreSQL, etc.).
- Implémenter une gestion des utilisateurs avec authentification.
- Ajouter des tests d'intégration.

---

## **Références**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/)
- [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/)
- [Terraform Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)

