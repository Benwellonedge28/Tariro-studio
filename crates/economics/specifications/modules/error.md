# Cost accounting outcomes

**ZIP-ECONOMICS-ERROR-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/error.rs`

## Required implementation behavior

Distinguish unknown rate, inactive currency, arithmetic, insufficient budget, duplicate receipt and unknown charge. Keep sensitive upstream data redacted.

## Acceptance

**ZIP-ECONOMICS-ERROR-T01.** Provider timeout cannot turn uncertain charge into zero.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
