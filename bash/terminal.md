[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[bash index source](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md)



# the `bash` terminal

These notes need a big recompile. They were a frustrated response to `bash` terminal colorization,
so reminiscent of fighter pilots turning off all the display clutter in their HUDs. 



## green and black perhaps?


- Context: A PC running the `Terminal` application
    - Tab: `Ubuntu` (a user-friendly distribution built on Debian Linux)
        - There is but one Linux kernel... and many *ornamentations* including Ubuntu
        - Association: Windows Subsystem for Linux version 2 (WSL-2)
        - [`bash`](https://en.wikipedia.org/wiki/Shell_(computing)): the command line interface to Linux, access to operating system services
    - Tab: `ssh` to a cloud VM; similar issues
- Screen text is a lot of (unpleasant) colors: both in `bash` and the `vim` editor
    - `ls` produces a lot of colorizing
    - Plus the command prompt is complicated
- I might enjoy a black screen, green text, and a prompt like `(active-env) cloud$ `



### rewrite paused here...


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


