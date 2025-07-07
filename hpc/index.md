[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


# high performance computing

We oversimplify High Performance Computing to mean: Multiple computers networked together with very 
low communication latency creating in effect a supercomputer. How is this done on prem? How is it 
done on the three primary cloud platforms? 


### uw on-premise hpc


This will be a slightly abstracted description of working on facilities at the University of Washington.


- Get white listed with access to Klone, Tillicum and Kopah
    - Respectively HPC blades, GPU sysytems, and S3-style object storage
    - Follow instructions to get MFA 
- `ssh NetID@klone.hyak.uw.edu`
    - This is the login node (not necessarily where work gets done)


### AWS Parallel Computing Service PCS


<img src="../assets/img/AWS_PCS_Architecture.png"
     alt="AWS Parallel Computing Service architecture diagram"
     height="300"
     style="float: center; margin-right: 10px;" />


- [AWS PCS introduction / overview video](https://www.youtube.com/watch?v=ciHU2fDzhSc)
- Slurm controller
- Login node group
- Compute node group


### Azure


### GCP




