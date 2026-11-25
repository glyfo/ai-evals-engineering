# Part 2: Before your first AI trace

This example contains the artifacts that turn a manual refund process into an evaluable agent.

| Step | Artifact | Example |
| --- | --- | --- |
| 1 | Process map | [Refund variants](process/refund.md) |
| 2 | Routine and oracles | [Refund routine](spec/refund-routine.md) |
| 3 | Scenario | [S04](scenarios/S04.yaml) |
| 4 | Simulated environment | [Refund tools](src/refunds.py) |
| 5 | Graded trace | [S04-run-2](traces/S04-run-2.yaml) |

Run the example from the repository root:

```bash
python -m pip install -r requirements.txt
python part-02-bootstrapping/src/refunds.py
python -m unittest discover -s part-02-bootstrapping/tests -v
```

The test verifies the teaching case. The agent calls `create_return`. The tool returns `SERVICE_UNAVAILABLE`. The final state has zero returns, but the agent incorrectly says that it created one.
