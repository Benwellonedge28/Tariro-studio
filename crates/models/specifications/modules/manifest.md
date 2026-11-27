# Versioned model manifest

**ZIP-MODELS-MANIFEST-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/manifest.rs`

## Required implementation behavior

Pin shard digest/length, formats, tokenizer, expected capabilities, license metadata and provenance. Validate schema before file access.

## Acceptance

**ZIP-MODELS-MANIFEST-T01.** Duplicate shard path and unknown schema reject before allocation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
