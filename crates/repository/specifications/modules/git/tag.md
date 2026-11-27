# Scoped tag management

**ZIP-REPOSITORY-GIT-TAG-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/tag.rs`

## Required implementation behavior

Require tagged repo identity, exact object ID and owner-approved tag namespace. Creating or replacing a release tag is separate from branch write. Verify requested name/object after effect.

## Acceptance

**ZIP-REPOSITORY-GIT-TAG-T01.** Existing tag pointing elsewhere is conflict, no automatic overwrite.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
