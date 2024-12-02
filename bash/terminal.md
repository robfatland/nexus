# the bash terminal

## Just green and black please

- I work on a PC running a `bash` shell terminal probably associated with the Windows Subsystem for Linux v2 (WSL-2 ("Weasel"))
- I am logged in to a Virtual Machine on the cloud
- The text is a lot of nauseating colors: both in the `bash` shell and in the `vi` editor
    - Note: At some point `vi` became `vim` but they are the same thing
    - The `ls` command seems to be doing a lot of colorizing, in particular
    - oh also the prompt is some byzantine 'meaningful' string
- I just want green text on a black background and a prompt like `(active-env)vm>`



### **`bash`**

The Ubuntu bash shell running on a Windows PC can be customized independently from
customizing bash on a VM. 

# left off here

- From the top window bar: Right click, select Properties, and set Color to green on black
- Increase font size, adjust whatever else you like
- Type `ls -al` to observe that *color support* is still enabled. Yeccch.
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

`vi` and `vim` are the same editor, specificially an ancient text editor 
with arcane syntax inherited from an even older editor called `ed`. `vim` 
is the modern version of `vi`. 


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


