# Qualification and cleanup evidence

**ZIP-SANDBOX-VERIFICATION-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/verification.rs`

## Required implementation behavior

Record backend/version, requested controls, observed bounds, termination status and fixture provenance. An untested capability remains unavailable.

## Acceptance

**ZIP-SANDBOX-VERIFICATION-T01.** Verify network deny, link confinement and descendant cleanup before claiming production support.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
