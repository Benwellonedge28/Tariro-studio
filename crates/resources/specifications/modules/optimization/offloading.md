# Authorized placement change

**ZIP-RESOURCES-OPTIMIZATION-OFFLOADING-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/optimization/offloading.rs`

## Boundary and inputs

Return only routable candidates from enrolled providers or nodes with fresh verified identities, supported execution capabilities, approved locality and compatible data classes. Require live permission for transfer and an enforceable budget in the applicable currency or usage units. A remote observation is scoped to its own service and never enlarges a local pool.

## Behavior and failure handling

Compare eligible candidates with the preapproved ordering and stable identity tie-break. Produce a typed proposed demand with provider, data-class and pricing revisions. The owning adapter rechecks live authorization, data scope, exact destination, verified budget and lease before sending. No provider call is made merely to establish an option without authority. Ambiguous original work is reconciled before replacement according to its effect boundary.

## Acceptance

**ZIP-RESOURCES-OPTIMIZATION-OFFLOADING-T01.** Induce local GPU shortage with a remote candidate that lacks egress grant, then with a stale budget. Observe no remote calls and no change to spend limits. A fully verified candidate remains a proposal until an authorized lease and route are accepted.
