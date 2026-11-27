# Subsystem contract

**ZIP-DOCUMENTATION-DESIGN-SUBSYSTEM-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/design/subsystem.rs`

## Required implementation behavior

Specify responsibilities, actors, state, dependencies, policy and independent acceptance for the subsystem. Trace its contract to explicit component files.

## Acceptance

**ZIP-DOCUMENTATION-DESIGN-SUBSYSTEM-T01.** Missing inter-component protocol remains design blocker.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
