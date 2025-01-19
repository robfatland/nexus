[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main](https://github.com/robfatland/nexus/tree/main)


# Python

- Recommendation: The [Python Data Science Handbook by Jake Vander Plas](https://jakevdp.github.io/PythonDataScienceHandbook/)



## Topics covered here

A wish list...


- 'hashable'
    - means *immutable* and subject to hashing
        - to *hash* means to create a unique numerical identifier for an object
        - mutable non-hashables include lists, dictionaries and sets
        - hashable objects include strings, floats, ints, tuples (if containing immutables), frozen sets
        - use `hash(som_object)` to raise an error if it is not hashable
- dictionaries: more than an inconvenient version of a list
- yield
- decorators



## hashing

This code: 


```
print('this string', hash('this string'))
print(10, hash(10))
n = 10
print(n, hash(n))
n = 10.0
print(n, hash(n))
n = 10.1
print(n, hash(n))
```


produces


```
this string 8534039767811493564
10 10
10 10
10.0 10
10.1 230584300921368586
```

So 10^20 is roughly the dynamic range apparent in Python hashing. This is the case as well for larger objects such as a 
string of 600 characters. There are say (10^2)^20 possible strings of length 20... so surely it is possible to have 
hash collisions. These do happen (and the birthday paradox is relevant). There are two ideas to note in consequence:


- Hashing is not encoding; it is labeling. There is no intent to reconstruct the value being hashed.
- Hashing collisions can raise issues like how to deal with storage/retrieval; but this is Someone Elses Problem.  
