# Bounded memory compression

**ZIP-MEMORY-COMPRESSION-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/compression.rs`

## Required implementation behavior

Select eligible payload, preserve metadata, provenance and qualified reversibility where required. Verify result size/digest before replacing view.

## Acceptance

**ZIP-MEMORY-COMPRESSION-T01.** Compression failure preserves prior verified record.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
