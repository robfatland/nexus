[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


# ssh tunnels


## Overview


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
  
  
