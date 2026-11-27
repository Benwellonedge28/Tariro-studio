# Scoped model discovery

**ZIP-MODELS-DISCOVERY-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/discovery.rs`

## Required implementation behavior

Read only approved roots/catalogs under finite budget and record partial candidate scan. Discovery does not load, download or trust model metadata.

## Acceptance

**ZIP-MODELS-DISCOVERY-T01.** Offline catalog inspection performs no external fetch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
