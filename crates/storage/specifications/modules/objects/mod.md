# Content-addressed layering

**ZIP-STORAGE-OBJECTS-MOD-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/objects/mod.rs`

## Required implementation behavior

Expose immutable object IDs, staging and verified open. Keep metadata activation separate from temporary bytes and never imply reference existence from a staged path.

## Acceptance

**ZIP-STORAGE-OBJECTS-MOD-T01.** Attempt reading by an unpromoted reference and verify safe unavailable status.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
