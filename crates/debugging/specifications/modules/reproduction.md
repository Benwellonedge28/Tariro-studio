# Controlled reproduction

**ZIP-DEBUGGING-REPRODUCTION-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/reproduction.rs`

## Required implementation behavior

Pin environment, input, steps and baseline; compare observed failure while varying declared factors only. Enforce configured attempts and deadline.

## Acceptance

**ZIP-DEBUGGING-REPRODUCTION-T01.** Nonreproducible scenario remains explicitly uncertain.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
