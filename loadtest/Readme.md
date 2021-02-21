# Table of Contents

- **[Overview](#Overview)**

## Overview

In this project we will use Azure DevOps to create a disposable test environment to run different automated tests on our application. We will use

- Postman for application test
- Selenium for User Interface test
- Jmeter for Load test

All of the above tests will leverage Azure DevOps platform. We will also use Terraform IAC to create the disposable test environment.

## Terraform

Terraform IAC is used to create the test environment. Code under the terraform modules will create out disposable test environment.

### Terraform State File Storage Account

We will create the terraform state file storage account using the script below

```bash
az_storage.sh
```

Take a note of the `client_id, client_secret, tenant_id, access_key` this will be needed for the terraform script to keep the terraform state file.

![Screenshot of Terraform Storage](screenshots/Terraform_Storage.JPG)

### Terraform create Test Environment

Terraform test environment will be created during different stages of the Pipeline.

- Build stage of the pipeline will do the Terraform Init and Plan operation
- Provision_Terraform_Resources stage of the pipeline will actually do the terraform apply which will provision our test Infrastructure.
- All sensitive variables will be passed as a Pipeline secret variable. 

![Screenshot of Terraform Init](screenshots/Terraform_Init.JPG)

![Screenshot of Terraform Plan](screenshots/Terraform_Plan.JPG)

![Screenshot of Terraform Apply](screenshots/Terraform_Apply.JPG)

![Screenshot of Terraform Infra](screenshots/Terraform_Infra.JPG)