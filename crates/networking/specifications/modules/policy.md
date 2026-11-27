# Effective egress authorization

**ZIP-NETWORKING-POLICY-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/policy.rs`

## Required implementation behavior

Intersect current grant, profile, approved destination and data class, enforceable limits and capability. Recheck resolved address and redirect before effects.

## Acceptance

**ZIP-NETWORKING-POLICY-T01.** Public URL resolving to forbidden network cannot receive a request.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
