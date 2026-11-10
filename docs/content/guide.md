---
title: "Guide"
description: "How to use Essai: installation, task files, evaluation runs, overlap checks and comparison with uncertainty. Outline; coming soon."
summary: "From a task file and a pinned model to a result with its record and its uncertainty."
lede: "How a task file and a pinned model become a result that someone else can repeat, with its record and its uncertainty."
outlineTitle: "Planned chapters"
outline:
  - id: installation
    title: "Installation"
    text: "Installing a released version, and the optional extras that bring in model libraries only when they are needed."
  - id: first-evaluation
    title: "A first evaluation"
    text: "Deterministic evaluation of a tiny local model on a synthetic task, on CPU."
  - id: tasks
    title: "Writing a task"
    text: "Task definitions as versioned files: inputs, references, metric, and the exact prompt or scoring procedure."
  - id: runs
    title: "Running an evaluation"
    text: "Runs against a model pinned to a commit hash, with fixed seeds and decoding settings."
  - id: outputs
    title: "Run record and per-item outputs"
    text: "What Essai writes for every run, following the [Fonderie run record](https://fonderie-dev.github.io/website/methode/#the-run-record), and how to read the per-item outputs."
  - id: overlap
    title: "Train–test overlap"
    text: "Checking evaluation items against a training manifest from [Affinage](https://fonderie-dev.github.io/fonderie-affinage/) before a result is reported."
  - id: comparison
    title: "Comparing models"
    text: "Comparison across models, revisions and [Burin](https://fonderie-dev.github.io/fonderie-burin/) edits on the same tasks."
  - id: uncertainty
    title: "Reporting with uncertainty"
    text: "Bootstrap intervals instead of single numbers, and how to read them."
---

## Available now: install from source

There is no release yet. The scaffold installs from a clone of the repository:

```sh
git clone https://github.com/fonderie-dev/fonderie-essai.git
cd fonderie-essai
python -m pip install -e ".[dev]"
python -m pytest
```

The tests need neither a GPU nor downloads.
