# Danga build adapter

**ZIP-COMPILATION-ADAPTERS-DANGA-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/danga.rs`

## Required implementation behavior

Negotiate exact Danga and Zamani toolchain capabilities and lockfile policy. Do not infer build support from executable presence.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-DANGA-T01.** Unsupported toolchain revision remains unavailable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
