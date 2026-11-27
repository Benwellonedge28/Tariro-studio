# Durable or ephemeral storage

**ZIP-MEMORY-STORE-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/store.rs`

## Required implementation behavior

Choose by policy, apply quota, compare generation and atomically write object/ref/index/outbox. Confirm durable receipt only through qualified backend.

## Acceptance

**ZIP-MEMORY-STORE-T01.** Failed object staging cannot leave active metadata.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
