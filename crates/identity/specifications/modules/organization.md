# Organization identity boundary

**ZIP-IDENTITY-ORGANIZATION-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/organization.rs`

## Required implementation behavior

Maintain organization ID and member link identities; role policy derives from validated membership records, never supplied display names.

## Acceptance

**ZIP-IDENTITY-ORGANIZATION-T01.** Identical display names in different organizations remain distinct.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
