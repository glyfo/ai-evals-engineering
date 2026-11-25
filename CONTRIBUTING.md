# Contributing

## Report a reproducible problem

Open an issue with the repository version, Python version, the command you ran, the full error output, and the smallest input that reproduces the problem. Remove customer data, credentials, and internal URLs before you post.

## Propose a change

Keep each pull request focused. Update the relevant process, routine, scenario, trace, and test together when you change an evaluation artifact. Run the full test suite before you open the pull request:

```bash
python -m unittest discover -s part-02-bootstrapping/tests -v
```

## Write evaluation artifacts

Use stable IDs. Link each scenario to one process variant, routine, and oracle. State expected outcomes in final system state. Do not grade a response as successful when the simulated system state contradicts it.
