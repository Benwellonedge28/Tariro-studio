# Resource admission and accounting

**Contract version** 1.0. Master design §71.

## Contract

All externally supplied quantities are nonnegative bounded integers: bytes, millisecond duration, count, tokens and currency minor units paired with ISO currency. A request reserves the entire vector across host, workspace and assignment pools. Reservations contain an attempt ID, expiration and an observed-usage record.

## Execution and integration

The personal profile follows RESOURCE_MANAGEMENT.md. Permit a smaller request only when policy names a quality floor and the plan records the downgrade. Unknown capacities reject hard-guarantee requests. A reservation may be freed after confirmed teardown or fenced recovery.

## Verification

Run concurrent reservations at exact remaining capacity. Force memory pressure and verify no second generation model and no eviction of pinned evidence.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [resources crate design](../../crates/resources/DESIGN.md)
- [configuration crate design](../../crates/configuration/DESIGN.md)
- [economics crate design](../../crates/economics/DESIGN.md)
