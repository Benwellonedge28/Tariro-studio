# Mandatory isolation verification

**ZIP-SANDBOX-ISOLATION-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/isolation.rs`

## Required implementation behavior

Verify filesystem, network, credential and process controls as required, and produce exact capability receipt. Changes invalidate launch approval.

## Acceptance

**ZIP-SANDBOX-ISOLATION-T01.** Missing isolation dimension denies even with valid workload lease.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
