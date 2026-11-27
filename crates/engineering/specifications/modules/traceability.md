# End-to-end candidate evidence links

**ZIP-ENGINEERING-TRACEABILITY-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/traceability.rs`

## Required implementation behavior

Bind approved requirement IDs, staged diff paths and actual verification reports to one exact candidate. Preserve unresolved and stale links.

## Acceptance

**ZIP-ENGINEERING-TRACEABILITY-T01.** Old candidate evidence cannot certify current change.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
