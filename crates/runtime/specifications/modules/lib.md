# Runtime facade

**ZIP-RUNTIME-LIB-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/lib.rs`

## Required implementation behavior

Export handle, builder and lifecycle DTOs; keep worker bookkeeping private. Creating the crate facade does not start workers or make system calls.

## Acceptance

**ZIP-RUNTIME-LIB-T01.** Link through the public facade with a fake executor and no runtime processes.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
