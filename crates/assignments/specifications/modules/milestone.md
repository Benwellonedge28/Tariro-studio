# Aggregate progress milestone

**ZIP-ASSIGNMENTS-MILESTONE-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/milestone.rs`

## Required implementation behavior

A milestone is a named set of required gates. Report reached only from verified task/requirement state in one revision. Never calculate success by elapsed time or agent response.

## Acceptance

**ZIP-ASSIGNMENTS-MILESTONE-T01.** Missing evidence keeps milestone pending even with all tasks reported executed.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
