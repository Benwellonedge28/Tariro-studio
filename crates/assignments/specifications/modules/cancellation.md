# Assignment cancellation ownership

**ZIP-ASSIGNMENTS-CANCELLATION-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/cancellation.rs`

## Required implementation behavior

Accept current owner-authorized cancel command. Close intake, cancel live lease and record intent. Reconcile committed or unknown effects before terminal outcome; release only after cleanup.

## Acceptance

**ZIP-ASSIGNMENTS-CANCELLATION-T01.** Cancel during commit yields distinguishable committed or unresolved receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
