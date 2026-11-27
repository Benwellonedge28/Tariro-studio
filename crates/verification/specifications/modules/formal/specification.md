# Versioned formal input

**ZIP-VERIFICATION-FORMAL-SPECIFICATION-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/formal/specification.rs`

## Required implementation behavior

Bind model, assumptions, exact state semantics and proof goals to a qualified parser. Reject unsupported or unbounded obligations unless admitted under verified limits.

## Acceptance

**ZIP-VERIFICATION-FORMAL-SPECIFICATION-T01.** Unknown imported model schema does not silently weaken an obligation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
