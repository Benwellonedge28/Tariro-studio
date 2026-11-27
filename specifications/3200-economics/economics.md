# Budgets and usage

**Contract version** 1.0. Master design §71.

## Contract

Store quote with provider/model, pricing revision, units, currency, estimated minor units and expiry. Store reservations before expenses and settle against observed usage. Unsettled action retains reservation.

## Execution and integration

Compute with checked fixed-point arithmetic and per-assignment/workspace limits. Price drift or indeterminate receipts block repeat spending until reconciliation. No payment execution.

## Verification

Concurrent requests at a cap, retry with a lost receipt and test price changes between quote and request.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [economics crate design](../../crates/economics/DESIGN.md)
- [resources crate design](../../crates/resources/DESIGN.md)
