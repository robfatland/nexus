[nexus published](https://robfatland.github.io/nexus), [nexus index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


# Loose strands


This page is an **actionable TODO list** for nexus content development. Items here represent
gaps to fill, content to relocate, or investigations to pursue.


## Active TODOs


### Content to create or expand

- [ ] Find out and resolve why Chris Simmons says Micro Mamba not Anaconda and even not Miniconda
- [ ] Get links to MSE544 cloud infrastructure topic labs (VMs, databases, serverless, containers)
- [ ] WSL-2 dedicated setup page (currently scattered across lexicon and bash)
- [ ] Docker/container hands-on usage procedures (beyond eigenconcepts)
- [ ] `flameshot` screencap workflow documentation (unbinding Print Screen key from OneNote)
- [ ] Python package publishing workflow
- [ ] Cloud security basics page
- [ ] SSH key management and `authorized_keys` explanation
- [ ] CPU monitoring on many-core machines (`top`, CloudWatch)

### Content to relocate or merge

- [x] Consolidate LaTeX cheat sheet material → [documentation/latex.md](https://github.com/robfatland/nexus/blob/gh-pages/documentation/latex.md)
- [ ] Ocean science content: Move to dedicated oceanography repo (epipelargosy, VIIRS, ARGO, ROMS, etc.)

### Links to investigate and potentially incorporate

- [ ] [Cloud Maven Fossil Cloud Resource Site](http://cloudmaven.github.io/documentation) — historical reference
- [ ] [Oorjit repo on preemptible VMs](https://github.com/oorjitchowdhary/ml-training-preemptible-vms)
- [ ] [Rob's notes in Oorjit's repo](https://github.com/oorjitchowdhary/ml-training-preemptible-vms/blob/main/assets/notesbyrob.md)


## Burning questions (aspirational)

- How do I manage Python environments? → [bash/env.md](https://github.com/robfatland/nexus/blob/gh-pages/bash/env.md)
- How do I publish my code as a Python package? → [python/packages.md](https://github.com/robfatland/nexus/blob/gh-pages/python/packages.md) (stub)
- How do I build an API-based resource? → [data/api.md](https://github.com/robfatland/nexus/blob/gh-pages/data/api.md)
- How do I safely manage sensitive data? → cloud security (not yet written)
- How do I manage code development with GitHub? → [git/index.md](https://github.com/robfatland/nexus/blob/gh-pages/git/index.md)
- How do I turn off colorization in bash and vi? → [bash/terminal.md](https://github.com/robfatland/nexus/blob/gh-pages/bash/terminal.md)
- How do I set up a cloud VM with Jupyter via ssh tunnel? → [bash/tunneling.md](https://github.com/robfatland/nexus/blob/gh-pages/bash/tunneling.md)


## CloudBank reference links

These are external resources related to CloudBank and cloud education:

- [VM, Database, Serverless tutorials (Azure) source](https://github.com/cloudbank-project/az-serverless-tutorial/tree/main)
    - [Published](https://cloudbank-project.github.io/az-serverless-tutorial/)
- [Containerization source](https://github.com/naclomi/containers-tutorial)
    - [Published](https://naclomi.github.io/containers-tutorial/)
- [CloudBank zero2Data](https://github.com/cloudbank-project/Zero2Data)
- [CloudBank spend tracking](https://github.com/cloudbank-project/burnop)
- [Cloud 101/102 (2017)](https://github.com/robfatland/cloud101102)


## Related repos (R's GitHub)

Repos that may contain material worth scraping into nexus:

- `runawaytrain` — AWS Organizations, API use
- `greenandblack` — bash/vi customization (predecessor to nexus bash/terminal content)
- `cbburn` — pandas DataFrame manipulation
- `digitaltwin`, `serverless`, `costnotify`, `nlp`, `carpentries` — various stubs

### CloudMaven GitHub repos to evaluate

(From former `cloud_adjudicator.md`)

- `documentation` — the main CM docs site
- `cloudmaven` — org landing page
- `tutorial_contents`
- `dssg2017` — relates to the 101 series
- `s3-bucket-listing` — prima facie usable
- `geohack_copy`
- `cloud101_aws`, `cloud101_spot_ELB`, `cloud101_intro`, `cloud101_cfncluster`, `cloud101_cloudproviders`, `cloud101_webframework`, `cloud101demo_beanstalk`, `cloud101_costing`, `cloud101_template`


## Useful references

- [LaTeX](https://github.com/robfatland/nexus/blob/gh-pages/documentation/markdown.md#latex)
- [Hugo](https://gohugo.io/), [Jekyll](https://jekyllrb.com/)
- [Python packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Sphinx documentation generator](https://kanishkvarshney.medium.com/python-documentation-generating-html-using-sphinx-a0d909f5e963)
