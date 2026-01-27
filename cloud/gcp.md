[nexus published](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


## R Studio Server on a GCP Compute Engine VM


The Google Cloud Platform (gcp) like other cloud platforms includes both managed and un-managed versions 
of cloud services. This page in particular looks at the installation of R Studio for use by a research
team in both unmanaged and managed context, respectively using GCP Compute Engine and GCP Workstation.


Directly below I annotate setting up R Studio Server on an unmanaged VM (the GCP jargon for this is
"Compute Engine"). Below that I annotate setting up the managed alternative, R Studio Dekstop on
a GCP Workstation. The latter is more expensive to operate and the setup process is a bit more 
arcane (it incorporates Containers and so on); but the end result is more of a desktop working 
environment. For more: See below the section on **Setting up a GCP Workstation**.


### Overview of the procedure

The cloud VM is an "e2-medium" that will run like $25 / month. I'd suggest doing the installation on
that for practice; and then delete it and have another go on a more powerful VM. The only downside to
doing just one install on a powerful machine first go is it misses the repetition reinforcement.


Now we want to get on the VM command line. The operating system is Ubuntu Linux and the shell to use 
is the `bash` shell. There are multiple ways to get there but the simplest is to click a button in
the GCP console that launches a dedicated `bash` window. This is described below. 


Now from the command line on the VM it takes about five commands to install R, install the R Studio
Server, and get the Server running. By default it latches onto port 8787; that is where it intends 
to receive User input and send back R Studio responses. But by default this port is closed off to 
the outside world. In fact the only open port is port 22 which is where the `bash` shell is connected.


One more small task from the command line is to create a User called `rstudio` with a password so 
we can authenticate when we connect to R Studio Server. 


We're back in the GCP console for the next step. Now we create a Rule that says "Ok to connect to port 
8787 from anywhere on the internet". We name this rule "allow-rstudio". It exists in a vacuum for the 
moment. It might sound a bit unsafe and that's absolutely correct, especially with such a simple 
username/password setup. So this is something to return to once the basics are working.

Now (still in the console) we navigate over to the control panel for the VM. (We are ignoring the `bash`
shell at this point.) We associate the above allow-rstudio Rule with our VMs Network settings. That is
all that is required to connect to R Studio Server from a browser window in a laptop. What goes in the 
browser window is described below; it will look like `http://127.48.76.111:8787` where you can see the
port number at the end there. 


### Condensed Procedure


- Use the GCP console to start a VM and then log on to it using the console `ssh` button for the instance
- Issue these Linux commands
    - `sudo apt update`
    - `sudo apt install -y r-base r-base-dev`
    - `sudo apt install -y gdebi-core`
    - `wget https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2024.12.0-467-amd64.deb`
    - `sudo gdebi -n rstudio-server-2024.12.0-467-amd64.deb`
    - `sudo adduser rstudio`
-  Back on the GCP console...
    - Create a Firewall Rule `allow-rstudio` granting TCP access to port 8787 from anywhere
    - Add the tag for this rule to the VM
- In the browser address bar connect via `http://<ipaddress>:8787` and login as user `rstudio`


### Procedure


- Log in to https://console.cloud.google.com; and be sure to choose your intended *project*
    - The following steps can be done using the GCP Command Line Interface (CLI) which is called `gcloud`
    - However these instructions are for doing everything in the console
- GCP console: Create a VM
    - In the Console the VM Create Wizard has about 7 stages (see the left sidebar)
    - We have very little to do here, really only on the first and second of these stages
    - First stage:
        - Chose a clear purpose-specific name for the VM, ideally short
        - Chose the closest possible region e.g. `us-west1` for Oregon. Leave Zone as `any`.
        - Instance type: Select `E2`; specifically e2-medium. This will run about $25/month
    - Do not jump the queue by clicking the **Create** button; there is more to be done
    - Do click the second stage (left sidebar) to chose `OS and Storage`
        - Change the operating system: Select a current version of Ubuntu; the rest default
    - Go to the next tab: Data Protection. Consider the options that suit your project.
        - If you regularly commit your code to GitHub then this is redundant
        - If your data / results are expensive to reproduce: Read more about Backups and Snapshots
    - Go to the fourth tab: Networking
        - Do not change anything here; just note the Firewall options for context
        - The eventual idea will be to open port 8787 for `tcp` traffic to support R Studio Server
    - Click on the Create button
        - Go to the VM Instances, find the running instance, note the **External** IP Address
        - For example 12.123.12.123. I will refer to this as <ip-address> below
- GCP console: Connect via `ssh` to the VM
    - Navigate in the console to the VM instances table as described above
    - Find the VM you just started: Notice there is a "Connect" column
    - Under that column, for your instance, click `ssh`
        - This opens up a terminal window where you will have a `bash` prompt on the VM
        - You are the root user so you invoke this when necessary with `sudo`
- Do some configuration steps on the VM from the `bash` shell
    - `sudo apt update`
    - `sudo apt install -y r-base r-base-dev` (this takes a minute or two)
    - Install RStudio Server: 3 commands
        - Note: The `wget` command stipulates a particular version...
            - ...which (version shown: 26-JAN-2026) can become outdated...
            - ...in which case one would look up current versions
        - `sudo apt install -y gdebi-core`
        - `wget https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2024.12.0-467-amd64.deb`
        - `sudo gdebi -n rstudio-server-2024.12.0-467-amd64.deb`
- Create an RStudio user
    - On the `bash` command line: `sudo adduser rstudio`
    - Set a password; I used `krypton`
    - Enter additional User metadata if useful
- Open firewall port 8787 using the GCP Console:
    - Go to VPC network --> Firewall
    - Click `Create Firewall Rule`
    - Configure:
        - Name: `allow-rstudio`
        - Direction: Ingress
        - Action on match: Allow
        - Targets: Specified target tags
        - Target tags: rstudio-server
        - Source filter: IP ranges
        - Source IP ranges: `0.0.0.0/0`
        - Protocols and ports: Check "Specified protocols and ports"
        - TCP: `8787`
    - Click `Create`
- Add the tag for this Rule to the VM:
    - Go to Compute Engine --> VM instances
    - Click your VM name
    - Click `Edit` at top
    - Scroll to Network tags
    - Add: `rstudio-server`
    - Click `Save`
    - Now port 8787 is accessible from anywhere (which in Network-speak is `0.0.0.0/0`)
- Connect through a browser
    - In the address bar type `http://<ipaddress>:8787`
    - Login as user `rstudio` using the password you chose


### Diagnostic remarks


- From the `bash` shell: `sudo systemctl status rstudio-server` will confirm the server is running
    - Restart: `sudo systemctl restart rstudio-server`
- `R --version` to see which version of R is installed
- `which R` to see where R runs *from*
- On my first go I was able to log in but the Studio then failed to start up
    - I used a Coding Assistant to diagnost the problem down
    - This proved to be a version incompatibility: R Studio Server versus R.
    - The CA gave me revised installation commands and this fixed the issue
 
### Shutting it off, starting it back up

- The VM can be stopped from the console so as not to pay the hourly rate when it is not in use
- Re-starting it (say the next day): See above command
- Not covered here: Re-starting R Studio Server every time the machine boots
    - This can be built into the VM startup procedure
 

## R Studio Desktop on a GCP Workstation


In the sections above we have a procedure for setting up a Google Cloud Platform (GCP)
"Compute Engine" instance (a Virtual Machine (VM)) and connecting over the Internet
to set up a browser-based R Studio Server environment. This section will go 
through the alternative option of using a GCP Workstation to install and access
R Studio Desktop. (Both options avoid the paid license.)  Before diving into the 
Workstation setup procedure here are some Coding Assistant remarks characterizing 
the differences:


##### Major Differences


Aspect	        Compute Engine	            Workstations
Access	        Web browser (port 8787)	    Remote desktop + native apps
RStudio Type	Server edition	            Desktop edition
Setup	        Manual installation	        Container-based
Management	    DIY	                        Fully managed
Cost	        VM + storage	            Higher (managed service premium)
Scaling	        Manual	                    Auto-scaling
Security	    Manual firewall	            Built-in IAM integration



<table style="margin-left: 0;">
<tr><th></th><th>p:</th><th>2</th><th>3</th><th>5</th><th>7</th><th>11</th><th>13</th><th>moonlight</th></tr>
<tr><td>$\alpha:$</td><td><b>1</b></td><td>1</td>
    <td>2</td><td>4</td><td>6</td><td>$\cdot$</td><td>12</td><td>drive</td></tr>
<tr><td></td><td><b>2</b></td><td>2</td><td>6</td>
    <td>$\cdot$</td><td>$\cdot$</td><td>$\cdot$</td><td>$\cdot$</td><td>$\pi$</td></tr>
<tr><td></td><td><b>3</b></td><td>4</td><td>$\cdot$</td>
    <td>$\cdot$</td><td>$\cdot$</td><td>$\cdot$</td><td>$\cdot$</td><td>on</td></tr>
</table>


##### Advantages of Workstations


- Native RStudio Desktop (not web interface)
- Better performance for graphics/plotting
- Integrated file management
- No port management needed
- Automatic backups


##### When to Use Each


Compute Engine: Simple, cost-effective, web-based R development
Workstations: Enterprise environments, native desktop experience, managed infrastructure


Bottom Line: Workstations provide a more desktop-like experience but at higher cost and 
complexity compared to the simple RStudio Server on Compute Engine.
