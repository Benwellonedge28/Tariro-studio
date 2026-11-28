# Bounded proposal comparison

**ZIP-ORCHESTRATION-STRATEGIES-DEBATE-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/strategies/debate.rs`

## Boundary and inputs

Evaluate a bounded number of authorized alternatives using configured round, input and time budgets. Record evidence and uncertainty per proposal and preserve author and reviewer identities. Choose stable evaluation and tie ordering from the pinned plan. Each round may rank already admitted evidence without authorizing new effects.

## Behavior and failure handling

Stop on an independently verified outcome or a blocked verdict with remaining uncertainty. Exhausting time or rounds never implies agreement. Duplicate evidence digests do not add independent support. Preserve minority evidence and use the authorized escalation path when a required question remains open. Replaying the same round reconstructs its decision without extending the budget.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-DEBATE-T01.** Run equivalent input in two orders, then exhaust the final round with a contradictory receipt. Verify stable ordering, explicit unresolved uncertainty and zero approval or execution as a result of exhaustion.
