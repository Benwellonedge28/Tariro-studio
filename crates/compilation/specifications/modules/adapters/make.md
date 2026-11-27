# Make build adapter

**ZIP-COMPILATION-ADAPTERS-MAKE-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/make.rs`

## Required implementation behavior

Use approved makefile and target with structured argv under sandbox. Recipes inherit only admitted resources and environment.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-MAKE-T01.** Untrusted Make recipe cannot bypass network or filesystem isolation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
