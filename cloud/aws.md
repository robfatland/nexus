[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), [cloud index source](https://github.com/robfatland/nexus/blob/gh-pages/cloud/index.md)


# aws

## Aspirational


Repeat this process on the Kopah system


## Overview


- AWS = Amazon Web Services
- Each *service* is related to compute, storage and/or networking; plus cyberinfrastructure built around other technologies.
- Considering storage we have various forms of *block* storage and likewise for *object* storage.
- This narrative will focus on object storage which is retained in **S3 buckets**.
- One bucket has an unbounded storage capacity costing $23 / Terabyte / month.
- S3 buckets store file in their entirety; not as indexable bytes.
- To understand object storage it would be helpful to have a direct connection to it.
    - In this way we can experiment with file access
- The objective here is to track a process: Mounting S3 buckets as drives on a localhost or cloud VM.
- There are multiple access modes for AWS S3 object storage
    - Console access: Can upload/download files
    - CLI access: Uses the command utility `aws` which must first be installed
    - Programmatic access using the Python AWS library `boto3`
    - Application access


# aws cli


- [Get started guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- On my `localhost`: `conda create --name aws` so as to have a dedicated environment
- `conda activate aws`
- Before the install worked I was obliged to install `unzip` using `sudo apt install unzip`... then:
    - `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    - `unzip awscliv2.zip`
    - `sudo ./aws/install`
    - `rm awscliv2.zip`
    - As a result: `aws --version` gives `aws-cli/2.27.48 etcetera`


Now we can set up authentication by running `aws configure` 
- Access Key ID: Obtain from AWS console; keep away from GitHub repos $^*$
- Secrete Key: As above
- Default region name: use `uswest-2`
- Default output format use `json` (other options: `text`, `table`, `yaml`)


$^*$ Access keys committed to GitHub are found by bad actors. This leads to thousands of dollars
in fees almost immediately. Therefore: Take care never to put an access key file anywhere near
a GitHub repo folder. 


The `aws` cli interface should now be ready to operate; and will self-authenticate whenever it runs and interacts
with the Amazon cloud. In this instance I found that my **S3 Browser** application was failing; and it seems to
be using the same access key as the one I used in `aws configure`. Therefore I will log in to the AWS console
for this account and determine whether the access key is still valid. 

