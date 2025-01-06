[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


`bash index.md`: will point to terminal, tunnel sub-pages and other topics


### how to bootstrap an Ubuntu VM (AWS Spot case study)

- console: Find instance, check or select
- reboot the VM
- use the Connect button > Connect to instance page > Use EC2 Instance Connect > Connect

```
which python3
git clone https://github.com/robfatland/ant
cd ~
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/minoconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
export PATH=~/miniconda3/bin:$PATH
sudo apt install jupyter-core
which jupyter
sudo apt update
sudo apt upgrade
sudo apt install python3-pip -y
which pip
which pip3
sudo apt install python3.12-venv
python3 -m venv test-env
source test-env/bin/activate
deactivate
source test-env/bin/activate
echo put an alias for this activate command in .bashrc_aliases
pip install pandas
pip install matplotlib
```






### arcane bash task: What is the volume of each subdirectory in this directory?

```
du -h -d1
```


# Draft Material from a previous iteration


This is sort of an introduction; it is not really vetted for use at this time.


## A quick rundown on `bash`


`bash` is an abbreviation for *the Bourne Again Shell*, an interface to the UNIX operating
system. Or more constructively to its descendent operating system Linux.


The transaction is this: You have a prompt that echoes whatever you type at the
keyboard. You go ahead and type a command together with some appended arguments or 
qualifiers, as needed, and you hit the `enter` key, and the shell does its best to 
find and execute that command and provide feedback on how things went, returning
at the end of all this once again to the prompt. 


This command/response pattern is interactive. The commands are programs stored
in memory. 


You may ask: What about automatically running a sequence of commands to accomplish
a larger task. No problem: Edit a text file filled with Linux commands, save it 
as `go.script`, and at the command prompt issue the command `source go.script`.
The shell will attempt to run the `source` program, operating on our file `go.script`;
and the `source` program will in turn attempt to execute the individual 
commands in sequence.


There are three other things to mention. 


First, the file system is organized as a big tree; and we start a couple
levels up from the ground floor in a user home directory, say `/home/rob`. 


* `pwd`
* `ls`
* `mkdir child`
* `cd child`
* `pwd`
* `cd .`
* `pwd`
* `cd ..`
* `pwd`
* `ls -al`


List files with `ls`; and list *all* the files with `ls -al`. 
In your home directory notice there is a file called `.bashrc`. 


Because it starts with a period it is considered a system file 
so it does not get listed by the vanilla `ls` command. This is a script file
that runs when you log in and configures things for you, including what your
prompt looks like. You can edit it and run it again to effect your changes
by saying `source .bashrc`. If you are interested in a bit of customizing
you can ask me about the `greenandblack` repo. But anyway sometimes these
'starts with a period' files are actually directories; and they can be 
surprisingly big. And *sometimes* they can even hold secret things like
github *login credentials*. So it is important to maintain a sense of discretion
when you copy a repo from GitHub to a local clone. Make sure nothing winds 
up in your repo directory that should not be there; because when you run 
`git push` to copy your changes back to your safe copy, there your credentials
will be in public view on GitHub. You would think that nobody will ever notice
because who goes around looking at billions of repos all the time. But the 
answer is: Bots do. And they scrape credentials and do whatever naughty things
they were programmed to do. So that's an introduction to the purpose and perils
of your home directory. 


Third, each file and each directory has an access permission string associated
with it. You will see this when you issue `ls -al`. There are three fields,
each consisting of three values. There is also a leading character that tells
you if a file is actually a directory. Here is an example:


```
-rwxrwxrwx 1 kilroy kilroy  2668 Apr 19 15:50 terraform.tf
drwxr-xr-x 1 kilroy kilroy  4096 May 16 19:16 miniconda3
```


The upper file permission field starts with `-`. This means it is a file. Then is 
has `rwx`, then `rwx` again, and then `rwx` again. The first one means that you,
the User have read/write/execute permissions on this file. The second trio refers
to people in the same user Group as you. The third trio refers to Others; anyone
using this computer. This is really a holdover from when systems were commonly shared
by larger groups of people. However it is good to know what this means; and you can
modify the permission string for any file you own using the change mode command, `chmod`.


By the way the lower file
begins with `d`. This means it is a directory. Notice that in this case the User can
read/write/execute; but both Group and Other users can only read and execute. They 
cannot write changes to this directory. 


## Editors


Many use `EMACS` or similar "light" versions of this popular editor. The pattern seems to be 
that they sacrifice a little bit of real-estate at the bottom of the screen to present a ctrl-key
menu for save/exit/etcetera options. This is one good path to having the means to edit text files.


Another approach is to learn the peculiar syntax of the `vi` editor. `vi` has been improved so 
now it is called `vim`. It has both an `<insert>` and an `<escape>` mode so one has to develop
a little mental bit for which one you are currently in. When in escape mode you can move your 
cursor around or issue terse little commands that appear at the bottom of the screen. This is 
the sort of thing you would learn to do in an afternoon on a "learn vi" interactive website. 


I was introduced to `vi` so that is what I use. I think it is pretty amusing although sometimes
the feature creep has made it look very cluttered; so I've put a little effort into retro-simplification.
Again that is in my `greenandblack` repo. 

## linux commands

- `source fu.script` executes the commands in `fu.script`
- `cd` to change directory`
- `pwd` print working directory
- `chmod` change permissions
- `ls` list directory contents; `ls -al` for a comprehensive view
- `rm file` to delete `file`
- `rmdir dir` to delete a (necessarily empty) directory
- `less file` to view the contents of `file` interactively (remembering that less is more)
- `more file` as an older version of `less`
- `cp a b` to copy file `a` to a new file called `b`
- `mv a b` renames file `a` to be file `b`
- `cat file1 >> file2` copies the contents of file1 onto the end of file2
- `grep mohawk file1.txt` searches for the occurrence of string `mohawk` in `file1.txt`
    - You can also open the file in an editor and search for `mohawk`; a little more time consuming
- `df .` prints the volume of the file system
- `du -h -d1` prints the volume of each directory in the current directory
    - This is a great sanity check to see if any directories have grown monstrous huge
    - You can also use it to descend into a directory and sort out where specifically monsters live
- `history` lists your recent commands in chronological order, conveniently numbering them
- `!54` re-issues command number 54 from your history
- `!!` re-runs the last command you gave


By the way: Certain text files can be edited (with care). For example `.bashrc`. But other files
can be very prone to ***breaking*** when edited as they were not intended for editor-based
modification. A good example is an IPython or Jupyter notebook file (file extension `.ipynb`). 


## git

There are two starting points. First is creating a repo of your own on GitHub from scratch
and then cloning it locally; and modifying the local copy; and updating the GitHub copy; 
then modifying that repo directly on GitHub; and then updating your local copy. Let's call
that **Track A**. 


Second is copying an existing repo that belongs to someone else as your starting point.
We'll call that **Track B**.

### Track A

- Log in to GitHub
- Create new repository
    - Give it as simple a name as you can think of
    - Add an MIT License (assuming it is public / open source)
    - Start it off with a `README.md` file; you don't need to edit this.
    - Save it and note the clone URL
- On your local computer
    - `cd ~`
    - `git clone https://github.com/youraccount/yourrepo.git`
        - A clone will appear as subdirectory `yourrepo`
        - You are now all set to start making modifications to the repo

Time to synch back to the GitHub copy, i.e. push your changes to GitHub.

- On your local computer
    - `cd ~/yourrepo` to put yourself in the base directory of the repo
    - `git pull` to make sure nothing has changed at GitHub
        - Sometimes I edit README files on GitHub and then forget I did so
    - `git add .` makes all your changes available to commit
    - `git commit -m 'a short remark telling what I did'`
    - `git push`
        - Here you should need to authenticate: Username and GitHub password
        - You can search on 'saving github credentials locally' to make this step automatic

That should do it. Once you have it down it is pretty fast; just three commands: `git add .; git commit; git push`.

## Track B

On GitHub: Fork the source repo you are interested in (provided this does not step on anyone's 
intentions concerning use). Now proceed as in **Track A**.


## Something goes wrong


Sometimes edits and pulls and pushes and mistakes can cross wires. A drastic-sounding solution 
that isn't really drastic is to re-name your local directory `myrepo_oops` and regard is as a 
"source bin". It is no longer a git repository; but it has some good stuff in it that *isn't* 
on GitHub just yet. You just set that aside for a moment. 


Now go and do the clone from GitHub to your local machine.
You can do this because the repo directory isn't there anymore; you renamed it.
So you have a fresh, accurate clone of your GitHub repo on your local machine.


Now you can move things you changed from your feeder bin directory back into your cloned repo
folder. You should be able to git add/commit/push this back to GitHub and if all goes well you
are back to good. 


Conversely if things get busted *on GitHub*: Similar procedure. Here I'm assuming you have 
all the stuff you need on your local machine. So create a new repo on GitHub with a new name.
Clone that locally. Update the local copy from the local good stuff. `git push` that back up 
to GitHub. Now you can even delete the old GitHub repo if you like. 


This doesn't even touch 94% of GitHubs powerful features like rollbacks and such. This is just
a basic get started toolkit. Plan to learn `git` properly and teach it to me.













