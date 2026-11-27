# Atomic snapshot activation

**ZIP-CONFIGURATION-LOADER-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/loader.rs`

## Required implementation behavior

load(input: LayerSources, current: Option<SnapshotRevision>) -> Result<ResolvedConfig, ConfigError>. Read bootstrap budget from trusted launch context, load in order, validate whole snapshot, then compare pointer revision and activate.

## Acceptance

**ZIP-CONFIGURATION-LOADER-T01.** Inject failure during layer read and during validation; prior snapshot remains active and readers see no mixed generation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
