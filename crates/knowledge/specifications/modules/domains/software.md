# Software graph semantics

**ZIP-KNOWLEDGE-DOMAINS-SOFTWARE-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/domains/software.rs`

## Required implementation behavior

Model files, symbols and calls with qualified source spans and pinned analysis revision. Distinguish static from inferred relationships.

## Acceptance

**ZIP-KNOWLEDGE-DOMAINS-SOFTWARE-T01.** Dynamic calls do not appear as confirmed edges without evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
