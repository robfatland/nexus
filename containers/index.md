[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


# containers


## notes from working through the [544 tutorial](https://naclomi.github.io/containers-tutorial/)


- Prerequisite: [Set up a cloud VM (Azure) as a workstation](https://cloudbank-project.github.io/az-serverless-tutorial/workstation/)
    - Uses VSCode to `ssh` to a `bash` shell
 


### Notes from the MSE544 labs plus YouTube videos


* Docker is a software development platform and a virtualization technology; key concept is hermetic operation, no shock waves into the system at large
    * except the shock waves we want of preserving compute module results
* Docker applications can therefore run anywhere; they are system agnostic
    * Docker communicates "natively" (directly) with the system kernel
* Resource optimization: Multiple Docker containers run on a single system (VM say)...
    * ...from a common source image? Share files to reduce footprint!
* Resource provisioning
    * Docker Container assigned so much RAM, CPU cores etcetera by a management service
    * For example on AWS use Elastic Container Service to construct a Task...
        * ...Task: Composed of many Container runs
* Bottom line of Containers is **Run Many, Run Anywhere**: Scale and consistency
    * VMs can be bulky and slow
        * Containers only virtualize the OS, not the hardware
* Three fundamental elements: Docker file, Docker image, Docker container
    - Docker File is like DNA: Code: How to build an image 
        - Start with `FROM base_image`
        - `RUN` commands to customize 
        - `ENV` commands to set environment variables used inside the running Container
        - `CMD` or `ENTRYPOINT` to stipulate what happens at runtime
    - Docker Image: an immutable file
        - A snapshot of software + dependencies all the way down to the OS level
        - Configured content can be spun up as a container
    - Docker Container is the executable compute module
    

### The Docker developer mindset


- a `dockerfile` resides in a host folder
- a Docker `image` lives *somewhere* (not our concern, managed behind the scenes)
- the `docker` *command* is a **command line interface**
    - interfaces with the **docker daemon/engine**  that manages everything docker
- On a PC: Enabled by Docker Desktop (app) + WSL2


