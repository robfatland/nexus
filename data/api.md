[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[data index source](https://github.com/robfatland/nexus/blob/gh-pages/data/index.md)


# api


The objective is to build an API that can return data from a NoSQL database.


- Version 1: The MSE544 [Periodic table exercise](#the-mse544-periodic-table)
- Version 2: The Cloud Clinic 2 [Ocean Observatory exercise](#ocean-observatory-data)


## The MSE544 periodic table


- CosmosDB instance: `robs-data-ocean`
- Databases
    - `periodic-db`
        - Container: `elements`
    - `oceanography`
        - Container: `osb_profile`
        - Container: `osb_temperature`
        - Container: `osb_salinity`


***For follow-along annotation (Periodic table of elements): Keep reading***


***For the oceanography segment: [Jump down in this document](#oceanography)***


This narrative follows the [MSE544 course activity](https://cloudbank-project.github.io/az-serverless-tutorial/) 
built as proof of concept on Azure. This does not include 
[***Containerization with docker***](https://naclomi.github.io/containers-tutorial/).


- Not annotated yet: Start up and configure a VM on the Azure cloud as a base of operations
- Annotation in process: Create an Azure NoSQL database and publish the periodic table of elements
    - Azure brand name for NoSQL database service is "Cosmos DB"
- Annotated: Create a serverless function (on Azure called a 'Function App') that incorporates an API
    - ...in Python
    - ...connect to, accesses the NoSQL database
 - Not really covered yet: Debugging methods


The first milestone is interrogating the periodic table for information on (say) Sodium
from the Azure portal viewed in a browser tab. The second milestone is making the same
sodium query from a blank browser tab. The browser (via a URL) invokes an episodic burst
of simple activity generically called a "cloud serverless function". The brand name in this
case for Azure is "Azure Function" or equivalently "Azure Function App". 


The third milestone is to interrogate the periodic table from code, specifically using 
a Python program that uses the Python `requests` library. This Python program is an 
API *Client* where the database and Azure Function app together comprise the API (cloud data)
*Server*. At the end of all this we have a completely automated program-to-program data 
access procedure that models everything that happens on the internet. Underlying all of
this is a message passing protocol called `HTTP`. 


Two things to build out in one's comprehension are *debugging methods* and *underlying context*.


A note on process: 
This walkthrough makes extensive use of two virtual **workshops** (to avoid using the word *environment*).
The first workshop is the `bash` shell running on a low-power, low-cost on-demand virtual machine (VM) on the 
Azure cloud. The second workshop is the **VSCode** application, a popular and free IDE available from 
Microsoft. Both the VM and the VSCode workshops integrate well with the Azure cloud. 


## Skipped for now: Set up a VM


## Build the NoSQL Database


This will be called `robs-data-ocean` and it is built on the Azure portal, being careful to check 
**Do not apply** on the "Free Tier Discount". And West US 2 (Moses Lake). Be sure as well to 
**Disable** both aspects of Global Distribution. 


> Not addressed: apt install of `pip` and `venv` was already done for (below, out of sequence)
> the Function App... in this case why no environment creation prior? Nothing about `PATH`.
> I decide to close this VSCode session and start clean... but as I already ran it there is
> nothing to be done in `sudo apt install -y` for `python` and `venv`. Ok... and
> `pip3 install -r requirements.txt` takes some time but is also ok.


Execute the loader Python script: 

```
python3 process.py periodic-table.csv
```

## debugging


While testing the database build steps I ran into an error during `python process.py periodic-table.csv`. 
It appeared to be a library import statement for `pandas`. Three debug procedures:


- copy/paste the error message or fractions thereof in the browser search window
    - Possibly helpful: prepend qualifiers like "Azure" or "Python"
    - This often finds related stack overflow (etc) pages
    - These may or may *not* be helpful; proceed with caution
- Create a simplified version of the program to isolate the error
    - Example: the error message cites a problem at line 12
    - Create a 12-line version of the program and see if this still gives the error
    - In this case there was some sort of arcane library incompatibility...
- Simplify `requirements.txt` and reinstall the environment
    - To get Python library version numbers for installed modules:
        - `pip show numpy` and the much simpler `pip list`
    - To uninstall: `pip uninstall -r requirements.txt`
    - To simplify the listing: `pandas==2.0.3` becomes simply `pandas`, and so on
    - To reinstall: `pip install -r requirements.txt`
    - The `process.py` file was restored to its intended content; and now ran to completion


Working with the continuously evolving collection of Python libraries can be a murky process.
Debugging steps such as described above are simple; and simple is a recommended way to start.


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


 ***Integrate this response***


- Can of worms
    - For a read-only API with data that is not privacy-sensitive (like the periodic table), the main reason to secure it is to prevent someone from using it too much and driving up your bill.
    - The general way to "secure" an API is with a "token" or "key" (synonyms in this context), which is really just an ultra-long randomly generated password.
    - Every user who will be accessing your API gets a token.
    - They go to great effort to not accidentally publish the token to github.
    - The API administrator needs a way of easily disabling any given token, given the above github scenario.
    - They also usually want some way to keep track of the person to whom the token was assigned.
    - The key is provided in every API request, but usually as an HTTP header rather than a URL variable
        - (eg, it's invisibly a part of the request rather than something that appears after the "?" in the request URL)
    - You could hypothetically code the logic to manage and check keys into your python program, but Azure Function Apps has some of that machinery built for you already, and that's what we should be using here.
        - For a few reasons:
            - (1) we don't have to worry about doing it wrong
            - (2) we don't have to do all that engineering work
            - (3) presumably we would get billed for the seconds our python code was checking keys, whereas if we use Azure Function App's built-in key system my assumption is we would not
    - [Here's the documentation on how keys work in Azure Function Apps](https://learn.microsoft.com/en-us/azure/azure-functions/function-keys-how-to?tabs=azure-portal)


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


## oceanography


### Process


- [GeoSmart Jupyter book `oceanography`](https://github.com/geo-smart/oceanography)
    - From this repository the first important source code file is `shallowprofiler.py`
        - Adapting `ReadProfileMetadata()` code: single site, adapting to Oregon slope base, January 2022
        - On the Azure VM we have a db-populate directory with example code `process.py`
            - This was used above to load periodic table rows as dictionaries
        - Copied this code to a new file `process_profiles.py`
            - Modify this file to build a profile metadata loader > the `osb_profiles` container
    - Populate containers `osb_temperature` and `osb_salinity`
 

This code is a simple CSV reader selecting out key metadata for profiler behavior.
The profiler is an instrument pod parked at 200 meters depth that goes through a
controlled ascent/descent to near the surface, nine times per day. Each profile is
marked by four timestamps: Start of rest, start of ascent, start of descent, end of 
descent.


```
# read and format profile metadata: OSB, JAN-2022
import pandas as pd
df = pd.read_csv(sys.argv[1], usecols=["1","2","7","8","13","14","16","17"])
df.columns=['rest start time','rest start depth','ascent start time','ascent start depth',
            'descent start time','descent start depth','descent end time','descent end depth']
df['rest start time'] = pd.to_datetime(df['rest start time'])
df['ascent start time'] = pd.to_datetime(df['ascent start time'])
df['descent start time'] = pd.to_datetime(df['descent start time'])
df['descent end time'] = pd.to_datetime(df['descent end time'])
```



