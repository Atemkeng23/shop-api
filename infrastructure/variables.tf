# Nom du groupe de ressources
variable "resource_group_name" {
  default = "shop-app-rg"
  description = "Nom du groupe de ressources"
}

# Localisation Azure
variable "location" {
  default = "West Europe"
  description = "Région Azure"
}

# Nom du plan App Service
variable "app_service_plan_name" {
  default = "shop-app-plan"
  description = "Nom du plan App Service"
}

# Nom de l'App Service
variable "app_service_name" {
  default = "shop-app"
  description = "Nom de l'application App Service"
}

# Variables pour le serveur SQL
variable "sql_server_name" {
  default = "shop-sql-server"
  description = "Nom du serveur SQL"
}

variable "sql_admin_username" {
  default = "adminuser"
  description = "Nom de l'administrateur SQL"
}

variable "sql_admin_password" {
  default = "P@ssword123!"
  description = "Mot de passe de l'administrateur SQL"
}

variable "sql_database_name" {
  default = "shop-database"
  description = "Nom de la base de données SQL"
}
