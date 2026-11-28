# Qualified role and provider route

**ZIP-ORCHESTRATION-ROUTING-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/routing.rs`

## Boundary and inputs

Consider only agents and provider routes with qualified capability, role eligibility, current scope, required data class and known availability. Match input privacy and locality before ranking. Use the approved route comparator and stable identity as tie-break. Bind the candidate's observed capability and policy revisions to the proposal.

## Behavior and failure handling

Never route to a location outside the authorized selection. Missing local capability yields NoEligibleAgent when no other authorized route exists. A new grant is required to consider an alternative that changes recipient, data locality, cost scope or effect capability. The owning adapter rechecks availability and authorization before opening a channel. Ranking itself uses caller-supplied observations.

## Acceptance

**ZIP-ORCHESTRATION-ROUTING-T01.** Remove the only qualified local route under an offline policy and supply a remote candidate with a higher score. Verify no remote selection or network call. Restore two equally qualified local candidates and obtain identical routing under permuted input.
