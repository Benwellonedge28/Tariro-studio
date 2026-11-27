# Versioned tool manifest

**ZIP-TOOLS-MANIFEST-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/manifest.rs`

## Required implementation behavior

Validate required fields, schema/version and allowed effect declarations before registration. Record immutable digest. Reject unknown mandatory fields.

## Acceptance

**ZIP-TOOLS-MANIFEST-T01.** A manifest with undeclared operation cannot activate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
