# Case and component normalization

**ZIP-FILESYSTEM-NORMALIZATION-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/normalization.rs`

## Required implementation behavior

Apply target filesystem normalization to comparison keys, preserve canonical display spelling, reject ambiguity rather than coalescing distinct files. Enforce caller-supplied length and depth.

## Acceptance

**ZIP-FILESYSTEM-NORMALIZATION-T01.** Two names that collapse on a case-folding destination conflict.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
