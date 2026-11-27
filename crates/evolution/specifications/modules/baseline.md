# Pinned evidence baseline

**ZIP-EVOLUTION-BASELINE-001 · v1.0 · Owner:** Evolution maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/evolution/src/baseline.rs`

## Required implementation behavior

Record current candidate, toolchain, configuration, fixtures and accepted outcomes necessary for comparison.

## Acceptance

**ZIP-EVOLUTION-BASELINE-T01.** Changed fixture invalidates reuse of old baseline result.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
