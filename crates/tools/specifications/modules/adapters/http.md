# Scoped HTTP tool adapter

**ZIP-TOOLS-ADAPTERS-HTTP-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/adapters/http.rs`

## Required implementation behavior

Verify destination and egress class, tighten response size and timeout, and preserve redirects policy. Require effect key for supported mutations.

## Acceptance

**ZIP-TOOLS-ADAPTERS-HTTP-T01.** Cross-origin redirect cannot inherit authorization or credential.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
