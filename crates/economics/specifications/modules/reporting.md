# Observed cost reporting

**ZIP-ECONOMICS-REPORTING-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/reporting.rs`

## Required implementation behavior

Show estimated, reserved, observed and unresolved amounts separately by exact scope and rate revision. No settlement or money transfer.

## Acceptance

**ZIP-ECONOMICS-REPORTING-T01.** Ambiguous provider usage remains visibly unresolved.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
