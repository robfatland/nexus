**nexus** is a *threefold* documentation resource for open research: *native*, *external* (via *pointers*, usually URLs), 
and *hybrid*. Hybrid documentation is commentary produced by working through an external resource such as a tutorial. This
is intended to fill context gaps, note gotchas and so on: Make the path easier to follow.


You are reading [meta-narrative for the nexus repo](https://github.com/robfatland/nexus). 
**nexus** content resides in the [`gh-pages` branch](https://github.com/robfatland/nexus/tree/gh-pages)
and this is published at [https://robfatland.github.io/nexus](https://robfatland.github.io/nexus).


# [nexus](https://robfatland.github.io/nexus/)


[This repo](https://github.com/robfatland/nexus/tree/main) started life as 'how to disable garish fonts in
a typical **`bash`** interface'. I just want green characters on a black background and one day I got sick of 
looking up the procedure yet again. To generalize the process, nexus is now here to remind me how open
science procedure works and, related, how to build research computing cyberinfrastructure.


## Example motivating tasks


Each of the following examples links to some corresponding work. 


- Task Zero: How do I manage Python environments?
- Task I wrote some code that is very specific to some oceanography data. How do I publish it as a package?
- Task 2: I derived some results as useful data. How do I publish it as an API-accessible resource?
- Task 3: I am working with some sensitive data and I want to be really careful about restricting access.
- Task 4: I like having my code backed up in a GitHub repo. What are the ten `git` commands I need to master?


## Navigating this GitHub repository


This repo has a `main` branch which primarily consists of this README file. Then there is the publication
component in a `gh-pages` branch. Every time there is a commit to this branch: A (much prettier) documentation
website is refreshed. 


- [nexus content `gh-pages` branch](https://github.com/robfatland/nexus/tree/gh-pages)
- [nexus published website](https://robfatland.github.io/nexus).
- [nexus 'main' branch](https://github.com/robfatland/nexus).


## nexus aspirations (the to-do list)

- TCOTU: Understanding, building, maintaining, using Python environments
    - corollary: customizing `bash`, `vi` to a simple appearance
    - **`ssh`** tunnels from one machine to another
    - headless `jupyter` running on a cloud VM with a localhost laptop interface
- Comparison: **`miniconda`** versus **`anaconda`**
- PC-based Linux / IDE: **`Ubuntu bash`**, **`WSL-2`**, **`VSCode`**
    - Containerization
    - conda environments
- cloud infrastructure building
        - Data systems, APIs
        - Building a Flask server
        - Cloud security
        - ML/AI: CNN, NLP
        - varieties of cloud CLI
        - cloud spend notification
        - stopping runaway cloud spend automatically
- [Python's guide to publishing a software package](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- My repository-based projects
    - [epipelargosy, an oceanography project]()
    - [steam: university-level STE(A)M notes](https://github.com/robfatland/steam)
    - [sodium: a study of distributed forms of information](https://github.com/robfatland/sodium)
    - [analytic number theory](https://github.com/robfatland/ant)
    - [middle school level STE(A)M outreach](https://github.com/robfatland/othermathclub)
