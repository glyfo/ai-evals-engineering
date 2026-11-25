# AI evals engineering

Runnable companion material for the eight-edition "Engineering of AI Evals" series by GLYFO LABS.

The articles are published on Medium. This repository is the home for the material that accompanies every edition, including runnable examples when an edition needs them.

## Follow the series

The series has eight editions. Use this index to move between each Medium article and its repository material.

| Edition | Article and repository material | Status |
| --- | --- | --- |
| 1 | [Your AI Works. Can You Prove It?](https://medium.com/@falexm/your-ai-works-can-you-prove-it-part-1-of-8-the-engineering-of-ai-evals-322bbc732a8d) and [repository introduction](part-01-introduction/) | Available |
| 2 | [Before Your First AI Trace](part-02-bootstrapping/) | Available |
| 3 | Repository material | Added with edition 3 |
| 4 | Repository material | Added with edition 4 |
| 5 | Repository material | Added with edition 5 |
| 6 | Repository material | Added with edition 6 |
| 7 | Repository material | Added with edition 7 |
| 8 | Repository material | Added with edition 8 |

To keep your local copy current, run `git pull` on the `main` branch before starting a new edition.

## Run edition 1

Use Python 3.10 or later.

```bash
python part-01-introduction/src/agent_loop.py
python -m unittest discover -s part-01-introduction/tests -v
```

The output shows two examples. The chatbot answers one message without a tool. The agent loop decides to look up a policy, observes the result, then answers.

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

Each edition has a top-level `part-XX-*` directory. Directories can contain an introduction, runnable examples, or both.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request. Do not add customer data, credentials, or production traces.
