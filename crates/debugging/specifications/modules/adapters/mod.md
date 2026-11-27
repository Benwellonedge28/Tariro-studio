# Debugger capability negotiation

**ZIP-DEBUGGING-ADAPTERS-MOD-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/adapters/mod.rs`

## Required implementation behavior

Select qualified DAP/GDB/LLDB adapter by target, feature and authority. No implicit process attachment.

## Acceptance

**ZIP-DEBUGGING-ADAPTERS-MOD-T01.** Unsupported adapter reports unavailable without creating process.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
