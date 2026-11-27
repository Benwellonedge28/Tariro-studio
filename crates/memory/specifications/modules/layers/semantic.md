# Qualified semantic store

**ZIP-MEMORY-LAYERS-SEMANTIC-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/layers/semantic.rs`

## Required implementation behavior

Store concepts and content references by exact embedding version and scope, distinguishing inferred claims. Revalidate before retrieval.

## Acceptance

**ZIP-MEMORY-LAYERS-SEMANTIC-T01.** Incompatible embedding versions remain separate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
