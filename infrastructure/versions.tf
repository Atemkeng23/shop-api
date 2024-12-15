terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"  # Assure-toi d'utiliser une version compatible
    }
  }

  required_version = ">= 1.0.0"
}
