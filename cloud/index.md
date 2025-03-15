[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), [cloud index source](https://github.com/robfatland/nexus/blob/gh-pages/cloud/index.md)


# cloud


"Cloud" in the context of research computing refers to *commercial clouds*, particularly AWS, GCP and Azure,
where Virtual Machines are available on a pay-as-you-go basis. The content of this repo *does not* however
concern "cloud" consumer services like iCloud and Google Drive.


[Essay: Is cloud computing a good idea for you?](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md#the-basic-idea-here)


## children


- [spot market](https://github.com/robfatland/nexus/blob/gh-pages/cloud/spot.md) 
- [studies](https://github.com/robfatland/nexus/blob/gh-pages/cloud/studies.md)
- [organizations](https://github.com/robfatland/nexus/blob/gh-pages/cloud/organizations.md)


## references


- [VM, Database, Serverless tutorials (Azure) source](https://github.com/cloudbank-project/az-serverless-tutorial/tree/main)
    - [VM, Database, Serverless tutorials (Azure) published](https://cloudbank-project.github.io/az-serverless-tutorial/)
- [Containerization source](https://github.com/naclomi/containers-tutorial)
    - [Containerization published](https://naclomi.github.io/containers-tutorial/)
    - [Carpentries introduction to docker containers](https://carpentries-incubator.github.io/docker-introduction/)
- Build an HPC cluster on a cloud platform: [AWS PCS](https://youtu.be/ciHU2fDzhSc?si=mVxL8qAjJALq8vl8), Azure, GCP
- [Superb learning channel for the AWS cloud platform](https://www.youtube.com/@TechHpc)



Cloud computing for research comes at a dollar cost. We are interested in optimizing spend.


* Preemptible instance use on the cloud (70-90% savings)
    * [Dedicated notes here in nexus](https://github.com/robfatland/nexus/edit/gh-pages/cloud/spot.md)
    * [Oorjit's repo on ML using preemptible VMs](https://github.com/oorjitchowdhary/ml-training-preemptible-vms/blob/main/README.md)


## open topic: access control

* subnet masks and so on
## cloud clinics


* 23-JAN-2025 11:30AM PDT **Checkpointing methods: Getting $3.33 of cloud compute for $1.00**
    * [connect link], [recording link]  
    * Abstract: In today’s busy world we can lose track of small details that have a big impact.
Suppose you have a cloud budget of $10,000 but your computations could be scaled up beyond
that limitation to produce better research. What you need is access to immutable storage (easy),
access to cheap preemptible cloud VM instances (easy) and a reliable method of checkpointing
your progress (easy? hard?). This one-two-three punch means you can purchase $33,333 worth of
cloud computing for a mere $10,000 and get better research results as a consequence. This cloud
clinic will catch you up on the how-tos and other small details of such a substantial gain in
compute power. We use a CNN as our example implementation of a compute-intensive research task.



## AWS EC2 Virtual Machines


AWS virtual machines fall into a variety of categories and size scales; so there is some studying
up to do in deciding which instance to select. A typical powerful workstation will run between $0.50
and $1.00 per hour; so it is important to Stop (not Terminate) the instance when it is not in use.


Below are remarks on non-GPU and then GPU-based VMs. Following that are instructions for logging in to
a VM on AWS by means of the VSCode application.


### non-GPU instances


- [Information on naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html)
- Examples from the compute-optimized C-series
    - c6id.4xlarge
        - C = compute optimized, 6 = generation 6
        - i = Intel processors (contrast: 'a' for AMD processors)
        - d = instance store volumes: temporary, high-performance block-level storage...
            - ...physically attached to the host computer running the EC2 instance
            - ...fast data access
            - ...but data is lost if the instance is stopped or terminated
        - 4xlarge = 16vCPU, 32GB RAM, $.8344 per hour for Ubuntu
        - 12xlarge = 48vCPU, 96GB RAM, $2.5032 per hour for Ubuntu: Cost scales linearly with vCPU count and RAM
    - c6i.4xlarge: C-series, 6th-generation, Intel, 16vCPU, 32GB RAM, $0.708/hr Ubuntu
    - c7i-flex.4xlarge: C, 7th-gen, Intel, 16vCPU, 32GB RAM, $0.7063/hr Ubuntu
        - The `-flex` modifier is reputed to be "5% cost savings with occasional performance hit"
        - This choice would be a nominal cost optimizer but 'remains to be shown'
        - This suggests benchmarking identical configurations on a moderate processing task
            - How would a cheaper C5 or C4 compare?
            - How to ensure the entire vCPU bank is engaged?


### gpu instances


- P and G series are recommended [GPU-compatible EC2 instance types](https://docs.aws.amazon.com/dlami/latest/devguide/gpu.html)
- Here is a helpful [medium article](https://nishant-parmar.medium.com/using-aws-g-and-p-series-ec2-instances-for-high-quality-rendering-cloud-gaming-and-machine-55195075334c)


### Log in from VSCode

- Use [this tutorial](https://cloudbank-project.github.io/az-serverless-tutorial/workstation/) to connect to the VM from VSCode

