# Scope attenuation and exact rules

**ZIP-GOVERNANCE-CONSTRAINTS-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/constraints.rs`

## Boundary and inputs

Accept typed allowed paths, effects, destinations, audiences, ceilings, validity and exact obligations from applicable policy and grant layers. All inputs must carry verified source and scope. Keep an omitted permission distinct from an explicitly unrestricted dimension that is allowed only when the governing policy expressly provides it.

## Behavior and failure handling

Intersect allowed sets, take the minimum of comparable ceilings, take the latest start and earliest expiry, and union required obligations. Require exact rules to agree. Incompatible units, empty admissible scope, unresolved attributes or inconsistent exact rules deny. A child needs a verified live parent even if its requested scope is a subset. Preserve which policy layers determined the result.

## Acceptance

**ZIP-GOVERNANCE-CONSTRAINTS-T01.** Intersect overlapping path scopes and a tighter budget. Then attempt to add a destination, mix currencies and specify incompatible exact requirements. Each invalid candidate must fail before effect claim.
