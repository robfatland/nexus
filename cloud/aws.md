[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), [cloud index source](https://github.com/robfatland/nexus/blob/gh-pages/cloud/index.md)


# aws


Lots to do on the AWS cloud; so let's start with integrating infinite cloud storage with our local computing environment. 


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


Here is [a helpful YouTube lecture](https://youtu.be/RNOxlcaAMpg) on working with AWS Mountpoint.
The notes below expand on the following procedure, to this end.


- Establish a Linux working environment; `bash` at least and perhaps `miniconda` 
- If not in place already: Install the AWS command line interface
- Optional for AWS Virtual Machines
    - Define and assign a Role rather than use an Access Key (see next step)
    - This is a 'better practice' way to handle authentication
    - Done easily using the AWS console
        - The Role is assigned a Policy; and the VM then assumes this Role
- Configure the cli and verify it authenticates to AWS
    - The localhost method uses an Access Key: Handle with care
- Install `mountpoint` available from AWS
- Use `aws s3` to create an S3 bucket
- Use `mkdir` to create an empty folder `bucket`
- Use `mount-s3` to mount the S3 bucket as a pseudo-filesystem on the `bucket` folder
    - Enable file deletion by appending `--allow-delete`
- Test file create / delete in the `bucket` folder


The following sections follow this narrative in more detail.


## aws cli


- [AWS get started guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- On my `localhost`:
    - `conda create --name aws` provides a dedicated environment
    - `conda activate aws` makes this the active environment
    - [Install libraries](https://github.com/robfatland/nexus/blob/gh-pages/bash/env.md#project-installation-notes) for example:
        - `conda install jupyterlab`
        - `conda install pandas`
        - `conda install matplotlib`
- To install `aws` I first had to install `unzip`
    - `sudo apt install unzip`
    - `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"`
    - `unzip awscliv2.zip`
    - `sudo ./aws/install`
    - `rm awscliv2.zip`
    - Result: `aws --version` gives `aws-cli/2.27.48 etcetera`


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
`aws configure` process fixed this. Now we proceed to reference commands: 


- `aws sts get-caller-identity` to verify the `aws cli` configuration is ok
- `aws configure list` to examinen the configuration parameters
- `aws s3 ls` to get a list of buckets
- `aws s3 mb s3://erdos-23049527340598` to create a bucket of that name
- `aws s3 rb s3://erdos-23049527340598` to remove and add `--force` if it has contents


## mount point


- Determine which version to install: [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mountpoint-installation.html)
- My Linux distribution is Ubuntu so: `wget https://s3.amazonaws.com/mountpoint-s3-release/latest/x86_64/mount-s3.deb`
- `mount-s3.deb` is a 12MB file
- `sudo apt-get install ./mount-s3.deb`
- Verify: `mount-s3 --version` gives `mount-s3 1.19.0`
- Both `aws` and `mount-s3` are global: `/usr/local/bin` and `/usr/bin` respectively, not in a `miniconda` environment


## mount and use bucket


This is the payoff; the following commands and comments begin a narrative on 'getting' how object storage 
is and is not equivalent to a standard Linux folder. Not to bury the lead however: Once the bucket is 
mounted on a local folder (the second command below) we have what *appears* to be a file folder on our localhost
machine that is in fact virtual infinite storage on the Amazon cloud. Some would say that's pretty cool. 


- `mkdir bucket`
- `mount-s3 erdos-23049527340598 bucket`
- `ls -al bucket`
- `cd bucket`
- `ls -al`
- `touch tfile.txt`
- `vi tfile.txt`
    - Modify and attempt to save: Error message (because one can't edit object files)
    - Save to new filename: Success (because one can create new files in object storage)
    - Quit the `vim` editor
- `ls -al` may list several additional files associated with a `vim` session (swap etcetera)
- `rm tfile.txt` results in `Operation not permitted`: This bucket has not been granted `delete` permission
- `mkdir subbucket` creates a subfolder as expected
- `subbucket` does not appear in the `S3` application *until* it contains at least one object (file)


At this point let's delete the bucket and rebuild it with `delete object` permission built in.
There is nothing preventing mounting the *same* S3 bucket `erdos-23049527340598` on a different folder
*provided* that folder is not inside the `bucket` folder. 


- `cd ~`
- `mkdir bucket2`
- `mount-s3 erdos-23049527340598 bucket2 --allow-delete` results in `bucket erdos-23049527340598 is mounted at bucket2` 


Now verify `bucket2` permits object deletion where `bucket` does not: 


```
(aws)$ ls -al bucket/tfile.txt
... bucket/tfile.txt ...
(aws)$ ls -al bucket2/tfile.txt
... bucket2/tfile.txt ...
(aws)$ rm bucket/tfile.txt
rm: cannot remove 'bucket/tfile.txt': Operation not permitted
(aws)$ rm bucket2/tfile.txt
(aws)$ ls -al bucket/tfile.txt
ls: cannot access 'bucket/tfile.txt': No such file or directory
```


## Aspirations


- What happens when we power cycle localhost?
- Repeat for Kopah
    - `mount-s3 my-bucket /path --endpoint-url https://etcetera`
- Use Jupyter to test `boto3`
- Fill in VM Role details
- Extend to a Container example

