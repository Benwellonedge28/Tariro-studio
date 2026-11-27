# Scoped documentation batch seal

**ZIP-DOCUMENTATION-BATCHING-001 · v1.1 candidate · Owner** Documentation maintainers

**Planned source** `crates/documentation/src/batching.rs`

Read the configured exact count, eligible paths and operation constraints from the live assignment grant. Use the full authoritative staged diff from the [repository contract](../../../../specifications/1400-repositories/repositories.md). Compare changed outputs with the set of required verified units. Require exactly one unit per changed eligible Markdown path, and a matching artifact digest and preimage for each. Check actual cardinality after normalizing approved paths. Duplicate or unchanged files cannot increase the count. Extra, deleted, renamed, binary and out-of-scope entries block the reference workflow.

Run final-tree validation for all cross-links, anchor obligations, canonical references and dependency consistency. Freeze the reviewed tree, sorted diff, per-file evidence, instructions, assignments and grant identities together. A short exact batch remains AwaitingApproval and preserves its checkpoints. Reject the first over-limit staging proposal before writing. Do not insert filler or silently resize the approved batch. A changed approved count is applied through an explicit revised grant and plan. Reference Vimbai exact count is 30 for that grant.

**ZIP-DOCUMENTATION-BATCHING-T01.** Reject file 31 on the 30-file fixture. A 12-file final batch waits for revised scope. Approving 12 can seal under revised authority when all other conditions pass.
