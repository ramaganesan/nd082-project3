#Store Terraform state in Azure Storage:
#!/usr/bin/env bash

set -e
trap 'catch $? $LINENO' EXIT

catch() {
  echo "catching!"
  if [ "$1" != "0" ]; then
    # error handling goes here
    echo "Error $1 occurred on $2"
  fi
}
echo "Running Script"

RESOURCE_GROUP_NAME=nd082-tstate_rg
STORAGE_ACCOUNT_NAME=nd082tfstorage$RANDOM
CONTAINER_NAME=nd082tfcontainer

# Create resource group
az group create --name $RESOURCE_GROUP_NAME --location eastus

# Create storage account
az storage account create --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --sku Standard_LRS --encryption-services blob

# Get storage account key
ACCOUNT_KEY=$(az storage account keys list --resource-group $RESOURCE_GROUP_NAME --account-name $STORAGE_ACCOUNT_NAME --query '[0].value' -o tsv)

# Create blob container
az storage container create --name $CONTAINER_NAME --account-name $STORAGE_ACCOUNT_NAME --account-key $ACCOUNT_KEY

echo "storage_account_name: $STORAGE_ACCOUNT_NAME"
echo "container_name: $CONTAINER_NAME"
echo "access_key: $ACCOUNT_KEY"