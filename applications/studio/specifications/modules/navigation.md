# Typed scoped routes

**ZIP-STUDIO-NAVIGATION-001 · v1.0 · Owner:** Studio maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/studio/src/navigation.rs`

## Required implementation behavior

Represent route with workspace and optional typed identity. Validate target scope before opening view and distinguish missing from stale projection. Persist only user navigation preference.

## Acceptance

**ZIP-STUDIO-NAVIGATION-T01.** A route cannot open another workspace through untrusted document content.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
