# Qualified academic evidence adapter

**ZIP-RESEARCH-PROVIDERS-ACADEMIC-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/providers/academic.rs`

## Required implementation behavior

Track paper version and metadata, distinguish abstract and inspected full text, respect approved access and excerpt bounds.

## Acceptance

**ZIP-RESEARCH-PROVIDERS-ACADEMIC-T01.** Abstract-only reading cannot verify unobserved method details.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
