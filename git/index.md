[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


# `git` and GitHub


"If it's not in `git` it doesn't exist." -Chris Simmons


## The levels of `git`


- Level 0: The gh-pages gotcha (multi-branch repos)
- Level 1: Basics — the six commands you need
- Level 2: Resolving conflicts, stashing
- Level 3: GitHub integration, branching, pull requests, actions


## Level 0: The gh-pages gotcha


This applies to repos like `nexus` that use GitHub Pages on a `gh-pages` branch.
The default `git clone` only gives you `main`. To get the `gh-pages` content:


```
cd ~
git clone -b gh-pages https://github.com/robfatland/nexus nexus-pages
```

Alternatively, use `git worktree` to have both branches checked out simultaneously:

```
git -C ~/nexus worktree add ~/nexus-pages gh-pages
```

This creates a second working directory for the `gh-pages` branch while sharing
the same underlying repo history.


## Level 1: Basics


A [GitHub](https://github.com) account has an organization name — I'll use `lemon` — so we have
`https://github.com/lemon`. Within that we create repositories, e.g. `https://github.com/lemon/ocean`.


### Create and clone a repo

```
cd ~
git clone https://github.com/lemon/ocean
cd ocean
```

### The daily workflow: pull, add, commit, push

```
cd ~/ocean
git pull --rebase
git add .
git commit -m 'a comment on what I modified just now'
git push
```

Why `git pull --rebase` first? If you've committed changes from another machine, the GitHub
version may be "ahead" of your local copy. Pulling first brings in those changes so your
push merges cleanly. If `git pull --rebase` generates an error, reverse with `git rebase --abort`.
See [this YouTube video](https://youtu.be/xN1-2p06Urc) for more on why `--rebase`.


### Synching multiple repos with a script

For multiple repos, a shell script saves time:

```
# pull.sh
echo ant
cd ~/ant; git pull
cd ~
```

Run with: `source pull.sh`


## Level 2: Resolving conflicts

When `git pull` encounters conflicting changes, git marks the conflicts in the affected files.
Open them, look for `<<<<<<<`, `=======`, `>>>>>>>` markers, resolve manually, then:

```
git add <resolved-file>
git commit -m 'resolved merge conflict'
git push
```

### Stashing

If you have uncommitted changes and need to pull:

```
git stash
git pull --rebase
git stash pop
```


## Level 3: Advanced topics


- **Automatic authentication**: `git config --global credential.helper store`, then push once with your token
- **Large data**: Keep repos under ~100MB. Use `.gitignore` to exclude data files.
- **Undoing mistakes**: `git reset --hard HEAD` (discard uncommitted changes) or `git reset --hard HEAD~1` (undo last commit)
    - HEAD~n means n commits back
- **Branching and pull requests**: For collaborative workflows (not covered here yet)


## The "nuclear option" for recovery

Sometimes edits and pulls and pushes cross wires. A pragmatic fix:

1. Rename your local directory: `mv myrepo myrepo_oops` (it's now just a "source bin", no longer a git repo)
2. Clone fresh from GitHub: `git clone https://github.com/lemon/myrepo`
3. Copy your good changes from `myrepo_oops` back into the fresh clone
4. `git add . && git commit -m 'recovered' && git push`

Conversely if GitHub is busted: Create a new repo on GitHub, clone it locally, copy in your good local files, push.

This doesn't touch 94% of git's powerful features like rollbacks. It's a basic get-started toolkit.
