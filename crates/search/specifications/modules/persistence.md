# Index recovery and durable manifests

**ZIP-SEARCH-PERSISTENCE-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/persistence.rs`

## Required implementation behavior

Persist immutable index manifest and verified artifact refs, recover last complete generation, rebuild explicitly on corruption.

## Acceptance

**ZIP-SEARCH-PERSISTENCE-T01.** Interrupted publish leaves prior complete index active.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
