# Component integration contract

**ZIP-DOCUMENTATION-DESIGN-INTEGRATION-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/design/integration.rs`

## Required implementation behavior

Map both sides of the boundary, applicable version/feature, request authority, expected replies and fallback policy. Specify required fixture conditions.

## Acceptance

**ZIP-DOCUMENTATION-DESIGN-INTEGRATION-T01.** Unsupported version cannot be described as silently compatible.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
