# Exact authorized batch semantics

**ZIP-ASSIGNMENTS-BATCHING-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/batching.rs`

## Required implementation behavior

Count distinct final normalized output paths, verify each against authorized type/scope/evidence and seal digest of sorted manifest. Exact batch agreement applies only to that grant. Short batch awaits approval and extra item is denied.

## Acceptance

**ZIP-ASSIGNMENTS-BATCHING-T01.** Reference agreement enforces thirty; an independently authorized different count works without code changes.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
