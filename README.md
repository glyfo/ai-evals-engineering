# AI evals engineering

Runnable examples for the eight-edition "Engineering of AI Evals" series by GLYFO LABS.

This repository contains the runnable companion material for each edition. A new top-level `part-XX-*` directory appears when its edition is published.

## Follow the series

The series has eight editions. The repository currently includes the following companion example.

| Edition | Companion example | Status |
| --- | --- | --- |
| 2 | [Before Your First AI Trace](part-02-bootstrapping/) | Available |
| 1, 3-8 | Companion examples | Added when published |

To keep your local copy current, run `git pull` on the `main` branch before starting a new edition.

## Run edition 2

Use Python 3.10 or later.

```bash
git clone https://github.com/glyfo/ai-evals-engineering.git
cd ai-evals-engineering
python -m pip install -r requirements.txt
python part-02-bootstrapping/src/refunds.py
python -m unittest discover -s part-02-bootstrapping/tests -v
```

The first command prints the S04 trace. It ends with a passing state grade and a failing claim grade. The test suite passes when it detects that intended failure.

## Repository layout

```text
part-02-bootstrapping/
  process/       Process variants
  spec/          Routines and outcome oracles
  scenarios/     Versioned test cases
  src/           Simulated tools and grader
  tests/         Runnable checks
  traces/        Readable trace examples
```

Each published companion example has its own top-level `part-XX-*` directory.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request. Do not add customer data, credentials, or production traces.
