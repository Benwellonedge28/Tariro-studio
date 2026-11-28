# Proposal compatibility review

**ZIP-ORCHESTRATION-NEGOTIATION-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/negotiation.rs`

## Boundary and inputs

Accept bounded typed proposals binding actor, candidate digest, constraints, resource assumptions and expected state. Verify all proposals against the same authorized comparison scope. Keep each origin and distinguish fixed requirements, compatible preferences and unavailable observations.

## Behavior and failure handling

Check scope and preconditions before computing overlap. Intersect compatible bounds in the same dimensions, reject contradictory exact assumptions, and report unresolved mandatory evidence without choosing a winner. A compatible counterproposal is a new reviewable candidate. Its digest and approval are separate from the inputs. Negotiation performs no reservation, enactment or authority change.

## Acceptance

**ZIP-ORCHESTRATION-NEGOTIATION-T01.** Provide mutually exclusive exact requirements and a pair that can fit only when one shared capacity is measured. Observe explicit conflict and unavailable evidence respectively. Reverse proposal order without changing either result.
