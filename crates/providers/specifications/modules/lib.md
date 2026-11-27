# Provider adapter facade

**ZIP-PROVIDERS-LIB-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/lib.rs`

## Required implementation behavior

Expose qualified manifests, registry and request ports. Adapters activate explicitly. Linking makes no provider calls.

## Acceptance

**ZIP-PROVIDERS-LIB-T01.** Offline metadata consumer has no outbound effects.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
