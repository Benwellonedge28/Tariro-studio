# Untrusted change hints

**ZIP-FILESYSTEM-WATCHER-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/watcher.rs`

## Boundary and inputs

Treat a watcher event as an advisory hint scoped to an enrolled root and generation. Coalesce bounded events deterministically and record overflow, loss and watcher restart. No event can certify a file change or authorize reading it.

## Behavior and failure handling

Invalidate incremental state on a detected gap, sequence uncertainty or unsupported backend. Schedule a bounded authorized rescan under the owning snapshot workflow. A stable current duplicate hint may be collapsed. Preserve safe reason codes without leaking unrelated host paths.

## Acceptance

**ZIP-FILESYSTEM-WATCHER-T01.** Drop one event and force overflow. Verify explicit rescan-required state and no complete snapshot from remaining events. Supply an unauthorized event and confirm no file access is triggered.
