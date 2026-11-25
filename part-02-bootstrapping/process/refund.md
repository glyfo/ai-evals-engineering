# Refund process map

## Inputs

A process analyst reviews the operating procedure, closed tickets, and event logs with senior support operators. The examples below use synthetic data.

## Variants

### REF-V1: Clean refund

The customer is verified. The order exists. The order is eligible within the 30-day return window. The system creates a return or reports the tool failure.

### REF-V2: Missing order

The customer is verified, but the order lookup finds no matching order. The agent must not create a return. The agent asks for the correct order reference or routes the case for review.

### REF-V3: Policy exception

The order exists, but the request falls outside the standard policy or needs supervisor approval. The agent records the case for supervisor review and does not promise a return.

## Terminal states

Each variant ends in one recorded system state: a return exists, no return exists because the order is missing, or no return exists because a supervisor must decide.
