# Token accounting

**ZIP-CONTEXT-TOKEN-BUDGET-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/token_budget.rs`

## Required implementation behavior

Track required, optional and output reservations using checked additions and scoped lease. Account for template overhead and cite final tokenizer identity.

## Acceptance

**ZIP-CONTEXT-TOKEN-BUDGET-T01.** A template changing token count cannot exceed admitted budget.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
