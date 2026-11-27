# Immutable artifact bindings

**ZIP-WORKFLOWS-ARTIFACTS-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/artifacts.rs`

An artifact binds workflow run and plan, producing node and accepted attempt, output name and schema, data class, byte length and immutable digest, evidence reference and scope. The producer stages bytes under admitted storage and the verifier checks them before a checkpoint exposes the binding. Consumers resolve immutable names through a successful producer checkpoint. Match type, version, run, plan, output name and live access scope before reading. A plan-authorized import has its own verified provenance and identity as an immutable workflow input.

A skipped optional producer contributes explicit typed absence. It cannot supply a required output. Never substitute an old run's output by matching filename or descriptive name. Corrupt or missing bytes block the dependent. Pin evidence and objects under assigned storage retention until an authorized lifecycle operation releases them.

**ZIP-WORKFLOWS-ARTIFACTS-T01.** An artifact in the wrong run, from a stale attempt or with a different digest cannot satisfy a required input.
