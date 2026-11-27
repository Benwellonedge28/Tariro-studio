# Immutable source citation

**ZIP-DOCUMENTATION-SOURCE-REFERENCES-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/source_references.rs`

## Required implementation behavior

Bind claim to canonical path, pinned commit or digest, and verified source range if declared. Report broken or unfetched references distinctly.

## Acceptance

**ZIP-DOCUMENTATION-SOURCE-REFERENCES-T01.** Moved file in new commit invalidates stale referenced evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
