# Resource budget view

**ZIP-CONFIGURATION-RESOURCES-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/resources.rs`

## Required implementation behavior

Expose typed read-only resource policy by revision. Separate configured ceilings, derived capacity and exact assignment constraints. Missing required finite value denies admission.

## Acceptance

**ZIP-CONFIGURATION-RESOURCES-T01.** Zero, unknown and finite positive values remain distinguishable at the resource boundary.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
