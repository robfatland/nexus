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



## gpu instances on AWS


- P and G series are recommended [GPU-compatible EC2 instance types](https://docs.aws.amazon.com/dlami/latest/devguide/gpu.html)
- Here is a helpful [medium article](https://nishant-parmar.medium.com/using-aws-g-and-p-series-ec2-instances-for-high-quality-rendering-cloud-gaming-and-machine-55195075334c)
