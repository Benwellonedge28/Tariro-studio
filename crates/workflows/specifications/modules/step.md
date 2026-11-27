# Typed step effect contract

**ZIP-WORKFLOWS-STEP-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/step.rs`

## Required implementation behavior

Pin exact adapter capability, input digest, scope, lease need and error handling; seal output after observed result and reconciliation.

## Acceptance

**ZIP-WORKFLOWS-STEP-T01.** Step with changed input cannot use previous receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
