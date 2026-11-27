# Typed tool argument parsing

**ZIP-TOOLS-ARGUMENTS-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/arguments.rs`

## Required implementation behavior

Validate strict schema and scoped paths/identifiers, then normalize canonical arguments. Bound byte and list sizes before materialization.

## Acceptance

**ZIP-TOOLS-ARGUMENTS-T01.** Arbitrary command text fails the expected typed argument schema.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
