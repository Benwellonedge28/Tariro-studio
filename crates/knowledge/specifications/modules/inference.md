# Bounded inferred edge generation

**ZIP-KNOWLEDGE-INFERENCE-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/inference.rs`

## Required implementation behavior

Apply qualified versioned rules to scoped snapshots with finite traversal and label derived edges with premises. Do not override observed facts.

## Acceptance

**ZIP-KNOWLEDGE-INFERENCE-T01.** Derived edge loses qualification when source premise is invalidated.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
