# Terminal capability facade

**ZIP-TERMINAL-LIB-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/lib.rs`

## Required implementation behavior

Expose typed command, execution and output ports through supervised sandbox. No default shell entry point.

## Acceptance

**ZIP-TERMINAL-LIB-T01.** Downstream code cannot execute an arbitrary untyped command from public facade.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
