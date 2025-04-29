[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)

- [ai index src](https://github.com/robfatland/nexus/blob/gh-pages/ai/index.md)
- [google](https://github.com/robfatland/nexus/blob/gh-pages/ai/gcp.md) cloud: A simple vertex/gemini example
- [aws](https://github.com/robfatland/nexus/blob/gh-pages/ai/aws.md) cloud: stub
- [azure](https://github.com/robfatland/nexus/blob/gh-pages/ai/azure.md) cloud: stub


# artificial intelligence


This page touches on the *broad* definition of artificial intelligence as forms of autonomous computation. 
This big region on the AI Euler diagram encompasses all manners and forms of AI: Machine Learning, Deep Learning, 
Convolutional Neural Networks, Supervised and Unsupervised forms of training, clustering algorithms such as 
K-means and so forth.


The related sub-pages linked above -- *gcp*, *aws* and *azure* -- are AI notes on cloud-specific technology stacks.


## resources


- UCLA law professor John Villasenor has written [essays on AI in relation to society](https://johnvillasenor.com/artificial-intelligence/).
- [A study of LLM-to-LLM conversations by UW student Harvy Gandhi](https://medium.com/@harvygandhi2/ai-to-ai-conversations-unraveling-the-future-of-intelligent-systems-6e360c629734)


## cloud platform technologies


- AWS
    - SageMaker
    - Bedrock
    - Foundation Model emphasis
    - Anthropic > Claude
    - Dedicated hardware: Trainium, Inferentia
- Azure
    - AI Foundry
    - AI Studio
    - ML Studio
- GCP
    - Gemini: An LLM
    - Vertex AI: A platform for building, training and deploying AI models
        - More simply: Can be used as an interface to a multitude of models (including Gemini)


## independent generative AI programs


- Amplify at Vanderbilt
- OLMO at AI2
- Maizey at UMich

## context

Suggestion: Build a prompt using the "PACE" guideline acronym: State Problem, Action, Context, Example.


## ai recipe

Let's run through a HuggingFace example subject to these constraints:

- Easy to implement on Ubuntu Linux running on WSL2 in turn on a Windows laptop
- Very lightweight processing task


Update the Advanced Package Tool `apt` library registry; and permit it to make upgrades of
installed libraries: 


```
sudo apt update
sudo apt upgrade
```

Ensure that `python`, `pip` and `conda` are installed. Let's assume `pip` will do the job: 
First install `pytorch`, then `transformers`.  


```
pip install torch
pip install transformers
```

To set up a browser-based interface: Clone the following repository:


```
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui/
```

Need to elaborate and set up an environment: MISSING STEP

```
pip install -r requirements.txt
```


"Run the application"... ?!?!?!???

```
./start_linux.sh  # On Linux
```

Example pre-trained model: DistilBERT


```
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
result = sentiment_pipeline("I love Hugging Face!")
print(result)
```


More from the AI: 

YouTube: Search "Running HuggingFace models on WSL2" or "Using HuggingFace Transformers on Ubuntu" for a visual guide.


- DistilBERT: A smaller, faster, and cheaper version of BERT. It is well-suited for tasks like text classification and sentiment analysis 1 .

- BERT: A versatile model for various NLP tasks, including question answering and natural language inference 1 .

- RoBERTa: An optimized version of BERT that improves performance on NLP tasks 1 .
