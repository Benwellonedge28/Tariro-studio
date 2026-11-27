# Architecture graph semantics

**ZIP-KNOWLEDGE-DOMAINS-ARCHITECTURE-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/domains/architecture.rs`

## Required implementation behavior

Represent component, dependency, ownership and design decisions with pinned sources. Validate relation direction for dependency edges.

## Acceptance

**ZIP-KNOWLEDGE-DOMAINS-ARCHITECTURE-T01.** A proposed decision does not replace active graph facts.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
