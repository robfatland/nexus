[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


# Loose strands


This page is an accumulator for nexus feeder content: Various places where research computing information is parked 
(including cloud infrastructure material).


## Find out and resolve why Chris Simmons says Micro Mamba not Anaconda and even not Miniconda

## CloudBank strands

- Incidental locations
    - gh-pages branch README: brief notes on publishing with gh-pages
    - R's OneNote
    - GDrive (3+ orgs)
    - GitHub fossils
        - R's relevant GitHub repos
        - [Cloud 101/102 dates back to 2017](https://github.com/robfatland/cloud101102)
        - [curriculum](https://github.com/robfatland/curriculum) is some teraform stuff; this will take 10 minutes to scrape and delete
        - **cli** likewise scrape and delete
        - **cloudsecurity**
        - **quantum**
        - **zero2x**
        - **costnotify**
        - **nlp**
        - **serverless**
        - **digitaltwin**
        - **runawaytrain**
        - **carpentries**
        - **cbburn**
        - **git**
        - Oceanography (not CI-useful but relevant to data science)
            - [oceanography (current, Jupyter book)](https://github.com/robfatland/oceanography)
            - [galleryclone](https://github.com/robfatland/galleryclone), [notebooks](https://github.com/robfatland/notebooks), [chlorophyll](https://github.com/robfatland/chlorophyll)
            - **ocean**, **golive**, **sensors**
- Tilde: Specifically work slash uw research programs
- MSE544 Cloud Skills
    - [VMs + Database + Serverless (Azure) source](https://github.com/cloudbank-project/az-serverless-tutorial/tree/main)]
        - [VMs + Database + Serverless as published](https://cloudbank-project.github.io/az-serverless-tutorial/)
    - [Containerization source](https://github.com/naclomi/containers-tutorial)
        - [Containerization published](https://naclomi.github.io/containers-tutorial/)
        - See also the [Carpentries introduction to docker](https://carpentries-incubator.github.io/docker-introduction/)
- [Cloud Maven Fossil Cloud Resource Site](http://cloudmaven.github.io/documentation)
    - [Cloud Maven on GitHub](https://github.com/cloudmaven)
    - [CM Documentation on GitHub](https://github.com/cloudmaven/documentation)
    - [HIPAA](https://cloudmaven.github.io/documentation/aws_hipaa.html)
    - [data security](https://cloudmaven.github.io/documentation/cc_data_security.html)
    - [polemics](https://cloudmaven.github.io/documentation/ccs_precis.html#introduction)
    - [root index](https://cloudmaven.github.io/documentation/index.html)
- CloudBank GitHub organization
    - [zero2Data](https://github.com/cloudbank-project/Zero2Data)
    - [spend tracking](https://github.com/cloudbank-project/burnop)
- Git
    - https://git-scm.com/ and also https://cloudmaven.github.io/documentation/rc_github.html
    - https://github.com
- Python and Jupyter
    - PyPI, the Python Package Index
    - `pip` in relation to `requirements.txt`
    - `conda` in relation to `environment.yml`
    - Anaconda, -c conda-forge
    - https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html
    - https://jupyter.readthedocs.io/en/latest/projects/kernels.html
    - https://zero-to-jupyterhub.readthedocs.io/en/latest/
        - [Hybrid Zero2JupyterHub on the Azure cloud](https://github.com/robfatland/zero2x/tree/master/Z2JH)
    - https://github.com/jupyter/nbviewer/blob/master/nbviewer/templates/faq.md
    - https://binder.readthedocs.io/en/latest/user-manual/overview/intro.html
    - [sphinx](https://kanishkvarshney.medium.com/python-documentation-generating-html-using-sphinx-a0d909f5e963)
- Case studies
    - [InSAR AMI by Scott Henderson](https://github.com/scottyhq/isce2binder)
        - Emphasis: Exemplary value as data curation on the cloud ([more of Scott's work](https://nbviewer.jupyter.org/github/scottyhq/))
    - [GCP clinical data warehouse](https://cloud.google.com/customers/colorado-center-for-personalized-medicine/)
    - [Yiyu Ni on preemptible instance use](https://github.com/SeisSCOPED/QuakeScope/blob/6d7ac909cce0889d4a33b6373dea7b4842694bc2/sb_catalog/configs/job_definition_picking.yaml#L39C1-L43C56)
        - [AWS on likelihood of preemption](https://aws.amazon.com/ec2/spot/instance-advisor/)
    - [Neotoma](https://www.neotomadb.org/about)
- Environments in relation to file system structure
- Useful stuff
    - [LaTeX]()
    - [Hugo](), [Jekyll]()
- [Oorjit repo: Originally studying preemptible](https://github.com/oorjitchowdhary/ml-training-preemptible-vms)
    - [Rob's notes in Oorjit's repo](https://github.com/oorjitchowdhary/ml-training-preemptible-vms/blob/main/assets/notesbyrob.md)

## clean slate project

- I have a Windows PC that runs an application called `Terminal`
    - This is a multi-tabbed application with Settings and a Chooser menu
    - There are two Linux options in the Terminal menu
        - `lsb_release -a` in "Linux 20.04" gives me 20.04: `/home/kilroy` with just some `.something` files and folders
        - `lsb_release -a` in "Linux" gives me 18.04: `/home/kilroy` with lots of repos, folders, files
    - One has a home directory full of stuff; the other has only `.something` files and directories
- WSL2 is running
- VSCode seems to have its own ideas
    - Terminal starts PowerShell which lands in C:\Users\kilroy (home directory of Windows User kilroy)
    - Terminal += Ubuntu (WSL) lands in bash but same location Windows User kilroy home
        - This is styled as `/mnt/c/Users/kilroy` in Linux
        - If I say `cd ~` I wind up in `/home/kilroy` the cluttered version
        - So the null hypothesis says `lsb_release -a` gives me Linux 18.04: Confirmed
    - Terminal += `Ubuntu-20.04 (WSL)` gives a new bash shell in `/mnt/c/Users/kilroy` with 20.04 confirmed
        - `cd ~` goes to `/home/kilroy` with `.something` content plus the `nobody_home` touch file
    - Terminal += `Azure Cloud Shell (bash)` does not work; some additional install `jsnode` missing
    - In summary both Linux installs are "visible" to VSCode through Ubuntu Terminal options
        - Both involve WSL and wander off into the respective home file systems
    - End result: VSCode agrees about which Ubuntu/Python/home
- Backing everything up
    - Back up both versions of Linux including the `.something` material
    - Back up the repos (with respect to the other PC also)
    - Back up the data folder
    - Back up the other folders
    - Be really sure everything important is recoverable
    - Note down the symlink connection to Windows filespace, particularly Downloads
    - Note down the environments: List them, get their dependency files `requirements.txt` etc
- uninstall Python definitely; start over with `miniconda`
- uninstall Linux maybe? What does `sudo apt update / upgrade` get us?
- Notice that `cli` commands like `az` and `aws` and `docker` will need to be reinstalled
    - Work from a plan for environments rather than improvising things
- uninstall Linux? Update?
- 

## Residual loose strands


* HyakAndCloud in `nexus`: `main`; and similar
* `flameshot` screencap workflow
    * To unbind the Print Screen key to OneNote screen capture in Windows:
        * Windows settings > Accessibility > Keyboard > Use the print screen key to open screen capture > toggle off


## Reminders on other simple little topics...


### Other Math Club on package installs


Look in the `Basic Programming.ipynb` in that same folder: On `conda-forge` for WSL-2 Linux 
and installing for IDLE installations using the Windows Command Prompt.


### Follow this up

How do I log in to another machine using `ssh` and `path/keypair.pem`?

```
> ssh -i path/keypair.pem username@123.123.123.123
```

### Follow this up

Q: When do I want to write a class in Python? (In Java everything is a class.)

A: When the object is something that has a state that you need to access at a later time. 

A2: If your functions call other functions you have written and you want to have future users swap those functions out. Like the ML metric function. You are using subclasses to replace old methods with new methods. 

### Follow this up


`sudo apt install -y nyancat`


...and a remark on the mechanics, separation of concerns, Ohm's law, that sort of thing


### Follow this up


save a file called `r.csv` with contents

```
row,a,b,c
1,3,3,3
2,4,2,3
3,5,1,4
```

issue:


```
import pandas as pd
q=pd.read_csv('../../../r.csv')
q
```

### Follow up CPU monitoring (many-core machine)


Wes says: "Use **`top`** from the bash command line."


Wes says: "CloudWatch metrics (AWS EC2 console GUI) are delayed, updated once every 5 minutes.
A localized spike in CPU use will take some time to display in the console. It is possible 
to pay for a higher sampling rate in the console... but why?"


### Keep a VM patched


```
sudo apt update -y && sudo apt upgrade -y
```


(Note: `apt` is the modern version of the older `apt-get`; more user friendly.)


## more residual remarks from the gh-pages README


- What are the relevant related repos ***R3***?
    - `runawaytrain` has AWS Organizations and some API use; so very AWS-cloud-centric 
    - formerly `reorganiseduponthefloor` has `git` and more: to transplant
    - `cbburn` does have some pandas DataFrame manipulation
    - `digitaltwin` is itself
    - `serverless` is itself


[This repo](https://github.com/robfatland/greenandblack/tree/main)
began as a Note To Self on simplifying format of the *Bourne again shell* **`bash`**: 
No colorized text, just green characters on a black background.

- customizing `bash` and `vi` is focused on green-on-black, a simple prompt, and text editing
- scope expanded to include
    - **`ssh`** tunnels from one machine to another
    - Difference: **`miniconda`** versus **`anaconda`**
    - Windows PC
        - **`Ubuntu bash`**
        - **`Windows Subsystem for Linux (WSL-2)`**
        - **`VSCode`**?
    - containers
    - conda environments


## nexus aspirations


- TCOTU: Understanding, building, maintaining, using Python environments
    - corollary: customizing `bash`, `vi` to a simple appearance
    - **`ssh`** tunnels from one machine to another
    - headless `jupyter` running on a cloud VM with a localhost laptop interface
- Comparison: **`miniconda`** versus **`anaconda`**
- PC-based Linux / IDE: **`Ubuntu bash`**, **`WSL-2`**, **`VSCode`**
    - Containerization
    - conda environments
- cloud infrastructure building
        - Data systems, APIs
        - Building a Flask server
        - Cloud security
        - ML/AI: CNN, NLP
        - varieties of cloud CLI
        - cloud spend notification
        - stopping runaway cloud spend automatically
- [Python's guide to publishing a software package](https://packaging.python.org/en/latest/tutorials/packaging-projects/)


## Burning questions

- How do I manage Python environments?
- How do I publish my oceanography code as a Python package?
- How do I build an API-based resource?
- How do I safely manage sensitive data?
- How do I manage my code development in relation to my GitHub repository?
- How do I turn off colorization in bash and vi? Just green on black please.
- How do I set up a cloud VM as my power workstation and use Jupyter there from my laptop?
