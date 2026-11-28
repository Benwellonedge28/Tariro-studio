# Durable emergency stop

**ZIP-GOVERNANCE-OVERSIGHT-EMERGENCY-STOP-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/oversight/emergency_stop.rs`

## Boundary and inputs

Accept a separately authorized stop command naming scope, exact request identity and expected control revision. Atomically set stopped state, advance the fencing epoch and record redacted intent and outbox. The committed stop blocks new effect claims before notifying any supervisor. Use checked epochs and retain the checkpoint after restart.

## Behavior and failure handling

Notify the owning execution boundary to close intake and reconcile running work. Existing receipts remain visible and leases remain held until verified cleanup. An exact replay returns the same stop receipt. Resume requires separate authenticated review, current revision and current policy. Clearing the stop flag never revives an earlier fenced grant or releases a resource automatically.

## Acceptance

**ZIP-GOVERNANCE-OVERSIGHT-EMERGENCY-STOP-T01.** Crash after stop commits and before notification. Reload, reject every new effect under prior scope, and preserve the previously committed receipt. Resume under a valid later command and verify the old grant is still fenced.
