# Deterministic scoped replay

**ZIP-DEBUGGING-REPLAY-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/replay.rs`

## Required implementation behavior

Use recorded inputs, environment and version; replay observable steps within budget and separately authorize external effects.

## Acceptance

**ZIP-DEBUGGING-REPLAY-T01.** Unknown effect cannot be replayed through generic adapter.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
