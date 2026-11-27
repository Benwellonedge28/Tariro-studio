# Versioned request envelope

**ZIP-INTELLIGENCE-REQUEST-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/request.rs`

## Required implementation behavior

Bind model capabilities, authorized context, route scope, output shape, budgets and deadline. Validate compatibility and references before allocation.

## Acceptance

**ZIP-INTELLIGENCE-REQUEST-T01.** Changed approved context or output schema requires current validation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
