# Scoped memory facade

**ZIP-MEMORY-LIB-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/lib.rs`

## Required implementation behavior

Expose scoped record, store, query and lifecycle ports, with default assignment-local storage. Linking performs no background synchronization.

## Acceptance

**ZIP-MEMORY-LIB-T01.** Creating client does not share memory or contact network.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
