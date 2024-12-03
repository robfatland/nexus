[nexus](https://robfatland.github.io/nexus), [source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


<img src="assets/img/greenandblack.png"
     alt="green and black icon"
     height="130"
     width="130"
     style="float: center; margin-right: 10px;" />


# nexus

nexus is a threefold documentation resource for open research: native, external (via pointers, usually URLs), and hybrid. 
Hybrid documentation is commentary produced by writing up notes whilst working through an external resource such as a 
tutorial. This is intended to fill context gaps, note gotchas and so on: Make the path easier to follow.


This (gh-pages-branch) source file is [`index.md`](https://github.com/robfatland/nexus/blob/gh-pages/index.md)).


- [published: nexus](https://robfatland.github.io/nexus) ~ [editable `index.md`](https://github.com/robfatland/nexus/blob/gh-pages/index.md)
- [published: lexicon](https://robfatland.github.io/nexus/lexicon) ~ [editable `lexicon.md`](https://github.com/robfatland/nexus/blob/gh-pages/lexicon.md)


## Topics


* [bash and related](https://robfatland.github.io/nexus/bash/), [source](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md)
    * environments
    * git
    * wrenching the appearance of the terminal
    * ssh tunnel
* [artificial intelligence](https://robfatland.github.io/nexus/ai/), [source](https://github.com/robfatland/nexus/blob/gh-pages/ai/index.md)
* [cloud infrastructure](https://robfatland.github.io/nexus/cloud/), [source](https://github.com/robfatland/nexus/blob/gh-pages/cloud/index.md)


### Everything I know about **`git`**


- `git pull` to get the latest; then `git add .` then `git commit -m 'ch ch ch changes'` then `git push`
- From `~` store creds using `git config --global credential.helper store`
- To abandon changes and back up: `git reset --hard HEAD` or if necessary `git reset --hard HEAD~1` etcetera
    - HEAD~n means n commits back



### What is the point of conda environments? 


`conda create/activate` commands engage Python environments as customized versions of 
our base environment. 


- Needed: How does the current environment appear in the Jupyter notebook server interface? 



## bash

### List volumes for only top-level directories

```
du -h -d1
```

### CPU monitoring (many-core machine)


Wes says: "Use **`top`** from the bash command line."


Wes says: "CloudWatch metrics (AWS EC2 console GUI) are delayed, updated once every 5 minutes.
A localized spike in CPU use will take some time to display in the console. It is possible 
to pay for a higher sampling rate in the console... but why?"


### Keep a VM patched

```
sudo apt-get update -y && sudo apt-get upgrade -y
```

# residual remarks from gh-pages README

- The `lexicon.md` list of terms is relevant, needs a ton of work
- The file `index.md` is a compendium of useful recipes including the titular material on simplifying bash windows; more work here also
- What are the relevant related repos $R^3$?
    - `runawaytrain` has AWS Organizations and some API use; so very AWS-cloud-centric 
    - `reorganiseduponthefloor` has notes on `git` and some other possibly useful notes
    - `cbburn` does have some pandas DataFrame manipulation
    - `digitaltwin` is itself
    - `serverless` is itself
    - Left Off Here


[This repo](https://github.com/robfatland/greenandblack/tree/main)
began as a Note To Self on simplifying format of the *Bourne again shell* **`bash`**: 
No colorized text, just green characters on a black background.


- this repo uses GitHub **pages** so switch to the **`gh-pages`** branch to edit content
- customizing `bash` and `vi` is focused on green-on-black, a simple prompt, and text editing
- scope expanded to include
    - **`ssh`** tunnels from one machine to another
    - Difference: **`miniconda`** versus **`anaconda`**
    - Windows PC
        - **`Ubuntu bash`**
        - **`Windows Subsystem for Linux (WSL-2)`**
        - **`VSCode`**?
    - containers
    - conda environments


