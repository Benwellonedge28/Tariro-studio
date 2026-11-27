# Resource admission and accounting

**Contract version** 1.1 candidate. Master design §§15 and 71.

## Contract

Use the [shared admission contract](../../RESOURCE_CONTRACT.md) for all resource-consuming operations. Each coordinate binds a scope, unit and relevant physical or service ID. Use nonnegative integers for charges and reservations. Express spend in currency minor units. Normalize discovery before budgeting. Represent operation deadlines with a monotonic instant and account for them independently of pooled capacity.

## Execution and integration

The personal profile follows [resource management](../../RESOURCE_MANAGEMENT.md). Profiles guide initial settings while validated policy and measured availability determine admission. Permit a smaller estimate only when it meets the approved quality floor. Return a lease only after capacity is committed. Unknown mandatory capacity blocks execution. After expiry or uncertain dispatch, fence the worker and keep the hold until reconciliation proves teardown and settles metered use.

## Verification

Apply the [acceptance fixtures](../../contracts/acceptance/resources/admission-fixtures.json) to known-zero and unknown capacity, competing requests, deadline independence, revocation, and restart. Test actual memory pressure with the configured model cap and verify that fallback protects pinned models. Record inputs, resolved policy, measurements, outcome and the evidence reference. Map release evidence to [requirements](../../REQUIREMENTS.md).

## Implementing components

- [Resources](../../crates/resources/DESIGN.md)
- [Configuration](../../crates/configuration/DESIGN.md)
- [Economics](../../crates/economics/DESIGN.md)
