# Remote effect lifecycle

**ZIP-DISTRIBUTED-EXECUTION-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/execution.rs`

## Required implementation behavior

Persist dispatch intent, authorize data transfer, send bounded task payload, verify receipt and reconcile missing outcomes before retry.

## Acceptance

**ZIP-DISTRIBUTED-EXECUTION-T01.** Response loss retains unresolved effect rather than duplicating dispatch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
