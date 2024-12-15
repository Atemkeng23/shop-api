provider "azurerm" {
  features {}
}

# Groupe de ressources
resource "azurerm_resource_group" "example" {
  name     = var.resource_group_name
  location = var.location
}

# Plan App Service (utilisation de azurerm_app_service_plan)
resource "azurerm_app_service_plan" "example" {
  name                = var.app_service_plan_name
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    tier = "Basic"  # Niveau du plan
    size = "B1"     # Taille du plan
  }
}

# App Service (corrige la référence à app_service_plan_id)
resource "azurerm_app_service" "example" {
  name                = "shop-app-${random_string.suffix.result}"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id
}

# Serveur SQL
resource "azurerm_mssql_server" "example" {
  name                         = "shop-sql-server-${random_string.suffix.result}"
  location                     = azurerm_resource_group.example.location
  resource_group_name          = azurerm_resource_group.example.name
  administrator_login          = var.sql_admin_username
  administrator_login_password = var.sql_admin_password
  version                      = "12.0"
}

# Base de données SQL (correctement reliée au serveur SQL)
resource "azurerm_mssql_database" "example" {
  name      = var.sql_database_name
  server_id = azurerm_mssql_server.example.id
  sku_name  = "Basic"
}

# Module : Groupe de ressources (optionnel)
module "resource_group" {
  source   = "./modules/resource_group"
  name     = var.resource_group_name
  location = var.location
}

resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}
