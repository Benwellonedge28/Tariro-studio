# Hybrid evidence boundary

**ZIP-REASONING-HYBRID-MOD-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/hybrid/mod.rs`

## Required implementation behavior

Combine deterministic and model-assisted outputs only under same pinned problem, separating confirmed from speculative results.

## Acceptance

**ZIP-REASONING-HYBRID-MOD-T01.** Generated suggestion cannot overwrite observed solver counterexample.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
