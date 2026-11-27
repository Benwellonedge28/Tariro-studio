# Explicit web retrieval adapter

**ZIP-RESEARCH-PROVIDERS-WEB-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/providers/web.rs`

## Required implementation behavior

Validate reviewed scheme, endpoint and redirects before egress, bound bytes and excerpts and mark retrieval failures honestly.

## Acceptance

**ZIP-RESEARCH-PROVIDERS-WEB-T01.** Private query restriction denies external transmission.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
