[nexus published](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


<img src="assets/img/greenandblack.png"
     alt="green and black icon"
     width="500"
     style="float: center; margin-right: 10px;" />



**nexus** is a *threefold documentation resource* centered on technology, tools and methods for 
open data science. Nexus is "How I Did It" notes in case I need to do it again in the future.
Content is threefold in the sense of: *native* plus *external* plus *hybrid* documentation. 
*Hybrid* is (native) commentary from working through (external) guides and tutorials.


## Interpreting the `nexus` content map 


Nexus is a 3-level tree of notes. Every page has a 'build' form which is all I really care about. 
However `nexus` also has a published `github pages` form with "published" URLs:
- [https://robfatland.github.io/nexus](https://robfatland.github.io/nexus) is the root i.e. tier 1
- [https://robfatland.github.io/nexus/bash](https://robfatland.github.io/nexus/bash) for tier 2 topics
- [https://robfatland.github.io/nexus/bash/git](https://robfatland.github.io/nexus/bash/git) for tier 3


### Structure of the content map


The use of keywords is intended to remind one of the page's detailed focus.

- Nexus Tier 1 (only one such page)
    - Indent 1 Type A: Tier 1+ subtopics: A **lexicon** and **loose strands**
    - Indent 1 Type B: Tier 2 topics such as `bash` (`bash/index.md`) (with keywords: giraffe Switzerland)
        - Indent 2: Tier 3 children such as `git` (`bash/git.md`) (with keywords: Albatross Spain)


### Content map


- [nexus root](https://github.com/robfatland/nexus/blob/gh-pages/index.md) (Level 1)
  - [lexicon](https://github.com/robfatland/nexus/blob/gh-pages/lexicon.md) (Level 1+)
  - [loose strands (a ttdl)](https://github.com/robfatland/nexus/blob/gh-pages/loosestrands.md) (Level 1+)
    - [bash](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md) (Level 2) 
        - [environments](https://github.com/robfatland/nexus/blob/gh-pages/bash/env.md) (Level 3)
        - [git and GitHub](https://github.com/robfatland/nexus/blob/gh-pages/bash/git.md) (Level 3)
        - [wrenching the terminal](https://github.com/robfatland/nexus/blob/gh-pages/bash/terminal.md) (Level 3)
        - [ssh tunneling](https://github.com/robfatland/nexus/blob/gh-pages/bash/tunneling.md) (Level 3)
    - [data](https://github.com/robfatland/nexus/blob/gh-pages/data/index.md) (stub)
        - [api](https://github.com/robfatland/nexus/blob/gh-pages/data/api.md) (keywords: NoSQL API serverless Azure periodic table ocean science data publication)
    - [hpc](https://github.com/robfatland/nexus/blob/gh-pages/hpc/index.md) (stub)
    - [cloud](https://github.com/robfatland/nexus/blob/gh-pages/cloud/index.md) (keywords: VM login using VSCode plus basics and links)
        - [spot market / preemptibl instances](https://github.com/robfatland/nexus/blob/gh-pages/cloud/spot.md) (keywords: preemptible spot market checkpoint)
        - [studies](https://github.com/robfatland/nexus/blob/gh-pages/cloud/studies.md) (keywords: SCOPED Neotoma nascent link-based stub)
        - [organizations](https://github.com/robfatland/nexus/blob/gh-pages/cloud/organizations.md) (keywords: AWS organizations services) (**Note: Rebrand as AWS-organizations**)
        - [aws object storage](https://github.com/robfatland/nexus/blob/gh-pages/cloud/aws.md) (keywords: local drive S3 object storage)
        - [aws ai](https://github.com/robfatland/nexus/blob/gh-pages/cloud/aws-ai.md) (keywords: AWS AI workshop notes SageMaker Bedrock) (**Note: Merge with AI-AWS**)
        - [azure](https://github.com/robfatland/nexus/blob/gh-pages/cloud/azure.md) (stub)
        - [gcp](https://github.com/robfatland/nexus/blob/gh-pages/cloud/gcp.md) (stub)
    - [manim](https://github.com/robfatland/nexus/blob/gh-pages/manim/index.md) (nascent notes on getting started)
    - [(meta-)documentation](https://github.com/robfatland/nexus/blob/gh-pages/documentation/index.md) (stub; mentions flameshot)
    - [python](https://github.com/robfatland/nexus/blob/gh-pages/python/index.md) (keywords: topics to learn, a start on hashing)
        - [jupyter](https://github.com/robfatland/nexus/blob/gh-pages/python/jupyter.md) (keywords: Littlest, image display, list directory, slider control (stub))
        - [python packages](https://github.com/robfatland/nexus/blob/gh-pages/python/packages.md) (stub: should namedrop apt, pip, conda, mamba, pixi)
    - [containers](https://github.com/robfatland/nexus/blob/gh-pages/containers/index.md) (keywords: nascent eigenconcept notes refers MSE544)
    - [artificial intelligence](https://github.com/robfatland/nexus/blob/gh-pages/ai/index.md) (keywords: AI eigenconcepts nascent notes)
        - [gcp](https://github.com/robfatland/nexus/blob/gh-pages/ai/gcp.md) (keywords: Gemini bootstrap notes)
        - [aws](https://github.com/robfatland/nexus/blob/gh-pages/ai/aws.md) (get started pointers)
        - [azure](https://github.com/robfatland/nexus/blob/gh-pages/ai/azure.md) 
    - [quantum computing](https://github.com/robfatland/nexus/blob/gh-pages/quantum/index.md) (stub)
        - [hadamard gates](https://github.com/robfatland/nexus/blob/gh-pages/quantum/hadamard.md) (stub)
    - [earth science](https://github.com/robfatland/nexus/blob/gh-pages/earth/index.md) (stub)
        - [earth science data](https://github.com/robfatland/nexus/blob/gh-pages/earth/data.md) (stub)


[Essay: Understanding the cloud-for-research time investment](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md#the-basic-idea-here)


## Why is nexus?


**nexus** is a response to the tech 'profusion/latency' problem faced by scientists who need a degree of
familiarity with computing infrastructure. The scientist is first a Builder and then a User where they
can focus on the actual research. Suppose a research team needs to puzzle out how to develop code for 
and then run a *lot* of compute tasks on a limited budget; so perhaps containerization and Jupyter Lab servers 
are pieces of the solution. Once set in place the *how to* can be forgotten... but *how to* invariably 
comes up again at some point down the road, be that weeks or months or a year. It is onerous and depressing 
to have to begin again as Builder *de novo*. Nichte diese Töne: `nexus` hopes to be helpful.

