# Versioned provider registry

**ZIP-PROVIDERS-REGISTRY-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/registry.rs`

## Required implementation behavior

Register approved adapters by stable ID/version, enforce quotas and retain immutable activation receipt. No implicit external registration.

## Acceptance

**ZIP-PROVIDERS-REGISTRY-T01.** Conflicting versions cannot silently replace reviewed provider.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
