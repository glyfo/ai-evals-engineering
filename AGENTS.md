# AI evals engineering

## Purpose

This repository contains runnable examples for the "Engineering of AI Evals" series. Each top-level `part-XX-*` directory is a self-contained example.

## Before you change code

- Read the relevant `README.md`, process map, routine, scenario, trace, and tests.
- Keep all artifacts public-safe. Do not add credentials, customer data, internal URLs, or production traces.
- Preserve stable IDs. A scenario must link to its process variant, routine, and oracle.

## Evaluation artifacts

When you change an evaluation behavior, update the related artifacts in the same change:

- `process/` for the human process and terminal states.
- `spec/` for the agent routine and outcome oracles.
- `scenarios/` for versioned test inputs.
- `src/` for the simulated environment and grading logic.
- `traces/` for readable graded examples.
- `tests/` for executable checks.

Grade the final system state separately from the agent's claim. Never mark a claim as successful when the simulated state contradicts it.

## Python

- Support Python 3.10 and later.
- Use the standard library unless `requirements.txt` declares a dependency.
- Load YAML with PyYAML only.
- Keep examples deterministic and use synthetic identifiers.

## Validation

Run these commands from the repository root before you hand off a change:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s part-02-bootstrapping/tests -v
python part-02-bootstrapping/src/refunds.py
```

Report the commands you ran and any commands you could not run.

## Git workflow

- Keep one focused change per commit.
- Do not rewrite history or discard uncommitted work unless the user explicitly asks.
- Inspect `git status --short --branch` before committing or pushing.
- Do not push, open a pull request, or change repository settings without the user's approval.
