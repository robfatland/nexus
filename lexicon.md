# nexus lexicon

- [published: nexus](https://robfatland.github.io/nexus), and then
[the editable index.md](https://github.com/robfatland/nexus/blob/gh-pages/index.md)
- [published: this lexicon](https://robfatland.github.io/nexus/lexicon), and then
[the editable lexicon.md](https://github.com/robfatland/nexus/blob/gh-pages/lexicon.md)


## Quo vadis?

- All headings have corresponding short lexicon entries
    - This is a two-way street: Look for content in this file that ought to be reindexed to elsewhere!
- Statement of purpose at the top
- Define *pedagogy from the Book*
    - Example: { Open Science + Back up + s/w control + community + intercompatibility } > implications
        - GitHub > Environments > Miniconda > IPython > Jupyter
    - Meta: Documentation sufficiency threshold: Operations = { create, delete, rebuild } 
        - Example: Core `git`, Meso `git`, Pro `git`
- Overcommunicate: Featured narratives
    - Here is the sidebar narrative of baseline workflow
    - `bash > conda activate > cd ~ > jupyter lab > browser > edit > save > commit`
        - "Notice we did nothing with data; that is an expansion topic covered elsewhere"
        - "Notice we did not talk about servers and cloud; another expansion topic"
- Overcommunication: Lateral comparatives
    - I installed Python on my PC (IDLE?) and WSL-2 is Linux with Miniconda installed...
        - The former gives me IDLE and a runtime that doesn't balk on Turtles
        - The latter gives me `jupyter lab` but balks on Turtles
        - And then VSCode seems to know about one of them... or the other?
        - Bottom line it feels like I have a lot of friction and/or schism built into my working environment
            - And incidentally how do I install packages that can be used by IDLE?


### WSL-2 aka Windows Subsystem for Linux (v2) aka "Weasel"


- WSL-2 is a *compatibility layer* (see following section)
    - The underlying idea is to support the Linux core, particularly 'Linux system calls' in Windows
    - WSL-1 original basis: Without a Virtual Machine or a dual-boot OS
        - How: Give the Windows kernel the capacity to execute Linux system calls
    - Superseded by WSL-2
    - Uses a full-blown virtual machine (VM) to run a full Linux kernel
        - How does this run and interact with Windows?
- Bottom line: WSL-2 on a Windows machine provides a `bash` interface to a Linux VM 
    - What is meant by a *compatibility layer*
        - It is an interface: Foreign system binaries run on a host system
        - Host system is Windows, compatibility layer is WSL-2
            - Foreign system binary is Linux.
            - "Enable WSL-2 so as to run Linux on Windows"


> Question: Can I use my Windows chooser (windows key) to find **`bash`**?


- Installation
    - Windows Command Prompt as Administrator: `wsl --install` and re-start the PC
    - Command Prompt > `wsl` > bash shell; try `ls`


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


> Odd: I can use my Windows chooser (windows key) to find **`bash`**. How did that get there?


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


Linux is an operating system traceable back to UNIX. It consists of two parts, one immutably constant everywhere in the universe and
the other part mutable and subject to stylization (Red Hat, Debian, Ubuntu and so on)


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
