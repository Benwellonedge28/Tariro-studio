# Governed evolution facade

**ZIP-EVOLUTION-LIB-001 · v1.0 · Owner:** Evolution maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/evolution/src/lib.rs`

## Required implementation behavior

Expose proposal, experiment and evaluation ports. Linking does not change code, policy or deployed state.

## Acceptance

**ZIP-EVOLUTION-LIB-T01.** Proposal-only client starts no external effects.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
