[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), [cloud index source](https://github.com/robfatland/nexus/blob/gh-pages/cloud/index.md)


# aws

## Aspirational


- Repeat this process on the Kopah system.
- Link back to and forward from `environments` so Jupyter set up is called back


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

