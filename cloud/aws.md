[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), [cloud index source](https://github.com/robfatland/nexus/blob/gh-pages/cloud/index.md)


# aws

## Aspirational


- Repeat this process on Kopah
- Link back to and forward from `environments` so Jupyter set up is called back
- Show how this works on both a cloud VM and on localhost
- Extend this use of S3 to Containers


## Overview


- AWS = Amazon Web Services
- Each *service* is related to compute, storage and/or networking; plus cyberinfrastructure built around other technologies.
- Considering storage we have various forms of *block* storage and likewise for *object* storage.
- This narrative will focus on object storage which is retained in **S3 buckets**.
    - Hence S3 is the AWS object storage *service*. ("S3" = Simple Storage Service)
- In addition to the S3 service we are focused here on a related service called **Mountpoint**
    - Mountpoint will prove to be a translational *convenience* service
- S3 object storage operates by means of *buckets* which contain a collection of objects
    - Objects are equivalent to files; so at a high level a bucket is analogous to a folder
    - A bucket has a name consisting of numbers, letters and hyphens (no underscores)
        - This name resides in a global namespace where it is obliged to be unique.
        - It is very unlikely we will be able to create a bucket named `mybucket`
        - It is very likely we will be able to create a bucket named `icesat-II-deform-01012024-U6837154`
        - This suggests programmatic management of bucket names will be a good approach
- One bucket has an unbounded storage capacity
    - The cost of storing one Terabyte of data for one month on AWS S3 is $23
- S3 buckets store files in their entirety; there is no support for `seek()` operations
- To work with object storage we need a coherent formalism
    - Here we are concerned with two such formalisms
        - First: The `aws` command line interface (cli)
            - Commands are of the form `aws s3 <subcommand> <args>`
            - These can be issued for example from localhost or from a cloud VM
            - They will self-authenticate using stored credentials
            - The `aws` cli makes use of an S3 API
        - Second: The `mountpoint` service mimics mounting a drive (Linux only)
            - This makes an S3 bucket *appear* to be a folder + contents
            - There are some caveats on how this works to keep in mind in practice
- The goal here is to cover these two methods: S3 access via `aws` cli and S3 access via mountpoint
    - Mounting S3 buckets as drives on a localhost or cloud VM can streamline cloud use 
- There are multiple access modes for AWS S3 object storage
    - Console access: Can upload/download files
    - CLI access: Uses the command utility `aws` which must first be installed
    - Programmatic access using the Python AWS library `boto3`
    - Application access


## condensed narrative


- Establish a Linux working environment; perhaps a `conda` environment 
- Install the AWS command line interface (cli)
- Configure the cli and verify it is authenticating to the AWS cloud
- Verify that `aws s3` commands work
- Role?
- Install `mountpoint`?
- Mount an S3 bucket as a pseudo-filesystem
- Test file manipulation on this filesystem


## aws cli


- [AWS get started guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- On my `localhost`:
    - `conda create --name aws` provides a dedicated environment
    - `conda activate aws` makes this the active environment
    - [Install libraries](https://github.com/robfatland/nexus/blob/gh-pages/bash/env.md#project-installation-notes) for example:
        - `conda install jupyterlab`
        - `conda install pandas`
        - `conda install matplotlib`
- Before the install worked I was obliged to install `unzip` using `sudo apt install unzip`... then:
    - `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"`
    - `unzip awscliv2.zip`
    - `sudo ./aws/install`
    - `rm awscliv2.zip`
    - As a result: `aws --version` gives `aws-cli/2.27.48 etcetera`


Now we can set up authentication by running `aws configure` 
- Access Key ID: Obtain from AWS console; keep away from GitHub repos $^*$
- Secrete Key: As above
- Default region name: use `us-west-2` and if you get this wrong (like `uswest-2`) you will be stuck with *Can't connect* errors
- Default output format use `json` (other options: `text`, `table`, `yaml`)


$^*$ Access keys committed to GitHub are found by bad actors. This leads to thousands of dollars
in fees almost immediately. Therefore: Take care never to put an access key file anywhere near
a GitHub repo folder. 


The `aws` cli interface should now be ready to operate; and will self-authenticate whenever it runs and interacts
with the Amazon cloud. 


Problem: The **S3 Browser** application was failing to list buckets for the account I was using. This means the
access key is no longer valid. Regenerating a new key and installing it in the S3 Browser profile; and in the 
`aws configure` process fixed this. Now we have reference commands: 


- `aws sts get-caller-identity` to verify the `aws cli` configuration is ok
- `aws configure list` to examinen the configuration parameters
- `aws s3 ls` to get a list of buckets
- `aws s3 mb s3://erdos-23049527340598` to create a bucket of that name
- `aws s3 rb s3://erdos-23049527340598` to remove and add `--force` if it has contents


## mount point

S3 is an object store.
