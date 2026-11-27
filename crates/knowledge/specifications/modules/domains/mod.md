# Ontology extension boundary

**ZIP-KNOWLEDGE-DOMAINS-MOD-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/domains/mod.rs`

## Required implementation behavior

Select qualified domain/version and validate common IDs, scope and evidence. Unsupported domain remains opaque.

## Acceptance

**ZIP-KNOWLEDGE-DOMAINS-MOD-T01.** Unknown domain does not map to privileged organization facts.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
