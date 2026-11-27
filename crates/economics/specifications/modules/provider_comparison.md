# Comparable provider price view

**ZIP-ECONOMICS-PROVIDER-COMPARISON-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/provider_comparison.rs`

## Required implementation behavior

Normalize quoted units and rate validity, separate estimates from actual bills, and mark unknown currency conversion or unqualified offerings.

## Acceptance

**ZIP-ECONOMICS-PROVIDER-COMPARISON-T01.** Different tokens/currency cannot silently compare as equal.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
