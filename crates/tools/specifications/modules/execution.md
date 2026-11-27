# Supervised invocation execution

**ZIP-TOOLS-EXECUTION-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/execution.rs`

## Required implementation behavior

Persist bounded intent, dispatch qualified adapter under lease, collect typed receipt and classify unknowns. Cancel through supervisor and preserve cleanup evidence.

## Acceptance

**ZIP-TOOLS-EXECUTION-T01.** Unknown mutation result stays pending until read-only reconciliation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
