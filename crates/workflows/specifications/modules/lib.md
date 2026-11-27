# Workflow service boundary

**ZIP-WORKFLOWS-LIB-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/lib.rs`

## Required implementation behavior

Export definition, validation, compiler and execution ports; capability actions go through typed services. No effects on import.

## Acceptance

**ZIP-WORKFLOWS-LIB-T01.** Parsing and validating workflow works with all effect adapters disabled.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
