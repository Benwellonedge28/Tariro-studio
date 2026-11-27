# Durable principal or session fencing

**ZIP-IDENTITY-REVOCATION-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/revocation.rs`

## Required implementation behavior

Advance identity/session epoch transactionally with audit event. Requests under old epoch deny after restart. Reconcile already dispatched effects separately.

## Acceptance

**ZIP-IDENTITY-REVOCATION-T01.** Concurrent request after epoch commit cannot claim a new effect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
