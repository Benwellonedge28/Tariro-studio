# Verification failure classes

**ZIP-VERIFICATION-ERROR-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/error.rs`

## Required implementation behavior

Differentiate missing evidence, stale candidate, bad provenance, timeout, runner unavailable, failed check and blocked policy. Preserve authorized requirement reference.

## Acceptance

**ZIP-VERIFICATION-ERROR-T01.** Missing check does not coerce into pass or executed failure.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
