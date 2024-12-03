[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


This **README** anchors the github pages branch of the `nexus` repo. It supersedes `index.md` 
but I think maybe the README is unnecessary because it is not published; so it would just be 
redundant with the main branch README. 


* [nexus main branch](https://github.com/robfatland/nexus/tree/main)
* [nexus published](https://robfatland.github.io/nexus).


## How is this site built and published? 


This **nexus** repo uses a [Jekyll](https://jekyllrb.com/) template (the free service is called *GitHub pages*) 
to generate a nicely formatted static website.  The content resides in the repo on a code branch called `gh-pages`. 
Publication is triggered automatically after each *commit*. URLs:


- [main branch of the nexus GitHub repo](https://github.com/robfatland/nexus/tree/main)
- [gh-pages branch](https://github.com/robfatland/nexus/tree/gh-pages)
- [The nexus static website](https://robfatland.github.io/nexus/)


Here is how to get one of these https://**organization**.github.io/**repo** websites started:


- Create some repository on GitHub
- Menus: Github --> repo --> Settings --> **pages** tab on the left; choose a *theme*
- Switch to the `gh-pages` branch: From the `Main` branch, use the chooser
- At the documentation site it will be `index.md` that renders (not a README)
    - Edits can be a little slow to propagate; refresh!
- The root directory `index.md` renders as default content
    - Add other folders and markdown; but cross reference using documentation website URLs, not GitHub URLs
        - Example: **`https://organization.github.io/repo-name/subfolder`** renders the **`index.md`** therein





