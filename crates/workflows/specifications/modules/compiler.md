# Deterministic workflow plan

**ZIP-WORKFLOWS-COMPILER-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/compiler.rs`

## Required implementation behavior

Resolve versions, expand bounded graphs, validate input/output links and produce ordered immutable executable plan with approval requirements.

## Acceptance

**ZIP-WORKFLOWS-COMPILER-T01.** Equivalent definition order yields same plan digest.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
