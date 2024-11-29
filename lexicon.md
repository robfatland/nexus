# nexus lexicon

- [published: nexus](https://robfatland.github.io/nexus), and then
[the editable index.md](https://github.com/robfatland/nexus/blob/gh-pages/index.md)
- [published: this lexicon](https://robfatland.github.io/nexus/lexicon), and then
[the editable lexicon.md](https://github.com/robfatland/nexus/blob/gh-pages/lexicon.md)


## Quo vadis?


- 12/23 did some editing of this content
- Where this should get to is
    - All the headings should have definitions
    - Statement of purpose at the top
    - Define environments early
    - Arrive at miniconda as the target, then interactive Python, then the Jupyter family
        - For each technology we want to have enough information to create, delete and rebuild without loss of existing effort
            - Best for not losing existing effort: Software control
            - This in turn implies rudimentary `git` commands
            - The advanced `git` skill is reconciling incompatible merges
- Basic `bash > cd ~ > jupyter lab > copy paste > edit > save > commit`
    - The version of this that runs on a Linux server on Azure, on AWS
- Incidental questions it would be good to answer
    - What if I installed Python and I have IDLE and so on... is this creating friction with the miniconda installation?
        - Digress into IDLE and how package installation is done in that context...


### Weasel?


- ***Weasel*** is my informal, unendorsed pronunciation of WSL-2, the second version of the Windows Subsystem for Linux
    - WSL-2 is a *compatibility layer* (see following section)
    - The underlying idea is to support the Linux core, particularly 'Linux system calls' in Windows somehow
        - WSL-1 original idea: Do so without a Virtual Machine or a dual-boot OS
            - ...by giving the Windows kernel the capacity to execute Linux system calls
    - Superseded by WSL-2
        - Uses a full-blown virtual machine (VM) to run a Linux kernel
        - Inviting questions on how this runs and interacts with Windows
            - And this is out of local scope because...
            - ...the focus of this repo is just getting a framework in place
         
> Bottom line: The plan is to enable WSL-2 on a Windows machine in support of Linux


### More on WSL-2: A *compatibility layer*


A compatibility layer is an interface that allows binaries from a foreign system to run on a host 
system. 

In the WSL-2 discussion above, the host system is Windows and the compatibility layer is 
Windows Subsystem for Linux v2, abbreviated WSL-2. 
The foreign system binary is Linux. One enables WSL-2 so as to run Linux on Windows.

At the Windows Command Prompt -- as Administrator -- one can install `wsl` if needed via `wsl --install`. 
(Re-start the PC at this point.) Thence: A `wsl` command starts a bash shell in the Command window. 


```
C:\Windows\system32> wsl

(base) username> pwd

/mnt/c/WINDOWS/system32

(base) username> cd ~
(base) username> pwd

/home/username

(base) username> exit

C:\WINDOWS\system32>
```


Now the darndest thing is I can also use my Windows chooser (windows key) to find **`bash`**. How did 
that get there? ...more to do here...


### **`Anaconda`**?


- Anaconda is the proper name for the large **Python distribution**
    - ...featuring a *lot* of pre-installed data science libraries 
    - Anaconda can be seen as a **data science platform** that happens to use Python
- Anaconda installed in a Linux operating system includes the package manager `conda`
    - As the name implies, `conda` is a management tool
        - Management task: Install or uninstall libraries
            - These are used by Python code for specialized tasks such as SVD
        - Management task: Create or delete Python *environments*
    - Related commands are `pip` and `apt-get`
        - `pip` is also a Python package installer/manager
            - A distinction between `conda` and `pip` is attempted [here on stack overflow](https://stackoverflow.com/questions/54834579/specific-reasons-to-favor-pip-vs-conda-when-installing-python-packages)
        - `apt-get` is a **Linux** command line tool for interacting with a package management system for Linux distributions
            - This package management system is called the Advanced Package Tool, hence APT, hence `apt-get`
            - `apt-get` is hence a Linux analog of Python package management tools like `conda` and `pip`


> Bottom line: **Anaconda** is a large Python distribution that includes package and environment management tools.
> [More here](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))


### What is **`miniconda`**


- **`miniconda`** is a minimal Python installation that also includes the `conda` package manager
    - Description
        - miniconda includes the Python kernel
        - miniconda does not include many of the libraries pre-installed in an Anaconda installation
        - miniconda consequently installs much faster and has a smaller footprint
            - The implication is that needed libraries can be installed subsequently
            - [Comparative article: Anaconda versus Miniconda](https://www.educative.io/edpresso/anaconda-vs-miniconda)
    - miniconda installation
        - Given below are miniconda installation steps circa 2022
            - These proceed to start a Jupyter notebook server
        - Recommendation: Do not follow these command verbatim; rather look up the current procedure
        

```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda install ipython
conda install jupyter
conda create -n python313 python=3.13
conda activate python313
jupyter notebook
```

### What is **`conda-forge`**?



### What is VSCode?


### What is **`bash`**?


### What is **`Linux`**?


Linux is an operating system traceable back to UNIX.


#### Which version of the Linux operating system am I running? 


```
cat /etc/os-release

NAME="Ubuntu"
VERSION="18.04.2 LTS (Bionic Beaver)"
PRETTY_NAME="Ubuntu 18.04.2 LTS"
VERSION_ID="18.04"
etcetera

lsb_release -a

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.2 LTS
Release:        18.04
Codename:       bionic
```


### What is **`vi`** or **`vim`**?

[**`vi`** is a visual text editor](https://en.wikipedia.org/wiki/Vi)
created by Bill Joy back in the mid-1970s, associated with UNIX/Linux.
**`vim`** is an improved 
and very compatible version. The main point of `vi` from my perspective
is: Sharp learning cost and then it becomes second nature; and this
is primarily due to the intrinsic <escape> mode which gives access
to a command line at the bottom of the screen.
  

In recent years `vi/vim` has accumulated features like color-coded
text which is one of the motivations for this repository. Apparently
when Heads Up Displays were introduced in the military the pilots 
would often switch them off because it they just amounted to visual clutter.



### What is **`Jupyter`**?


### What is **`git`**?


### What is GitHub?


### What is Binder?


### What is an environment?


### What is **`environment.yml`**?


### What is **`requirements.txt`**?


I can "install" something called WSL... or maybe it is combined with "turning on Linux" inside Windows. But I can also install Ubuntu bash. Which opens a bash terminal in my home directory... where miniconda is not installed. So I install miniconda and now I can create and activate environments. And I can start a Jupyter notebook server. But the other day my Ubuntu <start> icon stopped working. So I forced Ubuntu to start using the Windows start utility. So it started. So I said "ls" and everything was gone. So all my hard work evaporated (except that it was mostly synched with GitHub so Hah Hah Hah on the gods of data loss). So 
  
  
  ### What is a web framework?
  
  
  ### What is flask?
