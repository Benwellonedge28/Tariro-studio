# Runtime cancellation protocol

**ZIP-RUNTIME-CONTROL-CANCELLATION-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/control/cancellation.rs`

## Required implementation behavior

Observe sticky token, stop intake, request cooperative stop, then enforce configured grace and verify descendants. Committed or ambiguous external effects are recorded separately.

## Acceptance

**ZIP-RUNTIME-CONTROL-CANCELLATION-T01.** Cancel at pre-dispatch, post-commit and during teardown, with no lost obligation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
