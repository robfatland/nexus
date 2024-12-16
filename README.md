[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main branch](https://github.com/robfatland/nexus/tree/main)


This **`README.md`** shows up only on the github pages branch of the `nexus` repo. (There is another `README.md` on the
main branch.) This `README.md` does not get published to the corresponding [`nexus website`](https://robfatland.github.io/nexus);
rather the source for the root published page is `index.md`, also in this directory.


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





