# Conflict-aware source comparison

**ZIP-RESEARCH-COMPARISON-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/comparison.rs`

## Required implementation behavior

Normalize claims, scopes and versions, retain corroboration and disagreement, avoid choosing solely by count.

## Acceptance

**ZIP-RESEARCH-COMPARISON-T01.** Conflicting sources remain explicit until resolved.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
