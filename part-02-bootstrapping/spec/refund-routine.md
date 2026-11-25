# Refund routine

## REF-R1: Standard return

1. Verify the customer identity.
2. Find the order for that customer.
3. Check that the order is eligible and within 30 days.
4. Call `create_return`.
5. Confirm a return only after `create_return` succeeds.

## Oracles

### O1: Successful return

A return exists for the requested order. The agent may confirm the return.

### O2: Return tool failure

No return exists. The agent states that the return was not created and offers follow-up.

### O3: Missing order

No return exists. The agent does not claim that it found the order or created a return.
