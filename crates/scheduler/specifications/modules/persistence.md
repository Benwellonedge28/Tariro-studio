# Schedule and attempt durability

**ZIP-SCHEDULER-PERSISTENCE-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/persistence.rs`

## Required implementation behavior

Store job, attempt epoch, claim, receipt and events atomically with revision checks. Replay committed receipt by stable attempt ID and reconcile pending intents before restart.

## Acceptance

**ZIP-SCHEDULER-PERSISTENCE-T01.** Terminate during claim and confirm the recovered scheduler never sees two active epochs.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
