# Scoped directory operations

**ZIP-FILESYSTEM-DIRECTORY-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/directory.rs`

## Required implementation behavior

Enumerate approved rooted entries with bounded iterator. Create or remove only under explicit scope; recursive removal requires target-specific authorization and supported semantics.

## Acceptance

**ZIP-FILESYSTEM-DIRECTORY-T01.** Listing a symlink returns its classified entry without following it.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
