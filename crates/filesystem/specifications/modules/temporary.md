# Private staging lifecycle

**ZIP-FILESYSTEM-TEMPORARY-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/temporary.rs`

## Required implementation behavior

Allocate same-volume private temporary name under scoped directory and track owner. Reap only promoted or abandoned owned items after reconciliation.

## Acceptance

**ZIP-FILESYSTEM-TEMPORARY-T01.** Cleanup skips unrelated preexisting files and preserves unknown promotion evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
