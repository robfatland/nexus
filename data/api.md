[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


# api


The objective is to build an API that can return data from a NoSQL database.


## notes from the 554 walkthrough

This narrative follows the [MSE554 course activity]() which was built as a proof of concept on Azure. 
The first step is to set up a NoSQL database on the Azure service "Cosmos DB" that is populated with 
a table, namely the periodic table of elements. The second step is to build and test a very simple 
working Azure function app. This is a serverless function that will be deployed on the Azure cloud
where it will quietly listen for API calls from now until the end of time. 


Once this is done the third step is to connect the database table to the function app so that someone 
can interrogate the periodic table for information on Manganese. 


This walkthrough makes extensive use of two collateral tools working together. The first is a fairly
low-power on-demand VM on the Azure cloud. The second is the VSCode application, a popular (for good
reason) IDE. As both the VM and the VSCode application are built by Microsoft it is no shock to learn
that they integrate well with Azure. 

- various things happen that I'm skipping for now
- we reach the point of testing the Function App on the VM
    - `func --version`
    - `fund start` starts the VM's version of the API
        - Note that Azure function core tools appropriate (forward) port 7071
        - this allows `https://localhost:7071` to connect to the VM's running service
            - this is not the actual Function App. It is a test environment.
            - Super convenient: We test the API without publishing it to an Azure cloud Function App
- we reach the point of deploying the Function App to Azure
    - We log in to Azure from the Azure VM (incongruous but there it is)
        - `az login` parses as **azure command line interface** = `az` followed by **action** = `login`
    - This output is surprising for two reasons
 
```
prompt$ func azure functionapp publish myfunction

Local python version '3.12.8' is different from the version expected for your deployed Function App.
This may result in 'ModuleNotFound' errors in Azure Functions. Please create a Python Function App
for version 3.12 or change the virtual environment on your local machine to match '3.11'.
Getting site publishing info...
[2025-02-01T02:24:36.122Z] Starting the function app deployment...
[2025-02-01T02:24:36.131Z] Creating archive for current directory...
Performing remote build for functions project.
Uploading 45.67 MB
```
    
