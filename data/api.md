[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


# api


The objective is to build an API that can return data from a NoSQL database.


## notes from the 554 walkthrough

This narrative follows the [MSE554 course activity](https://cloudbank-project.github.io/az-serverless-tutorial/) 
built as proof of concept on Azure. 

- Start up and configure a VM on the Azure cloud as a base of operations
- Create a NoSQL database, again on Azure, and publish the periodic table of elements to it
    - The Azure brand name for a NoSQL database is "Cosmos DB"
- Create a serverless function (on Azure called a 'Function App') that incorporates an API
    - In this case the API is written in Python
    - It connects to and uses the NoSQL database
 

The first major success milestone is when I can interrogate the periodic table for information 
on Sodium. 


Two things I want to pay attention to are debugging methods and calling out "under the hood"
functionality. The idea is to broaden understanding beyond "copy and paste this magic command"
approach to building a cloud data system.


This walkthrough makes extensive use of two **environments** used in combination. The first is 
a low-power, low-cost on-demand virtual machine (VM) on the Azure cloud. The second is an application
called **VSCode**, a popular free IDE available from Microsoft. Both the VM and VSCode 
integrate well with the Azure cloud. 


## Skip for now: VM

## Skip for now: Build the NoSQL Database

## Build the Azure Function App

- skip for now: multiple steps leading up to `Hey Galaxy` test code
- skip for now: In the interest of whatabout: Can we use a `conda` environment?

> Note: Whilst starting up the `bash` shell the file `.bashrc` is executed. It
> does some configuration; and as it runs it checks
> in turn for a file called `.bash_aliases`. If *that* file exists: `.bashrc` will
> runs it as a subsidiary script. We can put two useful items in this file so we
> do not have to remember *magic commands*. The first item is an alias for "change to
> the `db-api` folder and start up the working Python environment `app-env`".
> The second item is a print statement (using the `echo` command) that *reminds*
> us of this alias. For example the following code can go anywhere in `.bash_aliases`:


```
echo aliased fnappenv to relocate and activate the API dev environment
alias fnappenv='cd ~/db-api; source app-env/bin/activate; func --version'
```

- skip for now: remarks on Azure Function Core Tools and the utility command `func`
    - Includes `How does the localhost test work?' and the default port 7071 forward.
- Testing the Function App on the VM
    - `func --version` checks to see the Azure Function 
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
    
