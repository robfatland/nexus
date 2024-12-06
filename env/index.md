# Python environments


This is an ambitious topic because of its many tentacles. Rather than abandon 
all hope I'm going to start with the concept of the `import` utility.



## `import`


Suppose I have written some code in a Jupyter notebook that calculates
a value I assign to a variable `t`.  Suffering from delusions of grandeur my 
immediate thought is 'this wonderful code belongs in its own module file... so I can use
it from anywhere... and what is more I should publish it as a Python package for all the 
world to install and import and use!' This is an altruistic impulse--good for me--but
how to proceed? Here is how to make the dream a reality:

- decide on a reasonably short name for the module: I choose *ant*.
- open my editor and cut-paste the code from `b.ipynb` into `ant.py`
- convert the code to a function called `Totient(n)`
    - remember to include a docstring
- below the function code create a test program in the `ant.py` file:


```
if __init__ == "__main__":
    t = Totient(10)
    if not t == 4: print("Totient() fails for n = 10")
    else:          print("Totient() passes its test")
```

- save the file `ant.py`
- run the file as a program to ensure the test passes: `python3 ant.py`
- Back in the Jupyter notebook `b.ipynb` write these two lines of code
 
```
from ant import Totient

t = Totient(73)
```

- Decide that this module should definitely be published as a Python package
- Search online for *how to publish a Python package* and follow the tutorial
    - For more on this: See below


Now that I have done that: I should really consult with Naomi about how to properly
do the import. Why not use `from ant import *`? Why not use `import ant`?


In answer to the second question: `import ant` is a perfectly reasonable thing
to do. Then I will have to say `t = ant.Totient(n)`. If the `ant` module evolves
to feature more functions (aka methods): My notebook will have access to those
as well through this `import`.


The first question 'Why not say `from ant import *` has an involved answer but
the TLDR is ***don't do this***.


### Why we do not use `from ant import *`


This practice pollutes the global namespace where the `import` runs, in this 
example the notebook `b.ipynb`. The module file `ant.py` has a global namespace 
as does any Python ...um... "entity".  A namespace is a dictionary mapping strings
to the address of corresponding code. The global namespace of a module coexists 
with the global namespace of the notebook: They each have their own. The 
intersection of their respective namespaces is the empty set. 


Suppose `ant.py` includes the line `from math import cos`. When the module executes
(for example as a result of the `import` line in `b.ipynb`):  The global namespace 
will have a new dictionary entry. The key of this entry will be `cos` and the value 
will be a pointer to the cosine function code. By using pointers to code the code
itself exists only once in this Python universe (rather than making multiple
copies of the same code every time something imports it). 


Noting that the module `ant.py` executes due to the `import ant` in `b.ipynb`:
What does this mean? It means that Python will attempt to run all the code in
the module, thereby populating that module's global namespace. But what if there
is code in `ant.py` we *do not* want running during an `import`?  For example:
code that tests the module's functions. This is why `if __init__ == "__main__"`
was included: It runs when the module is run via `python3 ant.py` but it does
not run during the `import` code execution. 


## Publishing a Python package

- here is where I left off
