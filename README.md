# Essai

Reproducible evaluation of models on scientific tasks. Part of
[Fonderie](https://github.com/fonderie-dev).

An *essai* is the assay: the test that establishes what a casting actually
contains.

> **Status: scaffold (○○○).** The package installs and its smoke test passes.
> None of the scope below is implemented yet.

## Intended scope

- Task definitions as versioned files: inputs, references, metric, and the
  exact prompt or scoring procedure.
- Runs against a model pinned to a commit hash, with fixed seeds and decoding
  settings, producing a run record and per-item outputs.
- Checks for overlap between evaluation items and a training manifest from
  [Affinage](https://github.com/fonderie-dev/fonderie-affinage).
- Comparison across models, revisions and
  [Burin](https://github.com/fonderie-dev/fonderie-burin) edits, reported with
  uncertainty intervals rather than single numbers.

Not in scope: a public leaderboard; evaluation through hosted model APIs
unless a task definition requires it explicitly.

## First milestones

1. Task-file format and validator.
2. Deterministic evaluation of a tiny local model on a synthetic task, inside
   the test suite.
3. Result comparison with bootstrap intervals.

## Development

```sh
python -m pip install -e ".[dev]"
ruff check . && ruff format --check .
python -m pytest
```

```
src/fonderie_essai/   package
tests/                pytest suite: no downloads, no GPU
```

CI runs the shared
[Fonderie workflow](https://github.com/fonderie-dev/.github/blob/main/.github/workflows/python-check.yaml)
on Python 3.11–3.14.

## Licence

Apache-2.0; see [LICENSE](LICENSE) and [NOTICE](NOTICE). Models and task data
evaluated with this package keep their own licences. © 2026 R. Heller.
