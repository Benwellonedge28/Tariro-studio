# Immutable observed result

**ZIP-VERIFICATION-EVIDENCE-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/evidence.rs`

## Required implementation behavior

Persist candidate/plan/input digest, test ID, tool/runner version, observed result kind and artifact reference. Use typed status and scoped reads.

## Acceptance

**ZIP-VERIFICATION-EVIDENCE-T01.** A report with mismatched artifact digest cannot satisfy a gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
