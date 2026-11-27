# Structured platform argument encoding

**ZIP-TERMINAL-ARGUMENTS-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/arguments.rs`

## Required implementation behavior

Pass argv without shell interpolation. Validate argument count, bytes, platform representation and embedded NUL before launch. Document Windows adapter encoding restrictions.

## Acceptance

**ZIP-TERMINAL-ARGUMENTS-T01.** Synthetic metacharacters reach only the selected executable as literal argument data.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
