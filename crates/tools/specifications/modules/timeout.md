# Deadline negotiation

**ZIP-TOOLS-TIMEOUT-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/timeout.rs`

## Required implementation behavior

Use earliest operation, lease and adapter deadlines, all finite. Expired mutation remains unresolved if effect may have crossed dispatch boundary.

## Acceptance

**ZIP-TOOLS-TIMEOUT-T01.** Timing out receive does not classify remote operation as absent.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
