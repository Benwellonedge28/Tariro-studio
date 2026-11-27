# Sandbox lifecycle vocabulary

**ZIP-SANDBOX-LIFECYCLE-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/lifecycle.rs`

## Required implementation behavior

Use Preparing, Ready, Running, Draining, Closed or FailedWithCleanup. Validate events and epoch. Closed requires cleanup proof and cannot relaunch.

## Acceptance

**ZIP-SANDBOX-LIFECYCLE-T01.** Backend error after spawn becomes cleanup pending and retains lease.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
