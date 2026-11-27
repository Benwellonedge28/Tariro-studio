# In-process tool adapter

**ZIP-TOOLS-ADAPTERS-NATIVE-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/adapters/native.rs`

## Required implementation behavior

Use reviewed typed adapter, check before effect and enforce cooperative cancellation and budget. No raw host APIs outside assigned scope.

## Acceptance

**ZIP-TOOLS-ADAPTERS-NATIVE-T01.** An implementation lacking required isolation cannot be advertised bound.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
