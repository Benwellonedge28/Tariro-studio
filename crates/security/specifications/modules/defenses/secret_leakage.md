# Sensitive content gate

**ZIP-SECURITY-DEFENSES-SECRET-LEAKAGE-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/defenses/secret_leakage.rs`

## Required implementation behavior

Classify outputs by schema and trusted canary detectors, redact before retention, and block uncertain privileged egress pending review.

## Acceptance

**ZIP-SECURITY-DEFENSES-SECRET-LEAKAGE-T01.** Repository containing synthetic token cannot expose it in model context.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
