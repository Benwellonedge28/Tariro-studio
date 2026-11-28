# Typed configuration and resource profiles

The [resource key catalog](../contracts/resources/budget-keys.json) assigns a unit, owner and enforcement point to every listed operational key. The [base defaults](defaults/limits.toml) are conservative starting values and must pass the policy and capacity resolution described in [CONFIGURATION_STANDARD.md](../CONFIGURATION_STANDARD.md). Numeric values belong in reviewed configuration or policy.

Profiles define workload preferences. A preference can reduce parallelism or select a locality allowed by policy. It cannot make an operation available where discovery or enforcement is missing, nor override an exact assignment rule. Policy wins on egress, spending and task authority. Capacity changes invalidate admission snapshots for new work; already occupied resources must be reconciled before release.

## Bootstrap and validation

Load defaults in a bounded stream. The launcher supplies an already-validated bootstrap byte budget from its trusted initialization context. Reject absent or unbounded bootstrap values. The resolved `configuration.max_layer_bytes` applies to subsequent layers and reloads. Reject duplicate/unknown keys, non-integer limits, zero where the registry requires positivity, and values that cannot be represented by the operation's unit. Record configuration and capacity revisions with each lease.

Fresh profiles start local. Selecting a distributed profile permits discovery only after separate network and node authorization. Exact reference counts such as Vimbai's 30 files are defined by its assignment agreement. No general default file count is inferred from that fixture.

For profiles with `derive_from_admission.keys`, omit the listed default slot caps from preference resolution. Compute finite effective capacity from enforceable per-unit demand and current pool availability, intersect it with administrative caps, and deny if no finite value can be derived. Derivation never removes a mandatory ceiling. An explicit profile numeric override and derivation for the same key are mutually exclusive.

The [v2 defaults schema](schemas/limits-v2.schema.json) validates the parsed base defaults tree. Keep the [v1 defaults schema](schemas/limits.schema.json) for edition detection and migration. Select the exact schema by the declared version before normalization. Reject unknown versions and validate both ends of the v1-to-v2 migration. The [resource budget view](../crates/configuration/specifications/modules/resources.md) owns the migration and provenance rules for the new drain budget. Profile and policy input versions are governed by their own schemas.

The loader also enforces cross-key relations, profile permissions and adapter representability before activation. The shipped drain duration is a configurable starting preference. See [ordered shutdown](../crates/runtime/specifications/modules/control/shutdown.md) for deadline selection and recovery.
