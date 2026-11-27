# Scoped incremental ingestion

**ZIP-SEARCH-INGESTION-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/ingestion.rs`

## Required implementation behavior

Authorize source before tokenization/embedding, validate revision, bound resources and stage deterministic changes.

## Acceptance

**ZIP-SEARCH-INGESTION-T01.** Partial ingestion never becomes complete active index.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
