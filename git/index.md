[nexus pub](https://robfatland.github.io/nexus), [root index src](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[main branch](https://github.com/robfatland/nexus/tree/main)




# `git` and `GitHub`


The most *basic* `git/GitHub` scenario uses GitHub as a stable safe backup for my software. I tend to develop this
software on a local machine like a laptop. More involved scenarios follow: What if I am collaborating in a team? 
What if I need to run my project code on a more powerful computer? And so on. For the moment I will kick these
considerations down the road and stick with "GitHub is my code backup. A truck can run over my laptop and I
will not have lost any work."


Suppose I have a [GitHub](https://github.com) account under the name `lemon` and I create a repository called `ocean`. 
I want to edit `ocean` locally; so in my `bash` shell on my laptop I execute

```
cd ~
git clone https://github.com/lemon/ocean
```

Now I `cd` into this directory and begin editing content. Maybe I add some Jupyter notebooks and some
small data files. I want now to push the edits back up to GitHub to replace the older version residing
there. This way I have updated my *safe code backup in the cloud*. The update requires four `git` commands:


```
cd ~/ocean
git pull
git add .
git commit -m 'a comment on what I edited just now`
git push
```


Why is the first `git` command `git pull`? This is out of habit in case I work occasionally from a
different computer. If I have committed changes from another computer (so the GitHub copy is "ahead"
of my local copy) I want to update my local copy to be in synch. As I am doing this update from
my current local computer the operation is a `pull`. This can create collisions in repo content 
that are not easily resolved. So both before working on the repo and before doing a push it is
a good habit to "make sure the coast is clear" by running `git pull`. 


In an ideal world all I need to know to use `git` and `GitHub` are these five `git` qualifiers:
`git clone`, `git pull`, `git add`, `git commit` and `git push`. In practice however there are 
some other `git` skills that are worth learning. There is also the useful step of setting up
automatic authentication using a token so that I do not have to bother with that every time I do 
a push. 


## Notes on what else


- From `~` store creds using `git config --global credential.helper store`
- To abandon changes and back up: `git reset --hard HEAD` or if necessary `git reset --hard HEAD~1` etcetera
    - HEAD~n means n commits back
 


# Residual notes relocated but not evaluated


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


