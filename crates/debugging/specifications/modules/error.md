# Debug failure vocabulary

**ZIP-DEBUGGING-ERROR-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/error.rs`

## Required implementation behavior

Distinguish no reproduction, invalid target, adapter unavailable, denied attachment, budget, timeout and incomplete evidence.

## Acceptance

**ZIP-DEBUGGING-ERROR-T01.** Unknown session result produces no verified repair.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
