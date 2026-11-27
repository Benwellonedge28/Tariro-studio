# Document format adapters

**ZIP-DOCUMENTATION-FORMATS-MOD-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/formats/mod.rs`

## Required implementation behavior

Resolve qualified format adapter and version for scoped source and output. Format parsing cannot perform network, shell or publication.

## Acceptance

**ZIP-DOCUMENTATION-FORMATS-MOD-T01.** Unqualified adapter returns unsupported rather than passing raw data through.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
