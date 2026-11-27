# Bounded deterministic properties

**ZIP-TESTING-PROPERTY-BASED-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/property_based.rs`

## Required implementation behavior

Record property/version, seed, generator config and shrink budget, retain minimal observed counterexample under current lease.

## Acceptance

**ZIP-TESTING-PROPERTY-BASED-T01.** Same seed and pinned generator replay failure.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
