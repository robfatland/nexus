[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


[ai index src](https://github.com/robfatland/nexus/blob/gh-pages/ai/index.md)


# AI on the Amazon Web Services cloud platform

- [Instructions](https://catalog.workshops.aws/building-agentic-workflows/en-US/bedrock-api)
- Log in to an active account
- [Enable model access](https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess)
    - Includes some light justification verbiage for Anthropic
- Choose "Do it on your own" rather than as part of an event
    - This leads to a [page describing what must be installed](https://catalog.workshops.aws/building-agentic-workflows/en-US/on_your_own)
    - The IDE in particular will be VS Code Code-Server

 
## Build a working environment on EC2 including Q Developer access


- EC2: Ubuntu Server latest; say c5.xlarge; keypair; new security group
    - SG: SSH(22) - 0.0.0.0/0 or be more specific
    - HTTP (80) - 0 etc
    - HTTPS (443) - 0 etc
    - Custom TCP (8501) 0 etc for Streamlit, a Web App Builder application
    - Custom TCP (8080) 0 etc for VS Code Server
    - 32GB gp3 root drive
    - Advanced Details > IAM Instance Profile: Create a role with Bedrock permissions
- Create IAM Role for Bedrock Access
    - IAM > Roles > Create Role
        - Trusted Entity: EC2
        - Permissions: AmazonBedrockFullAccess
        - EC2InstanceConnect (optional?)
        - Name: EC2-Bedrock-Role
    - Attach this to the above EC2 instance
- Connect, set up environment
    - `ssh -i keypair.pem ubuntu@ect-public-ip`
- Install VS Code Server
    - Not tested yet; here is the command sequence:


```
curl -fsSL https://code-server.dev/install.sh | sh

mkdir -p ~/.config/code-server
cat > ~/.config/code-server/config.yaml << EOF
bind-addr: 0.0.0.0:8080
auth: password
password: your-secure-password
cert: false
EOF

# Start VS Code Server
sudo systemctl enable --now code-server@ubuntu
```

Here the 'your-secure-password' is an arbitrary password I select. I use it in 
authenticating in to the VS Code Server instance: Prompted when navigating to
`http://ec2-ip-address:8080`.


Here is a variant of the above that auto-generates a 20-character password.


```
# Generate a random password
PASSWORD=$(openssl rand -base64 20)
echo "Your VS Code Server password: $PASSWORD"

# Use it in config
cat > ~/.config/code-server/config.yaml << EOF
bind-addr: 0.0.0.0:8080
auth: password
password: $PASSWORD
cert: false
EOF
```


- Install Python3


Notice this relies on `pip`. 


```
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3 and pip
sudo apt install -y python3 python3-pip python3-venv git

# Install development tools
sudo apt install -y build-essential curl wget

# Upgrade pip and install common packages
# `networkx` is just an example non-standard library (graph theory)
# `boto3` is the AWS API Python library
# `streamlit` is a library for building web apps
# `transformers` and `torch` are used to implement HF models
# `pillow` is the standard Python image processing library (evolved from PIL)
pip3 install --upgrade pip
pip3 install networkx boto3 streamlit transformers torch pillow
```


- Enable Amazon Q Developer
    - In VS Code Server aka browser address `http://the-ec2-ip:8080`
        - Open Extensions (Ctrl + Shift + X)
        - Search `Amazon Q`
        - Install `Amazon Q Developer` extension
        - Sign in with AWS Builder ID or "AWS Credentials"
            - Credentials by means of Access Key via the CLI: Next section


- Configure AWS Credentials if needed


```
# Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Configure (if not using IAM role)
# This prompts for four parameters: Region, Format (JSON), two keys from an access key file
aws configure
```


- Enable Bedrock Models
    - AWS Console for this account > Bedrock > Enable Access >
    - Select desired models, request access "Next > Submit" > Verify (couple minutes)

 - Test setup
    - Create this test file in VS Code Server:
  
```
import boto3
import networkx as nx

# Test Bedrock connection
bedrock = boto3.client('bedrock-runtime', region_name='us-west-2')
print("Bedrock client created successfully")

# Test NetworkX
G = nx.Graph()
G.add_edge('A', 'B')
print(f"NetworkX working: {list(G.edges())}")
```





