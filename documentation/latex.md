[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md),
[documentation index](https://github.com/robfatland/nexus/blob/gh-pages/documentation/index.md)


# LaTeX in Jupyter Markdown Cells

Quick reference for LaTeX math typesetting in Jupyter notebooks. This page consolidates
patterns from across the nexus and ant repositories into a single findable reference.

External reference: [OEIS LaTeX symbol list](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols).


## Equation Delimiters

| Delimiter | Effect | Use case |
| :--- | :--- | :--- |
| `$...$` | Inline, compact | Flowing with text: $x = y$ |
| `$$...$$` | Centered standalone | Displayed equations (centered) |
| `$\begin{align}...\end{align}$` | Left-justified standalone | Preferred for proofs and derivations |
| `\begin{equation}...\end{equation}` | Centered, numbered (in LaTeX; no number in Jupyter) | Formal equations |

**Recommendation:** Use `$\begin{align}...\end{align}$` for standalone equations. It gives
full-size formatting (sums, products render properly) while staying left-justified, which
reads better in a notebook context than centered `$$`.

Example:

```
$\begin{align}\sum_{p=2,3,\dots}^{\infty}\frac{1}{p}\end{align}$
```

renders as a left-justified, full-size sum.


## Multi-line Equations

**Aligned on `&`** (use `\\` for line breaks):

```
$\begin{align}
\sigma(n)
= \; & \sigma(2^{a-1}) \cdot \sigma(p) \\
= \; & (2^a-1) \cdot (p + 1) \\
= \; & 2n
\end{align}$
```

**Left-justified sequence** (prefix each line with `&`):

```
$\begin{align}
& a = 4 \\
& b = 7a \\
& d = b - a - x
\end{align}$
```

**Right-justified sequence** (no `&` prefix):

```
$\begin{align}
a = 4 \\
b = 7a \\
d = b - a - x
\end{align}$
```


## Cases (Piecewise Functions)

```
$\begin{align}
\mu(n) = \begin{cases}
1 & \textrm{ if } n = 1 \\
(-1)^k & \textrm{ if } n \textrm{ is a product of } k \textrm{ distinct primes} \\
0 & \textrm{ otherwise}
\end{cases}
\end{align}$
```


## Stacked Conditions Under Sums

Use `\substack` for multiple conditions:

```
$\begin{align}\sum_{\substack{k=-5\\k \neq 0}}^{5} \pi_k \end{align}$
```

Or use `\atop` (older style, font shrinks with nesting):

```
$\begin{align}
\sum_{k=1 \atop (k, d) = 1}^{d} f\Biggl( \frac{k}{d} \Biggr)
\end{align}$
```


## Symbols & Operators

| Pattern | LaTeX | Rendered |
| :--- | :--- | :--- |
| does not divide | `\nmid` | $a \nmid b$ |
| element of | `\in` | $a \in B$ |
| such that | `\ni` or `\backepsilon` | $\ni$ |
| there exists | `\exists` | $\exists$ |
| for all | `\forall` | $\forall x \in A$ |
| negation | `\neg` | $\neg a$ |
| iff | `\iff` | $\iff$ |
| congruent | `\equiv` | $\equiv$ |
| defined as | `:=` or `\stackrel{\mathrm{def}}{=}` | $:=$ |
| questioned equality | `\stackrel{?}{=}` | $a \stackrel{?}{=} b$ |
| set intersection | `\cap`, `\bigcap` | $A \cap B$ |
| set union | `\cup` | $A \cup B$ |
| empty set | `\emptyset` | $\emptyset$ |
| product | `\prod_{a}^{b}` | $\prod_{a}^{b}$ |
| sum | `\sum_{c}^{d}` | $\sum_{c}^{d}$ |
| integral | `\int_{a}^{b} f(x) \; dx` | $\int_{a}^{b} f(x) \; dx$ |
| floor | `\lfloor x \rfloor` | $\lfloor x \rfloor$ |
| norm | `\lVert x \rVert` | $\lVert x \rVert$ |
| absolute value | `\big| a \big|` | $\big| a \big|$ |
| big-oh | `\mathcal{O}(f(x))` | $\mathcal{O}(f(x))$ |
| contradiction | `\otimes` | $\otimes$ |


## Font Styles

| Style | LaTeX | Rendered |
| :--- | :--- | :--- |
| blackboard bold | `\mathbb{R}` | $\mathbb{R} \; \mathbb{Z} \; \mathbb{N}$ |
| calligraphy | `\mathcal{A}` | $\mathcal{A B C D E F}$ |
| text in equations | `\textrm{ text }` | $x \textrm{ divides } y$ |
| hat | `\hat{x}` | $\hat{x}$ |
| tilde | `\tilde{x}` | $\tilde{x}$ |
| vector arrow | `\vec{x}` | $\vec{x}$ |
| phi variants | `\phi` vs `\varphi` | $\phi \quad \varphi$ |


## Font Sizing

Sizes in ascending order: `\tiny`, `\scriptsize`, `\small`, `\normalsize`, `\large`, `\Large`, `\LARGE`, `\huge`, `\Huge`.

Wrap in curly braces to compartmentalize: `{\Large \sum}` gives ${\Large \sum}$

```
$\begin{align}{\\Huge \prod_{i=1}^{n}\frac{1}{i^2}}\end{align}$
```

Notes:
- `\footnotesize` is not recognized in Jupyter's MathJax.
- Nesting size commands does not compound (no effect).
- Sizes below `\small` (`\scriptsize`, `\tiny`) work but differences are subtle.


## Font Color

Use `\color{name}{content}`:

```
$\begin{align}\color{blue}{\Large \ngtr} \color{red}{\small \prod_{i=1}^{n}\frac{1}{i^2}} \color{green}{\Huge \infty}\end{align}$
```

Available colors include: red, blue, green, orange, purple, cyan, magenta, black, white.


## Delimiters & Sizing

**Auto-sizing** with `\left` / `\right`:

```
$\left\lfloor \frac{x}{d} \right\rfloor$
$\left\{ \sum_{d|n} \frac{n}{d} \right\}$
```

**Manual sizing**: `\bigl(` `\Bigl(` `\biggl(` `\Biggl(`


## Matrices

```
$A=\left[{\begin{array}{cc}
   a & b \\
   c & d \\
  \end{array}}\right]$
```

Column vector:

```
$\tilde{v}=\left[{\begin{array}{c}x\\y\end{array}}\right]$
```


## Raising & Lowering

Push a subscript down: `\lower1ex{content}`

```
$\sigma_{\lower1ex{1 - \alpha}}$ vs $\sigma_{1 - \alpha}$
```

General positioning with `\raise` and `\lower` using `Nex` units.


## Spacing

| Command | Width | Example |
| :--- | :--- | :--- |
| `\;` | thick space | $a \; b$ |
| `\ ` (backslash-space) | medium space | $a \ b$ |
| `\,` | thin space | $a \, b$ |
| `\quad` | em-width | $a \quad b$ |
| `\qquad` | 2 em-widths | $a \qquad b$ |

Compare: $xy$ vs $x \; y$ vs $x \quad y$


## Non-LaTeX: Unicode & HTML Entities

**QED tombstones**:
- Filled: &#x220e; (`&#x220e;`)
- Outline box: &#x2610; (`&#x2610;`)
- Usage: `$(c, d)=1.\;\;$ &#x2610;`

**Special characters**: Use Unicode directly — Möbius (ö), Erdős (ő), Gödel (ö).

**Line breaks**: Use `<br>` or `<BR>` for vertical spacing between markdown blocks.


## Equation Numbering (Manual Hack)

Jupyter has no native equation numbering. Workaround: pad with `\;` spacers:

```
$\begin{align}
v + f = e + 2
\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;
(1)
\end{align}$
```

Not elegant, but functional.


## Tables with LaTeX

Markdown tables work but are always centered. For left-justified tables, use HTML:

```html
<table style="margin-left: 0;">
<tr><th>p:</th><th>2</th><th>3</th><th>5</th></tr>
<tr><td>$\alpha = 1$</td><td>1</td><td>2</td><td>4</td></tr>
</table>
```

CSS/`<div>` methods for left-justifying markdown tables don't work reliably in Jupyter.


---

## Origin

This page consolidates LaTeX patterns from:
- `nexus/LaTeX methods.ipynb` (main branch) — sizing, color, matrices, alignment experiments
- `ant/LaTeX patterns.ipynb` — symbols, operators, equation layouts, cases, tables
- `nexus/documentation/markdown.md` (gh-pages) — historical anecdote about TeX/LaTeX

The source notebooks remain in their respective repos as working examples.
