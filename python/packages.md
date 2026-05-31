[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md),
[python index](https://github.com/robfatland/nexus/blob/gh-pages/python/index.md)


# Python packages

> **Stub.** This page is a placeholder for notes on Python package management.

## Package managers to document

- `apt` — Linux system-level package manager (Debian/Ubuntu)
- `pip` — Python's native package installer (works with `requirements.txt`)
- `conda` — Anaconda/Miniconda package and environment manager (works with `environment.yml`)
- `mamba` / `micromamba` — faster drop-in replacement for `conda`
- `pixi` — newer Rust-based package manager compatible with conda-forge

## Related pages

- [conda environments](https://github.com/robfatland/nexus/blob/gh-pages/bash/env.md) — detailed environment management
- [bootstrapping a VM](https://github.com/robfatland/nexus/blob/gh-pages/bash/index.md#bootstrapping-a-cloud-data-science-vm) — installing miniconda from scratch

## TODO

- Compare `pip install` vs `conda install` for common data science libraries
- Document `requirements.txt` vs `environment.yml` workflows
- Note on `conda-forge` as a channel
- Publishing a Python package (link to [Python packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/))
