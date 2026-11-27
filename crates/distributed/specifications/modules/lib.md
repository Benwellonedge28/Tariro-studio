# Distributed execution facade

**ZIP-DISTRIBUTED-LIB-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/lib.rs`

## Required implementation behavior

Expose node, task lease and coordinator ports. Remote execution remains opt-in and no discovery happens on import.

## Acceptance

**ZIP-DISTRIBUTED-LIB-T01.** Local consumers run without network initialization.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
