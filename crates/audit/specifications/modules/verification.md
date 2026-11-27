# Audit acceptance fixtures and verdicts

**ZIP-AUDIT-VERIFICATION-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/verification.rs`

## Required implementation behavior

Recompute chain, confirm authorized records and linked evidence, return passed/failed/blocked with exact candidate digest. Do not certify unrelated scope.

## Acceptance

**ZIP-AUDIT-VERIFICATION-T01.** Missing required record blocks verdict even with consistent remaining chain.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
