[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


# api


The objective is to build an API that can return data from a NoSQL database.


## notes from the 554 walkthrough

This narrative follows the [MSE554 course activity](https://cloudbank-project.github.io/az-serverless-tutorial/) 
built as proof of concept on Azure. This does not include 
[***Containerization with docker***](https://naclomi.github.io/containers-tutorial/).


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


> On starting `bash` the script file `~/.bashrc` is run as a configuration step.
> As `.bashrc` runs it checks for a file called `.bash_aliases`. If *that* file
> exists: `.bashrc` will run it; so it is a subsidiary script. We can put two
> useful items in this file so as not to have to remember any *magic commands*.
> The first item is an alias for "go to
> the `db-api` folder and start up the working Python environment `app-env`".
> The second item is a print statement (using the `echo` command) that *reminds*
> us of this alias. For example the following code can go anywhere in `.bash_aliases`:


```
echo aliased fnappenv to relocate and activate the API dev environment
alias fnappenv='cd ~/db-api; source app-env/bin/activate; func --version'
```

> To check that it works properly: Re-run `~/.bashrc`:


```
source ~/.bashrc
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
- WARNING: There is a bump in the road ahead.
    - If something goes wrong: ***Do Not Try To Debug The Problem***
    - Rather: Keep reading further in the instructions.
- Deploying the Function App to Azure
    - We log in to Azure from the Azure VM
        - This may seem a bit incongruous but there it is: VMs are not technically *inside* the Azure fence
        - `az login` parses as **azure command line interface** = `az` followed by **action** = `login`
    - The load time is a bit slow: 5 minutes or so
        - Develop and test on localhost is therefore appealing
            - Surprise! Even database calls work from localhost
            - `http://localhost:7071/api/lookup?name=Sodium` returns with `[{"AtomicNumber": 11,` etcetera
        - Database query using `lookup?name=Sodium`
            - The code uploaded to Azure is never visible to the outside world
            - The code should I choose to commit it to a GitHub repo contains a Primary Key
                - This authenticates the Function App to the NoSQL database
                    - The Primary Key seems like a security risk
        - The syntax for multiple routes (api calls) and argument parsing (the `key=value` sequence)
            - api call syntax: `http://abc.net/api/route?name1=value1&name2=value2&name3=value3`
            

            - The corresponding interpretation code is arcane; see below
    - What happens during deployment to Azure?
        - Presume the entirety of `db-api` is uploaded to an Azure *something*. Container?
            - Seems to be 48MB
        - Presume `python3 -m pip install -r requirements.txt` is run during deployment


## api code


We have an excellent working example above. Using the Python `requests.get()` method is another way to access:


```
response = requests.get("https://pythonbytes.azurewebsites.net/api/lookup/", params={"name": "Carbon"})
```
