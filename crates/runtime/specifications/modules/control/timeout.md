# Monotonic deadline calculation

**ZIP-RUNTIME-CONTROL-TIMEOUT-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/control/timeout.rs`

## Required implementation behavior

Compute effective deadline as minimum of request, lease and policy deadlines. Illegal overflow rejects before dispatch. Distinguish timeout from explicit cancel and clean termination.

## Acceptance

**ZIP-RUNTIME-CONTROL-TIMEOUT-T01.** Wall-clock changes do not alter remaining monotonic deadline.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
