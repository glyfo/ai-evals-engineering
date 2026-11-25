# Part 1: Your AI Works. Can You Prove It?

Part 1 introduces the eight-edition "Engineering of AI Evals" series.

Read the article on Medium: [Your AI Works. Can You Prove It? Part 1 of 8: The Engineering of AI Evals](https://medium.com/@falexm/your-ai-works-can-you-prove-it-part-1-of-8-the-engineering-of-ai-evals-322bbc732a8d).

This directory contains the companion examples for the first edition.

## Chatbot and agent loop

A chatbot receives a message and returns one response. It does not call a tool or repeat a decision.

An agent loop receives a message, decides what information it needs, calls a tool, observes the result, then decides how to answer. The loop stops after the agent has enough information.

| Example | What it demonstrates |
| --- | --- |
| `C01` | A chatbot replies to a greeting in one turn with zero tool calls. |
| `A01` | An agent loop looks up a return policy before it answers. |

Run both examples from the repository root:

```bash
python part-01-introduction/src/agent_loop.py
python -m unittest discover -s part-01-introduction/tests -v
```

Read the [process map](process/conversation.md), [routines and oracles](spec/conversation-routine.md), [scenarios](scenarios/), and [graded traces](traces/) to inspect each example.

Part 2 adds a fuller runnable example: [Before Your First AI Trace](../part-02-bootstrapping/).
