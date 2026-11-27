# Pure condition evaluation

**ZIP-WORKFLOWS-CONDITION-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/condition.rs`

## Required implementation behavior

Evaluate typed data under scoped immutable inputs, bounded complexity and deterministic error order. Missing required values deny branch choice.

## Acceptance

**ZIP-WORKFLOWS-CONDITION-T01.** Undefined value does not become implicit true.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
