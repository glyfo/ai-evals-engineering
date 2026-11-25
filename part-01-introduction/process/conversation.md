# Conversation process map

## Inputs

The examples use one synthetic user message. The agent-loop example also uses a fixed policy record.

## Variants

### CONV-V1: Single-turn chatbot

The user sends a greeting. The chatbot returns one response. It does not call a tool.

### AGENT-V1: Policy lookup agent

The user asks for the return window. The agent looks up the policy, observes the result, and answers from that result.

## Terminal states

`CONV-V1` ends after one assistant response with zero tool calls. `AGENT-V1` ends after one policy lookup and one assistant response.
