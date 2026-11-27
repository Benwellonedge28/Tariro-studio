# Pinned end-to-end scenario

**ZIP-TESTING-END-TO-END-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/end_to_end.rs`

## Required implementation behavior

Follow approved workflows with exact fixtures and effects under independent authorization; audit verified outputs, restart and failure gates.

## Acceptance

**ZIP-TESTING-END-TO-END-T01.** Lost remote reply reconciles without duplicate effect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
