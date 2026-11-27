# Budgeted state exploration

**ZIP-VERIFICATION-FORMAL-MODEL-CHECKING-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/formal/model_checking.rs`

## Required implementation behavior

Run deterministic exploration or qualified checker under resource/state budget. Distinguish valid proof, counterexample, exhaustion and unsupported.

## Acceptance

**ZIP-VERIFICATION-FORMAL-MODEL-CHECKING-T01.** State bound reached is incomplete, never universal success.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
