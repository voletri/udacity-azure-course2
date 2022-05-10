# Overview

<TODO: complete this with an overview of your project>

# Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
* A link to a spreadsheet that includes the original and final project plan>

# Instructions


## Architectural Diagram
![](images/0_architecture.png)

## Project cloned into Azure Cloud Shell
* Go to https://portal.azure.com/#cloudshell/ and run command:
```
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
```
* Add public key to GitHub. (GitHub > Settings > SSH and GPG keys > Paste > Add the key)
* Clone the repository
```
git clone git@github.com:voletri/udacity-azure-course2.git
```
![](images/2_ssh_git_clone.png)

## Passing tests that are displayed after running the `make all` command from the `Makefile`
* Create a virtual environment
```
python3 -m venv ~/.udacity-azure-course2
source ~/.udacity-azure-course2/bin/activate
```
* Run: make all
```
cd udacity-azure-course2
make all
```
![](images/3_make_all.png)
* The following commands can be run in order to then test and start the application:
```
export FLASK_APP=app.py
flask run
```
![](images/4_app_running_locally.png)
## Project running on Azure App Service
* Go to https://portal.azure.com/#cloudshell/
* Run command to create webapp:
```
az webapp up --sku F1 -n udacity-azure-course2
```
* Confirm webapp is created successfully
![](images/1_create_webapp.png)

    Confirm app is up and running
    ```
    https://udacity-azure-course2.azurewebsites.net
    ```
![](images/5_app_running.png)
## Configure GitHub Actions
* GitHub > Actions > set up a workflow yourself
```
name: Python application test with Github Actions

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.7
      uses: actions/setup-python@v1
      with:
        python-version: 3.7
    - name: Install dependencies
      run: |
        make install
    - name: Lint with pylint
      run: |
        make lint
    - name: Test with pytest
      run: |
        make test
```
![](images/6_Github_action.png)
## Configure Azure Pipeline
[Note the official documentation should be referred to and double checked asyou setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelinesecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
(.udacity-azure-course2) tri@Azure:~/udacity-azure-course2$ sh make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


