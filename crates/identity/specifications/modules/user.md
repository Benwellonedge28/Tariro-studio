# Human account representation

**ZIP-IDENTITY-USER-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/user.rs`

## Required implementation behavior

Record identity and active memberships; separate profile edits from role changes. Require revision compare-and-swap for identity updates.

## Acceptance

**ZIP-IDENTITY-USER-T01.** Changing display name cannot grant repository permission.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
