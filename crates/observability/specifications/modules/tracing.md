# Scoped trace propagation

**ZIP-OBSERVABILITY-TRACING-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/tracing.rs`

## Required implementation behavior

Bind correlation/parent IDs to admitted task, validate incoming context, and use bounded span metadata without sensitive content.

## Acceptance

**ZIP-OBSERVABILITY-TRACING-T01.** Cross-tenant identifiers cannot overtake local trace authority.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
