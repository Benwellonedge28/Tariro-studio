# Typed scoped workflow values

**ZIP-WORKFLOWS-VARIABLES-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/variables.rs`

## Required implementation behavior

Resolve immutable inputs, typed outputs and default values without widening scope. Redact secret references and reject unsafe reference expansion.

## Acceptance

**ZIP-WORKFLOWS-VARIABLES-T01.** A secret reference cannot become serialized raw string.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
