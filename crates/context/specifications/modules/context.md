# Bound context bundle

**ZIP-CONTEXT-CONTEXT-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/context.rs`

## Required implementation behavior

Bind context to snapshot, assignment scope, selection policy, tokenizer and digest. Record required items, ranked optional items and omissions by reason.

## Acceptance

**ZIP-CONTEXT-CONTEXT-T01.** A bundle from another scope fails provider dispatch checks.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
