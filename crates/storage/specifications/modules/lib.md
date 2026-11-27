# Storage crate wiring

**ZIP-STORAGE-LIB-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/lib.rs`

## Required implementation behavior

Expose storage backend, transactions, schema, object and backup ports. Own no global database. Backends activate only by qualified feature and selected profile.

## Acceptance

**ZIP-STORAGE-LIB-T01.** Compile the facade without a remote service or implicit file creation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
