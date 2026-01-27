[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[bash index source](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md)

# ssh tunnels


`ssh` tunnels enable us to log in to remote machines and run `jupyter lab` by means of port forwarding. 
[This lab](https://github.com/cloudbank-project/az-serverless-tutorial/blob/main/content/workstation/_index.md) 
walks through setting up **VS Code Server** in this manner. My notes are below under the heading
[Using VSCode Server](#Using-VSCode-Server].


## Overview


This page describes `ssh` tunnel use through the specific application of using a cloud virtual machine
as a working Jupyter environment. These instructions were written using an Azure VM (hence the 
Username is `azureuser`) but they apply equally to other cloud platforms / remote VMs. On AWS the
Ubuntu default username would be `ubuntu` rather than `azureuser`.


Suppose I want to run a Jupyter notebook server on a cloud Virtual Machine. I will view and interact with this 
from my laptop web browser. I can select a VM with a desired level of compute power. I can run the
`jupyter` notebook server on an internet-facing VM (less secure) or on a cloud-internal VM (more secure). 
This approach is simpler than building a "Littlest Jupyter Hub" which in turn is much simpler than building 
a full-scale Jupyter Hub. Let's review these three options briefly, with build times being "YMMV".


- Full-scale Jupyter Hub: Provides Jupyter Lab Server for hundreds, even thousands of individuals
    - Build time: Days to learn and build a first time; with necessary ongoing care and feeding
- Littlest Jupyter hub: Jupyter Lab Server for two up to 12 people
    - Build time: Set up in half a day; plan on occasional updating
- Jupyter Lab Server on a VM: For one person
    - Build time: Up and running in an hour; update whenever


In all cases each User should take advantage of independent software versioning such as GitHub.


One way to proceed is to employ the `ssh` protocol to create a secure tunnel between machines. We consider
two configurations:


```
my laptop <-----> cloud VM (running jupyter)

my laptop <-----> cloud VM (bastion) <------> cloud VM (running jupyter)
```


### Using VSCode Server

*Abbreviated notes* for reference; see 
[the lab](https://github.com/cloudbank-project/az-serverless-tutorial/blob/main/content/workstation/_index.md)
for the complete careful procedure.

- Click the **><** icon at lower left to bring up the connection menu
- `Connect to Host... remote ssh` > Add new > `123.12.23.123`
- Where to save? `/home/user/.ssh/config`: Open this and edit an entry to read:

```
Identity string goes here, such as Ocean Chlorophyll Project VM
  HostName 123.12.23.123
  User azureuser
  IdentityFile "/home/user/.keypairs/some_keypair_filename.pem"
```

- connect and test port forwarding by `jupyter lab`
- 

### One hop ssh tunnel: Laptop direct to Jupyter server VM


This approach is the simpler of the two. It does mean that the Jupyter server VM has a public ip address
so there is more potential exposure. Nevertheless it should be emphasized that `ssh` is a widely adopted
protocol because it is reliably secure. The following presumes that a conda environment `work-env` has 
previously been configured as the working environment; which is where `jupyter` is installed. We provide 
an example `git clone` operation to provide some test IPython notebook content.


```
cloud-VM$ cd ~
cloud-VM$ git clone https://github.com/robfatland/ant
cloud-VM$ conda activate work-env
(work-env)cloud-VM$ (jupyter lab --no-browser --port=8889) &
```


The second command starts a jupyter lab notebook server; and this process will provide an access 
token which should be copied to the laptop. Example token: `5ea4583257df6cb49234ff38427cd1e53a80281aeca5d2e3`.
Also given: A keypair file `keypair.pem` exists in folder `~/.keypairs`. The cloud VM has an
ip address `123.123.123.12` and the username is `ubuntu`. Notice that in the above command port `8889`
has been associated with the jupyter lab notebook server.


```
laptop$ chmod 400 ~/.keypairs/keypair.pem
laptop$ ssh -N -f -i .keypairs/keypair.pem -L localhost:7005:localhost:8889 ubuntu@123.123.123.12
```

The second command above establishes an `ssh` tunnel between local port 7005 on the laptop and
remote port 8889 on the cloud VM. Assuming the connection goes through it is now simply a 
matter of entering `localhost:7005` into the laptop browser address bar. This will 
establish a connection to the cloud jupyter notebook server, probably with a prompt to 
enter the token recorded above. Once the token is authenticated the jupyter environment
should be available. This includes `bash` access to the VM.


### Two hop ssh tunnel: Laptop to bastion VM to Jupyter server VM


This approach presumes that a (less exposed / more secure) VM called `worker` is configured and running
inside the cloud, for example (using AWS terminology) on a *private subnet* with ip address `10.0.1.128`. 
An intermediary VM called `bastion` is running as well on this private subnet. `bastion` also has a
public ip address `123.123.123.12`.  The objective here is to establish a two-hop ssh tunnel. 

Note that we need two keypair files: `bastion.pem` located on the laptop in `~/.keypairs` and
`worker.pem` located on `bastion` in `~/.keypairs`. The `chmod` command included here is only 
run once to adjust the keypair file permissions.


The following command sequence indicates which computer we are addressing through the command line 
by means of the prompt. From `laptop` in a `bash` shell:


```
laptop$ cd ~
laptop$ chmod 400 ~/.keypairs/bastion.pem
laptop$ ssh -i ~/.keypairs/bastion.pem ubuntu@123.123.123.12`

bastion$ cd ~
bastion$ chmod 400 ~/.keypairs/worker.pem
bastion$ ssh -i ~/.keypairs/worker.pem ubuntu@10.0.1.128

worker$ cd ~
worker$ git clone https://github.com/robfatland/ant
worker$ conda activate work-env
(work-env)worker$ (jupyter lab --no-browser --port=8889) &
```


As noted: The jupyter notebook server will start as a background process that will
persist after logging off of `worker`; and we are obliged to copy the token provided
for later authentication. Example token: `5ea4583257df6cb49234ff38427cd1e53a80281aeca5d2e3`.


Next we return to the `bastion` VM to create the first part of the tunnel.
We then return to the local `laptop` to create the second part of the tunnel.


```
(work-env)worker$ exit

bastion$ ssh -N -f -i ~/.keypairs/worker.pem -L localhost:7006:localhost:8889 ubuntu@10.0.1.128
bastion$ exit

laptop$ ssh -N -f -i ~/.keypairs/bastion.pem -L localhost:7005:localhost:7006 ubuntu@123.123.123.12
```

As above it remains to enter `localhost:7004` in the laptop web browser address bar to
open the `jupyter` notebook server interface.

  
  
