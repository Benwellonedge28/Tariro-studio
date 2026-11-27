# Durable scope fencing

**ZIP-GOVERNANCE-AUTHORIZATION-REVOCATION-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/authorization/revocation.rs`

## Required implementation behavior

Advance checked revocation epoch and record actor/reason atomically with outbox. Block future claims under old epoch; reconcile already-started effects.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-REVOCATION-T01.** After restart, prior grants remain fenced and existing receipts visible.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
