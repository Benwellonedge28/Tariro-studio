# Discovery snapshot assembly

**ZIP-RESOURCES-DISCOVERY-MOD-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/discovery/mod.rs`

## Required implementation behavior

Collect discovered pool records with units, source, age, enforceability and scope. Absence is Unknown. Publish atomically at a new revision and never mix metrics from incompatible host generations.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-MOD-T01.** One probe failure preserves other records and cannot create an optimistic unknown pool.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
