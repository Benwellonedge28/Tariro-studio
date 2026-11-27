# Typed API and compatibility

**ZIP-ENGINEERING-ARCHITECTURE-INTERFACES-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/architecture/interfaces.rs`

## Required implementation behavior

Pin interface version, complete Rust signatures, error semantics and permission/ownership contracts. Check against negotiated consumer/provider fixture.

## Acceptance

**ZIP-ENGINEERING-ARCHITECTURE-INTERFACES-T01.** Unsupported major or lifetime mismatch blocks contract qualification.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
