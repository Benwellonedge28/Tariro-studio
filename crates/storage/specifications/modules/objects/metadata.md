# Object reference accounting

**ZIP-STORAGE-OBJECTS-METADATA-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/objects/metadata.rs`

## Required implementation behavior

Store immutable digest/length and reference count in the same transaction as domain links. Use checked delta and reject underflow; publish readiness only after qualified byte promotion.

## Acceptance

**ZIP-STORAGE-OBJECTS-METADATA-T01.** Reference rollback unwinds both link and refcount; negative delta cannot wrap to a huge count.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
