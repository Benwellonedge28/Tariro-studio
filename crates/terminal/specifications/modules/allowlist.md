# Executable identity restrictions

**ZIP-TERMINAL-ALLOWLIST-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/allowlist.rs`

## Required implementation behavior

Resolve explicit executable capability and version/integrity by approved resolver. Match actual executable rather than caller label or inherited search path.

## Acceptance

**ZIP-TERMINAL-ALLOWLIST-T01.** An executable with same name in an unapproved directory is denied.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
