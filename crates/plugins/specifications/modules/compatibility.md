# Version and capability negotiation

**ZIP-PLUGINS-COMPATIBILITY-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/compatibility.rs`

## Required implementation behavior

Require exact qualified host/plugin contract and expected imports, data, isolation and resource capability. Unknown major or unknown port rejects.

## Acceptance

**ZIP-PLUGINS-COMPATIBILITY-T01.** Matching vendor name cannot bypass interface mismatch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
