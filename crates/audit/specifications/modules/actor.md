# Attribution identity

**ZIP-AUDIT-ACTOR-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/actor.rs`

## Required implementation behavior

Record stable principal ID, workspace, actor type and provenance, never raw identity credentials. Unknown actor cannot authorize privileged append.

## Acceptance

**ZIP-AUDIT-ACTOR-T01.** Unauthenticated event cannot be attributed to a legitimate owner.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
