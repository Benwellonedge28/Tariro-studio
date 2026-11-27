# Incremental bounded indexing

**ZIP-REPOSITORY-INDEXING-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/indexing.rs`

## Required implementation behavior

Read paths and Git blobs under snapshot, budget and access limits. Keep cursor and content IDs; skip unsupported/binary content explicitly with evidence.

## Acceptance

**ZIP-REPOSITORY-INDEXING-T01.** Changed file triggers only affected revisions; incomplete traversal does not masquerade as full index.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
