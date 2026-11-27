# Tool failure vocabulary

**ZIP-TOOLS-ERROR-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/error.rs`

## Required implementation behavior

Classify invalid arguments, unsupported capability, denied scope, timeout, resource exhaustion, unknown effect and adapter failure. Contain upstream raw errors.

## Acceptance

**ZIP-TOOLS-ERROR-T01.** Mismatched schema can be returned without exposing raw input.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
