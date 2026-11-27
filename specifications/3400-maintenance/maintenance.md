# Maintenance operations

**Contract version** 1.0. Master design §71.

## Contract

Maintenance jobs report integrity, disk use, migration readiness and backup verification. A maintenance plan records schedule, operations, reachability calculation, expected free space and preconditions.

## Execution and integration

Scan and stage non-destructively; require scoped authority for destructive pruning and upgrades. Never delete pinned artifacts or unexpired recovery sources. Reconcile interrupted runs from manifests.

## Verification

Trigger low disk, interrupted cleanup and process restart, then verify protected files remain and recovery recommendation is precise.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [maintenance crate design](../../crates/maintenance/DESIGN.md)
- [storage crate design](../../crates/storage/DESIGN.md)
- [audit crate design](../../crates/audit/DESIGN.md)
