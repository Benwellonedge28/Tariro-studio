# Strategy selection boundary

**ZIP-ORCHESTRATION-STRATEGIES-MOD-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/strategies/mod.rs`

## Boundary and inputs

Resolve a strategy identifier and edition from the approved assignment and Configuration snapshot. Explicit serial execution overrides profiling preferences for additional concurrency. Validate readiness, conflict scope and effective agent ceilings before passing a pinned input to a strategy module. An unknown or unavailable strategy cannot silently widen execution.

## Behavior and failure handling

Strategy output consists of a bounded ordered proposal and expected revisions. It cannot delegate authority, charge Resources, bypass Verification or settle conflict by vote. Maintain a separate review binding wherever verification policy requires independence. Apply proposals through the owning assignment and Scheduler control paths. Invalid strategy results leave the durable graph unchanged.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-MOD-T01.** Resolve an unavailable strategy and a parallel preference under an explicitly serial plan. Verify typed denial in the first case and at most one serial proposal in the second. Pass a proposal without independent review where required and verify it cannot satisfy acceptance.
