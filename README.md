[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main branch](https://github.com/robfatland/nexus/tree/main)


This **`README.md`** shows up only on the GitHub pages branch of the `nexus` repo. (There is another `README.md` on the
main branch.) This `README.md` does not get published to the corresponding [`nexus website`](https://robfatland.github.io/nexus);
rather the source for the root published page is `index.md`, also in this directory.


## How is this site built and published? 


This **nexus** repo uses a [Jekyll](https://jekyllrb.com/) template (the free service is called *GitHub Pages*) 
to generate a nicely formatted static website. The content resides in the repo on a code branch called `gh-pages`. 
Publication is triggered automatically after each *commit*. URLs:


- [main branch of the nexus GitHub repo](https://github.com/robfatland/nexus/tree/main)
- [gh-pages branch](https://github.com/robfatland/nexus/tree/gh-pages)
- [The nexus static website](https://robfatland.github.io/nexus/)


## Link convention


**Internal links in nexus point to the gh-pages branch source**, not to the published website. This is
because the primary mode of interaction is editing content directly on the gh-pages branch (either in
the browser or via a local editor like Kiro). The published website is a read-only output; the source
is where work happens.

Example internal link format:
```
[bash notes](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md)
```

The published website URLs (`https://robfatland.github.io/nexus/...`) are useful for sharing with
others who just want to read, but are not used for internal cross-references.


## How to set up a GitHub Pages site like this


- Create a repository on GitHub
- Settings → **Pages** tab → choose a theme (or add `_config.yml` manually)
- Switch to the `gh-pages` branch (use the branch chooser or create it)
- The root `index.md` renders as the site's home page (not README.md)
- Each subfolder's `index.md` renders at its corresponding URL path
- Edits can be slow to propagate; refresh the published site after a minute or two
