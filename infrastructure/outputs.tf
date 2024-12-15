output "app_service_url" {
  value = azurerm_app_service.example.default_site_hostname
}

output "sql_connection_string" {
  value = "Server=${azurerm_mssql_server.example.fully_qualified_domain_name};Database=${azurerm_mssql_database.example.name};User Id=${var.sql_admin_username};Password=${var.sql_admin_password};"
}
