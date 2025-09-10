- [nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)
- [python src](https://github.com/robfatland/nexus/blob/gh-pages/python/index.md)
- [packages](https://github.com/robfatland/nexus/blob/gh-pages/python/packages.md)


# jupyter


Below are notes on useful tasks from within a Jupyter notebook. The follow an intermezzo on building a Littlest Jupyter Hub.
This is a Jupyter Lab / Notebook server replicated several times for multiple users on a single machine. 


## Notes on the Littlest Jupyter Hub


The Littlest Jupyter Hub swaps large scale for small scale and complexity for simplicity. An extended example
case is given below; but before that a word on scale and durability. First let's differentiate the Jupyter 
Hub from Jupyter Lab (or equivalently Jupyter Notebook). The former, the Hub, is infrastructure to serve
multiple Jupyter Lab environments to multiple Users. Each User has their own home directory and often a
pre-built set of Jupyter notebooks (file extension `.ipynb`). In this way User A can make changes and write new
code without running afoul of the work of Users B, C and D. Finally a small detail: The Jupyter Lab environment
runs in a browser and -- for a given notebook cell -- displays the amount of RAM in use. This is helpful
information for judging the size of the Python execution task in relation to the total RAM available, a limiting
factor in hosting multiple Jupyter Labs within a single Jupyter Hub on a single VM. Now to scale:


If I need a single Jupyter Lab instance: I can simply start up a Virtual Machine and proceed to install
a Python distribution and related packages. (There are notes on this here at `nexus` including ways to
port-forward the interface: `ssh` tunnel or `VSCode` for example.)


If I need a large number of Jupyter Lab instances; like 100 of them for a large course with 100 students: I can 
follow the full Jupyter Hub instruction path. This makes use of containers and kubernetes to orchestrate them.


If I need between-two-and-a-few Jupyter Lab instances; like for myself and my three collaborators: The Littlest
Jupyter Hub just might be a good Goldilocks solution. It installs on a single Virtual Machine and provides
processing power, RAM and disk space in the moderate-to-a-lot range depending on which VM I choose. 


### The Littlest Jupyter Hub example case


Suppose one is giving a lecture with the title 'Getting Excited About Data Science'. This lecture will feature 
a student hands-on segment using a Jupyter Lab environment that has been prepared in advance. Consider the 
following qualifiers: 


- The Jupyter Hub is not intended to last longer than a few hours or a couple of days
- Cloud managed notebook services are unsuitable for some reason ("Can't use Colab because of X Y and Z")
- There will be 10 or perhaps even as many as 30 students each needing their own Jupyter Lab
- We are budget-conscious and plan to spend at most $30 on cloud resources
- Student connect experience: Browser > URL > username > password
- Result: Arrive in a pre-populated home directory: 3 notebooks are already here
- Home directories stored in File Share storage: Not object, not block: A network drive (aka NFS)
    - Block storage is the default but to provision it can get expensive and we are being frugal
    - On AWS we have the EFS service; on Azure we have Fileshare
        - These NFS-style shared drives are paid for on a usage (not reserved capacity) basis
        - The down sides: They are a bit slower and can be more complicated to implement

With these conditions the next step is to answer some procedural questions:

- How big of a VM do we need?
- How to get the Littlest Jupyter Hub to place User home directories on the File Share?
- How to configure Username / Password access?
- How to make the three instructional notebooks appear automatically in the User home directory?
    - `nbgitpuller` is a standard method but a bit complicated
 

### Sizing the VM


- Most of the time students are not running code and/or cells run for a fraction of a second
- The limiting resource is actually RAM
- Benchmark for yourself, then multiply by n_students
- e.g. 300MB x 30 students = 9GB so 10GB RAM + RAM for Linux etc so 16GB RAM
            - So this was actually developed on a smaller VM, stop, resize,
- How to benchmark: Use the status bar value for kernel RAM use at bottom of page
- more notes on slack


## Returning to operation in Jupyter


Common Jupyter notebook actions: In relation to a GitHub repo. 


## Topics


- [Display an image](#display-an-image)
- [List directory contents](#list-directory-contents)
- [Use a slider control](#use-a-slider-control)


## Display an image


Many ways to do this: From Python or markdown. This method is simple Python and it appears 
to translate to a proper render in a Jupyter book. Archetype: See the `epipelargosy.ipynb`
chapter in the oceanography Jupyter book.


```
from IPython.display import Image
Image(filename='../relative/path/someimage.png', width=400)
```

This is a "tip of iceberge" remark; there is more to look into and make good use of here. For
example the `IPython.display` library features `SVG`, `display`, `display_svg`, `Audio`, `YouTubeVideo`
and more. To get rolling on this jump into the
[`display` module documentation](https://ipython.readthedocs.io/en/8.26.0/api/generated/IPython.display.html).


Another library: `PIL` for example:


```
from PIL import Image
Image.open(f).resize((width,height),Image.ANTIALIAS)
```


### Markdown approaches to display an image


I think this renders in the Jupyter book but not in Jupyter lab: 


```
{figure} ../img/revelle.jpg
---
height: 300px
name: directive-fig
---
Research Vessel Revelle (Scripps)
```


While this HTML-looking stuff renders in Jupyter lab but not in a Jupyter book: 


```
<BR>
<img src="./../img/revelle.jpg" style="float: left;" alt="drawing" width="600"/>
<div style="clear: left">
<BR>
```


## List directory contents

And related operating system interaction from Python: Use the `os` and `pathlib` libraries.

```
import os

path = "/path/to/directory"
files_and_dirs = os.listdir(path)
cwd = os.getcwd()
```

```
datafilelist = [x for x in dir(obj) if not x.startswith('__')]
```


## Use a slider control
