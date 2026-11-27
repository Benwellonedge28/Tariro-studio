# Aggregate construction

**ZIP-ASSIGNMENTS-ASSIGNMENT-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/assignment.rs`

## Required implementation behavior

create(spec: ValidatedSpec, actor: Principal, id: AssignmentId) -> Result<AssignmentDraft, AssignmentError>. Pin repository ID/base, scope, requirements, revision and actor. Initial state is Submitted and grants are absent until verified.

## Acceptance

**ZIP-ASSIGNMENTS-ASSIGNMENT-T01.** Missing pinned base or owner produces no persisted aggregate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
