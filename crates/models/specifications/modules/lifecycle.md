# Model durable state machine

**ZIP-MODELS-LIFECYCLE-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/lifecycle.rs`

## Required implementation behavior

Use Discovered, Staging, Verified, Ready, Draining, Removed and Failed. Activate only after qualified integrity/compatibility and required approvals.

## Acceptance

**ZIP-MODELS-LIFECYCLE-T01.** Cancelled staging remains unavailable and recoverable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
