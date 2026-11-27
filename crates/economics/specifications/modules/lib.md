# Resource cost boundary

**ZIP-ECONOMICS-LIB-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/lib.rs`

## Required implementation behavior

Expose estimates, budget admission and observed accounting. No money transfer or settlement API.

## Acceptance

**ZIP-ECONOMICS-LIB-T01.** Facade imports and local estimates cannot move funds.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
