[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main branch](https://github.com/robfatland/nexus/tree/main)


# `index.md` anchor of documentation subfolder in nexus

## ambitious agenda


Documentation should include use of `top` and timing code execution. Cause those are documentation skills.



# Previous iteration content on markdown


## 1 headers


GitHub supports markdown format: When a github file with extension `.md` is opened 
(in a browser I mean) the contents are reflected according to "markdown" formatting protocol.


Common markdown formatting includes ***headers***. The following text:

```
# Major Heading
## Subsection
### Subsubsection
#### Pretty fine grained at this point
##### Very fine grain
```

renders as

# Major Heading
## Subsection
### Subsubsection
#### Pretty fine grained at this point
##### Very fine grain



## 2 The back-tick character 


The back-tick found at keyboard upper left looks like this: \` .
To print this character here I used the backslash *literal* delimiter; so the markdown is **\\\`**  . 


Use: Back-ticks produce fixed-width-font text. This is useful for indicating or quoting `commands` and 
`code`. 


A single back-tick keeps the resulting text inline with the surrounding text. For example this sentence has \`True\` in the markdown which renders inline as `True`. 
Three back-ticks delimit multi-line code blocks:


```
def Bumpkins(n, qi):
    for i in range(n):
        print('oh dear, this is tragic...')
```

Notice that the back-tick is a *verbatim* delimeter. Other delimiters are not respected when they occur 
inside a backtick field. However asterisk delimiters *outside* of backtick delimiters work fine. Compare:
`**asterisks inside**` versus **`asterisks on the outside`**. 


## 3 asterisks


In this text please find single, double, and triple asterisk delimiters. 
\*Single\*. \*\*Double\*\*. \*\*\*Triple\*\*\* produces *Single* **Double** ***Triple***. 


## 4 quotations


A leading `>` character renders text as a quotation. 


> This is useful to offset "special note" offset blocks of text. 


## 5 hyperlinks 


Place the text to appear within square bracks and follow it with no spaces by the link URL 
in parentheses. [This link goes to the Google search page](https://google.com). It
is constructed as `[link text](https://google.com)`. 


Within a document viewed in a browser: Holding the cursor over a link reveals the link address.
Within a page, links to headers are simple: Type a pound sign \# followed by
a header name with spaces replaced by hyphens. (It may not work at the moment.)


This `[header section link](#1-headers)` becomes [header section link](#1-headers).



## 6 html


HTML can be embedded in a markdown file.


## LaTeX digression


Some time ago computer scientist Don Knuth was asked to write a short book on programming. 
He was working as an assistant professor at a small liberal arts college in Pasadena and 
had lots of time to spare. So he took a close look at the suggestion and decided that he had 
a better more ambitious idea for a book that would require as many as 12 chapters. He 
embarked on this expanded project which became a treatise on computer science, with refinements
still keeping him occupied to this day. For more interesting ideas from Professor Knuth 
look for him on YouTube. 


The book, by the way, became a series of six books known collectively as TAOCP. This is short 
for The Art Of Computer Programming. Still back in time when Volume 2 was going through 
the publication process (this was 1976) some proof sheets were sent to Professor Knuth for 
approval. He found the layout and typesetting wanting, and being an energetic individual 
with lots of spare time he solved the problem of re-typesetting his book by designing and 
writing a typesetting system. This he published so as to ensure it would be universally available 
for anyone's use at no cost, forever. This system he named TeX. It went through
many revisions until its official release in 1989 but long before then it was widely adopted
in academia. TeX was also over time augmented by a content-oriented *wrapper* called LaTeX 
that used TeX under the hood.


TeX and LaTeX have been used to typeset thousands of books, hundreds of thousands
of academic articles, many thousands of dissertations and theses (including mine), 
and so on; all driven by a simple desire to move from 'painful to look at' to 
'simply a joy to read'. $\tau h \alpha \nu \kappa \sigma \; \; \Delta \omicron \nu$.



(And LaTeX equations now render from GitHub markdown.)


$\begin{align}
y = \sqrt{x}
\end{align}$


