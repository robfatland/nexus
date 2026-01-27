[nexus published](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


# gcp


The Google Cloud Platform (gcp) has some excellent features. Also, like with other cloud platforms, there are managed and
un-managed versions of services. Here we annotate the process of setting up RStudio on an unmanaged VM (GCP jargon: 
"Compute Engine").


- Log in to https://console.cloud.google.com; and be sure to choose the intended *project*
    - The following steps can be done using the GCP Command Line Interface (CLI) which is called `gcloud`
- GCP console: Create a VM
    - In the Console the Wizard has about 7 stages (left sidebar)
    - We have very little to do here, really only on the first and second stages
    - First stage: Chose a clear purpose-specific name for the VM
        - Chose the closest possible region e.g. `us-west1` for Oregon. Leave Zone as `any`.
        - Instance type: Select `E2`; specifically e2-medium. This will run about $25/month
    - Do not jump the queue by clicking the **Create** button; there is more to be done
    - Do click the second page (left sidebar) to chose OS and Storage
        - Change the operating system: Select a current version of Ubuntu; the rest default
    - Go to the next tab: Data Protection. Consider the options that suit your project.
        - If you regularly commit your code to GitHub then this is redundant
        - If your data / results are expensive to reproduce: Read more about Backups and Snapshots
    - Go to the fourth tab: Networking
        - Do not change anything here; just note the Firewall options for context
        - The eventual idea will be to open port 8787 for `tcp` traffic to support RStudio
    - Click on the Create button
        - Go to the VM Instances, find the running instance, note the External IP Address
        - For example 12.123.12.123. I will refer to this as <ip-address> below
- GCP console: Connect via `ssh` to the VM
    - Navigate in the console to the VM instances table
    - Find the VM you just started: Notice there is a "Connect" column
    - Under that column, for your instance, click `ssh`
        - This opens up a terminal window where you will have a `bash` prompt on the VM
- Do some configuration steps on the VM from the `bash` shell
    - `sudo apt update` (I often run `sudo apt upgrade -y` after doing this)
    - `sudo apt install -y r-base r-base-dev` (this takes a minute or two)
    - Install RStudio Server: 3 commands
        - Note: The `wget` command stipulates a particular version; so this might become outdated...
            - ...in which case you would need to go look up more current versions of things
        - `sudo apt install -y gdebi-core`
        - `wget https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2024.12.0-467-amd64.deb`
        - `sudo gdebi -n rstudio-server-2024.12.0-467-amd64.deb`

# Restart
sudo systemctl restart rstudio-server
    - Create an RStudio user
        - `sudo adduser rstudio`
        - Set a password: I used `krypton`
        - ...also entered the additional User metadata
- Open firewall port 8787 using GCP Console:
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
- Add the tag to the VM:
    - Go to Compute Engine --> VM instances
    - Click your VM name
    - Click EDIT at top
    - Scroll to Network tags
    - Add: `rstudio-server`
    - Click `Save`
    - Now port 8787 is accessible from anywhere (which in Network-speak is `0.0.0.0/0`)
- Connect through a browser
    - In the address bar type `http://<ipaddress>:8787`
    - Login as user `rstudio` using the password you chose


Here are some diagnostic commands if RStudio does not appear in the browser window.

- From the `bash` shell: `sudo systemctl status rstudio-server`
- `R --version`
- `which R`


I used a Coding Assistant to eventually narrow the problem down to an incompatibility in
versions: R Studio Server versus the revision of R. 
