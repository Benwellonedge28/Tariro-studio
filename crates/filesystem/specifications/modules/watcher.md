# Untrusted change hints

**ZIP-FILESYSTEM-WATCHER-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/watcher.rs`

## Required implementation behavior

Deliver bounded coalesced hints bound to root generation. Overflow invalidates incremental state and triggers bounded rescan. Watch event does not confer authorization.

## Acceptance

**ZIP-FILESYSTEM-WATCHER-T01.** Dropped event produces rescan requirement, not omitted change.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
