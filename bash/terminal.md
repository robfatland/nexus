[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)

# the bash terminal


## green and black please


- I am working on a PC running the **Terminal** application
    - I have a tab open that is running the Ubuntu
*Bourne Again SHell* ([`bash`](https://en.wikipedia.org/wiki/Shell_(computing)))
    - this is (most likely) associated with the Windows Subsystem for Linux
        - This Linux subsystem is (2024) on version 2 hence WSL-2 (which I pronounce as 'Weasel')
        - Again this is the Ubuntu distribution of Linux
            - There is only one Linux kernel...
                - ...but there are many *ornamentations* of this kernel available out there...
                - ...and these are termed **distributions**
                - ...of which Ubuntu is one. Debian is another, Red Hat is another, and so on
    - `bash` is the command line interface to Linux: Access to operating system services
- Perhaps I am also logged in to a Virtual Machine (henceforth ***VM***) on the cloud
    - ...but I will ignore this for the moment
- The screen text is in a lot of nauseating colors
    - both in the `bash` shell and in the `vi` editor
        - Historical note: At some point the `vi` editor became `vim`. They are the same thing.
    - Also the `ls` command seems to be doing a lot of colorizing
    - Also the prompt is some byzantine 'meaningful' string
- I want green text on a black background and a prompt like `(active-env)vm>`



### **Terminal: Local `bash`**


Rewrite got to about here...


- Top-of-window bar > clean spot > right click > Settings
- Use the left sub-topic menu to go through and customize everything that looks worth the bother
- Create a new color scheme, re-name it, make green the foreground, set it to default
- issue the command `ls -al .bash*` to see `bashrc`-related files


### historical version here down


- Comment out these lines in `.bashrc`

```
# enable color support of ls and also add handy aliases
#if [ -x /usr/bin/dircolors ]; then
#    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
#    alias ls='ls --color=auto'
#    #alias dir='dir --color=auto'
#    #alias vdir='vdir --color=auto'
#
#    alias grep='grep --color=auto'
#    alias fgrep='fgrep --color=auto'
#    alias egrep='egrep --color=auto'
#fi
```

- Command line: `source ~/.bashrc`
- Check with `ls -al` again


### **Terminal: cloud VM**


### green text


For green text type this on the command line: `echo -e "Default \e[32mDefault"`


### prompt fix


The prompt's job is to tell me which computer I am entering commands on (and possibly whether
I am working inside a conda environment).


- Edit `~/.bashrc' in `vi`, scroll past the `$PS1` stuff
    - `$PS1` is a variable for the default bash prompt 
- Add this line:


```
PS1="my computer> "
```

- Command line: `source ~/.bashrc`

Now the prompt tells me when I am working on my local machine.
For VMs: Use simple but instructive prompts in like fashion. 

A conda environment name will be prepended to this bash prompt. By default this
prompt will be `(base) my computer> `. This is ok by me: When I switch
environments by means of `conda activate some-environment` the prompt will 
automatically change the prompt to `(some-environment) my computer>`. 


### ls fix

To change the colors of the text produced by `ls` check an online resource like [**this**](https://linuxhint.com/ls_colors_bash/).
The bare-bones to make directory names green is like so: 


- `dircolors -b >> .bashrc` appends the current **ls** color scheme to `.bashrc`
- edit `.bashrc` and go to the end of the file 
- Observe the dense text we just added:

```
LS_COLORS=`rs=0:di=01;34....etcetera etcetera etceters....;export LS_COLORS`
```

- These are key-value pairs. 
- The color green is '32' so find the entry for `di` (directory) and set it to `di=01;32`. 
- `source ~/.bashrc`
- `ls -al`


### **`vi`** fix

`vi` is an ancient text editor with arcane syntax inherited from an even older editor called `ed`. 
`vim` is the modern version of `vi`. 


To disable a profusion of colorized text in `vi`: In escape mode type `:syntax off`. 


To disable a profusion of colorized text **permanently**:


```
vi ~/.vimrc

<escape>
G
o
syntax off
<escape>
:wq
```

- Re-run `vi` to verify this worked


