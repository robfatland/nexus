[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[data index source](https://github.com/robfatland/nexus/blob/gh-pages/data/index.md)


# api


The objective is to build an API that can return data from a NoSQL database.


- Version 1: The MSE544 [Periodic table exercise](#the-mse544-periodic-table)
- Version 2: The Cloud Clinic 2 [Ocean Observatory exercise](#ocean-observatory-data)


## The MSE544 periodic table

MSE544 is a data science course taught at the University of Washington by Professor Luna Huang. 
Part of the course covers skills for building research computing infrastructure on the public cloud.


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


### Resuming a paused project


Suppose we have to step away for a few days: From a VM where we are working on 
some project. Some simple advance steps can facilitate smooth resumption: Use
the `.bashrc` and `.bash_aliases` to save configuration aliases and print a
message on how to resume using `echo`. 


- **Start** the VM for example from the portal or console
- Run `VSCode` and `ssh` into this VM
- In VSCode > terminal > read the login message
    - ...this reminds us of configuration aliases we set up before the hiatus
        - For example: activating an environment, moving to the working directory


#### the `robotron` alias


I use the alias `robotron` as it is eye-catching. Some Linux aliases are defined on 
login when the user's `bash` script `~/.bashrc` is automatically run.
This script also checks for and (if it exists) runs a sub-script called `~/.bash_aliases`. 
*That* is a good place to add custom aliases; and `echo` statements that remind us
of those aliases. For example: Add these at the end of `~/.bash_aliases`:

```
echo Use **robotron** to relocate and activate the development environment
alias robotron='cd ~/db-api; source app-env/bin/activate; func --version'
```


Test this:


```
source ~/.bashrc
```


### open task


Need remarks on `Azure Function Core Tools` in relation to the utility command `func`.
Need remarks on `How does the localhost test work?' and the default port 7071 forward.
Need a work-through example of using API keys provided by Azure Function Apps.


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


### database access risk


We consider three aspects of risk:
- The Azure Function App database access credentials become public
- The credentials we install on the development VM become public
- The API itself becomes public



- On the first topic: Code published to Azure (in a Function App) is not visible to the outside world
    - The Function App does have database access credentials 'built in'
    - We can regard these as safe


- On the second topic: The code on the development VM contains two pieces of authentication information
    - `ACCOUNT_HOST` is the database ip address
    - `ACCOUNT_KEY` is the database access key
    - Neither of these should be openly visible to the world
    - Suppose I accidentally commit this code to GitHub: This is a big security hole
        - Be careful to set up `.gitignore` and test it with fake credentials
        - Remember that GitHub retains older versions of code
            - If credentials are compromised: Generate new credentials 


- Thoughts on the API being public
    - The periodic table example is a read-only API and the data is not privacy-sensitive
    - This represents low risk; the there are two reasons to consider securing it
        - A bot could maliciously use the API many times costing you money
        - You may envision future work where privacy *will* be important
        - You may envision future work where the database will continue to accumulate new data
    - The general way to secure an API is with a *token* or synonymously a *key*
        - In practice this is a very long (hundreds of characters) randomly generated password
    - Every approved API User will receive a token
        - They take great care not to publish this token for example to GitHub
    - In the event of an accidental breach of security: The API Administrator needs a means of easily disabling any token
    - This also implies tracking the status of each person to whom a token is assigned
    - The token is passed in every API request as an HTTP header (not as a URL variable)
        - This HTTP *header* comes along invisibly in the HTTP *request*
        - i.e. it does not appear after the "?" in the request URL
    - One *could* code the logic of token management into the Python server-side API program...
        - ...however Azure Function Apps has built-in machinery for this purpose...
        - ...so *that* is what we should use, for several reasons:
            - we do not have to worry about doing it incorrectly
            - we do not have to do the (considerable) engineering work
            - using Azure Function App's built-in key system is very cheap 
    - [Documentation: How keys work in Azure Function Apps](https://learn.microsoft.com/en-us/azure/azure-functions/function-keys-how-to?tabs=azure-portal)


### Azure function app routes


- The syntax for a basic API call has two components built into the URL
    - A route which corresponds to a particular API call
        - `https://myfunctionapp.azurewebsites.net/api/myroute`
    - A sequence of zero or more `key=value` arguments; suppose we are using three:
        - to the above example append `?key1=value1&key2=value2&key3=value3`
- A successful API call returns formatted text that our Client code unpacks


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


This segment of the `nexus api` page concerns the "shoebox problem": A research team has an old 
shoebox full of data tapes from ten years back. They would like to make that data available: For 
themselves, their collaborators and possibly for other research teams. The end result would be a
data access API. Here we go through the steps to build a non-trivial example.


### Narrative


- Get the data in digital form
- Set up / run pre-processing: Get a test dataset in tabular (`csv`) form
    - In the worked example below the dataset is about 400MB as text
        - Two sensors
        - One sample per second
        - Three values per sample: Timestamp, pressure, measurement
            - First sensor measures temperature; second measures salinity
- Establish a moderate-size cloud Virtual Machine
    - Connect using VSCode as described above
    - Configure the cloud VM as described above
- Establish a NoSQL database on the cloud
    - This working example uses CosmosDB on Azure
    - The cloud VM will load tabular data into the database...
        - ...so it will need authentication credentials: See above
- Move the tabular data to the cloud VM
    - For example use secure ftp `sftp`:
        - `chmod 400 .keypairs/cloud_VM_keypair.pem`
        - `sftp -i .keypairs/cloud_VM_keypair.pem username@123.123.12.12`
        - `sftp> put tabularfile.csv`
- Create a program to load the tabular data into the database
    - The key line of code on Azure is `container.create_item(record)`
    - This is naively run once per measurement
- Build a serverless function with a simple API for access to the data
    - The API has a URL and one or more *routes* as above
    - Test the API using a Client running on a handy laptop
    - The Client could also be tested from the cloud VM
    - Authentication and use
        - At this point the API calls do not use authentication keys
        - As such the API is considered to be *anonymous*
        - The data should not be sensitive
        - The Client code can be shared for example through a GitHub repository
            - This is the approach used for this example
        - The Client code could also be published as a Python library
        - Future changes beyond this example should take privacy and security into account
- The end result experience for "some other scientist"...
    - Scientist does a `git clone` of the Client repository
    - The repository includes a test IPython notebook
    - The repository also has a Python `client.py` file
        - The notebook includes a cell with these two lines of code:

```
import oceanclient as oc
oc.Chart('04-JAN-2022', 7)
```


The resulting chart looks like this:




Figure caption: There are two sensors -- temperature and salinity -- that record data once per
second from an oceanographic installation 100 km off the coast of Oregon at the base of the 
continental shelf. Nine times per day these sensors are raised and then lowered through the 
upper 200 meters of the ocean resulting in a profile of temperature and salinity with depth.

The scientist does not know when the profiling runs happen; only that they are fairly 
consistent in timing under normal conditions. The `Chart()` function call given above 
represents the scientist saying "For January 4, 2022: Show me temperature and salinity
for profile number 7." 



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
# pseudo-code for loading profile data into a container
# read and format profile metadata: OSB, JAN-2022; all content treated as strings
import pandas as pd
df = pd.read_csv(filename, usecols=["1","2","7","8","13","14","16","17"])
df.columns=['rest start time','rest start depth','ascent start time','ascent start depth',
            'descent start time','descent start depth','descent end time','descent end depth']
print(df.shape)

# Timestamps are not used; but here is a type conversion for a given column:
# df['rest start time'] = pd.to_datetime(df['rest start time'])

# open the connection to the target NoSQL database container
client = etcetera; see tutorial
db =
container =

# for each row in the CSV file create a database entry
for record in df.to_dict(orient='records'):
    record["id"] = record["ascent start time"]
    container.create_item(body=record)
```

### oceanography api builds


#### profile api


The profiles use `ascent start time` as their Container `id`. The Container is `osb_profiles`
which encodes the site name Oregon Slope Base (OSB) in the Container name. The data covers 
January 2022 so there are 31 days and up to nine profiles per day for a total of 279 possible
entries or 'documents'.


To keep things simple we assume the id keys are alphabetic and can be compared using
less than / greater than `<` and `>`. These are datetime strings. 


Once we establish that the two API parameters `day` 
and `index` are in the proper range we have the API code do a query on the osb-profiles
Container and return the requested values: `ascent_start_time` and `descent_start_time`. 
Suppose the API call passes `day=3` and `index=1`, the first of four
These will be text strings of the form `2022-01-03 20:37:00` and `2022-01-01 21:49:00`.
This indicates that the ascent duration was 


#### Python to SQL query formalism


Here is some simplified pseudo-code: Setting up an Azure serverless function to query a NoSQL 
database container. In this case the User has stipulated `lookup` (the *route*) as well as a
single parameter `name=Sodium`. The lookup is intended to return some information about Sodium
from the periodic table. 


In what follows let's attempt to differentiate Python namespace from NoSQL query machinery.
There is one NoSQL variable in use, called `@id`. This is used for an equality comparative; 
and we know it is SQL because only one equals sign is needed: `WHERE r.id=@id`.

```
# route "lookup" pulls element information by name
@app.route(route="lookup", auth_level=func.AuthLevel.ANONYMOUS)
def lookup(req: func.HttpRequest) -> func.HttpResponse:

    # Get the "name=Sodium" key-value input from the URL
    element = req.params.get('name')       # element will now be a string with value 'Sodium'
    if element:

        establish client, db, and container: See the tutorial
        
        # `items` will be a list of one or more dictionaries, in fact just one because the API call
        # requested the one element 'Sodium'. For ocean data we will have `profile` and `sensor` queries.
        # These will return one dictionary and thousands of dictionaries respectively.
        items = list(container.query_items(query="SELECT * FROM r WHERE r.id=@id",
                                           parameters=[{"name": "@id", "value": element}],
                                           enable_cross_partition_query=True))

        # remove extraneous information, 'serialize' to json and send this in the HttpResponse()
        stripPrivateKeys(items)
        items_json = json.dumps(items)
        return func.HttpResponse(items_json, mimetype="application/json", status_code=200)
```

From this pseudo-code we proceed to this interpretation:

- `container.query_items()` is a method that executes a query on a NoSQL Container
    - The method has three key-value arguments: `query`, `parameters` and `enable_cross_partition_query`
        - `query="SELECT etcetera"` assigns `query` a string to be interpreted as a NoSQL query
            - `r.id=@id` means 'Does the `id` of `r` precisely equal the value of SQL variable `@id`?'
            - the value of `@id` is set in the `parameters=` assignment
                - [{"name": "@id", "value": doc_id}]`.
    - What the code is doing: When `container.query_items()` runs a query...
        - ...it must provide a list of usable SQL variables within the SQL code
    - These SQL variables in this list appear in Python code as a list of (one or more) dictionaries...
        - ...each of which represents a SQL variable by means of two keys:
            - name: of the SQL variable we will use in the query
            - value: a value from the Python namespace transcribed into the SQL variable.
        - This is where and how the value of @id is assigned
    - The value of the SQL variable is that of a Python variable `doc_id`
    - We'd need to see the Python value assignment to `doc_id` to say more
    - Probably in a `lookup` call it takes the value `Sodium` from `name=Sodium` (to be verified)
    - We follow this `query / parameters / [{ . . . }] / @id` protocol...
        - ...rather than just using `Sodium` directly from the API request...
        - ...to avoid the *Little Bobby Tables* situation (cf xkcd).
        - The invisible machinery of `query_items()` and `parameters` does the safety checks for us 


#### sensor api
