[nexus](https://robfatland.github.io/nexus), [main index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[cloud index source](https://github.com/robfatland/nexus/blob/gh-pages/cloud/index.md)


# organizations


Concerns running a program with multiple people accessing the cloud under one organizing program. Two
sub-cases are considered: First multiple research groups mapping to multiple cloud accounts (AWS-specific).
Second a single subscription supporting a college course with (say) 100 students (Azure-specific). 


## Amazon Web Services


Managing a single AWS account can be done by a research team. Here we are considering putting a program in place
that will help manage multiple accounts. A full-scale version of this idea across multiple clouds is found in 
the [CloudBank](https://cloudbank.org) project. Here we consider ten or so projects each with a particular
budget plan. For example one project may plan to spend $10k over 10 months at a monthly estimated spend in k$ of 
{ 0, 0, 1, 1, 1, 2, 4, 1, 0, 0 }. The idea here is to note the AWS services that can be used to help reduce 
the time spent on managing the overall program. Steps and considerations:


- Establish a payer account with a bill payment mechanism in place.
- Use the **Organizations** service to create a category structure.
    - Integrates with Service Control Policies (SCPs)
- Establish a numbered sequence of root account IDs.
    - These correspond 1:1 to AWS accounts identified by 12-digit number.
- Create sub-accounts one per research project.
    - Each has an associated root email account
    - Establish a budget plan for each sub-account
    - The idea is to log and track spend by project to adhere to its budget plan
    - Log in as root
        - First time: Can use `forgot password` to set up a password
    - Create an Administrative Privileges group; other groups as needed 
    - Create IAM Users: PI and named colleagues: Console access: Download/send credentials


### Outstanding topics


- Method not yet covered: The team has an existing AWS account they wish to transfer to sub-account status with respect to 
the above payer account.
- Supporting AWS technologies and services
    - [AWS documentation: Services complementing *Organizations*](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html)
    - AWS *Organizations*: need specifics on controlling access to resources
    - AWS *Cloud Formation*: definition needed
    - AWS *Cloud Trail*: Logging transactions on AWS
        - Exposition needed on enabling, log access, log query, automation
    - AWS *Cloud Watch*: ...
        - AWS *EventBridge*: ...
    - AWS *Account Management*: ...
    - AWS *Landing Zone*: A multi-account environment configured to be secure.
        - What is an example of a "no brainer" use of Landing Zone?
    - AWS *Control Tower*: Automates creation of new AWS accounts
        - Features include:
            - Centralized logging: Need full exposition
            - Monitor compliance: Exposition needed
        - How are Control Tower and Landing Zone used together?
    - AWS *Lambda*: Serverless functions that can be triggered on an automated schedule
    - AWS < spending alarms >: ...
    - AWS *IAM*: ...
    - AWS *IAM Identity Center*: ...
    - AWS *Config*: ...
    - AWS *Audit Manager*
    - AWS *Artifact*
    - AWS *Backup*
    - AWS *Billing and Cost Management*
    - *Amazon Detective*
    - *Amazon GuardDuty*
- Desirable functionality
    - Burn rate threshold triggers a damage control process ("runaway train scenario")
    - Automated daily spend report as a single email with a status value in the Subject
        - Green / Yellow / Red



## Azure


Consider a single Azure Subscription that will support a 12-week course with 100 students.
Cloud-specific lessons concern VMs, Containers, Serverless Functions and configuring and 
using a NoSQL Database.


## Google Cloud Platform
