<img src="assets/img/greenandblack.png"
     alt="green and black icon"
     height="130"
     width="130"
     style="float: center; margin-right: 10px;" />


# nexus

nexus is a threefold documentation resource for open research: native, external (via pointers, usually URLs), and hybrid. 
Hybrid documentation is commentary produced by working through an external resource such as a tutorial. This is intended 
to fill context gaps, note gotchas and so on: Make the path easier to follow.


This (gh-pages-branch) source file is [`index.md`](https://github.com/robfatland/nexus/blob/gh-pages/index.md)).


- [published: nexus](https://robfatland.github.io/nexus) ~ [editable `index.md`](https://github.com/robfatland/nexus/blob/gh-pages/index.md)
- [published: lexicon](https://robfatland.github.io/nexus/lexicon) ~ [editable `lexicon.md`](https://github.com/robfatland/nexus/blob/gh-pages/lexicon.md)


## How is this site built and published? 


This **nexus** repo uses a [Jekyll](https://jekyllrb.com/) template (the free service is called *GitHub pages*) 
to generate a nicely formatted static website.  The content resides in the repo on a code branch called `gh-pages`. 
Publication is triggered automatically after each *commit*. URLs:


- [main branch of the nexus GitHub repo](https://github.com/robfatland/nexus/tree/main)
- [gh-pages branch](https://github.com/robfatland/nexus/tree/gh-pages)
- [The nexus static website](https://robfatland.github.io/nexus/)


Here is how to get one of these https://**organization**.github.io/**repo** websites started:


- Create some repository on GitHub
- Menus: Github --> repo --> Settings --> **pages** tab on the left; choose a *theme*
- Switch to the `gh-pages` branch: From the `Main` branch, use the chooser
- At the documentation site it will be `index.md` that renders (not a README)
    - Edits can be a little slow to propagate; refresh!
- The root directory `index.md` renders as default content
    - Add other folders and markdown; but cross reference using documentation website URLs, not GitHub URLs
        - Example: **`https://organization.github.io/repo-name/subfolder`** renders the **`index.md`** therein



## Topics


* [wrenching the terminal](https://github.com/robfatland/nexus/blob/gh-pages/bash/terminal.md)
published [as](https://robfatland.github.io/nexus/bash/terminal).


# left off here


* [ssh tunnel](https://robfatland.github.io/nexus#ssh-tunnel)
* [bash](https://robfatland.github.io/nexus#bash)



## motivating rant please?


I want to understand--say--my Linux bash installation on my Windows laptop... and I want simple
green text on a black background.  Not a lot of 'informative' colorized text. I did it once...
long ago... but there were
all these squonking little details. Every two years or so, give or take, I have to drag through
the same piddly little web searches and glaring my way through Stack Overflow answers...rrrrrr...
You know what this is? This is the curse of having a semi-IT
job while being a not-very-IT personality. So I put in some extra effort on these notes
and every couple years they will save me... hours? days? minutes? of teeth gnashing.







### Everything I know about **`git`**

- `git pull` to get the latest; then `git add .` then `git commit -m 'ch ch ch changes'` then `git push`
- From `~` store creds using `git config --global credential.helper store`
- To abandon changes and back up: `git reset --hard HEAD` or if necessary `git reset --hard HEAD~1` etcetera
    - HEAD~n means n commits back



### What is the point of conda environments? 


`conda create/activate` commands engage Python environments as customized versions of 
our base environment. 


- Needed: How does the current environment appear in the Jupyter notebook server interface? 


## ssh tunnel

### Outline


I want to run Jupyter on a secure VM inside the AWS cloud on a private subnet. Let's call this VM **`worker`**.
I have an intermediary bastion server called **`bastion`**. I'm going to connect from my local machine to
**bastion** to **worker** so that in my browser I see a Jupyter notebook server that is in fact running on **worker**. 
That means a two-hop ssh tunnel.


### Procedure


If **`bastion`** has a moving target public ip address: Assign it a fixed ip address. For example on AWS
this is called an *elastic ip*. Now that ip address can be baked into a connect alias.


- From **`local`** `bash`:

```
 $ ssh -i bastion.pem ubuntu@12.23.34.45
```

- Customize the environment... I hear green and black is nice
- From **`local`**: Move the `worker.pem` file to **`bastion`**
 
```
$ sftp -i bastion.pem ubuntu@12.23.34.45
sftp> put worker.pem
```

- **`ssh`** from **`local`** to **`bastion`** to **`worker`**
    - `ssh ubuntu@12.23.34.45 -i bastion.pem`
    - `ssh -i worker.pem ubuntu@10.0.1.234`
        - This uses the VPC private subnet ip address for **`worker`**


- On worker start a headless Jupyter notebook server
    - `(jupyter notebook --no-browser --port=8889) &`
        - The choice of port is fairly arbitrary; but we do not want it to collide with a port that is in use
        - This command produces a lot of output
        - Towards the end: copy the long token string
            - It looks like **`4109891ab3e0ec38c2aec9c427c8be11eda975ab2882a52a`**
    - `exit`
    - First time doing this: Log back in to **`worker`** and verify the server is still running 
        - `ps -ef | grep jupyter`
        - `exit`
    - On **`bastion`** create an ssh tunnel
        - `ssh -N -f -i worker.pem -L localhost:7005:localhost:8889 ubuntu@10.0.1.234`
            - Same as above remark: On port choice 7005
            - This command associates inbound **`bastion`** traffic on port 7005 to outbound > **`worker`** port 8889
        - `exit`
    - On **`local`** create the second part of the tunnel to **`bastion`**
        - `ssh -N -f -i bastion.pem -L localhost:7004:localhost:7005 ubuntu@12.23.34.45`
    - **`local`** browser address bar
        - `localhost:7004`
        - If promnpted: paste in token string copied above
  
  

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




