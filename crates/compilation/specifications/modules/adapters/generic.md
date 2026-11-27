# Explicit generic build adapter

**ZIP-COMPILATION-ADAPTERS-GENERIC-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/generic.rs`

## Required implementation behavior

Use reviewed typed executable/argv, expected artifacts and qualified sandbox. Never synthesize a shell command from project content.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-GENERIC-T01.** Unspecified outputs block build qualification.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
