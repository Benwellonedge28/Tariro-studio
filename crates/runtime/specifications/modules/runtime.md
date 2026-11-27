# Primary runtime control

**ZIP-RUNTIME-RUNTIME-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/runtime.rs`

## Required implementation behavior

Accept typed start/pause/cancel/shutdown commands via supervisor. Validate runtime lifecycle and lease before submission. Source effects pass their own governance gate.

## Acceptance

**ZIP-RUNTIME-RUNTIME-T01.** A request received during draining is rejected before queuing.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
