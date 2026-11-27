# Immutable isolation policy

**ZIP-SANDBOX-PROFILE-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/profile.rs`

## Required implementation behavior

Bind roots, network, environment, process and resource controls to profile and revision. Intersect task additions with mandatory policy. Unknown required control rejects.

## Acceptance

**ZIP-SANDBOX-PROFILE-T01.** A user profile cannot enable mandatory-denied egress.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
