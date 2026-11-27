# Context access and egress isolation

**ZIP-CONTEXT-ISOLATION-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/isolation.rs`

## Required implementation behavior

Keep project and assignment namespaces isolated. Apply secret filtering and separate remote disclosure permission at provider boundary.

## Acceptance

**ZIP-CONTEXT-ISOLATION-T01.** Local context cannot be reused in an unapproved remote request.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
