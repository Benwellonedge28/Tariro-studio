# Engineering result vocabulary

**ZIP-ENGINEERING-ERROR-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/error.rs`

## Required implementation behavior

Classify invalid requirement, inconsistent architecture, stale candidate, scoped denial, patch conflict and missing evidence.

## Acceptance

**ZIP-ENGINEERING-ERROR-T01.** A cleanly staged patch cannot be reported as verified when a check failed.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
