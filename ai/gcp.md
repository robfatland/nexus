[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


[ai index src](https://github.com/robfatland/nexus/blob/gh-pages/ai/index.md)


# artificial intelligence on the Google Cloud Platform


These notes cover some basic Vertex AI API examples. Access will be from a Jupyter notebook avoiding colab.
(This is not a preference; just simpler at the moment.)


First get access to Gemini on the Google cloud. 
- Find the Gemini for Google Cloud page in the console using search
- Click "Enable"
- Go get some coffee... this tends to take a few minutes



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
import os
import vertexai

PROJECT_ID = "<some text identifier>"
LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-east4")
vertexai.init(project=PROJECT_ID, location=LOCATION)
```


Now we have a handle through the `vertexai` object. From here
import some libraries.


```
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmBlockThreshold,
    HarmCategory,
    Image,
    Part,
    SafetySetting,
)
```


model = GenerativeModel("gemini-2.0-flash")
response = model.generate_content("How does the Feynman path integral formulation permit speeds greater than the speed of light?")
print(response.text)




responses = model.generate_content("Why is the sky blue?", stream=True)
for response in responses:
    print(response.text, end="")




generation_config = GenerationConfig(
    temperature=0.9,
    top_p=1.0,
    top_k=32,
    candidate_count=1,
    max_output_tokens=8192,
)

response = model.generate_content(
    "Why is the sky blue?",
    generation_config=generation_config,
)

print(response.text)
