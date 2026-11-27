# Defensive boundary composition

**ZIP-SECURITY-DEFENSES-MOD-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/defenses/mod.rs`

## Required implementation behavior

Expose content isolation, safe execution, egress controls, supply review and secret hygiene checks. No detector output confers permission.

## Acceptance

**ZIP-SECURITY-DEFENSES-MOD-T01.** Suspicious detector score alone cannot alter effective grant.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
