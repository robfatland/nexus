---
inclusion: always
---

# Project Context

This is a GitHub repository primarily consisting of Markdown files (and Jupyter notebooks). Its purpose is to document common tasks in a personal "productivity environment" that supports research computing.

**Central fact:** This repo uses GitHub Pages. Virtually all of the content lives in the `gh-pages` branch, not `main`.

## Environment

- **Localhost:** A PC running WSL (Windows Subsystem for Linux)
- **Cloud:** Various cloud VMs used for compute-heavy work
- The workflow regularly bridges these two layers (e.g. SSH tunnels, remote Jupyter sessions)

## Work Style

- The work here is episodic and multi-task-oriented.
- Projects are frequently set aside for months at a time, then revisited.
- Upon returning to a project, significant re-learning is typically required.
- Documentation should therefore be written for a "future self" who has forgotten the details: explicit, step-by-step, and self-contained.

## AI-Assisted Workflow

With the advent of useful AI (specifically the Kiro IDE), the game has changed. The AI assistant's first task when engaging with this repo is to:

1. Review the existing documentation.
2. Refactor it for clarity, correctness, and consistency.
3. Verify that content is accurate and up to date.
4. Suggest gaps that might be filled — missing procedures, undocumented workflows, stale instructions.

## Findability

One of the biggest responsibilities of this repo is to **make material findable**. Documentation that exists but can't be located when needed is nearly as bad as documentation that doesn't exist. Structure, indexing, cross-linking, and clear naming all serve this goal.

## Key Recurring Task

Building an SSH tunnel to operate a Jupyter Lab environment on a cloud VM is an important and recurring workflow. Procedures for this (and similar remote-access patterns) should be documented clearly enough to follow cold.

## Writing Guidelines

- Favor clarity and completeness over brevity.
- Include exact commands, expected output, and troubleshooting notes where possible.
- Assume the reader has general technical competence but no memory of prior context.
- Use Markdown structure (headings, code blocks, numbered steps) to make procedures scannable.

## Pending Tasks

- ~~**LaTeX consolidation:** Merge LaTeX cheat sheet material~~ → Done: `documentation/latex.md` on gh-pages.
