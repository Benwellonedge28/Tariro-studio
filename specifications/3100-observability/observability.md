# Observability

**Contract version** 1.0. Master design §71.

## Contract

Use local structured spans and counters with correlation ID, monotonic duration and bounded metadata. Prevent repository names, raw path text and model prompts from becoming metric dimensions by default.

## Execution and integration

Export is opt-in and authorized independently. Bound cardinality and queues, count dropped diagnostics, and distinguish operational telemetry from audit evidence. Preserve durable effects when telemetry is unavailable.

## Verification

Generate high-cardinality diagnostic noise and verify the cap. Offline configuration emits no external telemetry.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [observability crate design](../../crates/observability/DESIGN.md)
- [audit crate design](../../crates/audit/DESIGN.md)
- [events crate design](../../crates/events/DESIGN.md)
