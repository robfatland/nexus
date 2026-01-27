[nexus published](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


## R Studio Server on a GCP Compute Engine VM


The Google Cloud Platform (GCP) like other cloud platforms includes both managed and un-managed versions 
of cloud services. This page in particular looks at the installation of R Studio for use by a research
team in both unmanaged and managed context, respectively using GCP Compute Engine and GCP Workstation.


Directly below I annotate setting up R Studio Server on an unmanaged VM (the GCP jargon for this is
"Compute Engine"). Below that I annotate setting up the managed alternative, R Studio Dekstop on
a GCP Workstation. The latter is more expensive to operate and the setup process is a bit more 
arcane (it incorporates Containers and so on); but the end result is more of a desktop working 
environment. For more: See below the section on **Setting up a GCP Workstation**.


> Note: I do not touch on paid versions of R Studio such as `Posit Workbench` or `R Studio
Desktop Pro`.


### Overview of the procedure


The cloud VM I use is an "e2-medium" that will cost like $25 / month. I suggest doing an installation 
on a small machine for practice; then delete it (or just stop it) and have another go on a more 
powerful VM. The downside to doing just one install on the powerful instance is missing the repetition 
reinforcement.


Now to get on the Ubuntu Linux VM `bash` command line. There are multiple ways to get there but the 
simplest is to click a button in the GCP console that launches a dedicated pop-out `bash` window. 


From the command line on the VM it takes about five commands to install R, install the R Studio
Server, and get the Server running. By default it latches onto port 8787; where it intends 
to send/receive information supporting the R Studio Server GUI. By default this port is closed to 
the outside world; the only open port is 22 for `ssh`.


A final Linux command line task is to create a User called `rstudio` with a password.


Now: Back in the GCP console for the next step: We create a Rule that permits connecting to port 
8787 from anywhere on the internet. We name this rule `allow-rstudio`. It exists in a vacuum. 


> Note: "Can connect from anywhere on the Internet" sounds a bit unsafe, especially with
> a simple username/password authentication. This is something to return to once the basic
> setup is working.


Now (still in the console) navigate to the the VM and associate the above `allow-rstudio` Rule 
with Network settings. We can now connect to R Studio Server from a browser window on a laptop. 
In the browser window: `http://112.48.76.111:8787` noting the port appended. 


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
    - I used a Coding Assistant to diagnose the problem
    - This proved to be version incompatibility: R Studio Server ~ R.
    - The CA gave me revised installation commands: fix worked

 
### Operation issues


To be aware of:


- Shutting the VM off, starting it again
    - The VM can be stopped from the console so as not to pay the hourly rate when it is not in use
    - Re-starting it (say the next day): See above command
    - Not covered here:
        - Automatically start R Studio Server each time the machine boots
        - Automatically stop the VM every workday at 7PM
        - Automatically start the VM every workday at 8AM
- Backing up the VM as a Machine Image
    - Serves as a backup of the entire machine
    - Can be used to start up a new VM with more compute power, other parameters changed
- Re-sizing the root disk
    - Do this when you realize you need more disk space, for example for data
- Revisit the Firewall rule permitting access from anywhere
    - Modify the CIDR block to permit traffic only from a small range of ip addresses
- Allocating and mounting an Object Storage bucket as a pseudo-drive on the VM
    - Intended to provide vast cheap (but not super-fast) data storage capacity
 

## R Studio Desktop on a GCP Workstation


In the sections above we have a procedure for setting up a Google Cloud Platform (GCP)
"Compute Engine" instance (a Virtual Machine (VM)) and connecting over the Internet
to set up a browser-based R Studio Server environment. This section will go 
through the alternative option of using a GCP Workstation to install and access
R Studio Desktop. (Both options avoid the paid license.)  Before diving into the 
Workstation setup procedure here are some Coding Assistant remarks characterizing 
the differences:


##### Major Differences


<table style="margin-left: 0;">
<tr><th>Aspect</th><th>Compute Engine</th><th>Workstations</th></tr>
<tr><td>Access</td><td>Web browser (port 8787)</td><td>Remote desktop + native apps</td>
<tr><td>RStudio Type</td><td>Server edition</td><td>Desktop edition</td>
<tr><td>Setup</td><td>Manual installation</td><td>Container-based</td>
<tr><td>Management</td><td>DIY</td><td>Fully managed</td>
<tr><td>Cost</td><td>VM + Storage</td><td>Higher (managed service premium)</td>
<tr><td>Scaling</td><td>Manual</td><td>Auto-scaling</td>
<tr><td>Security</td><td>Manual firewall</td><td>Built-in IAM integration</td>
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

