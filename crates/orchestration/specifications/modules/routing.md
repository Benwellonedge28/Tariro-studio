# Qualified role and provider route

**ZIP-ORCHESTRATION-ROUTING-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/routing.rs`

## Required implementation behavior

Filter route by task capability, data locality, role and actual availability. Resolve tie by stable ID. Require new grant for unauthorized alternatives.

## Acceptance

**ZIP-ORCHESTRATION-ROUTING-T01.** Unavailable local route does not activate an external provider.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
