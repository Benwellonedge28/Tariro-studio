# Canonical identity indexing

**ZIP-IDENTITY-REGISTRY-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/registry.rs`

## Required implementation behavior

Index typed IDs and trusted issuer/subject pairs; enforce uniqueness and snapshot consistency. Identity lookup alone grants no authorization.

## Acceptance

**ZIP-IDENTITY-REGISTRY-T01.** Duplicate issuer/subject mapping fails atomically.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
