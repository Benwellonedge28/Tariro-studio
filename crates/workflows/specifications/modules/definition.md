# Declarative workflow DTO

**ZIP-WORKFLOWS-DEFINITION-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/definition.rs`

## Required implementation behavior

Bind graph, inputs, typed capability names, policy references, budgets and explicit effect categories. Unknown mandatory fields fail strict decode.

## Acceptance

**ZIP-WORKFLOWS-DEFINITION-T01.** Malformed descriptor cannot activate an operation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
