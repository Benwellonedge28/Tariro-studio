# Configuration schema migration

**ZIP-CONFIGURATION-MIGRATION-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/migration.rs`

## Boundary and inputs

Accept a read-only parsed base layer with explicit edition, target edition and the verified release baseline, when the approved migration edge requires one. Validate the input against its own strict edition before changing any values. Support the v1-to-v2 base defaults edge defined by [resource settings](resources.md). Preserve all prior values and bytes, import only the new drain setting from verified v2 defaults, and record artifact provenance.

## Behavior and failure handling

Build a temporary v2 tree in memory under the same admitted decode and working-memory bounds. Validate it against the target schema before returning it to [loader](loader.md). A v2 source with the required key missing fails direct validation. Missing trust input, invalid source, unsupported edge, lossy downgrade or interruption yields no activated state. To roll back, select the retained input and compatible reader under current policy. Migration neither writes input files nor publishes a snapshot.

## Acceptance

**ZIP-CONFIGURATION-MIGRATION-T01.** Run RT-DRAIN-CFG-01 through RT-DRAIN-CFG-05 in the [drain fixtures](../../../../contracts/acceptance/runtime/drain-policy-fixtures.json). Kill after staging the migrated tree and before activation. The original bytes and previous active generation must remain available.
