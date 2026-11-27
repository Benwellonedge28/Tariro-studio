# Current grant gate

**ZIP-ASSIGNMENTS-AUTHORIZATION-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/authorization.rs`

## Required implementation behavior

Check authenticated actor, grant expiry/epoch, scope and exact plan/operation constraints immediately before effect claim. Persist grant reference, never token material.

## Acceptance

**ZIP-ASSIGNMENTS-AUTHORIZATION-T01.** Revoke between verification and push and confirm publication is denied.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
