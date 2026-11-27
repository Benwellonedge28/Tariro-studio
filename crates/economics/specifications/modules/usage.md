# Observed usage record

**ZIP-ECONOMICS-USAGE-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/usage.rs`

## Required implementation behavior

Bind provider/effect, units, source, revision and observed/estimated/unknown status. Confirm actual usage from qualified receipt.

## Acceptance

**ZIP-ECONOMICS-USAGE-T01.** Missing provider count does not become observed zero.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
