# Reproducible reasoning stage

**ZIP-REASONING-HYBRID-DETERMINISTIC-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/hybrid/deterministic.rs`

## Required implementation behavior

Apply pinned rules and bounded evaluation to exact inputs, preserve observed trace and failure reason.

## Acceptance

**ZIP-REASONING-HYBRID-DETERMINISTIC-T01.** Reordering equivalent input yields identical result.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
