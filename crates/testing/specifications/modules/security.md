# Defensive control assertions

**ZIP-TESTING-SECURITY-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/security.rs`

## Required implementation behavior

Use isolated synthetic fixtures to verify deny, redaction, revocation and containment against declared boundaries. No unauthorized target testing.

## Acceptance

**ZIP-TESTING-SECURITY-T01.** Canary cannot cross prohibited egress or appear in audit output.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
