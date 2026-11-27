# Capability-scoped execution context

**ZIP-RUNTIME-EXECUTION-EXECUTION-CONTEXT-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/execution/execution_context.rs`

## Required implementation behavior

Carry workspace, attempt epoch, plan digest, authorized ports, resource lease and monotonic deadline. Pass only opaque credential references and minimize model-visible fields.

## Acceptance

**ZIP-RUNTIME-EXECUTION-EXECUTION-CONTEXT-T01.** Context copy cannot add privileges or widen deadline beyond lease.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
