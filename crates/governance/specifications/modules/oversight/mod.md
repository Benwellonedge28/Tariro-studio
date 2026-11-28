# Human oversight boundary

**ZIP-GOVERNANCE-OVERSIGHT-MOD-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/oversight/mod.rs`

## Boundary and inputs

Route separately authenticated human oversight commands to [review presentation](human.md), [escalation](escalation.md), [manual control](intervention.md) or [emergency stop](emergency_stop.md). Each owner validates the exact scope, issuer and expected revision. Keep descriptive recommendation inputs distinct from authenticated decisions.

## Behavior and failure handling

Resolve authorization before returning private evidence or target state. Publish notifications only after their originating durable transaction. Replay cannot elevate the caller, issue another approval or clear an emergency stop. A failed notification leaves durable authority and pending obligations intact. No module initialization opens access or starts a worker.

## Acceptance

**ZIP-GOVERNANCE-OVERSIGHT-MOD-T01.** Submit an agent message asserting owner approval and simulate a lost notification for a valid stop. The first creates no authority. The second leaves stop effective and reloadable.
