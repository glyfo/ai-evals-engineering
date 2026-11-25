# Conversation routines and oracles

## CHAT-R1: Single-turn chatbot

1. Receive the user message.
2. Return one response.
3. End the conversation turn without a tool call.

## AGENT-R1: Minimal agent loop

1. Observe the user message.
2. Decide whether the agent needs the policy lookup tool.
3. Call `lookup_policy`.
4. Observe the tool result.
5. Decide on an answer that uses the result.
6. Return the answer and end the loop.

## Oracles

### O1: Chatbot response

The final state records one answer and zero tool calls. The chatbot greeting matches the expected response.

### O2: Agent-loop response

The final state records one policy lookup and one answer. The answer states the 30-day return window from the tool result.
