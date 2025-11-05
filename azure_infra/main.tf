terraform {
	required_providers {
		azurerm = {
			source  = "hashicorp/azurerm"
			version = ">= 3.0.0"
		}

        random = {
            source  = "hashicorp/random"
            version = "3.1.0"
        }
	}
}

provider "azurerm" {
	features {}
}

# =======================================
# Creating a resource group
# =======================================

resource "azurerm_resource_group" "storage"{
	name = "storage"
	location = "East US"
}

# =======================================
# Creating a random name for the storage account
# =======================================

resource "random_id" "account" {
  byte_length = 4
}


# =======================================
# Creating an azure storage account
# =======================================

resource "azurerm_storage_account" "backups" {
	name = "backups${random_id.account.hex}" 
    resource_group_name = azurerm_resource_group.storage.name
	location =  azurerm_resource_group.storage.location
    account_tier = "Standard"
    account_replication_type = "LRS"
    access_tier = "Cool"
}


# =======================================
# Outputs
# =======================================

output "storage_account_name" {
  description = "The name of the Azure Storage Account."
  value       = azurerm_storage_account.backups.name
}


# Sensible output
output "storage_account_primary_access_key" {
  description = "The primary access key for the Azure Storage Account."
  value       = azurerm_storage_account.backups.primary_access_key
  sensitive   = true
}


# Sensible output
output "storage_account_connection_string" {
  description = "The connection string for the Azure Storage Account."
  value       = azurerm_storage_account.backups.primary_connection_string
  sensitive   = true
}