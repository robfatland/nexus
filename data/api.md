[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[data index source](https://github.com/robfatland/nexus/blob/gh-pages/data/index.md)


[uh oh error link](#process-dot-py-may-have-developed-an-incompatiblity)


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


## Skip for now: Set up a VM


## Build the NoSQL Database


This will be called `robs-data-ocean` and it is built on the Azure portal, being careful to check 
**Do not apply** on the "Free Tier Discount". And West US 2 (Moses Lake). Be sure as well to 
**Disable** both aspects of Global Distribution. 


> Not addressed: apt install of `pip` and `venv` was already done for (below, out of sequence)
> the Function App... in this case why no environment creation prior? Nothing about `PATH`.
> I decide to close this VSCode session and start clean... but as I already ran it there is
> nothing to be done in `sudo apt install -y` for `python` and `venv`. Ok... and
> `pip3 install -r requirements.txt` takes some time but is also ok. 

### process.py may have developed an incompatibility


```
(base) azureuser@rob-jan-2025-azure-vm:~/db-populate$ python3 process.py periodic-table.csv
Traceback (most recent call last):
  File "/home/azureuser/db-populate/process.py", line 8, in <module>
    import pandas as pd
  File "/home/azureuser/miniconda3/lib/python3.12/site-packages/pandas/__init__.py", line 22, in <module>
    from pandas.compat import is_numpy_dev as _is_numpy_dev  # pyright: ignore # noqa:F401
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/azureuser/miniconda3/lib/python3.12/site-packages/pandas/compat/__init__.py", line 25, in <module>
    from pandas.compat.numpy import (
  File "/home/azureuser/miniconda3/lib/python3.12/site-packages/pandas/compat/numpy/__init__.py", line 4, in <module>
    from pandas.util.version import Version
  File "/home/azureuser/miniconda3/lib/python3.12/site-packages/pandas/util/__init__.py", line 2, in <module>
    from pandas.util._decorators import (  # noqa:F401
  File "/home/azureuser/miniconda3/lib/python3.12/site-packages/pandas/util/_decorators.py", line 14, in <module>
    from pandas._libs.properties import cache_readonly
  File "/home/azureuser/miniconda3/lib/python3.12/site-packages/pandas/_libs/__init__.py", line 13, in <module>
    from pandas._libs.interval import Interval
  File "pandas/_libs/interval.pyx", line 1, in init pandas._libs.interval
ValueError: numpy.dtype size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject
(base) azureuser@rob-jan-2025-azure-vm:~/db-populate$
```

## Build the Azure Function App

- skip for now: multiple steps leading up to `Hey Galaxy` test code
- skip for now: In the interest of whatabout: Can we use a `conda` environment?


### Picking up where we left off


Suppose we have to step away from the project for a few days... upon return 
we want to pick up where we left off. To facilitate this


- **Start** the VM for example from the portal or console
- Run `VSCode` and use the lower-left button to start an `ssh` session on the VM
- In VSCode: Go to the terminal and view the login text...
    - ...which reminds us of an alias we set up before the hiatus!
    - ...which means ***Do it now!!*** (see below)
- Use the alias to move into the project folder and start the corresponding environment
- Start editing the project code and away we go


#### Setting up the `robotron` alias


I use `robotron` for the alias as slightly eye-catching. The backstory for this alias
business: On starting `bash` the script file `~/.bashrc` is executed as a shell script.
This does some configuration steps including checking for and (if it exists) running
a sub-script file called `.bash_aliases`. *That* is the file to edit. Add these two lines
at the end of the `.bash_aliases` file:

```
echo Use **robotron** to relocate and activate the development environment
alias robotron='cd ~/db-api; source app-env/bin/activate; func --version'
```


To test this:


```
source ~/.bashrc
```

### Skipped tasks/topics


- Remarks on Azure Function Core Tools and the utility command `func`
    - Includes `How does the localhost test work?' and the default port 7071 forward.


### Testing the Function App on the VM

- `func --version` checks to see the Azure Function 
- `func start` starts the VM's version of the API
    - Note that Azure function core tools appropriate (forward) port 7071
        - this allows `https://localhost:7071` to connect to the VM's running service
            - this is not the actual Function App. It is a test environment.
            - Super convenient: We test the API without publishing it to an Azure cloud Function App


### Publish Function App to the Azure cloud 


- ***WARNING***: There is a bump in the road ahead.
    - Publication/test: If something goes wrong: ***Do Not Try To Debug The Problem***
    - Rather: Keep reading further in the instructions.
- Deploying the Function App to Azure
    - We log in to Azure from the Azure VM: `az login`
        - `az login` = {**azure command line interface** = `az`} +  {**action** = `login`}
        - The Azure VM session is authenticated to interact with the azure cloud
    - Publication command is `func azure functionapp publish <project-name>`
    - The publication load time is a bit slow: 5 minutes or so before the prompt returns
        - This is why localhost testing is good
            - Possible because database calls work from localhost
                - Example: `http://localhost:7071/api/lookup?name=Sodium` works
                - This is possible for two reasons:
                    - Port 7071 forwards from our laptop to the Azure VM
                    - The code running on the Azure VM includes credentials to access the NoSQL Periodic table database


### On database query mechanics and risk


- Code published to Azure is never visible to the outside world
- The code on the VM contains authentication information
    - specifically `ACCOUNT_HOST` is the database ip address...
    - ...and `ACCOUNT_KEY` is the access key)
    - Suppose I accidentally commit this code to GitHub: I have created a huge security hole.
 

### Azure function app **routes**


- The syntax for the api has two components built into the URL
    - A route which corresponds to a particular api "command": `https://some.azurewebsites.net/api/someroute`
    - A sequence of zero or more `key=value` arguments: above + `?key1=value1&key2=value2` etcetera
- What comes back when the code successfully parses an api call is formatted text that we unpack


### What happens during deployment from the VM to the Function App on Azure?


- Most-to-all of the `db-api` folder is uploaded to Azure...
    - ...into a Container perhaps?
    - Volume seems to be 50MB
    - Slow (5 minutes) process is presume because `python3 -m pip install -r requirements.txt` runs during this deployment


## client code


In general we do not build an API in order to manually type API calls into a browser address bar. 
Rather we write code to make the API calls and parse the returned results. In Python the `requests` 
library is useful to this end, particularly `requests.get(url)`. The return value can be cast as
`json` format, in fact a list containing one dictionary. From the dictionary we have the attributes
of the named element. 


The following example client looks up electronegativity for 10 elements. The idea will be to make use 
of the existing `lookup` route provided by the API. The client code pulls out the resulting value; or
reports if there is no such value. This code also illustrates a simple timing mechanism that will 
indicate that most of the run time is spent waiting for the API call to return. Note that the 
client does not have any insight into the breakdown of this latency on the server side, for example
whether the delay is in the internet or in the database lookup.


```
import requests
import time

tt = time.time(); sum_ti = sum_tp = 0.

url = 'https://pythonbytes.azurewebsites.net/api/lookup'
elements = ['Fluorine', 'Sodium', 'Oxygen', 'Hydrogen', 'Carbon', 'Chlorine', 'Potassium', 'Calcium', 'Magnesium', 'Argon']
attribute = "Electronegativity"
print(attribute + ": ")
for e in elements:
    ti0 = time.time()
    d = requests.get(url + '?name=' + e).json()[0]
    ti1 = time.time()

    if attribute in d: print(e + ": " + str(d[attribute]))
    else:              print(e + " does not have a specified " + attribute)
    
    ti2 = time.time()

    sum_ti += ti1 - ti0
    sum_tp += ti2 - ti1
    
tt = time.time() - tt

print('\nFraction of time spent on requests.get():', round(sum_ti/tt, 3))
print('                       on print():',          round(sum_tp/tt))
```


Here is an alternative Python `requests.get()` call passing the key-value information in the request body
as dictionary `params`:


```
response = requests.get("https://pythonbytes.azurewebsites.net/api/lookup/", params={"name": "Sodium"})
```
