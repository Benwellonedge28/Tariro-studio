# Maintenance job states

**ZIP-MAINTENANCE-LIFECYCLE-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/lifecycle.rs`

## Required implementation behavior

Persist proposed, approved, staged, executing, verified, paused and unresolved with revision checks. Stop effect admission on revocation.

## Acceptance

**ZIP-MAINTENANCE-LIFECYCLE-T01.** Revoked maintenance job cannot start next step.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
