# Confirmed resource reclamation

**ZIP-SANDBOX-CLEANUP-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/cleanup.rs`

## Boundary and inputs

Consume a scoped recovery or supervisor command referencing the exact containment locator and current cleanup ownership. Close new work into the group, signal cooperative cancellation and follow the resolved stop-grace deadline. Escalate to trusted contained-group termination when the window ends.

## Behavior and failure handling

Require independent group-exit and usage evidence before reporting cleanup complete. Unknown descendants, refusal or unreachable observer leave a durable obligation. Runtime or the owning supervisor applies verified cleanup to Resources. Dropping a local handle, expiring a lease or reissuing termination does not release holds. Exact replay returns the known settlement or continues scoped inspection.

## Acceptance

**ZIP-SANDBOX-CLEANUP-T01.** Use an adapter that can report parent exit but cannot confirm the remaining fixture child. Verify cleanup stays incomplete and capacity is held. Supply trusted exit and usage evidence and verify one settlement.
