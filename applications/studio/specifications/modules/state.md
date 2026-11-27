# Immutable UI projection

**ZIP-STUDIO-STATE-001 · v1.0 · Owner:** Studio maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/studio/src/state.rs`

## Required implementation behavior

Own revisioned workspace view state, scoped selected item and pending approval receipt. Apply one reducer update per ordered event. Clear state on workspace switch.

## Acceptance

**ZIP-STUDIO-STATE-T01.** Late event from previous workspace cannot expose data or update current state.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
