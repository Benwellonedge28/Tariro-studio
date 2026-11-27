# Bounded standard output

**ZIP-TERMINAL-STDOUT-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/stdout.rs`

## Required implementation behavior

Charge bytes to combined output account before buffer/persist, maintain order within stream, and expose explicit truncation or output exhaustion.

## Acceptance

**ZIP-TERMINAL-STDOUT-T01.** Flooded stdout stops within admitted combined limit.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
