# Supervised agent run

**ZIP-AGENTS-EXECUTION-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/execution.rs`

## Boundary and inputs

Accept an authorized exact task, bound instance and expected revision through the agent dispatch interface. Construct the Runtime task binding through composition and obtain its matching lease from the authorized admission path. Commit an attempt intent before calling the [Runtime facade](../../../runtime/specifications/modules/runtime.md). Model output and tool requests are proposals with independent capability checks.

## Behavior and failure handling

Revalidate the live agent grant before context disclosure, execution and each protected effect. Use independently authorized stable effect intents. Keep Output provisional until Runtime and the owning verifier accept scoped evidence. After a lost launch or effect reply reconcile the original attempt. Cancel through the supervisor and retain previously committed receipts. A worker cannot free a reservation directly or reuse a stale execution binding.

## Acceptance

**ZIP-AGENTS-EXECUTION-T01.** Cancel after a synthetic provider confirms an effect but before the agent receives its response. Recover the same evidence, record no duplicate effect and verify revoked scope cannot authorize a successor.
