# Nested work accounting

**ZIP-ASSIGNMENTS-SUBTASK-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/subtask.rs`

## Required implementation behavior

Subtask inherits intersection of parent scope and explicit subtask budget. Use parent-relative stable key, bounded nesting and no new privileged effects from a child declaration.

## Acceptance

**ZIP-ASSIGNMENTS-SUBTASK-T01.** Subtask budget exceeding parent denies, while completion advances only its own checkpoint.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
