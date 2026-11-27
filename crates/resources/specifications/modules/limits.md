# Effective resource bound resolver

**ZIP-RESOURCES-LIMITS-001 · v1.1 candidate · Owner** Resources maintainers

**Planned source** `crates/resources/src/limits.rs`

Read the validated immutable configuration snapshot through the owning [configuration module](../../../configuration/specifications/modules/resources.md). Keep numeric policy bounds, measured physical capacity, and task-specific conditions in distinct fields. Use compatible units and record every contributing policy origin. Outdated policy revisions must be re-resolved before admission. Invalid units or checked arithmetic overflow fail the operation.

For each operation, combine the caller deadline and any tighter configured elapsed duration by taking the earliest process-local monotonic instant. Anchor duration to the supervisor's operation start and reject an overflow when computing the instant. Equality to the current monotonic instant has expired. The resulting deadline is checked independently of shared ledgers. It is never reconstructed from a wall timestamp across restart. Preserve explicit zero where an existing key permits it, while treating a missing required bound as unavailable. Separate an advisory hardware preference from a live measured capacity. Consult the [limits policy](../../../../LIMITS_POLICY.md) before adding new controls.

**ZIP-RESOURCES-LIMITS-T01.** Test disallowed missing and permitted zero inputs, mixed units, deadline equality and overflow. Two admissions with the same valid deadline and independent fitting pool balances can both succeed.
