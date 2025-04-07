[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md),
[bash index source](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md)



# git

## The three [sic] levels of `git`


- Level 0 the gh-pages gotcha
- Level 1 main (bulldozer) idea: Requires a basic set of six commands
- Level 2 mezzanine idea: Stashing and resolving conflicts
- Level 3 advanced uses: GitHub integration, branching, pull requests, actions, ... 


### Level 0 The gh-pages gotcha


This Level 0 deals with a *gotcha* that applies for example to this `nexus` repo: The repercussions
of multi-branch repos in relation to the `git` command. We might as well dispense with this before
getting into the ABCs of `git`. 


`git` manages time evolution of complex software projects by means of *branches*. In particular
`GitHub` has a built-in way to reflect repository content into a reader-friendly website by means
of an optional template called `gh-pages` (for "GitHub pages"). The default branch for a repo is
called `main` and then when we opt in to `gh-pages` there is a branch called, yes, `gh-pages`. Now
on the browser it is easy to bounce between branches in the console: There is a branch selector
drop-down. But when issuing `git clone my-gh-pages-based-repo` I only get the `main` branch. I do
not get the `gh-pages` content. So what to do here? 


The experiment I am trying is to use the `-b` switch for `git clone` to get the `gh-pages`
branch... but I think I am not supposed to do this *elsewhere* but I am doing that *anyway*.


```
cd ~
mkdir gh-pages_branch
cd gh-pages_branch
git clone -b gh-pages https://github.com/robfatland/nexuse
```


...then edit this file and do a push to see that it appears properly modified at GitHub...


...and indeed this worked as expected. This allows me to introduce IPython noteboooks 
into the gh-pages branch since they are easier to manufacture and refine on my workstation.



### Level 1 Basics

I want to start a new project with its own hermetic *repository*. I do this on the GitHub website to create
an empty repository; perhaps with a `README.md` file and a use license like the MIT one. So far so good...
but what am I going to get out of doing this empty box business? 

- `git clone` makes a local copy of a GitHub repo

### Level 2 Resolving conflicts

### Level 3 GitHub integration
