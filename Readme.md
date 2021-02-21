# Table of Contents

- **[Overview](#Overview)**
- **[Terraform](#Terraform)**
- **[PostMan for Application Testing](#PostMan-for-Application-Testing)**
- **[Selenium for User Interface Testing](#Selenium-for-User-Interface-Testing)**


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

## PostMan for Application Testing

We will be using PostMan for application testing. The result of the PostMan test will be published as Test Artifact during the Pipeline run. PostMan test is run during the execution of the Build stage of the pipeline

![Screenshot of PostMan Run](screenshots/Postman_Test_1.JPG)

![Screenshot of PostMan Run](screenshots/Postman_Test_2.JPG)

![Screenshot of PostMan Artifact](screenshots/Postman_Test_3.JPG)

The artifact is downloaded from the Azure DevOps and available under the `project-submission-artifacts` folder.

## Selenium for User Interface Testing

Selenium is used to test the User Interface. The Selenium test will be run in the Azure VM created using the Terraform IAC. We included the Azure VM as a test environment resource in our DevOps project and the test will be directly run on this VM. Please see the link below to create an environment
[Creating Environments in Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/deploy-linux-vm?view=azure-devops&tabs=java)

Selenium test will be run during the Deploy stage of the pipeline.

![Azure Environment](screenshots/Test_Environment.JPG)

### Azure Log Analytics

To collect the output of the Selenium test we will be leveraging the Azure Log Analytics service. This service will be configured to collect the application events, in our case the system log output of the Selenium Test run.

![Selenium Log Query](screenshots/Selenium_Logs_1.JPG)

![Selenium Log AgentConfig](screenshots/Selenium_Logs_2.JPG)

![Selenium Log VM](screenshots/Selenium_Logs_3.JPG)

The data output from the test is available as `project-submission-artifacts/query_data.csv`.

## JMeter for Load Testing

JMeter will be used for Load Testing. Load and Endurance testing will be run against the FakeRestAPI in the Load_Test stage of the Pipeline. Load test is run against the Activities Endpoint and Endurance Test is run against the Book Endpoint. The result of the Load Test will also be available as a Test Artifact and will be uploaded to the Test Results.

![JMeter Load Test1](screenshots/Load_Stress_Test_1.JPG)

![JMeter Load Test2](screenshots/Load_Stress_Test_2.JPG)

![JMeter Load Test3](screenshots/Load_Stress_Test_3.JPG)

![JMeter Load Test4](screenshots/Load_Stress_Test_4.JPG)

![JMeter Endurance Test1](screenshots/Load_Endurance_Test_1.JPG)

![JMeter Endurance Test2](screenshots/Load_Endurance_Test_2.JPG)

![JMeter Endurance Test3](screenshots/Load_Endurance_Test_3.JPG)

![JMeter Endurance Test4](screenshots/Load_Endurance_Test_4.JPG)

![JMeter Test](screenshots/Load_Test_Artifact.JPG)

The Load Test results are also available as `project-submission-artifacts/Stress-Test-Report.zip`, `project-submission-artifacts/Endurance-Test-Report.zip`.

### Azure Monitoring

We also monitor the performance of the application during Load test using Azure Monitor. We leverage the Azure App service Monitoring capabilities to generate custom alerts which can notify any infrastructure related issues.

![Azure Alert](screenshots/Azure_Monitor_1.JPG)

![Azure Alert Action](screenshots/Azure_Monitor_2.JPG)

![Azure Alert Email](screenshots/Azure_Monitor_3.JPG)

![Azure Alert Email](screenshots/Azure_Monitor_4.JPG)

![Azure Alert Email](screenshots/Azure_Monitor_5.JPG)