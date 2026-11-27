# Explicit resume command

**ZIP-ASSIGNMENTS-RESUME-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/resume.rs`

## Required implementation behavior

Validate current revision and live grant, pin original plan, call recovery to derive next unit and reacquire resource lease. Do not trust cached task handles or widen old approval.

## Acceptance

**ZIP-ASSIGNMENTS-RESUME-T01.** Expired grant pauses while prior verified artifacts remain referenced.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
