# Session-scoped memory

**ZIP-MEMORY-LAYERS-SESSION-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/layers/session.rs`

## Required implementation behavior

Bind to authenticated session and expiry; no permanent storage by default. Enforce revocation through live session epoch.

## Acceptance

**ZIP-MEMORY-LAYERS-SESSION-T01.** Logout makes cached session records inaccessible.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
