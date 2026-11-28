# Conflict-aware parallel proposals

**ZIP-ORCHESTRATION-STRATEGIES-PARALLEL-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/strategies/parallel.rs`

## Boundary and inputs

Select bounded ready tasks in canonical plan order. Partition using canonical write conflict keys from the trusted planner, including the exact workspace and normalized path or approved broader scope. Treat unknown or overlapping scopes as conflicting. Build a proposal up to the effective agent envelope, taking active and recovering agents into account.

## Behavior and failure handling

Apply revision-checked conflict protection before handoff so two concurrent rounds cannot assign overlapping writes. Independent candidates may proceed around an earlier conflicting candidate in stable order within the bounded scan. Each selected task requires Scheduler claim and assigned lease. Keep author and reviewer separation under Verification and keep conflicts unresolved until authorized resolution.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-PARALLEL-T01.** Offer two competing writes to the same normalized path, including aliases, and one independent task. With free slots verify no overlapping dispatch and the independent task can proceed. Rotate input order and confirm the same proposal.
