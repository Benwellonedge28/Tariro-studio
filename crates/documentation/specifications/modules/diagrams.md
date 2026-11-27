# Bounded diagram specification

**ZIP-DOCUMENTATION-DIAGRAMS-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/diagrams.rs`

## Required implementation behavior

Validate supported syntax and scope before rendering; treat links/directives as inert data unless explicitly sanctioned. Persist source digest and renderer version.

## Acceptance

**ZIP-DOCUMENTATION-DIAGRAMS-T01.** External include and unqualified render command are denied.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
