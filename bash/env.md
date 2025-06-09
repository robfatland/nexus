[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md),
[bash index source](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md)



# environments

## Python installations


There are good instructions online for installing various Python distributions. A distribution includes a version of the Python
interpreter (currently 3.something) plus default libraries plus an IDE. In these notes I avoid the (rather large) `Anaconda` 
installation preferring the stripped down `Miniconda` variant. This has relatively few libraries pre-installed so the idea is
to install them on an as-needed basis. Also worth researching: Other Python installations that run faster, see particularly
`Micromamba`. 


## Initialize conda


`conda init bash` will insert the miniconda `bin` directory at the top of the `bash` `PATH`. In this manner an
existing Python executable say within Linux is superseded by the one installed with `miniconda`.


## What are Python virtual environments?


> Note: An *Integrated Development Environment* (IDE) such as `IDLE` or `VSCode` is not to be confused with a Python
> virtual environment.

 
A Python virtual environment (or simply 'an environment') is created using a package/environment management utility such as 
[`conda`](https://en.wikipedia.org/wiki/Conda_(package_manager))
or [`venv`](https://docs.python.org/3/library/venv.html) which uses 
[`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager))
for package management. 
For a more in-depth view search online for tutorials, 
for example [like this one](https://realpython.com/python-virtual-environments-a-primer/).



Creating, activating, modifying, and deactivating Python virtual environments 
is the protocol for managing a larger computing environment. Each created environment acts as a distinct context. This
is in contrast to a 'kitchen sink' approach where all needed libraries are installed in one place, for example in the default 
`base` environment. This can be done of course but it can result in incompatibility errors, in part because the Python ecosystem 
is very dynamic and can involve complex dependencies.


In summary then, the advantages of using virtual environments include dependency isolation, reproducibility, conflict 
avoidance, ease of collaboration, and peace of mind from working in an uncluttered workspace.


> A note on using `venv`: This approach installs a sub-directory usually called `.venv` within a project folder. Adding
> this to `.gitignore` will avoid unnecessary commits. In contrast, `conda` environments tend to be installed within
> the `miniconda` folder (independent of project folders).


Installing packages (libraries) within an environment can be done on an as-needed basis; but reproducibility comes by
means of grocery list files (called *environment files*) that consist primarily of a list of libraries. 
Two common varieties are `environment.yml` and `requirements.txt` files. These
correspond respectively to `conda` and `pip`. Mnemonic: `p` is close to `q` and `c` is close to `e`. The idea is to
feed the package manager one of these environment files and let it solve for compatibilities and install corresponding
versions of the various packages.


To recapitulate, then: The environment command associated with Anaconda/Miniconda is `conda`,
both the open source package and environment management system and its eponymous utility command. 
It is an alternative or complement to the Python native package manager `pip` (package management)
together with `venv` (environment management). Both `pip` and `conda` can be used to install packages 
individually or *en masse* by means of grocery list files.


Some best practices
- Avoid mixing `conda install` and `pip install` in a given environment
- One environment per project
- Keep environments small
- Verify reproducibility by sharing environment files


## command reference


- `uname -a` for Linux OS details
- `lsb_release -a` for distribution/version
- `python --version`
- `which conda` verifies `conda` is installed
- `conda init bash` as noted puts the miniconda `bin` directory at the top of `PATH`
- `environment.yml` and `requirements.txt` are default configuration filenames
    - Associated respectively with `conda` and `pip` package managers
- [`conda env create --file environment.yml --name myusefulenv`](https://docs.conda.io/projects/conda/en/stable/commands/env/create.html)
- `pip install -r requirements.txt` 
- `conda deactivate` returns to the parent environment
- `conda create --name new_env_name` brings a new environment into play manually
    - `conda env list` lists the created environments
    - `conda activate envname`
        - The `bash` prompt reflects the active environment: `(envname) prompt>`
    - From an active environment: Newly installed libraries will be available *from this environment*
        - `pip install -r requirements.txt` is the `pip` way
        - `conda env update -f environment.yml` is the `conda` way
    - `conda env export` to produce `environment.yml` for the current environment
    - `conda remove -n envname --all` to delete
- `pip` to `requirements.txt` goes as follows
    - Create a virtual environment `python3 -m venv /path/to/new/virtual/env`
    - Install packages using `pip install <package>`
    - Save all packages `pip freeze > requirements.txt`
    - "Pin all the package versions"... not sure what the action is or what this means
    - Move `requirements.txt` to the root directory of the project


## project installation notes

This section tracks some personal environment names corresponding to projects; as well as 
(indented) module installations. Unless noted the modules are installed with `conda install`.

- numbertheory: Basic coursework; see [this source repository](https://github.com/robfatland/ant).
    - jupyterlab: run this using the command `jupyter-lab`
    - matplotlib: typical charting accessed in `pyplot` via `from matplotlib import pyplot as plt`
        - Note this breaks with the domain name heuristic.
    - potentially: `FLINT` and then `python-flint` wrapper
- epipelargosy
    - jupyterlab
    - matplotlib
    - pandas
- pbytes
    - jupyterlab
    - already done: requests, turtle
- sodium
    - jupyterlab
    - matplotlib
    - pandas

### Items this page should address


- Address how an active environment appears in a Jupyter notebook server interface
- Look up guidelines for how to not simply make one working environment != base and have *that* become the One Ring
- Look up guidelines on copying an environment to create a branch environment
- Write up how to document and easily select environments
- Cover the "manual approach" and the "requirements.txt" approach and the "whatchamacallit.yml" approach
- Debugging the dreaded incompatibility red ink
- When pip? When conda? What is conda forge?


This is obviously an ambitious topic with many tentacles. I continue next with the concept 
of the Python `import` utility.


## Python `import`


Suppose I have written some code in a Jupyter notebook that calculates
a value I assign to a variable `t`.  Suffering from delusions of grandeur my 
immediate thought is 'this wonderful code belongs in its own module file... so I can use
it from anywhere... and what is more I should publish it as a Python package for all the 
world to install and import and use!' This is an altruistic impulse--good for me--but
how to proceed? Here is how to make the dream a reality:

- decide on a reasonably short name for the module: I choose *ant*.
- open my editor and cut-paste the code from `b.ipynb` into `ant.py`
- convert the code to a function called `Totient(n)`
    - remember to include a docstring
- below the function code create a test program in the `ant.py` file:


```
if __init__ == "__main__":
    t = Totient(10)
    if not t == 4: print("Totient() fails for n = 10")
    else:          print("Totient() passes its test")
```

- save the file `ant.py`
- run the file as a program to ensure the test passes: `python3 ant.py`
- Back in the Jupyter notebook `b.ipynb` write these two lines of code
 
```
from ant import Totient

t = Totient(73)
```

- Decide that this module should definitely be published as a Python package
- Search online for *how to publish a Python package* and follow the tutorial
    - For more on this: See below


Now that I have done that: I should really consult with Naomi about how to properly
do the import. Why not use `from ant import *`? Why not use `import ant`?


In answer to the second question: `import ant` is a perfectly reasonable thing
to do. Then I will have to say `t = ant.Totient(n)`. If the `ant` module evolves
to feature more functions (aka methods): My notebook will have access to those
as well through this `import`.


The first question 'Why not say `from ant import *` has an involved answer but
the TLDR is ***don't do this***.


### Why we do not use `from ant import *`


This practice pollutes the global namespace where the `import` runs, in this 
example the notebook `b.ipynb`. The module file `ant.py` has a global namespace 
as does any Python ...um... "entity".  A namespace is a dictionary mapping strings
to the address of corresponding code. The global namespace of a module coexists 
with the global namespace of the notebook: They each have their own. The 
intersection of their respective namespaces is the empty set. 


Suppose `ant.py` includes the line `from math import cos`. When the module executes
(for example as a result of the `import` line in `b.ipynb`):  The global namespace 
will have a new dictionary entry. The key of this entry will be `cos` and the value 
will be a pointer to the cosine function code. By using pointers to code the code
itself exists only once in this Python universe (rather than making multiple
copies of the same code every time something imports it). 


Noting that the module `ant.py` executes due to the `import ant` in `b.ipynb`:
What does this mean? It means that Python will attempt to run all the code in
the module, thereby populating that module's global namespace. But what if there
is code in `ant.py` we *do not* want running during an `import`?  For example:
code that tests the module's functions. This is why `if __init__ == "__main__"`
was included: It runs when the module is run via `python3 ant.py` but it does
not run during the `import` code execution. 


## Publishing a Python package

- here is where I left off
