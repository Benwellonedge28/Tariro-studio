# Embedded in-process provider

**ZIP-INTELLIGENCE-PROVIDERS-EMBEDDED-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/providers/embedded.rs`

## Required implementation behavior

Qualify compatible model/runtime and budget, use bounded output and cooperative cancellation. Provider does not bypass sandbox/policy admission.

## Acceptance

**ZIP-INTELLIGENCE-PROVIDERS-EMBEDDED-T01.** Exhausted memory budget fails before model execution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
