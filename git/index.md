[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main branch](https://github.com/robfatland/nexus/tree/main)




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


