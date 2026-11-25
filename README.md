# AI evals engineering

Runnable examples for the "Engineering of AI Evals" series by GLYFO LABS.

The repository starts with [Part 2: Before Your First AI Trace](part-02-bootstrapping/). It turns a manual refund process into a process map, an agent routine, test scenarios, a simulated tool environment, and graded traces.

## Run Part 2

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

Each future series part will add one top-level `part-XX-...` directory.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request. Do not add customer data, credentials, or production traces.
