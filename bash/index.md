[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md),
[bash index source](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md)


# `bash`


The Bourne Again Shell... but *confidentially* the content here is one big cheat sheet 
for setting up a data science VM on the cloud running a Jupyter notebook server appearing 
in one's (say laptop) browser. 


## Children


- [environments](https://github.com/robfatland/nexus/blob/gh-pages/bash/env.md) including `import`
- [git](https://github.com/robfatland/nexus/blob/gh-pages/bash/git.md)
- [terminal](https://github.com/robfatland/nexus/blob/gh-pages/bash/terminal.md)
- [tunneling](https://github.com/robfatland/nexus/blob/gh-pages/bash/tunneling.md)



## Topics


- [bootstrapping a cloud data science VM](#bootstrapping-a-cloud-data-science-vm)
- [related links and resources](#related-links-and-resources)
- [linux on a PC running windows](#linux-on-a-pc-running-windows)
- [Ubuntu Jupyter via ssh tunnel](#ubuntu-jupyter-via-ssh-tunnel)
- [More on Linux](#more-on-linux)
- [What is the basic idea here?](#the-basic-idea-here)

## bootstrapping a cloud data science VM

[Click on this link](#the-basic-idea-here) to skip down to a writeup on "What's the basic idea here?"



- Task: Configure and operate a data science Virtual Machine (VM) on the cloud. 
- Remark: Notice this overlaps with the 544 source material and with API
- Remark: Anaconda relevance over Miniconda for data science libraries


### Precursor steps


- Set up a PC with some operating system that supports Linux
    - Laptop Linux will commonly support utility programs as needed, for example `conda`, `jupyter`, `docker`, `ssh`, `sftp`, `git`
    - Laptop Linux might also feature a command line interface utility for a cloud, such as the `aws` utility for AWS.
- Secure a cloud VM: For example through the cloud console or portal using a VM Create wizard
    - This process includes downloading a keypair file `CloudKeypair.pem` with permissions set to `0400` using `chmod`
- Get some coffee
- Log in to a `bash` terminal on the VM
    - From one's local/laptop `bash` via `ssh`
    - From VSCode, the useful IDE
    - From the cloud vendor's console typically called a cloud shell


We continue this narrative with two intermezzo sections: Resource links and notes on using 
Linux from a Windows PC. The narrative then jumps into the bootstrapping recipe for the cloud VM. 


## Related links and resources 


- [`conda` environments](https://robfatland.github.io/nexus/env)
- [`git`](https://robfatland.github.io/nexus/git)
- [`ssh` tunnels](https://robfatland.github.io/nexus/bash/tunnels)
- [terminal configuration](https://robfatland.github.io/nexus/bash/terminal)
- [cloud computing](https://robfatland.github.io/nexus/cloud)
- [ai](https://robfatland.github.io/nexus/ai)
- [vscode](https://robfatland.github.io/nexus/vscode)


## Linux on a PC running Windows


It is convenient to have a local ("laptop") instance of Linux. This is facilitated
on PCs running Windows via a *feature* called the **Windows Subsystem for Linux (WSL)**. 
This allows us to run Linux without needing a VM to run on the PC.


When setting up a hosted Linux environment in this context: Activate and use 
the Windows Subsystem for Linux ***version 2*** (WSL-2). See which version is active 
by opening a Command Prompt window as Administrator and issuing `wsl -l -v`. To 
change from WSL 1 to WSL 2: `wsl --set-version Ubuntu 2`.


One useful feature of mirroring the cloud VM environment on one's local laptop is 
coding locally, i.e. while not connected to the cloud VM. This is managed via 
`git push` and `git pull` commands.


Some of the GitHub synchronization can be done by means of shell scripts. For example
for repository `ant` one could set up a script called `pull.sh`:


```
echo ant
cd ~/ant; git pull
cd ~
```


This is run using `source pull.sh` and it "pays for itself" in workflow time once the
number of repos to synch exceeds 1.


If using Docker to build containers on the PC: Check that `docker` runs properly in 
`bash`. If `docker` could not be found, one workaround is to start the Docker *app*
which seems to activate docker integration with WSL-2.


The notes that follow on this page for configuring Linux on a cloud VM apply in some
measure to a laptop environment as well.


## Ubuntu Jupyter via ssh tunnel


More elaborate heading: **Bootstrapping an Ubuntu VM to run jupyter with a GitHub repo: Via an ssh tunnel**


The Bourne Again Shell (`bash`) together with `ssh` is our first resource in managing cloud Virtual Machine use 
as a research environment. The goal is to configure a cloud VM to have a GitHub repo and some data science
libraries, and then finally to start and use a Jupyter notebook server. 


> These notes were developed on AWS; and should be validated on other clouds.


- AWS Console: Find and select the EC2 instance
- Connect button > Connect page > Use EC2 Instance Connect > Connect
- Should reach a black screen with a `bash` prompt.
- Alternatively, from a laptop: `ssh -i ~/.keypairs/CloudKeypair.pem ubuntu@123.123.123.12`


> ***PRO TIP*** Getting a publickey error when trying the `ssh` to your VM?
> - Make sure you ran `chmod 400 CloudKeypair.pem`
> - Make sure you are using the correct username: Is it `ubuntu` or `ec2user` or `azureuser` or ...?
> - Make sure the home directory in VSCode is the same as that of your local Ubuntu shell
>     - Sometimes multiple editions of Linux get installed accidentally


Now on the VM: In `~` the `.ssh` directory includes a file `authorized_keys`. This file should
be pre-loaded from a keypair `.pem` file selected or generated during VM spin-up, what we
refer to here as `CloudKeyPair.pem`. The `authorized_keys` file resides on the VM to 
validate `ssh` connections. 


In what follows commands are given without indicating a `bash` prompt. 


Verify the version of Ubuntu using `lsb_release -a`.




This block installs the `miniconda` package.


```
cd ~
which python3
git clone https://github.com/robfatland/ant
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/minoconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```


To ensure access to `miniconda` from the command line, place the following line at the very end 
of `~/.bashrc`:


```
export PATH=~/miniconda3/bin:$PATH
```


Next: Run `~/.bashrc`, confirm the `conda` package manager is available, and 
have conda go through its initialization process.


```
source ~/.bashrc
which conda
conda init
source ~/.bashrc
```


> Note: `conda init` modifies `.bashrc` for conda environment use. It should suffice to run `source ~/.bashrc`.
> It should also suffice to log out and log back in to the VM (`exit`).


Incidentally in addition to package managers `conda` and `pip` there is also available in Linux
the Advanced Package Tool or `apt`. This is specific to Debian-based forms of Linux including
Ubuntu. One can update the package index and then upgrade installed packages using `apt`, as
follows. I claim this is a worthwhile perfunctory action as part of this bootstrap process.


```
sudo apt update -y
sudo apt upgrade -y
```

> Note: `pip` and `venv` can also be installed. The functionality we need is covered by
> `conda` however so this recipe page does not delve into `pip/venv` details.


Continuing with `conda` environments:


```
conda create --name testenv
ls -al ~/miniconda3/envs
conda env list
conda activate testenv
conda deactivate
conda activate testenv
```


The Linux command prompt should now look like: `(testenv) ubuntu@ip10.0.12.240:~$`


Install data science tools including the Jupyter notebook package.


```
conda install jupyter
which jupyter
conda install pandas -y
conda install numpy -y
conda install matplotlib -y
```

Suppose we step away and come back a few days later... what got installed?


```
conda list
```

### jupyter via `ssh` tunnel


We can now set up an `ssh` tunnel to a jupyter notebook server running on the VM.
This is described in more detail on the [nexus *tunnels*](https://robfatland.github.io/nexus/bash/tunnels) 
page. Here is the final command we run on the VM, to start the Jupyter notebook server process as a 
background task:


```
(jupyter lab --no-browser --port=8889) &
```


There will follow from this a lot of text output on the screen. From
this text: Find and copy the Jupyter access token, for example: 
`5ea4583257df6cb49234ff38427cd1e53a80281aeca5d2e3`


From the laptop create the `ssh` tunnel. It will serve as a secure connection between
the VM's Jupyter notebook server and a browser running on the laptop. 


```
 ssh -N -f -i .keypairs/CloudKeyPair.pem -L localhost:7005:localhost:8889 ubuntu@123.123.123.12
```

> Note: This does not reconnect you to `bash` on the cloud VM. Rather it creates a persistent tunnel.


To access the VM Jupyter notebook server via the tunnel: In a browser address bar enter 
the text `localhost:7005`. Another option is to include the token copied above, 
again placed in the browser address bar as:


```
http://localhost:7005/lab?token=5ea4583257df6cb49234ff38427cd1e53a80281aeca5d2e3
```


This command tells your browser to connect to port 7005. This was wired into port 8889 on
the cloud VM (previous `ssh` command). This in turn connects to the jupyter lab notebook
server running on the cloud VM. 


## More on Linux


`bash` is an abbreviation for *the Bourne Again Shell*, an interface to the UNIX operating
system. Or more constructively to its descendent operating system Linux.


### What is the file volume of each subdirectory from a given directory


```
du -h -d1
```


### Running a command sequence


Edit a text file with Linux commands, save it as `go.script`. Issue `source go.script`.
The `source` program will attempt to execute the individual commands in sequence.


Basic `bash` command sequence for file system navigation. This should become 
second nature.


```
pwd
ls
mkdir child
cd child
pwd
cd .
pwd
cd ..
pwd
ls -al
```


### `~/.bashrc`


A filename that begins with a period is considered a *system file*. It 
is not listed by a basic `ls` command; but it is visible from `ls -a`. 


We can edit, customize and run `.bashrc` by typing `source .bashrc`. 
It runs automatically on login. 



### `~/.something` folders


- May involve or retain credentials
- Should be treated very carefully ('administrative secrets') and should never
be copied into working folders or directories.
- In particular we need to be aware of repository clones that are pushed
back to GitHub to a local clone. There (we should assume) they are globally
visible. Careless misuse of `git push` regularly incurs tens of thousands
of dollars in unintended cloud spend.


### File premissions


Each file and directory has an associated access permission string, visible
via `ls -al`. There are three fields each consisting of three values. 
There is also a leading character that tells you if a file is a directory.


Output of `ls -al`: 


```
-rwxrwxrwx 1 kilroy kilroy  2668 Apr 19 15:50 terraform.tf
drwxr-xr-x 1 kilroy kilroy  4096 May 16 19:16 miniconda3
```


The `terraform` file permission field starts with `-` meaning it is an
ordinary file. `d` in this field for `miniconda3` means it is a directory. 
The `rwx` fields that follow are bitwise permission fields, in sequence
left to right for: the User, the Users Group, and Other Users on this 
computer. In the case of `miniconda3`: The Group and Other
permissions prevent anyone other than the User from writing in that folder.


We can modify the permission string for a file using the change mode 
command, `chmod`. We access documentation for this command by issuing 
the manual command: `man chmod`.



### Editors


`emacs`, `nano`, `zile` (etcetera) are popular editors in the same basic
format. A popular alternative is the `vi`, `vim` (etcetera) family of editors. 


### more Linux commands

- `rm file` deletes `file`
- `rmdir dir` deletes a (necessarily empty) directory
- `less file` views the contents of `file` interactively
- `more file` is an older version of `less`
- `cp a b` copies file `a` to a new file called `b`
- `mv a b` renames file `a` to file `b`
- `cat file1 >> file2` copies the contents of file1 onto the end of file2
- `grep mohawk file1.txt` searches for the occurrence of string `mohawk` in `file1.txt`
- `df .` prints the volume of the file system
- `du -h -d1` prints the volume of each directory in the current directory
- `history` lists your recent commands in chronological order, conveniently numbered
    - `!54` re-issues command number 54 from your history
    - `!!` re-runs the last command you gave
    - `!-3` re-runs the command 3 commands back in your history


## The basic idea here


[Return to top of page](#topics)


Many of us are accustomed to experiencing computers as physical boxes with a cable
running to a keyboard and another cable running to a monitor; or as an integrated laptop.
The transition to cloud computing is a potentially challenging process; and in particular
cloud virtual machines (VMs) can be a bit incongruous. 


As users of the 'computer as physical object' we experience our local environment through 
applications that feature very smooth, elaborate graphics that operate on some local data
files that reside on a local storage drive. Furthermore we experience a vast network beyond
our local computer as "a view of the Internet through the windows of browser tabs".
*Now* supposing we begin to explore cloud computing due to the availability of a vast pool 
of computing resources. These we can use and pay for by the hour, so far so good. The
conceptual shift to make this work -- what we write about here -- is a hybridizing of 
the "local computer view" and the "browser tab Internet view". 


The first step in this hybrid concept of computing is to rent a cloud Virtual Machine that 
is exclusively for our use: We are the `root` user. As such we want to install and run 
applications that operate just as an application works on our local laptop. This can be
disconcerting because the cloud VM obviously does not have direct access to data files on
our laptop. But we charge ahead for the moment: This `nexus` website emphasizes two such
applications from the outset, to run on a cloud VM. The first is a **Jupyter
notebook server** supporting Interactive Python (IPython). The second is an Integrated
Development Environment (IDE) that we use to build additional machinery on the
cloud. This IDE is called **VSCode** and it is widely regarded as very useful. 


What these two applications have in common is they present a smooth, elaborate interface
*to a working environment* that appears *on our local computer* (which I will tend to refer 
to as *our laptop*). We have yet to address the data files but that follows below. The 
main idea here is that cloud computing comes *to us, on our local computer* in some sense 
as a new version of our working research environment.  


Let's take this narrative from the top once more to add an important detail. We begin with 
*us researchers* interested in using the cloud. We rent a cloud Virtual Machine to use as 
a potentially very powerful working environment and we set up two applications to run on 
the cloud VM. These present an interface on our laptop by means of a secure connection called 
a *tunnel*, specifically an `ssh` tunnel. This tunnel is fast and secure, meaning there is
no way to intercept the traffic through it in any meaningful way. 


Now to the question of data files. As with the jump to the hybrid picture
of cloud VMs, the data situation is also a conceptual jump, arguably bigger.
The bottom line is: The cloud has unlimited low cost storage that will not
impact a typical research budget until the data volume approaches 200 TB. 
This is primarily due to multiple modes of data storage available on all cloud
platforms, the most fundamental being object storage that features fast access
at a rate of about $0.023 per GB per month.


This description is intended to lay out some details to frame the time commitment necessary
to learn to use cloud computing effectively. Learning the cloud "ropes" is on the one hand not 
trivial; and there are a number of questions and topics remaining to cover. 

















