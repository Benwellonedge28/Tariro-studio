# Schedule-time resource and scope guard

**ZIP-SCHEDULER-ADMISSION-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/admission.rs`

## Required implementation behavior

Check live authority, usable pool, demand and deadline immediately before claim. Compensate any unused reservation on conflict; never release occupied capacity before cleanup.

## Acceptance

**ZIP-SCHEDULER-ADMISSION-T01.** Revoked queued job performs no spawn.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
