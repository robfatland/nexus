[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


[ai index src](https://github.com/robfatland/nexus/blob/gh-pages/ai/index.md)

# Content sections


- AI on AWS pointers
- EC2 working environment build with Q Developer on VS Code Server
- Example Python Streamlit application: Uses 4 models, 2 AWS-hosted, 2 copied from HF



## AI on AWS pointers

- [Instructions](https://catalog.workshops.aws/building-agentic-workflows/en-US/bedrock-api)
- Log in to an active account
- [Enable model access](https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess)
    - Includes some light justification verbiage for Anthropic
- Choose "Do it on your own" rather than as part of an event
    - This leads to a [page describing what must be installed](https://catalog.workshops.aws/building-agentic-workflows/en-US/on_your_own)
    - The IDE in particular will be VS Code Server
 

Now: Upon subsequent turns of fate I arrived at the following (as-yet-untested) recipe for setting up 
a VS Code Server instance on an AWS EC2 instance with Q Developer enabled and a few minor whistles 
and bells. 

 
## EC2 working environment build with Q Developer on VS Code Server


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


Warning: `cert: false` means no SSL/TLS certificate will be in play. Communication
will be over unencrypted HTTP, not HTTPS. This is easily modified: One changes to 
the `.config/code-server/config.yaml` file: `cert: true`. The browser address still
uses `:8080` and we will see a browser warning 'Not secure'. To this we respond by 
clicking 'Advanced > Proceed` and we now have encrypted traffic. There is a more 
proper method of accomplishing this that involves using a domain name for the EC2; 
I skip this for now.


Above note there is 'your-secure-password'. This is an arbitrary password I select. 
I use it in authenticating in to the VS Code Server instance: As prompted when navigating to
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

WARNING: There may be a library incompatibility from this install when running
a streamlit web application. A solution that has proven to work is: 


```
pip install --upgrade boto3 botocore
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

## Example Python Streamlit application: Uses 4 models, 2 AWS-hosted, 2 copied from HF


```
import io
import json

import boto3
import streamlit as st
from PIL import Image
from transformers import GPT2LMHeadModel, GPT2Tokenizer, DistilBertTokenizer, DistilBertForSequenceClassification
import torch

st.title("AWS Bedrock Web App")  # Title of the application
st.subheader("Four models available")

# Turn base64 string to image with PIL
def base64_to_pil(base64_string):
    """
    Purpose:
        Turn base64 string to image with PIL
    Args/Requests:
         base64_string: base64 string of image
    Return:
        image: PIL image
    """
    import base64

    imgdata = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(imgdata))
    return image


bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2",
)


# Bedrock api call to Stable Image Core text to image model
def generate_image_sd(text):
    """
    Purpose:
        Uses Bedrock API to generate an Image
    Args/Requests:
         text: Prompt
    Return:
        image: base64 string of image
    """
    body = {
        "prompt": text,
        "output_format": "jpeg",
        "seed": 0,
    }
    body = json.dumps(body)
    modelId = "stability.stable-image-core-v1:1"
    response = bedrock_runtime.invoke_model(
        body=body, 
        modelId=modelId
    )
    response_body = json.loads(response["body"].read().decode("utf-8"))
    results = response_body["images"][0]
    return results

# Nova is an AWS hosted text completion model
def call_nova(
    system_prompt: str,
    prompt: str,
    model_id: str = "us.amazon.nova-pro-v1:0",
):
    prompt_config = {
        "system": [
            {"text": system_prompt}
        ],
        "messages": [
            {
                "role": "user",
                "content": [
                    {"text": prompt},
                ],
            }
        ],
    }
    body = json.dumps(prompt_config)
    modelId = model_id
    accept = "application/json"
    contentType = "application/json"
    response = bedrock_runtime.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )
    response_body = json.loads(response.get("body").read())
    results = response_body["output"]["message"]["content"][0].get("text")
    return results

@st.cache_resource
def load_gpt2():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    return tokenizer, model

def generate_gpt2_text(prompt, max_length=100):
    tokenizer, model = load_gpt2()
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@st.cache_resource
def load_distilbert():
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    return tokenizer, model

def classify_sentiment(text):
    tokenizer, model = load_distilbert()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    labels = ["NEGATIVE", "POSITIVE"]
    return f"{labels[predictions.argmax().item()]}: {predictions.max().item():.3f}"

models = ["Stable Image Core", "Amazon Nova Pro", "GPT2", "DistilBERT"]

current_model = st.selectbox("Select Model", models)

if current_model == "Stable Image Core":
    # text input
    prompt = st.text_area("Enter prompt")

    #  Generate image from prompt,
    if st.button("Generate Image"):
        base64_image = generate_image_sd(prompt)
        image = base64_to_pil(base64_image)
        st.image(image)

if current_model == "Amazon Nova Pro":
    system_prompt = st.text_area("Enter system prompt")
    prompt = st.text_area("Enter prompt")

    #  Generate text from prompt,
    if st.button("Call Nova"):
        generated_text = call_nova(system_prompt, prompt, "us.amazon.nova-pro-v1:0")
        st.markdown(generated_text)

if current_model == "GPT2":
    prompt = st.text_area("Enter prompt for GPT2")
    max_length = st.slider("Max length", 50, 200, 100)
    
    if st.button("Generate Text"):
        generated_text = generate_gpt2_text(prompt, max_length)
        st.markdown(generated_text)

if current_model == "DistilBERT":
    text = st.text_area("Enter text for sentiment analysis")
    
    if st.button("Analyze Sentiment"):
        sentiment = classify_sentiment(text)
        st.markdown(f"**Sentiment:** {sentiment}")

```



# Running Jupyter on an AWS EC2 VM


This uses port forwarding: From a laptop to the 
EC2 VM running Jupyter Lab. One can also use an `ssh` tunnel, 
more secure. The **nexus** writeup for `ssh` tunnels is
found [here](https://github.com/robfatland/nexus/blob/gh-pages/bash/tunneling.md).
It is also more secure to modify the communication
protocol from `http` to `https`.


- `pip3 install jupyter`
- `cd ~; git clone https://github.com/robfatland/ant`
- `jupyter lab --ip=0.0.0.0 --port=8888 --no-browser`
    - probably not necessary to append `--allow-root`
    - as the Jupyter Lab spins up (lots of print): Note the long token string
- In the laptop browser address bar type in `http://<EC2-public-ip-address>:8888/
    - Paste the token string from above


### If the preceding is not working...


The EC2 VM may not be configured for inbound `http` traffic on port 8888. 


- Open the AWS console to add an inbound rule to the VM's security group
    - `Type: Custom TCP`
    - `Port: 8888`
    - `Source: Your IP address (or 0.0.0.0/0 for any IP)`







