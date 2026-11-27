# Bounded cost estimate

**ZIP-ECONOMICS-ESTIMATION-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/estimation.rs`

## Required implementation behavior

Compute conservative finite maximum from checked quantities and approved rates. Label estimate and preserve assumptions and expiration.

## Acceptance

**ZIP-ECONOMICS-ESTIMATION-T01.** Overflow or unknown rate denies paid admission.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
