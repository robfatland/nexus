[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


[ai index src](https://github.com/robfatland/nexus/blob/gh-pages/ai/index.md)


# artificial intelligence on the Google Cloud Platform


Circumvent this content by working from [this GCP Quickstart page](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart).


This page covers a simple Vertex AI API example. Access is from a Jupyter notebook avoiding `colab`.
(This is not a preference; just simpler.)


The basic idea is that Vertex AI provides an interface / API to various AI models. We set things up, 
choose a particular model and send it a prompt. 


> Before you start: Be aware that GCP uses logical organization units called *Projects* which have both
> informal and formal labels. For example my Project is called `robs-project` *informally* but I refer to
> this project by its *formal* identifier `robs-project-314159`.
>
> Before you start: After logging in to GCP be sure to enable the Gemini API. See the Quickstart link above.
> The TLDR is: Find the **Gemini for Google Cloud** page in the console using search and click "Enable" (and get some coffee).



Go to Vertex AI in the GCP console -- again: You are logged in and associated with a Project. 
From the Vertex AI dashboard select Workbench (probably Workbench Instance). Start a Jupyter Notebook
with "Create New" or there may be some other rigamarole to get going. Eventually a VM (instance) 
starts up; so click on the Notebook instance then click the button Open Jupyter Lab. Voila a 
Jupyter Lab appears pre-stocked with all sorts of AI learning materials and examples. 


If the GCP AI platform is not installed (as in `import vertexai` does not work) it might help to install:


```
%pip install --upgrade --user google-cloud-aiplatform
```


One stop shopping, so far so good. For the next part: A *Project* on the Google Cloud is a billable entity associated with
an organization. This is referred to using `PROJECT_ID` so be aware this will cost money.


```
import vertexai
PROJECT_ID = "<formal project identifier (see comment above)>"
vertexai.init(project=PROJECT_ID, location="us-west1")
```


Now we have an API handle through the `vertexai` object. Next import some libraries, establish a connection to Gemini Flash and try a prompt.


```
from vertexai.generative_models import GenerationConfig, GenerativeModel, HarmBlockThreshold, HarmCategory, Image, Part, SafetySetting
model = GenerativeModel("gemini-2.0-flash")

def Q(s):
    response = model.generate_content(s)
    print(response.text)
    # Enable this to see a breakdown of the prompt/response: return response

Q("What are the integers between 3 and 7?")
```

Here is example code for tinkering with the basic LLM interface: 


```
generation_config = GenerationConfig(
    temperature=0.9,
    top_p=1.0,
    top_k=32,
    candidate_count=1,
    max_output_tokens=8192,
)

response = model.generate_content("Why is the sky blue?", generation_config=generation_config)
print(response.text)
```
