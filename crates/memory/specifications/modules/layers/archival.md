# Qualified archive storage

**ZIP-MEMORY-LAYERS-ARCHIVAL-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/layers/archival.rs`

## Required implementation behavior

Archive only eligible records under retention and integrity/secrecy rules. Discovery/restoration needs separate scope and verified manifest.

## Acceptance

**ZIP-MEMORY-LAYERS-ARCHIVAL-T01.** Archival manifest missing an object blocks restore.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
