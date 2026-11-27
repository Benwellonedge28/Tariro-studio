# Resolved context envelope

**ZIP-CONTEXT-WINDOW-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/window.rs`

## Required implementation behavior

Intersect advertised model window, reserved output, backend capacity and policy. Reject arithmetic overflow or no positive input allowance where required.

## Acceptance

**ZIP-CONTEXT-WINDOW-T01.** Input at exact accepted bound passes and one extra token fails.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
