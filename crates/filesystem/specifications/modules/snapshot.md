# Immutable read manifest

**ZIP-FILESYSTEM-SNAPSHOT-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/snapshot.rs`

## Required implementation behavior

Pin root revision/identity and bounded path-to-digest mapping. Verify content while scanning and reject changed identity. Snapshot does not grant read scope.

## Acceptance

**ZIP-FILESYSTEM-SNAPSHOT-T01.** Concurrent mutation yields changed-state status instead of mixed verified snapshot.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
