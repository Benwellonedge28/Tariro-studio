# Testing service boundary

**ZIP-TESTING-LIB-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/lib.rs`

## Required implementation behavior

Expose test plan, execution and observed results through injected runner. Linking invokes no fixture or app.

## Acceptance

**ZIP-TESTING-LIB-T01.** A test plan can be instantiated without sandbox startup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
