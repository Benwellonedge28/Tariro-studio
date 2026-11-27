# Platform keyring integration

**ZIP-SECURITY-SECRETS-KEYRING-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/secrets/keyring.rs`

## Required implementation behavior

Probe owner-scoped secure store, resolve typed reference and track backend identity. If required store is unavailable, block effect without plaintext fallback.

## Acceptance

**ZIP-SECURITY-SECRETS-KEYRING-T01.** Missing keyring never creates a local plaintext token file.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
