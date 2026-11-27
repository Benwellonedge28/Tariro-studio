# Snapshot manifest

**ZIP-REPOSITORY-MANIFEST-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/manifest.rs`

## Required implementation behavior

Record repository ID, commit ID, tree reference, instructions digest, tool/adapter capability and validation evidence. Keep object IDs typed by algorithm and do not reuse as grants.

## Acceptance

**ZIP-REPOSITORY-MANIFEST-T01.** Manifest with different repo ID or instructions digest fails revalidation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
