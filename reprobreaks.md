## Comments


Read 3/23/2026.


### Abstract


- "We propose" --> "We employ" (*)


### Keywords


- If possible: Suggest adding "open science" (***)


### 1 Introduction


#### Paragraph 2


There is a "best practice" comment opportunity here: `pip freeze` will tend to list package versions
in gory detail; but what about simplifying this down and letting the package manager sort it out? If you have any
insight to offer (and space to add it): I think it would be interesting as it falls under your primary conclusion. (**)


#### Paragraph 3


- Might define "artifact evaluation badge". (*) Likewise explain or reference "Software Heritage". 
- Question: Is there a means to the repro end of placing a Docker Image that contains everything? Or does that idea fail for some reason? 


#### Paragraph 4


Unclear on what is meant by "stratified".


#### Key finding (2)


- "can have" --> "had". Also "succeed" --> "succeeded".


#### Key finding (3)


Could number the three taxonomic categories (*)


### 2 Methodology


#### 2.1 Corpus Paragraph 2


- `.ipynb` comment raises an interesting point: The sub-topic of why a researcher stops at
their Jupyter notebook (`Run all cells` may have been their workflow) rather than creating
`.py` modules. This might be out of scope, granted. 


#### Paragraph 3


- 42 is appreciated
- Idle question: Does your evaluation system include Python code and does it therefore
pass self-scrutiny?

#### 2.2 Automated Stage 3


- Be nice to define / elaborate "Pydantic schema"
- suggest "; we" --> ". We"

#### Stage 4


- Suggest 900 sec --> 15 minutes


### 3 Failure Taxonomy


- Suggest "who can address the gap" --> "how authors could address the gap (wwhere some failure modes were noted above in 2.2):"


#### 3.2 Tier 2


- Does `no_runnable_code` include the case where only `.ipynb` files are present?
- Does `phantom_dependency` include failing to indicate `conda-forge` etc?
  

### 4 Results


#### 4.2 Build-Stage Findings


- suggest "(12.8%)" --> "one in eight"


#### 4.3 Framework Variation


May be out of scope but I do wonder why PyTorch does so poorly in comparison to TensorFlow. Speculation?


### 5 Discussion


#### 5.1 Paragraph 2 at the end: Suggest "but" --> "that"


#### 5.2 Relationship to Prior Work paragraph 1


First two sentences could be reworked to flow better. 


#### 5.3 Limitations


- Good show taking this on.
- Suggest "successful builds" --> "successful LLM-driven builds"
- I like the LLM conclusion at the end of this.
- Optional: Somewhere in this section you could acknowledge the gap between a workflow baked into a Jupyter notebook and one built on `.py` modules, as noted above. Not to throw either the notebooks or your evaluation system under the bus; just an observation.


### 6 Conclusion


This is really a matter of taste but when wandering into normative statements (i.e. how the world should be)
it is common practice in publications like this to use the "could" modality rather than "should". (I looked 
it up and these are respectively called *epistemic* and *deontic* modalities. Cool!) So for example: 


"conferences and journals **could** require and enforce [etcetera] for papers that include computational experiments"


I think your *further work* section is excellent. 
