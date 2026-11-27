# Design authoring role boundaries

**ZIP-DOCUMENTATION-DESIGN-MOD-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/design/mod.rs`

## Required implementation behavior

Route architecture, subsystem and component drafts to their declared contract roles; link shared definitions and preserve owner metadata.

## Acceptance

**ZIP-DOCUMENTATION-DESIGN-MOD-T01.** Unsupported document role cannot silently select generic complete status.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
