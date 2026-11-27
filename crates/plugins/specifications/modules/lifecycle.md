# Fenced plugin lifecycle

**ZIP-PLUGINS-LIFECYCLE-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/lifecycle.rs`

## Required implementation behavior

Represent installed, ready, active, draining, revoked and failed. Fence old epochs before new calls and retain unreaped cleanup obligations.

## Acceptance

**ZIP-PLUGINS-LIFECYCLE-T01.** Revoked instance cannot make new host calls.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
