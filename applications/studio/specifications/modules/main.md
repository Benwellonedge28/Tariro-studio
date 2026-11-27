# Native Studio composition

**ZIP-STUDIO-MAIN-001 · v1.0 · Owner:** Studio maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/studio/src/main.rs`

## Required implementation behavior

Wire application state and authorized local gateway adapter; keep input, data and metrics scoped to active workspace. No direct repository mutation from top-level UI.

## Acceptance

**ZIP-STUDIO-MAIN-T01.** Start offline with disabled remote features and no implicit effect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
