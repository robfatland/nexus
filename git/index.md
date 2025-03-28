[nexus pub](https://robfatland.github.io/nexus), [root index src](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[main branch](https://github.com/robfatland/nexus/tree/main)




# `git` and `GitHub`


The basic `git/GitHub` scenario has two aims: Create a safe version of a software project (on the cloud) and
manage revisions. The project corresopnds to a **repository** or **repo** residing in a folder with sub-folders.
Most content development happens on either a local machine (laptop, desktop, etc) or on a cloud VM. The latter
in particular if more compute power is needed; or if the project involves some web presence, for example when
building a data source with a dedicated API. We can also create content -- particularly documentation in markdown
format -- directly on GitHub by using the pencil icon at the upper right to go into a text editor mode. 


More involved scenarios for content development follow: Suppose I am collaborating with a team. Suppose 
the repository is automatically being published as a documentation website using GitHub *pages*; and so on. 
Well initially let us stay with "GitHub as safe copy with version control" and if a truck runs over my laptop 
I do not lose any work.


A [GitHub](https://github.com) account has an organization name -- I will use `lemon` -- and therein one or
more repositories. Suppose one of these is called `ocean`. This repository is created in an empty state from
the browser interface to GitHub at `https://github.com/lemon` with appropriate sign-in taken as read.


Now the `ocean` repo exists and I want to start building out the codebase on my laptop. In a `bash` shell 
on my laptop I execute `git clone` as follows:

```
cd ~
git clone https://github.com/lemon/ocean
cd ocean
```

Perhaps I create a couple of Python module files and a Jupyter notebook. Now it is time to synch up with the original
repo on GitHub using `git push`. The verb push the edits back up to GitHub to replace the older version residing
there. This way I have updated my *safe code backup in the cloud*. The update requires four `git` commands (verbs)
but first: There is a warning in [this YouTube video](https://youtu.be/xN1-2p06Urc) about `git pull`. So here
is the sequence with a mysterious qualifier added to `git pull`:


```
cd ~/ocean
git pull --rebase
git add .
git commit -m 'a comment on what I edited just now`
git push
```


Why is the first `git` command `git pull`? If I work occasionally on another computer (office machine, 
cloud VM etcetera) then I may have committed changes from that *elsewhere*. We say that the GitHub 
version of the repo is "ahead" of my local copy). I do `pull` first to bring in those changes where
hopefully they do not conflict with what I have been doing on *this* computer. Now when I do `add / commit / push`
my changes are merged with no errors or conflicts. The topic of collisions is discussed (or *will be* discussed)
in more detail below. To understand the `--rebase` qualifier: Watch that YouTube video. Those folks note: If
`git pull --rebase` generates an error this can be reversed with `git rebase --abort`.


In summary, in an ideal world: All I need in `git` verbs are `clone`, `pull`, `add`, `commit` and `push`. 



## Notes on what else


- Automatic authentication using a token to streamline the `push` process 
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


