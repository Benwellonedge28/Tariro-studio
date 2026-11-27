# Provider-bound secret references

**ZIP-PROVIDERS-CREDENTIALS-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/credentials.rs`

## Required implementation behavior

Resolve only opaque reference scoped to approved adapter, audience and operation. Never pass raw values to logs or configuration snapshots.

## Acceptance

**ZIP-PROVIDERS-CREDENTIALS-T01.** Wrong destination cannot receive credential.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
