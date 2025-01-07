[nexus pub](https://robfatland.github.io/nexus), [root index src](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[main branch](https://github.com/robfatland/nexus/tree/main)


# ssh tunnels


## Overview


Suppose I want to run a Jupyter notebook server on a cloud Virtual Machine. I will view and interact with this 
from my laptop web browser. I can select a VM with a desired level of compute power. I can run the
`jupyter` notebook server on an internet-facing VM (less secure) or on a cloud-internal VM (more secure). 
This approach is simpler than building a "Littlest Jupyter Hub" which in turn is much simpler than building 
a full-scale Jupyter Hub.


One way to proceed is to employ the `ssh` protocol to create a secure tunnel between machines. We consider
two configurations:


```
my laptop <-----> cloud VM (running jupyter)

my laptop <-----> cloud VM (bastion) <------> cloud VM (running jupyter)
```


### Configuration 1: Laptop direct to Jupyter server VM


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


### Configuration 2: Laptop to bastion VM to Jupyter server VM


This approach presumes that a (less exposed / more secure) VM called `worker` is configured and running
inside the cloud, for example (using AWS terminology) on a *private subnet* with ip address `10.0.1.128`. 
An intermediary VM called `bastion` is running as well on this private subnet. `bastion` also has a
public ip address `123.123.123.12`.  The objective here is to establish a two-hop ssh tunnel. 

Note that we need two keypair files: `bastion.pem` located on the laptop in `~/.keypairs` and
`worker.pem` located on `bastion` in `~/.keypairs`. 


The following 
command sequence indicates which computer we are addressing through the command line by means of 
the prompt. From my `laptop`, in a `bash` shell:


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

bastion$ ssh -N -f -i ~/.keypairs/worker.pem -L localhost:7005:localhost:8889 ubuntu@10.0.1.128
bastion$ exit

laptop$ ssh -N -f -i ~/.keypairs/bastion.pem -L localhost:7004:localhost:7005 ubuntu@123.123.123.12
```

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
  
  
