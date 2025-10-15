[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)

- [ai index src](https://github.com/robfatland/nexus/blob/gh-pages/ai/index.md)
- [google](https://github.com/robfatland/nexus/blob/gh-pages/ai/gcp.md) cloud: A simple vertex/gemini example
- [aws](https://github.com/robfatland/nexus/blob/gh-pages/ai/aws.md) cloud: stub
- [azure](https://github.com/robfatland/nexus/blob/gh-pages/ai/azure.md) cloud: stub


# en avance: Notes from a lecture 
## delivered by Elle O'Brien 14-October-2025
### UMich School of Information


Past org: Data Version Control


- Code LLMs (abbreviated here CL) regarding simulation, cata collection, etcetera
- Undertrained as a Developer? You must be a Scientist!
- Debugging code you didn't write is difficult
- Inaccuracies in code and comments are a liability
- Science context: What is "testing practice"?
- Survey of scientists who use CL: Excerpted outcomes
    - Who are you? Life sciences and engineering and etcetera
    - What CL do you use? Partial: They use Chatbots not GitHub Copilot 3:1
        - Chatbots produce longer blocks of code (hypothesis: this increases the cognitive load on R)
    - Use case: "language changes" (e.g. due to legacy code, changing labs, specialty tools etcetera)
    - Chat is 1000x easier than documentation...
        - Why use documentation? CL can read and apply it for me
    - Testing: Ad hoc, eyeball, not systematic
        - Unsurprising: This can easily lead to failure modes
    - Incorrect mental models by R can lead to failure modes


The bottom line seems to be: People with experience and skill in software development, the lower the
"productivity boost".


As part of this process: Be aware of the Retraction Watch database. 10s-of-k retraction; compare count of papers per year: 3 million.


Potential failure mode: The quality of scientific literature slowly and quietly degrades.


Potential failure mode: Scientists stop using professional caliber scientific software.


Potential failure mode: Public trust crisis, as featured in the New York Times. 


A bottom line I take away is that this is a Cautionary Tale deserving our attention and effort
as scientists. A grass roots approach (as suggested by the presenter) could begin with "buddy up"
with an RSE. 


Questions
- Does the advent of Model Context Protocol (MCP) represent an opportunity to mitigate negative outcomes?
    - The speaker made the point that a *chain* of reliabilities gives a collective multiplicative reliability i.e. much less than 1
    - The speaker also acknowledged the potential to mitigate; which is the notion I have picked up from a "front line" worker at AI2
- What is the status of RAG with respect to abstraction?



# artificial intelligence


This page touches on the *broad* definition of artificial intelligence as forms of autonomous computation. 
This big region on the AI Euler diagram encompasses all manners and forms of AI: Machine Learning, Deep Learning, 
Convolutional Neural Networks, Supervised and Unsupervised forms of training, clustering algorithms such as 
K-means, spectral graph theory, adversarial networks and that's just getting started.


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


## eigenconcept for ai


The central idea in generative AI is the transformer; and the central model hub is Hugging Face. 
Let's run through a HuggingFace use example subject to some constraints and see how the Python
library `transformers` comes into play. In particular we want to learn how to operate an instance of
a **`pipeline`** which is imported from `transformers`. This is queryable (analogous to `requests`)
using default models through an API; so the minimum viable code is down around 2, 3, 4 or so lines. 
The source video for this eigenconcept is [here on YouTube](https://youtu.be/QEaBAZQCtwE).


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
