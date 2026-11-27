# Context failure vocabulary

**ZIP-CONTEXT-ERROR-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/error.rs`

## Required implementation behavior

Distinguish out-of-scope, required context overflow, tokenizer unavailable, stale pin and capacity exhausted. Omit rejected data in errors.

## Acceptance

**ZIP-CONTEXT-ERROR-T01.** Sensitive path content cannot appear in rejection output.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
