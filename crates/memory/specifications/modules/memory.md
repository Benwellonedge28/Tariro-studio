# Memory service composition

**ZIP-MEMORY-MEMORY-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/memory.rs`

## Required implementation behavior

Validate current scope, select eligible layer and finite retention, stage observed records through store. No implicit durable persistence.

## Acceptance

**ZIP-MEMORY-MEMORY-T01.** Default assignment memory is lost on restart unless persistence was approved.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
