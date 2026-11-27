# Security facade

**ZIP-SECURITY-LIB-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/lib.rs`

## Required implementation behavior

Expose authorization, secret references, trust evidence and cryptographic ports; actual secret resolution remains inside an authorized adapter.

## Acceptance

**ZIP-SECURITY-LIB-T01.** Use a policy decision without loading a key or accessing network.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
