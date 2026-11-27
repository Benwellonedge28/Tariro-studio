# Deterministic admitted provider routing

**ZIP-PROVIDERS-ROUTING-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/routing.rs`

## Required implementation behavior

Filter by live policy, destination and data class, qualified capability and lease, then apply configured priority and stable tie-break.

## Acceptance

**ZIP-PROVIDERS-ROUTING-T01.** Configured provider outside grant excluded before transmission.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
