# Research observation lineage

**ZIP-RESEARCH-PROVENANCE-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/provenance.rs`

## Required implementation behavior

Record source identity, retrieval transform, date, scope, digest and qualification. Revalidation follows source version.

## Acceptance

**ZIP-RESEARCH-PROVENANCE-T01.** Generated summary cannot become provenance of external source.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
