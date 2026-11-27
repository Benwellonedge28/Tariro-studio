# Policy-limited workflow retry

**ZIP-WORKFLOWS-RETRY-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/retry.rs`

Retry eligibility requires a confirmed transient outcome with no unresolved effect and settled execution, unchanged plan and inputs, live permission and remaining authorised budget. A provider effect proven absent can reuse its original effect identity under its original compare conditions. Changing adapter parameters, output paths or effect identity requires review under a new plan. A compensated, skipped, expired or revoked node cannot silently become a fresh attempt.

Delegate job attempt increments and deadlines to the [scheduler retry contract](../../../scheduler/specifications/modules/retry.md). Use the same stable scheduler job for the node's approved attempts. Record the scheduler's chosen retry observation and never add a second independent retry counter or wake. On unknown submission or effect, reconcile original identity before another invocation. Retry cannot rewind verified completed work.

**ZIP-WORKFLOWS-RETRY-T01.** An uncertain external mutation blocks generic retry. An authorized definitive transient case uses the same job identity and the scheduler's recorded budget.
