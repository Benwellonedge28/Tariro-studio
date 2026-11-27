# Instruction resolution boundary

**ZIP-REPOSITORY-INSTRUCTIONS-MOD-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/instructions/mod.rs`

## Required implementation behavior

Expose discovery, parsing, hierarchy, precedence and validation as separate steps under immutable revision. None gains external effect authority.

## Acceptance

**ZIP-REPOSITORY-INSTRUCTIONS-MOD-T01.** Pinned instruction bundle remains stable across unrelated branch movement.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
