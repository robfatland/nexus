[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), [cloud index source](https://github.com/robfatland/nexus/blob/gh-pages/cloud/index.md)


# aws


The objective here is to track the process of mounting S3 buckets as drives on a localhost or cloud VM.


# the aws cli


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

