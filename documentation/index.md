# `index.md` anchor of documentation subfolder in nexus

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


## wandering off into the story


Now I turn to a digression. 


Some years ago Don Knuth was asked to write a book. 
He was working as an assistant professor at a small college in Pasadena at the time; and he took a 
close look at the challenge and replied: "Wait! My idea is a more ambitious and a better book... 12 chapters."
Whereupon he embarked on the expanded project which in turn expanded into a treatise on computer science,
and that work has occupied him to this day. He has done and still does other things as well, 
for example delivering an interesting lecture each December. (These lectures may be found on YouTube.)


The books he wrote are known collectively as TAOCP, short for The Art Of Computer Programming. 
By all accounts they are a remarkable series of books, six volumes to date. 
So here is a detail from that extended project: When Volume 2 was going through the publication 
process in 1976 some proofs were sent to Professor Knuth for approval. He found the layout,
the typesetting wanting... and being an energetic individual he solved the problem of re-typesetting 
his book properly by designing and writing a typesetting system. This he published
in such a manner as to ensure it would be universally available 
for anyone's use at no cost. Forever. This system he named TeX. It went through
many revisions from 1978 to 1989 when it was 'officially' released; but it was in
serious academic use as early as 1982. And it was augmented by a content-oriented 
'wrapper' called LaTeX that still used TeX under the hood.


TeX and LaTeX have proven phenomenally successful. Thousands of books and hundreds of thousands
of articles have been elevated from somewhere in the vicinity of 'painful to look at' into a
typesetting stratosphere, just simply a joy to read. By comparison markdown is a handy but 
very simple typesetting tool. So hurray for markdown, rejoice... but TeX exists.


This narrative continues in
[this document](https://github.com/robfatland/reorganiseduponthefloor/edit/main/git/bash_and_git.md)
to return `bash` and `git`. 
