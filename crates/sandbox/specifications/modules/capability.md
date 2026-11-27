# Qualification evidence DTO

**ZIP-SANDBOX-CAPABILITY-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/capability.rs`

## Required implementation behavior

Advertise each enforced control only after qualified platform evidence, distinguishing supported, unavailable and unknown. Compare required modes before activation.

## Acceptance

**ZIP-SANDBOX-CAPABILITY-T01.** Missing isolation evidence cannot map to support.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
