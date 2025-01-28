- [nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
- [python src](https://github.com/robfatland/nexus/blob/gh-pages/python/index.md)

# jupyter


Common Jupyter notebook actions; some in relation to a GitHub repo. 

## Topics


- [Display an image](#display-an-image)


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


Another library to experiment with is `PIL`:


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


