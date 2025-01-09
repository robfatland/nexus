[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


`bash index.md`: will point to terminal, tunnel sub-pages and other topics


# `bash` tactics


This region of `nexus` is focused on configuring and operating a cloud Virtual Machine for 
use in some form of data science. There are presumed precursor steps: Secure a VM, download
a keypair file `CloudKeyPair.pem` and change its file permissions to `0400`. Log in to a 
`bash` terminal on this VM. That's the main substance of the precursor steps before jumping into
the bootstrapping process outlined below. 


Sub-pages of this page go into sub-topic details: `conda` environments, `git`, `ssh` tunnels,
terminal configuration.


## Bootstrapping an Ubuntu VM to run jupyter with a GitHub repo: Via ssh tunnel


The Bourne Again Shell (`bash`) together with `ssh` is our first resource in managing cloud Virtual Machine use 
as a research environment. The goal is to configure a cloud VM to have a GitHub repo and some data science
libraries, and then finally to start and use a Jupyter notebook server. 


> These notes were developed on AWS; and should be validated on other clouds.


- AWS Console: Find and select the EC2 instance
- Connect button > Connect page > Use EC2 Instance Connect > Connect
- Should reach a black screen with a `bash` prompt.
- Alternatively, from a laptop: `ssh -i ~/.keypairs/CloudKeyPar.pem ubuntu@123.123.123.12`


Now on the VM: In `~` the `.ssh` directory includes a file `authorized_keys`. This file should
be pre-loaded from a keypair `.pem` file selected or generated during VM spin-up, what we
refer to here as `CloudKeyPair.pem`. The `authorized_keys` file resides on the VM to 
validate `ssh` connections. 


In what follows commands are given without indicating a `bash` prompt. The first
block of commands installs the `miniconda` package.


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
http://localhost:8888/lab?token=5ea4583257df6cb49234ff38427cd1e53a80281aeca5d2e3
```


## More about `bash` 


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

















