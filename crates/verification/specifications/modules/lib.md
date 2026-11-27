# Verification boundary

**ZIP-VERIFICATION-LIB-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/lib.rs`

## Required implementation behavior

Expose plan, verification runner, evidence and verdict. Observed checks are injected through qualified interfaces. No outbound effect from a library import.

## Acceptance

**ZIP-VERIFICATION-LIB-T01.** A mock runner and local evidence store suffice to evaluate a gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
