# Indexed source record

**ZIP-SEARCH-DOCUMENT-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/document.rs`

## Required implementation behavior

Record stable source ID, pinned bytes/digest, access policy and extractor version. Separate snippet from trusted source.

## Acceptance

**ZIP-SEARCH-DOCUMENT-T01.** Mismatched digest or revoked scope blocks snippet display.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
