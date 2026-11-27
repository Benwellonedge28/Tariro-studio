# Research provider negotiation

**ZIP-RESEARCH-PROVIDERS-MOD-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/providers/mod.rs`

## Required implementation behavior

Select qualified local/documentation/repository/academic/web adapter while respecting scope and format. Unsupported stays unavailable.

## Acceptance

**ZIP-RESEARCH-PROVIDERS-MOD-T01.** Missing documentation adapter does not activate web fallback.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
