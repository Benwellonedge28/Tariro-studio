# Bounded team definition

**ZIP-ORCHESTRATION-TEAM-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/team.rs`

## Boundary and inputs

Compile a bounded team from the approved assignment and versioned role catalog. Bind members to scoped principals, exact responsibilities, task dependencies, conflict identities and required reviewer independence. Use canonical task and identity order and reject duplicate or contradictory commitments before returning a plan.

## Behavior and failure handling

Validate role eligibility and the effective agent cap. Treat unfilled mandatory role or review requirements as blocked. A compiled team describes the proposed mapping and does not reserve leases or issue tool grants. A membership replacement makes a new versioned decision and preserves historical evidence. Revalidate the affected candidate and remaining graph before dispatch.

## Acceptance

**ZIP-ORCHESTRATION-TEAM-T01.** Assign an author as mandatory independent reviewer and verify planning fails. Add a qualified reviewer and permute membership input. Verify the same canonical mapping and no implicit resource request.
