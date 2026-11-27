# Canonical endpoint validation

**ZIP-NETWORKING-ENDPOINT-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/endpoint.rs`

## Required implementation behavior

Parse scheme, host and port using qualified parser. Reject userinfo, ambiguous hosts, invalid normalization and destinations outside the approved routed scope.

## Acceptance

**ZIP-NETWORKING-ENDPOINT-T01.** Equivalent hosts normalize consistently and prohibited target remains denied.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
