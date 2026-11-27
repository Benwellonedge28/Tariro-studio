# Read-only reporting and audit

**ZIP-ASSIGNMENTS-REPORTING-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/reporting.rs`

## Required implementation behavior

Read a scope-filtered consistent snapshot and summarize status, task progress, verification and unresolved effects. Never fetch private payloads to format status. Histories are cursor-bound.

## Acceptance

**ZIP-ASSIGNMENTS-REPORTING-T01.** Unauthorized workspace shows no summary or cursor; duplicate rendering is side-effect free.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
