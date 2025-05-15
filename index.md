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


- left-justified: To published GitHub pages
    - Indented: To `gh-pages` source markdown files
    - Each topic is anchored by `index.md` file with...
        - ...one or more children


Nexus is a 3-level tree. Here is the link map:


- [nexus](https://robfatland.github.io/nexus)
    - [nexus root index.md](https://github.com/robfatland/nexus/blob/gh-pages/index.md) (L1)
        - [nexus lexicon](https://github.com/robfatland/nexus/blob/gh-pages/lexicon.md)
        - [nexus loose strands (a ttdl)](https://github.com/robfatland/nexus/blob/gh-pages/loosestrands.md)
- [bash](https://robfatland.github.io/nexus/bash)
    - [bash index.md](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md)
        - [environments](https://github.com/robfatland/nexus/blob/gh-pages/bash/env.md)
        - [git and GitHub](https://github.com/robfatland/nexus/blob/gh-pages/bash/git.md)
        - [wrenching the terminal](https://github.com/robfatland/nexus/blob/gh-pages/bash/terminal.md)
        - [ssh tunneling](https://github.com/robfatland/nexus/blob/gh-pages/bash/tunneling.md)
- [data](https://robfatland.github.io/nexus/data)
    - [data index.md](https://github.com/robfatland/nexus/blob/gh-pages/data/index.md)
        - [api](https://github.com/robfatland/nexus/blob/gh-pages/data/api.md)
- [hpc](https://robfatland.github.io/nexus/hpc)
    - [hpc index.md](https://github.com/robfatland/nexus/blob/gh-pages/hpc/index.md)
- [cloud published](https://robfatland.github.io/nexus/cloud)
    - [cloud index.md](https://github.com/robfatland/nexus/blob/gh-pages/cloud/index.md)
        - [spot](https://github.com/robfatland/nexus/blob/gh-pages/cloud/spot.md)
        - [studies](https://github.com/robfatland/nexus/blob/gh-pages/cloud/studies.md)
- [manim published](https://robfatland.github.io/nexus/manim)
    - [manim index.md](https://github.com/robfatland/nexus/blob/gh-pages/manim/index.md)
- [(meta-)documentation published](https://robfatland.github.io/nexus/documentation)
    - [(meta-)documentation index.md](https://github.com/robfatland/nexus/blob/gh-pages/documentation/index.md)
- [python published](https://robfatland.github.io/nexus/python)
    - [python index.md](https://github.com/robfatland/nexus/blob/gh-pages/python/index.md)
        - [jupyter](https://github.com/robfatland/nexus/blob/gh-pages/python/jupyter.md)
        - [python packages](https://github.com/robfatland/nexus/blob/gh-pages/python/packages.md)
- [containers](https://robfatland.github.io/nexus/containers)
    - [containers index.md](https://github.com/robfatland/nexus/blob/gh-pages/containers/index.md)
- [artificial intelligence](https://robfatland.github.io/nexus/ai)
    - [artificial intelligence index.md](https://github.com/robfatland/nexus/blob/gh-pages/ai/index.md)
        - [gcp](https://github.com/robfatland/nexus/blob/gh-pages/ai/gcp.md)
        - [aws](https://github.com/robfatland/nexus/blob/gh-pages/ai/aws.md)
        - [azure](https://github.com/robfatland/nexus/blob/gh-pages/ai/azure.md)
- [quantum computing](https://robfatland.github.io/nexus/quantum)
    - [quantum computing index.md](https://github.com/robfatland/nexus/blob/gh-pages/quantum/index.md)
        - [Hadamard gates](https://github.com/robfatland/nexus/blob/gh-pages/quantum/hadamard.md)
- [earth science](https://robfatland.github.io/nexus/earth)
    - [earth science index.md](https://github.com/robfatland/nexus/blob/gh-pages/earth/index.md)
        - [data](https://github.com/robfatland/nexus/blob/gh-pages/earth/data.md)


[Essay: Understanding the cloud-for-research time investment](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md#the-basic-idea-here)


## Why is nexus?


**nexus** is a response to the tech 'profusion/latency' problem faced by scientists who need a degree of
familiarity with computing infrastructure. The scientist is first a Builder and then a User where they
can focus on the actual research. Suppose a research team needs to puzzle out how to develop code for 
and then run a *lot* of compute tasks on a limited budget; so perhaps containerization and Jupyter Lab servers 
are pieces of the solution. Once set in place the *how to* can be forgotten... but *how to* invariably 
comes up again at some point down the road, be that weeks or months or a year. It is onerous and depressing 
to have to begin again as Builder *de novo*. Nichte diese Töne: `nexus` hopes to be helpful.

