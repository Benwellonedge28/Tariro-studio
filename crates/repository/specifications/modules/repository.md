# Stable repository identity

**ZIP-REPOSITORY-REPOSITORY-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/repository.rs`

## Required implementation behavior

Bind local registered ID or provider immutable repo ID with owner/repository location and supported revision algorithm. Rename updates display location without changing identity.

## Acceptance

**ZIP-REPOSITORY-REPOSITORY-T01.** Remote name reuse with new provider ID fails authorization.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
