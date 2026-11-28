# Orchestrator execution loop

**ZIP-ORCHESTRATION-ORCHESTRATOR-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/orchestrator.rs`

## Boundary and inputs

Accept an authorized assignment and pinned reviewed plan through the [crate boundary](../../DESIGN.md). Compile and validate the execution graph before registering a plan. Capture graph and policy revisions, role and conflict requirements, and the effective agent envelope. Read progress from the owning assignment checkpoint and scheduler receipts.

## Behavior and failure handling

For each bounded planning round, collect durable ready tasks, apply the authorized strategy and resolve roles under current scope. Write a stable submission intent through Assignments before invoking Scheduler. Revalidate revisions at each external boundary. On accepted submission bind the durable Scheduler identity. On unknown result inspect the original identity, preserve its unresolved obligation and initiate no duplicate submission. Apply trusted completion under graph and attempt fencing. Waiters, retries and replanning use approved budgets.

## Acceptance

**ZIP-ORCHESTRATION-ORCHESTRATOR-T01.** Interrupt after Scheduler accepts a task and before Orchestration receives the reply. Restore the original assignment checkpoint, reconcile the one Scheduler job and confirm no duplicate submission or terminal transition.
