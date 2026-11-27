# Effective resource bound resolver

**ZIP-RESOURCES-LIMITS-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/limits.rs`

## Required implementation behavior

Compute finite minima for each compatible coordinate; reject absent required value, invalid unit and arithmetic overflow. Retain all contributing origins for diagnostics.

## Acceptance

**ZIP-RESOURCES-LIMITS-T01.** Unknown, exact zero and positive values produce separately testable decisions.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
