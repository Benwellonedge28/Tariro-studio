# Lightweight profile rules

**ZIP-CONFIGURATION-PROFILES-LIGHTWEIGHT-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/profiles/lightweight.rs`

## Required implementation behavior

Prefer serial execution and the smallest compatible admitted local model. Exact quality floors are assignment fields. If no admitted model fits, leave inference unavailable unless an authorized route exists.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-LIGHTWEIGHT-T01.** No compatible local model produces typed unavailability and zero hidden remote attempts.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
