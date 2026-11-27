# Typed interface specification

**ZIP-DOCUMENTATION-DESIGN-INTERFACE-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/design/interface.rs`

## Required implementation behavior

Record Rust signatures, lifetimes, units, semantics, compatibility and error behavior. Actual qualification fixture must match authoritative declarations.

## Acceptance

**ZIP-DOCUMENTATION-DESIGN-INTERFACE-T01.** Mismatched typed parameter or state-changing effect version blocks review.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
