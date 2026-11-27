# Identity service boundary

**ZIP-IDENTITY-LIB-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/lib.rs`

## Required implementation behavior

Expose typed principal, membership, authentication and session ports; inject storage and authenticator. Linking never opens a credential store.

## Acceptance

**ZIP-IDENTITY-LIB-T01.** Compile a downstream identity DTO consumer with no services initialized.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
