# Required evidence graph

**ZIP-VERIFICATION-REQUIREMENTS-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/requirements.rs`

## Required implementation behavior

Resolve stable requirement IDs to expected observations and mandatory/optional gates. Keep scope and exact candidate references. Missing required link blocks.

## Acceptance

**ZIP-VERIFICATION-REQUIREMENTS-T01.** Unknown requirement cannot be counted as satisfied.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
