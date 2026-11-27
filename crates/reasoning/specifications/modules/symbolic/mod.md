# Symbolic reasoning dispatch

**ZIP-REASONING-SYMBOLIC-MOD-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/symbolic/mod.rs`

## Required implementation behavior

Resolve qualified rules, logic and solver under controlled inputs and bounded resources. Unknown fragment unsupported.

## Acceptance

**ZIP-REASONING-SYMBOLIC-MOD-T01.** Unsupported operator cannot fall back to permissive evaluation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
