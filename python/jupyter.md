- [nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)
- [python src](https://github.com/robfatland/nexus/blob/gh-pages/python/index.md)
- [packages](https://github.com/robfatland/nexus/blob/gh-pages/python/packages.md)


# jupyter


## Notes on the Littlest Jupyter Hub


Suppose one is giving a lecture with the title 'Get Excited About Data Science'. This lecture will feature 
a student hands-on segment using a Jupyter Lab environment; but one that has been prepared in advance subject
to the following qualifiers: 


- The Jupyter Hub is not intended to last longer than a few hours or a couple of days
- Cloud notebook services are undesirable for some reason ("no Colab because X Y Z")
- There will be 10 or perhaps as many as 30 students, no more
- Let us be budget-conscious and spend at most $30 on cloud resources
- Student connect: Browser, URL, some username, one customized short-term password
    - Result: A pre-populated home directory: 3 notebooks are here
- Home directories stored in FILE storage: Not object, not block: A network drive
    - Block storage is like an internal drive so 64GB for a LJH
    - But I don't want to expend those dollars
    - So EFS which is NFS which on Azure is Azure Fileshare which is a floating drive that is pay by used capacity
- But there are some things to figure out...
    - How big is the VM gotta be?
    - How do I get JHub to put home directories in the Fileshare?
    - How do I have everyone launch their env with a single password?
    - How do I set up a starter file system with notebooks and such?
        - There is nbgitpuller which is flexible and nice but N didn't want that level of sophistication
    - The Azure-specific solution involved mounting the Azure network share to the VM
    - VM sizing
        - Most of the time your students are not running code
        - Split-second run time
        - The limiting resource is actually RAM
        - Benchmark for yourself, then multiply by n_students
        - e.g. 300MB x 30 students = 9GB so 10GB RAM + RAM for Linux etc so 16GB RAM
            - So this was actually developed on a smaller VM, stop, resize,
        - How to benchmark: Use the status bar value for kernel RAM use at bottom of page
- Get mechanical notes from slack


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
