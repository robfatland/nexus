[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


# Loose strands

## CloudBank strands

Sources...

- Incidental locations to check...
    - Both README files (main and gh-pages) of this repo; OneNote; GitHub fossils; GDrive (at least 3 orgs)
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
    - [flameshot]() + unbind prtscn
    - [LaTeX]()
    - [Hugo](), [Jekyll]()



## Residual loose strands


* Look at HyakAndCloud in the `main` branch; and scoop up anything else like that and move it to the pipeline here on gh-pages



To unbind the Print Screen key to OneNote screen capture in Windows:

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


`sudo apt-get install -y nyancat`


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
sudo apt-get update -y && sudo apt-get upgrade -y
```

alternative...?...

```
sudo apt update
sudo apt install
```

## more residual remarks from the gh-pages README

- The `lexicon.md` list of terms is relevant, needs a ton of work
- The file `index.md` is a compendium of useful recipes including the titular material on simplifying bash windows; more work here also
- What are the relevant related repos ***R3***?
    - `runawaytrain` has AWS Organizations and some API use; so very AWS-cloud-centric 
    - formerly `reorganiseduponthefloor` has `git` and more: to transplant
    - `cbburn` does have some pandas DataFrame manipulation
    - `digitaltwin` is itself
    - `serverless` is itself
    - Left Off Here


[This repo](https://github.com/robfatland/greenandblack/tree/main)
began as a Note To Self on simplifying format of the *Bourne again shell* **`bash`**: 
No colorized text, just green characters on a black background.


- this repo uses GitHub **pages** so switch to the **`gh-pages`** branch to edit content
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
