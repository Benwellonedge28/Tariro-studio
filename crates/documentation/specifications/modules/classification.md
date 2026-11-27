# Evidence-based document classification

**ZIP-DOCUMENTATION-CLASSIFICATION-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/classification.rs`

## Required implementation behavior

Use explicit reason codes for complete, incomplete, candidate placeholder and missing. Require reviewer confirmation for heuristic findings.

## Acceptance

**ZIP-DOCUMENTATION-CLASSIFICATION-T01.** An intentionally short valid decision record is not automatically replaced.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
