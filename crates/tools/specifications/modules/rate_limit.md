# Scoped tool rate accounting

**ZIP-TOOLS-RATE-LIMIT-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/rate_limit.rs`

## Boundary and inputs

Resolve scoped provider/operation rate envelope and separately applicable spend and occupancy budgets. Use the governing compatible units and authoritative current accounting. Reserve consumption atomically before launching concurrent operations. A rate value near exhaustion cannot expand the scope or extend an operation.

## Behavior and failure handling

Account verified consumption through the owning ledger. Restore only proven unused reservation under current ownership, and retain unsettled allowance after a lost response. A qualified retry-after supplies a lower bound on eligibility. Compare it with the current operation deadline without shortening the wait. If it reaches or exceeds that deadline, report deferred or expired without another execution.

## Acceptance

**ZIP-TOOLS-RATE-LIMIT-T01.** Race two requests for one remaining admitted unit and verify one commits. Lose the usage reply and confirm no speculative credit. Provide a delay beyond deadline and verify no retry.
