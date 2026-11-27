# Fail-closed verdict reduction

**ZIP-VERIFICATION-ACCEPTANCE-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/acceptance.rs`

## Required implementation behavior

Fail if any mandatory result failed; otherwise block if evidence is missing, stale or blocked; pass only if all mandatory current results pass. Preserve optional outcomes.

## Acceptance

**ZIP-VERIFICATION-ACCEPTANCE-T01.** Submit mixtures of failed, missing and passed and verify deterministic precedence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
